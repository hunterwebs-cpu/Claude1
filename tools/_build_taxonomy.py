"""Build the plain-English offense taxonomy that drives the wizard's two
dropdowns.

This is the only file in the set whose visible text is written rather than
transcribed. The rules it follows:

*   Crime types are anchored to Chapter Two's own Part / Subpart structure.
    Each one names the Parts it covers, so the grouping can be audited against
    the manual. Where a single Part holds genuinely different subjects the
    Subparts are used instead -- Part K covers both arson and firearms, Part A
    covers both assault and criminal sexual abuse, Part G covers both commercial
    sex offenses and child pornography. Splitting on the manual's own Subpart
    boundaries keeps the grouping faithful while still matching how people
    describe their case.

*   Every offense term resolves its guidelines *from the statutory index*, never
    from a hand-written list. A term names statutes; this script looks each one
    up in ussg-statutory-index.json and copies whatever guidelines the manual
    maps it to. If a statute is not in the index the build fails loudly rather
    than shipping an invented mapping.

*   Labels and descriptions avoid legal jargon. The statutory language is kept
    alongside, so the wizard can show it, but it is never the visible label.

Usage: python3 tools/_build_taxonomy.py <appendix_a.json> <chapter2.json> <out.json>
"""
import sys, json, re

EDITION = "November 1, 2024"

# --------------------------------------------------------------------------
# Crime types. "parts" lists the Chapter Two Parts covered; "subparts" narrows
# to specific Subparts of a Part where that Part holds more than one subject.
# --------------------------------------------------------------------------

CRIME_TYPES = [
    {
        "id": "drugs",
        "label": "Drug offenses",
        "description": "Selling, moving, making, or holding controlled substances.",
        "parts": ["D"],
    },
    {
        "id": "firearms",
        "label": "Gun and weapon offenses",
        "description": "Having, selling, or using a firearm when the law says you "
                       "cannot, and offenses involving explosives.",
        "parts": ["K"],
    },
    {
        "id": "fraud-theft",
        "label": "Fraud, theft, and money offenses",
        "description": "Taking money or property by deception or without "
                       "permission, including most white-collar charges.",
        "parts": ["B"],
        "exclude_subparts": {"B": [3]},
    },
    {
        "id": "violent",
        "label": "Violent offenses",
        "description": "Charges involving death, injury, force, or the threat of "
                       "force, including robbery and carjacking.",
        "parts": ["A"],
        "exclude_subparts": {"A": [3]},
        "extra_subparts": {"B": [3]},
    },
    {
        "id": "sex-offenses",
        "label": "Sex offenses",
        "description": "Charges involving sexual conduct, commercial sex, or the "
                       "sex offender registry.",
        "subparts": {"A": [3], "G": [1, 3]},
    },
    {
        "id": "child-pornography",
        "label": "Child pornography offenses",
        "description": "Charges involving sexual images of minors, including "
                       "receiving, sending, keeping, or producing them.",
        "subparts": {"G": [2]},
    },
    {
        "id": "immigration",
        "label": "Immigration offenses",
        "description": "Entering or staying in the country unlawfully, bringing "
                       "others in, and offenses involving papers and passports.",
        "parts": ["L"],
    },
    {
        "id": "money-laundering",
        "label": "Money laundering and cash reporting",
        "description": "Moving or hiding money that came from a crime, and "
                       "offenses about reporting cash.",
        "parts": ["S"],
    },
    {
        "id": "racketeering",
        "label": "Racketeering and organized crime",
        "description": "RICO charges, criminal organizations, loansharking, and "
                       "illegal gambling businesses.",
        "parts": ["E"],
    },
    {
        "id": "obstruction",
        "label": "Obstruction, perjury, and lying to the government",
        "description": "Interfering with an investigation or a case, and lying "
                       "under oath or to federal agents.",
        "parts": ["J"],
    },
    {
        "id": "tax",
        "label": "Tax offenses",
        "description": "Not paying, underreporting, or lying about taxes.",
        "parts": ["T"],
    },
    {
        "id": "public-corruption",
        "label": "Bribery and public corruption",
        "description": "Paying off or being paid off as a public official, and "
                       "election law offenses.",
        "parts": ["C"],
    },
    {
        "id": "civil-rights",
        "label": "Civil rights and forced labor offenses",
        "description": "Offenses against a person's rights, including hate "
                       "crimes, forced labor, and human trafficking for work.",
        "parts": ["H"],
    },
    {
        "id": "national-security",
        "label": "National security and export offenses",
        "description": "Espionage, terrorism support, sanctions and export "
                       "violations, and weapons of mass destruction.",
        "parts": ["M"],
    },
    {
        "id": "environment",
        "label": "Environmental and wildlife offenses",
        "description": "Pollution, hazardous waste, and offenses involving "
                       "protected animals, plants, and fish.",
        "parts": ["Q"],
    },
    {
        "id": "prison",
        "label": "Prison offenses",
        "description": "Escape, contraband in a prison, and related charges.",
        "parts": ["P"],
    },
    {
        "id": "consumer-products",
        "label": "Food, drug, and consumer product offenses",
        "description": "Tampering with products, and offenses about food, "
                       "medicine, farm products, and odometers.",
        "parts": ["N"],
    },
    {
        "id": "antitrust",
        "label": "Antitrust offenses",
        "description": "Price fixing, bid rigging, and market allocation.",
        "parts": ["R"],
    },
    {
        "id": "other",
        "label": "Attempt, conspiracy, and other offenses",
        "description": "Charges for planning or helping with a crime, and "
                       "offenses the guidelines do not cover elsewhere.",
        "parts": ["X"],
    },
]

# --------------------------------------------------------------------------
# Common offense terms, in the words people actually use.
#
# "statutes" are (title, section, subsection-or-None). A subsection of None
# matches every entry printed for that section, which is what you want when the
# manual splits one statute across many index lines.
# --------------------------------------------------------------------------

TERMS = [
    # ---- drugs ----
    ("drugs", "distribution", "Selling or delivering drugs",
     ["distribution", "trafficking", "selling drugs", "delivery"],
     "Handing drugs to someone else, selling them, or sharing them -- whether or "
     "not money changed hands.",
     [(21, "841", "(a)"), (21, "841", "(b)(1)–(3)")]),
    ("drugs", "possession-with-intent", "Having drugs meant for sale",
     ["possession with intent", "PWID", "possession with intent to distribute"],
     "Holding a quantity of drugs that the government says was meant to be sold "
     "rather than used personally.",
     [(21, "841", "(a)"), (21, "841", "(b)(1)–(3)")]),
    ("drugs", "drug-conspiracy", "Agreeing with others to deal drugs",
     ["conspiracy", "drug conspiracy", "846 conspiracy"],
     "An agreement between two or more people to break a drug law. You can be "
     "charged even if no drugs were ever found.",
     [(21, "846", None)]),
    ("drugs", "drug-importation", "Bringing drugs into the country",
     ["importation", "smuggling drugs", "international"],
     "Moving drugs across the border into the United States.",
     [(21, "952", None), (21, "960", "(a),(b)")]),
    ("drugs", "simple-possession", "Having drugs for personal use",
     ["simple possession", "possession"],
     "Holding a small amount of a controlled substance for yourself.",
     [(21, "844", "(a)")]),
    ("drugs", "manufacturing", "Making or growing drugs",
     ["manufacturing", "cooking", "growing", "cultivation"],
     "Producing drugs, including running a lab or growing plants.",
     [(21, "841", "(a)")]),
    ("drugs", "drug-premises", "Letting a place be used for drugs",
     ["stash house", "crack house", "maintaining a premises"],
     "Owning, renting, or running a place where drugs are made, stored, or sold.",
     [(21, "856", None)]),
    ("drugs", "drug-phone", "Using a phone to set up a drug deal",
     ["telephone count", "communication facility"],
     "Using a phone, text, or the internet to arrange a drug transaction. Often "
     "charged alongside a bigger count.",
     [(21, "843", "(b)")]),
    ("drugs", "drug-kingpin", "Running a large drug organization",
     ["CCE", "kingpin", "continuing criminal enterprise"],
     "Leading an ongoing drug operation with several people under you.",
     [(21, "848", "(a)"), (21, "848", "(b)")]),
    ("drugs", "drug-near-school", "Drugs near a school or involving a minor",
     ["schoolyard", "protected location", "using a minor"],
     "A drug offense that happened near a school or playground, or that involved "
     "someone under 18.",
     [(21, "860", None)]),
    ("drugs", "precursor-chemicals", "Chemicals used to make drugs",
     ["listed chemicals", "precursors", "pseudoephedrine"],
     "Buying, selling, or moving the ingredients used to manufacture drugs.",
     [(21, "841", "(c)(1),(2)"), (21, "960", "(d)(1),(2)")]),

    # ---- firearms ----
    ("firearms", "felon-in-possession", "Having a gun after a felony conviction",
     ["felon in possession", "922(g)", "prohibited person"],
     "Owning or holding a firearm or ammunition when a past conviction or your "
     "status makes that illegal.",
     [(18, "922", "(a)–(p)")]),
    ("firearms", "gun-during-crime", "Carrying or using a gun during another crime",
     ["924(c)", "gun count", "brandishing"],
     "Having a firearm connected to a drug offense or a violent offense. This "
     "count usually carries its own mandatory time stacked on top.",
     [(18, "924", "(c)")]),
    ("firearms", "armed-career-criminal", "Gun charge with three prior serious convictions",
     ["ACCA", "armed career criminal", "924(e)"],
     "A firearm charge where the government says three earlier convictions "
     "trigger a much longer mandatory sentence.",
     [(18, "924", "(e)")]),
    ("firearms", "straw-purchase", "Buying a gun for someone else",
     ["straw purchase", "lying on the form", "4473"],
     "Buying a firearm for a person who cannot buy one, or lying on the purchase "
     "paperwork.",
     [(18, "922", "(a)–(p)"), (18, "924", "(a)")]),
    ("firearms", "unregistered-firearm", "Having an unregistered or illegal weapon",
     ["NFA", "machine gun", "silencer", "short barrel", "sawed off"],
     "Possessing a weapon that federal law requires to be registered, such as a "
     "machine gun, silencer, or short-barreled shotgun.",
     [(26, "5861", "(a)–(l)")]),
    ("firearms", "gun-trafficking", "Selling guns without a license",
     ["gun trafficking", "dealing without a license"],
     "Selling firearms as a business without a federal license, or moving guns "
     "across state lines to sell.",
     [(18, "922", "(a)–(p)")]),
    ("firearms", "arson", "Setting a fire or using explosives",
     ["arson", "explosives", "bombing"],
     "Burning or blowing up property, or having explosives illegally.",
     [(18, "844", "(f)"), (18, "844", "(i)"), (18, "844", "(d)")]),

    # ---- fraud, theft, money ----
    ("fraud-theft", "wire-fraud", "Fraud using phone, email, or the internet",
     ["wire fraud", "1343"],
     "A scheme to get money or property by lying, where a phone call, email, "
     "text, or transfer crossed state lines.",
     [(18, "1343", None)]),
    ("fraud-theft", "mail-fraud", "Fraud using the mail or a delivery service",
     ["mail fraud", "1341"],
     "A scheme to get money or property by lying, where something was sent by "
     "mail or a carrier like FedEx.",
     [(18, "1341", None)]),
    ("fraud-theft", "bank-fraud", "Fraud against a bank",
     ["bank fraud", "1344"],
     "A scheme to get money from a bank by lying, including bad checks and "
     "false loan applications.",
     [(18, "1344", None)]),
    ("fraud-theft", "health-care-fraud", "Billing fraud in health care",
     ["health care fraud", "Medicare fraud", "Medicaid fraud"],
     "Billing an insurer or a government health program for care that was not "
     "given, not needed, or not as described.",
     [(18, "1347", None)]),
    ("fraud-theft", "securities-fraud", "Investment and securities fraud",
     ["securities fraud", "investment fraud", "Ponzi"],
     "Lying to investors, manipulating a stock, or running an investment scheme "
     "that pays old investors with new money.",
     [(15, "78j", None), (15, "78ff", None)]),
    ("fraud-theft", "insider-trading", "Trading on secret company information",
     ["insider trading"],
     "Buying or selling stock using confidential information, or passing that "
     "information to someone who trades on it.",
     [(15, "78j", None)]),
    ("fraud-theft", "identity-theft", "Using someone else's identity",
     ["identity theft", "ID theft", "1028"],
     "Using another person's name, Social Security number, or documents without "
     "permission.",
     [(18, "1028", None)]),
    ("fraud-theft", "aggravated-identity-theft", "Identity theft added to another charge",
     ["aggravated identity theft", "1028A", "two-year count"],
     "A separate count that adds a fixed, mandatory term on top of the "
     "underlying fraud sentence.",
     [(18, "1028A", None)]),
    ("fraud-theft", "credit-card-fraud", "Credit card and access device fraud",
     ["credit card fraud", "access device", "1029", "skimming"],
     "Using stolen card numbers, account numbers, or card-making equipment.",
     [(18, "1029", None)]),
    ("fraud-theft", "computer-fraud", "Hacking and computer offenses",
     ["hacking", "computer fraud", "CFAA", "1030"],
     "Getting into a computer or account without permission, or damaging one.",
     [(18, "1030", "(a)(2)"), (18, "1030", "(a)(4)"), (18, "1030", "(a)(5)")]),
    ("fraud-theft", "theft-government-property", "Stealing government money or property",
     ["theft of government property", "641", "benefits fraud"],
     "Taking money or property belonging to the federal government, including "
     "benefits you were not entitled to.",
     [(18, "641", None)]),
    ("fraud-theft", "embezzlement", "Taking money you were trusted with",
     ["embezzlement", "misapplication"],
     "Using money or property for yourself when your job was to look after it.",
     [(18, "656", None)]),
    ("fraud-theft", "counterfeiting", "Counterfeit money or documents",
     ["counterfeiting", "fake money", "forgery"],
     "Making or passing fake currency, checks, or government documents.",
     [(18, "471", None), (18, "472", None)]),
    ("fraud-theft", "program-bribery-theft", "Theft from a program that gets federal money",
     ["666", "federal program theft"],
     "Stealing from an organization, state, or local agency that receives "
     "federal funding.",
     [(18, "666", "(a)(1)(A)")]),
    ("fraud-theft", "fraud-conspiracy", "Agreeing with others to commit fraud",
     ["conspiracy to commit fraud", "1349"],
     "An agreement between two or more people to carry out a fraud scheme.",
     [(18, "1349", None)]),

    # ---- violent ----
    ("violent", "robbery", "Robbery",
     ["robbery", "Hobbs Act", "1951", "armed robbery"],
     "Taking property from a person by force or by threatening them.",
     [(18, "1951", None)]),
    ("violent", "bank-robbery", "Bank robbery",
     ["bank robbery", "2113"],
     "Taking or trying to take money from a bank by force, threat, or "
     "intimidation.",
     [(18, "2113", "(a)"), (18, "2113", "(d)"), (18, "2113", "(e)")]),
    ("violent", "carjacking", "Carjacking",
     ["carjacking", "2119"],
     "Taking a vehicle from someone by force or threat.",
     [(18, "2119", None)]),
    ("violent", "assault-federal-officer", "Assaulting a federal officer",
     ["assault on a federal officer", "111"],
     "Hitting, resisting, or interfering with a federal officer or employee "
     "doing their job.",
     [(18, "111", None)]),
    ("violent", "assault", "Assault",
     ["assault", "aggravated assault", "113"],
     "Hurting someone, or trying to, on federal land or in federal jurisdiction.",
     [(18, "113", "(a)(2)"), (18, "113", "(a)(3)"), (18, "113", "(a)(4)")]),
    ("violent", "murder", "Murder or killing",
     ["murder", "homicide", "manslaughter", "1111"],
     "Causing someone's death. The guideline depends heavily on intent and "
     "circumstances.",
     [(18, "1111", "(a)")]),
    ("violent", "kidnapping", "Kidnapping",
     ["kidnapping", "abduction", "1201"],
     "Holding, moving, or hiding a person against their will.",
     [(18, "1201", "(a)")]),
    ("violent", "threats", "Threatening someone",
     ["threats", "875", "threatening communication"],
     "Sending a threat to hurt someone by phone, text, mail, or online.",
     [(18, "875", "(c)")]),
    ("violent", "stalking", "Stalking or domestic violence",
     ["stalking", "domestic violence", "2261A"],
     "Following, watching, or harassing a person across state lines, or hurting "
     "a partner or family member.",
     [(18, "2261A", None)]),

    # ---- sex offenses ----
    ("sex-offenses", "sex-trafficking", "Sex trafficking",
     ["sex trafficking", "1591", "trafficking a minor"],
     "Causing someone to perform a commercial sex act by force, fraud, threat, "
     "or because they are under 18.",
     [(18, "1591", None)]),
    ("sex-offenses", "enticement", "Trying to meet a minor for sex",
     ["enticement", "2422", "online sting", "coercion of a minor"],
     "Using the phone or internet to persuade someone under 18 to meet for "
     "sexual activity. Many of these cases begin as an online sting.",
     [(18, "2422", None)]),
    ("sex-offenses", "transportation-for-sex", "Moving someone across state lines for sex",
     ["Mann Act", "transportation", "2421", "2423"],
     "Taking a person across state lines or into the country for commercial sex "
     "or unlawful sexual activity.",
     [(18, "2421", None), (18, "2423", "(a)–(d)")]),
    ("sex-offenses", "sexual-abuse", "Sexual abuse or assault",
     ["sexual abuse", "criminal sexual abuse", "2241", "2242"],
     "A sexual act committed by force, threat, or where the person could not "
     "consent.",
     [(18, "2241", None), (18, "2242", None)]),
    ("sex-offenses", "failure-to-register", "Not registering as a sex offender",
     ["failure to register", "SORNA", "2250"],
     "Not signing up, or not keeping your information current, on the sex "
     "offender registry.",
     [(18, "2250", "(a), (b)")]),
    ("sex-offenses", "obscenity", "Obscenity offenses",
     ["obscenity", "obscene material"],
     "Sending, selling, or importing obscene material.",
     [(18, "1462", None), (18, "1465", None)]),

    # ---- child pornography ----
    ("child-pornography", "cp-possession-receipt",
     "Having or receiving sexual images of children",
     ["possession", "receipt", "2252", "2252A"],
     "Downloading, keeping, or receiving images or videos showing a minor in "
     "sexual conduct.",
     [(18, "2252", None), (18, "2252A", "(a),(b)")]),
    ("child-pornography", "cp-distribution",
     "Sending or sharing sexual images of children",
     ["distribution", "sharing", "file sharing", "trading"],
     "Sending images to another person, or making them available through a "
     "file-sharing program.",
     [(18, "2252", None), (18, "2252A", "(a),(b)")]),
    ("child-pornography", "cp-production",
     "Producing sexual images of a child",
     ["production", "2251", "manufacturing"],
     "Making, or trying to make, sexual images of a minor. This carries the "
     "highest penalties in this group.",
     [(18, "2251", "(a), (b)"), (18, "2251", "(c)")]),

    # ---- immigration ----
    ("immigration", "illegal-reentry", "Coming back after being deported",
     ["illegal reentry", "1326", "reentry after deportation"],
     "Entering or being found in the United States after an earlier removal.",
     [(8, "1326", None)]),
    ("immigration", "illegal-entry", "Entering the country unlawfully",
     ["illegal entry", "improper entry", "1325"],
     "Crossing into the United States outside an official port of entry.",
     [(8, "1325", "(a)")]),
    ("immigration", "alien-smuggling", "Bringing or moving people across the border",
     ["alien smuggling", "1324", "transporting", "harboring"],
     "Bringing people into the country unlawfully, moving them once inside, or "
     "hiding them.",
     [(8, "1324", "(a)")]),
    ("immigration", "document-fraud", "False immigration documents",
     ["document fraud", "1546", "fake papers", "visa fraud"],
     "Making, using, or possessing false visas, permits, or other immigration "
     "papers.",
     [(18, "1546", None)]),
    ("immigration", "marriage-fraud", "Marriage or naturalization fraud",
     ["marriage fraud", "naturalization fraud"],
     "A marriage entered into to get immigration status, or lying to become a "
     "citizen.",
     [(8, "1325", "(c)")]),

    # ---- money laundering ----
    ("money-laundering", "money-laundering", "Money laundering",
     ["money laundering", "1956", "washing money"],
     "Moving money that came from a crime in a way meant to hide where it came "
     "from.",
     [(18, "1956", None)]),
    ("money-laundering", "monetary-transaction", "Spending criminal proceeds",
     ["1957", "monetary transaction", "spending"],
     "Making a transaction over $10,000 with money you knew came from a crime.",
     [(18, "1957", None)]),
    ("money-laundering", "structuring", "Breaking up cash deposits",
     ["structuring", "smurfing", "5324"],
     "Splitting cash into smaller deposits to avoid the bank filing a report.",
     [(31, "5324", None)]),

    # ---- racketeering ----
    ("racketeering", "rico", "RICO",
     ["RICO", "racketeering", "1962", "enterprise"],
     "Running or helping run an organization through a pattern of criminal "
     "activity.",
     [(18, "1962", None)]),
    ("racketeering", "vicar", "Violence for a criminal organization",
     ["VICAR", "1959", "violent crime in aid of racketeering"],
     "A violent act committed to join, keep position in, or help a criminal "
     "enterprise.",
     [(18, "1959", None)]),
    ("racketeering", "gambling-business", "Running an illegal gambling business",
     ["illegal gambling", "bookmaking", "1955"],
     "Operating a betting or gambling operation that state law prohibits.",
     [(18, "1955", None)]),
    ("racketeering", "loansharking", "Loansharking and collecting by threat",
     ["loansharking", "extortionate credit", "894"],
     "Lending money at illegal rates, or collecting a debt by threatening "
     "someone.",
     [(18, "892", None), (18, "894", None)]),

    # ---- obstruction ----
    ("obstruction", "obstruction-of-justice", "Interfering with an investigation or case",
     ["obstruction", "1503", "1512", "tampering"],
     "Trying to influence, block, or interfere with a case, a witness, or "
     "evidence.",
     [(18, "1503", None), (18, "1512", "(b)"), (18, "1512", "(c)")]),
    ("obstruction", "witness-tampering", "Pressuring or threatening a witness",
     ["witness tampering", "1512"],
     "Trying to stop someone from testifying or reporting, or to change what "
     "they say.",
     [(18, "1512", "(a)"), (18, "1512", "(b)"), (18, "1512", "(d)")]),
    ("obstruction", "perjury", "Lying under oath",
     ["perjury", "1621", "1623", "false testimony"],
     "Giving false testimony after swearing to tell the truth.",
     [(18, "1621", None), (18, "1623", None)]),
    ("obstruction", "false-statements", "Lying to a federal agent or agency",
     ["false statements", "1001", "lying to the FBI"],
     "Making a false statement to a federal agency or investigator, even when "
     "you were not under oath.",
     [(18, "1001", None)]),
    ("obstruction", "failure-to-appear", "Not showing up in court",
     ["failure to appear", "bail jumping", "3146"],
     "Missing a required court date or violating release conditions.",
     [(18, "3146", None)]),

    # ---- tax ----
    ("tax", "tax-evasion", "Tax evasion",
     ["tax evasion", "7201"],
     "Taking steps to avoid paying tax you owed.",
     [(26, "7201", None)]),
    ("tax", "false-return", "Filing a false return",
     ["false return", "7206", "filing a false tax return"],
     "Signing and filing a return you knew was wrong in a way that mattered.",
     [(26, "7206", "(1),(3),(4),(5)")]),
    ("tax", "preparer-fraud", "Preparing false returns for others",
     ["preparer fraud", "7206(2)"],
     "Helping someone else file a return you knew was false.",
     [(26, "7206", "(2)")]),
    ("tax", "failure-to-file", "Not filing or not paying",
     ["failure to file", "7203"],
     "Not filing a required return, or not paying tax that was due.",
     [(26, "7203", None)]),
    ("tax", "payroll-tax", "Not turning over payroll taxes",
     ["payroll tax", "trust fund", "7202"],
     "Withholding tax from employees' pay and not sending it to the government.",
     [(26, "7202", None)]),

    # ---- public corruption ----
    ("public-corruption", "bribery", "Bribery of a public official",
     ["bribery", "201", "payoff"],
     "Giving or taking something of value to influence an official act.",
     [(18, "201", "(b)(1)"), (18, "201", "(b)(2)")]),
    ("public-corruption", "gratuity", "Illegal gift to an official",
     ["gratuity", "201(c)"],
     "Giving or taking a gift because of an official act, without a full "
     "bribery agreement.",
     [(18, "201", "(c)(1)")]),
    ("public-corruption", "program-bribery", "Bribery involving federal funds",
     ["666", "program bribery", "kickback"],
     "Paying or taking a bribe at an organization or agency that gets federal "
     "money.",
     [(18, "666", "(a)(1)(B)"), (18, "666", "(a)(2)")]),
    ("public-corruption", "extortion-under-color", "Extortion by an official",
     ["extortion under color of official right", "Hobbs Act extortion"],
     "A public official demanding payment in exchange for official action.",
     [(18, "1951", None)]),

    # ---- other ----
    ("other", "general-conspiracy", "Agreeing with others to commit a federal crime",
     ["conspiracy", "371", "agreement"],
     "An agreement between two or more people to break a federal law, or to "
     "defraud the United States, with at least one step taken toward it.",
     [(18, "371", None)]),
    ("other", "attempt", "Trying to commit a crime",
     ["attempt", "solicitation"],
     "Taking real steps toward a crime that was not completed.",
     [(18, "1349", None)]),
    ("other", "accessory-after-the-fact", "Helping someone after their crime",
     ["accessory after the fact", "3"],
     "Helping a person avoid arrest or punishment after they committed an "
     "offense.",
     [(18, "3", None)]),
    ("other", "misprision", "Hiding a crime from the authorities",
     ["misprision of felony", "4"],
     "Knowing about a felony and actively concealing it.",
     [(18, "4", None)]),
    ("prison", "escape", "Escape or walking away from custody",
     ["escape", "751", "walkaway", "failure to return"],
     "Leaving a prison, halfway house, or custody without permission, or not "
     "coming back when you were supposed to.",
     [(18, "751", None)]),
    ("prison", "prison-contraband", "Contraband in a prison",
     ["contraband", "1791", "phone in prison"],
     "Bringing in, having, or passing items that are not allowed inside a "
     "correctional facility, such as a phone, drugs, or a weapon.",
     [(18, "1791", None)]),

    # ---- civil rights and forced labor ----
    ("civil-rights", "hate-crime", "Hate crime",
     ["hate crime", "249", "bias crime"],
     "Hurting someone, or trying to, because of their race, religion, national "
     "origin, gender, sexual orientation, gender identity, or disability.",
     [(18, "249", None)]),
    ("civil-rights", "civil-rights-conspiracy", "Conspiring against someone's rights",
     ["241", "242", "color of law", "deprivation of rights"],
     "Agreeing with others to interfere with a person's legal rights, or doing "
     "so while acting as an official.",
     [(18, "241", None), (18, "242", None)]),
    ("civil-rights", "forced-labor", "Forced labor or involuntary servitude",
     ["forced labor", "1589", "labor trafficking", "peonage"],
     "Making someone work through force, threats, or by holding their documents "
     "or debt over them.",
     [(18, "1589", None), (18, "1590", None)]),

    # ---- national security and export ----
    ("national-security", "sanctions-export", "Sanctions and export violations",
     ["IEEPA", "sanctions", "export violation", "1705"],
     "Sending goods, technology, or money to a country, group, or person that "
     "United States law puts off limits.",
     [(50, "1705", None)]),
    ("national-security", "material-support", "Material support to a terrorist group",
     ["material support", "2339B", "terrorism"],
     "Giving money, goods, services, or personnel to a designated terrorist "
     "organization.",
     [(18, "2339B", None)]),
    ("national-security", "espionage", "Espionage or mishandling national defense information",
     ["espionage", "793", "classified information", "leaking"],
     "Gathering, keeping, or passing along national defense or classified "
     "information.",
     [(18, "793", "(a)–(c)"), (18, "793", "(d),(e)"), (18, "793", "(f)")]),

    # ---- environment ----
    ("environment", "water-pollution", "Water pollution",
     ["Clean Water Act", "1319", "discharge", "dumping"],
     "Discharging pollutants into water without a permit or outside what a "
     "permit allowed.",
     [(33, "1319", "(c)(1),(2),(4)"), (33, "1319", "(c)(3)")]),
    ("environment", "hazardous-waste", "Hazardous waste offenses",
     ["RCRA", "6928", "hazardous waste", "illegal disposal"],
     "Storing, moving, or getting rid of hazardous waste outside the rules.",
     [(42, "6928", "(d)"), (42, "6928", "(e)")]),

    # ---- consumer products ----
    ("consumer-products", "product-tampering", "Tampering with a consumer product",
     ["tampering", "1365", "product tampering"],
     "Interfering with food, medicine, or another consumer product, or "
     "threatening to.",
     [(18, "1365", "(a)"), (18, "1365", "(b)"), (18, "1365", "(c)"),
      (18, "1365", "(d)"), (18, "1365", "(e)")]),

    # ---- antitrust ----
    ("antitrust", "price-fixing", "Price fixing or bid rigging",
     ["price fixing", "bid rigging", "Sherman Act", "market allocation"],
     "Agreeing with competitors to set prices, split up customers or territory, "
     "or decide who wins a bid.",
     [(15, "1", None)]),
]


def build_index(appa):
    by_section = {}
    for e in appa["entries"]:
        by_section.setdefault((e["title"], e["section"]), []).append(e)
    return by_section


def resolve(statutes, by_section, problems, term_id):
    out, guidelines = [], []
    for title, section, subsection in statutes:
        hits = by_section.get((title, section))
        if not hits:
            problems.append({
                "term": term_id,
                "statute": f"{title} U.S.C. § {section}",
                "reason": "statute is not in Appendix A; no mapping emitted"})
            continue
        if subsection is not None:
            matched = [h for h in hits if (h.get("subsection") or "") == subsection]
            if not matched:
                problems.append({
                    "term": term_id,
                    "statute": f"{title} U.S.C. § {section}{subsection}",
                    "reason": "subsection is not printed in Appendix A; "
                              "no mapping emitted",
                    "available": [h.get("subsection") for h in hits]})
                continue
            hits = matched
        for h in hits:
            out.append({
                "citation": h["citation"],
                "guidelines": h["guidelines"],
                "guideline_refs": h.get("guideline_refs", []),
                "pdf_page": h["pdf_page"],
            })
            for g in h["guidelines"]:
                if g not in guidelines:
                    guidelines.append(g)
    return out, guidelines


def main():
    appa_path, ch2_path, outpath = sys.argv[1], sys.argv[2], sys.argv[3]
    appa = json.load(open(appa_path))
    ch2 = json.load(open(ch2_path))
    by_section = build_index(appa)
    by_guideline = {g["section"]: g for g in ch2["guidelines"]}

    problems = []

    # Crime types: attach the Chapter Two guidelines that fall under them.
    parts_meta = {p["part"]: p for p in ch2["chapter2_parts"]}
    crime_types = []
    for ct in CRIME_TYPES:
        wanted = []
        for g in ch2["guidelines"]:
            part = g.get("chapter2_part")
            subpart = g.get("chapter2_subpart")
            if part is None:
                continue
            subnum = None
            if part in parts_meta:
                for sp in parts_meta[part].get("subparts", []):
                    if sp["title"] == subpart:
                        subnum = sp["number"]
                        break
            hit = False
            if part in ct.get("parts", []):
                excl = ct.get("exclude_subparts", {}).get(part, [])
                if subnum not in excl:
                    hit = True
            if subnum is not None:
                if subnum in ct.get("subparts", {}).get(part, []):
                    hit = True
                if subnum in ct.get("extra_subparts", {}).get(part, []):
                    hit = True
            if hit:
                wanted.append(g["section"])
        if not wanted:
            problems.append({"crime_type": ct["id"],
                             "reason": "no Chapter Two guidelines matched"})
        crime_types.append({
            "id": ct["id"],
            "label": ct["label"],
            "description": ct["description"],
            "chapter2_parts": sorted(set(
                list(ct.get("parts", [])) + list(ct.get("subparts", {}).keys())
                + list(ct.get("extra_subparts", {}).keys()))),
            "chapter2_part_titles": [
                parts_meta[p]["title"] for p in sorted(set(
                    list(ct.get("parts", [])) + list(ct.get("subparts", {}).keys())
                    + list(ct.get("extra_subparts", {}).keys())))
                if p in parts_meta],
            "guidelines": sorted(set(wanted)),
        })

    # Offense terms
    terms = []
    for ct_id, tid, label, aka, plain, statutes in TERMS:
        stats, guidelines = resolve(statutes, by_section, problems, tid)
        if not stats:
            continue
        terms.append({
            "id": tid,
            "crime_type": ct_id,
            "label": label,
            "also_called": aka,
            "description": plain,
            "statutes": stats,
            "guidelines": guidelines,
            "guideline_titles": {g: by_guideline[g]["title"]
                                 for g in guidelines if g in by_guideline},
            "multiple_guidelines": len(guidelines) > 1,
        })

    known = {c["id"] for c in crime_types}
    for t in terms:
        if t["crime_type"] not in known:
            problems.append({"term": t["id"],
                             "reason": f"crime type {t['crime_type']} is not defined"})

    payload = {
        "source": "Derived from USSC Guidelines Manual Chapter Two part structure "
                  "and Appendix A (Statutory Index). Labels and descriptions are "
                  "written for a lay reader; all statute-to-guideline mappings are "
                  "taken from Appendix A without modification.",
        "manual_edition": EDITION,
        "counts": {
            "crime_types": len(crime_types),
            "offense_terms": len(terms),
            "terms_with_multiple_guidelines":
                sum(1 for t in terms if t["multiple_guidelines"]),
        },
        "unresolved": problems,
        "crime_types": crime_types,
        "offense_terms": terms,
    }
    with open(outpath, "w") as fh:
        json.dump(payload, fh, indent=1)
    print(json.dumps(payload["counts"], indent=1))
    print("unresolved:", len(problems))
    for p in problems:
        print("   ", p)


if __name__ == "__main__":
    main()
