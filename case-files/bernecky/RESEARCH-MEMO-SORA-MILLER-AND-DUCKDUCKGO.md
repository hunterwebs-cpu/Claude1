# RESEARCH MEMO — (1) NY SORA "Internet Identifier" Case Law and Account-Ecosystem Facts; (2) DuckDuckGo vs. "In-Private" Browsing

**Re:** *United States v. Jeffrey Bernecky*, No. 6:18-CR-06018-DGL-MWP (W.D.N.Y.)
**Purpose:** Supports CIMP Agreement objections memo (Item(s) re: internet-account/identifier registration and Item 5's "in-private" browsing ban)
**Status:** Intelligence memo only — not for filing. Citation-verification notes appear inline and in a closing NOT VERIFIED section, consistent with this case's citation-rigor practice.

---

## SECTION 1 — NY SORA "Internet Identifier" Registration: The Real Case Is *People v. Ellis*, Not "*People v. Miller*"

### 1.1 Bottom line

The paralegal's recollection is **wrong on the case name** and **partially wrong on the holding**. No New York Court of Appeals decision called "*People v. Miller*" addresses SORA internet-identifier reporting. Multiple people named Miller have New York SORA-related appellate decisions (mostly risk-level classification disputes with no bearing on internet identifiers) — none of the "Miller" cases surfaced in this research decide the internet-identifier question. The actual controlling case is:

> **People v. Ellis**, 2019 NY Slip Op 05183 (N.Y. Ct. App. June 27, 2019) (Fahey, J.), affirming **162 A.D.3d 161** (4th Dept. 2018), reversing conviction and dismissing indictment as jurisdictionally defective.

**What *Ellis* actually holds** is narrower and more precise than "internet identifiers don't include the account, only the email":

- A **Facebook account (the platform/service itself)** is **not** an "internet identifier" under N.Y. Correction Law § 168-f(4), so a sex offender need not disclose to DCJS *that he has a Facebook account*.
- **But** the **identifier the offender actually uses to access or interact on that account** — i.e., the email address used to log in, **or** any screen name/pseudonym/alias used to interact with other users — **must still be disclosed**, because those fall within the statutory definition of "internet identifier."
- The court's own formulation: an internet identifier "is not the social networking website or application itself; rather, it is how someone identifies himself or herself when accessing a social networking account, whether it be with an electronic mail address or **some other name or title, such as a screen name or user name**."

So the correct one-line summary is: ***the platform/service is not a registrable identifier; the email address or screen-name/alias used on it is*** — not "only the email counts." A distinct public-facing username, handle, or channel name would independently qualify as a registrable "internet identifier" under *Ellis* if it functions as a designation for chat/social networking/communication. The paralegal's recollection oversimplifies this into "email only," which is not accurate and should not be repeated as the rule in any filing.

**Verification status:** This holding is confirmed by convergence across six independent secondary sources describing/quoting the opinion (FindLaw's case page, Justia's docket page, the New York Appellate Digest's case-by-case digest of the June 27, 2019 decision, the New York Criminal Lawyer Blog 24/7, an appellate-litigation.org case note, and a Mitchell Hamline sex-offense-litigation-policy case note), all stating the same holding in materially identical terms. I was not able to pull the primary slip-opinion text directly — nycourts.gov and CourtListener both returned bot-protection blocks (HTTP 403 / empty 202 responses) to automated fetch in this session. **Before filing, pull the primary opinion via Westlaw/Lexis/PACER or a direct browser visit to `https://www.nycourts.gov/reporter/3dseries/2019/2019_05183.htm` to get an exact pin cite and confirm the official N.Y.3d reporter citation** (search-engine snippets gave conflicting guesses for the N.Y.3d volume/page — 33 N.Y.3d 386, 33 N.Y.3d 947, and 33 N.Y.3d 582 all appeared in different low-quality snippets, which is itself a sign none of them should be trusted without a primary check). The reliable, checkable citation to use until then is the neutral one: **2019 NY Slip Op 05183**.

### 1.2 The statutory text itself (verified against primary/near-primary legislative text)

**N.Y. Correction Law § 168-a(18)** (definitions section), quoted verbatim from the New York State Senate's official codified-laws site (nysenate.gov):

> "'Internet identifiers' means electronic mail addresses and designations used for the purposes of chat, instant messaging, social networking or other similar internet communication."

**N.Y. Correction Law § 168-f(4)** (reporting duty), quoted verbatim from the same source:

> "Any sex offender shall register with the division no later than ten calendar days after any change of address, internet accounts with internet access providers belonging to such offender, internet identifiers that such offender uses, or his or her status of enrollment, attendance, employment or residence at any institution of higher education."

Two things follow directly from this text, independent of *Ellis*: (1) the statute's own defined term covers only **email addresses** and **designations used for chat/IM/social-networking/similar communication** — it does not, on its face, list "accounts," "services," "platforms," or "apps" as separately reportable things (that is exactly the textual hook *Ellis* used); and (2) the duty is triggered by a *change* — a new identifier the offender "uses" — not by continuing to use an identifier already on file.

### 1.3 Practical fact-check: does opening "a YouTube account" or "an Instagram account" create a new, separately reportable identifier when the person already has a registered Google or Facebook account?

This is squarely a factual question, not a legal one, and the technical answer is: **usually no new authentication identifier is created**, though a new *public-facing designation* (handle/channel name) could independently qualify.

**Google:** Google's own account-help documentation (support.google.com/accounts) states plainly that "a Google Account gives you access to many Google products" and separately confirms that Gmail is only one of several services tied to the same underlying account — the same login (email + password, or now often just the email + 2FA) is the credential for YouTube, Google Drive, Calendar, Google Play, Google Photos, etc. There is no separate "YouTube password" or "YouTube account" distinct from the Google Account; "opening a YouTube account" using an existing Gmail login does not create a new email address or new authentication identifier — it is the same identifier already on file, now used to access an additional Google product.

**Meta/Facebook:** Meta's own Help Center documentation on the "Accounts Center" (meta.com/help/accounts-center) confirms that Facebook and Instagram accounts can be linked in a single Accounts Center and configured so the same login credentials authenticate across both apps ("Select Allow all accounts to log into each other"); Meta states it is rolling this out so that, by default, linked accounts "will be able to log into each other." Whether a specific Instagram account is a *new* identifier under SORA does not turn on whether Meta's back-end links the login — it turns on whether the offender establishes a new email address or a new public-facing screen name/handle he did not previously report. If he logs into Instagram using the same already-registered Facebook credentials and does not adopt a new handle, no new statutorily defined identifier has been created.

**The one caveat, drawn from a real (but out-of-state, non-controlling) case:** *State v. White*, No. 2011-770 (N.H. 2012) (New Hampshire Supreme Court, decided Dec. 7, 2012), rejected an argument that opening a new MySpace account using an already-registered email address and the offender's real name eliminated the need to separately register the account. But that result rests on New Hampshire's *broader* statutory definition, which expressly lists "user profile information" as its own separately reportable category, distinct from "email addresses." New York's § 168-a(18) definition does **not** contain a "user profile" or "account" category — it is limited to email addresses and chat/IM/social-networking *designations*. *Ellis* is the direct product of that narrower NY text, and it reached the opposite conclusion from *White* on materially the same kind of fact pattern (a new social-media account, no new handle). This is a meaningful, honest distinction to draw in any filing: NY's statute was written narrower than New Hampshire's, and *Ellis* enforces that narrower text.

**Net practical conclusion for the motion:** If Bernecky already has a registered Google account/email on file with DCJS, opening "a YouTube account" through that same Google login is not, by itself, the creation of a new "internet identifier" under Correction Law § 168-a(18)/168-f(4) as construed in *Ellis* — it is continued use of an identifier (his email) already registered, accessing an additional product tied to the same underlying account. A *new* registration obligation would arise only if he adopted a new, distinct public-facing handle/channel name on YouTube that he had not previously disclosed. No case located (in NY or elsewhere) squarely addresses the "single-login, multiple-services" scenario by name; the *Ellis*/§ 168-a(18) textual analysis above is an extension by direct application of the statute and *Ellis*'s reasoning, not an on-point holding — disclose it that way in any drafted argument.

### 1.4 How this fits the motion

If Probation's stated basis for requiring separate state-police/DCJS registration of a "YouTube account" is that it is a distinct reportable internet account/identifier, *Ellis* directly undercuts that premise for the platform-as-such, and the Google-account-ecosystem facts above undercut it further where the login/email is already on file. This is a clean, narrow argument: ask the Court (or Probation, informally, before it becomes a violation dispute) to confirm that no new SORA registration obligation is triggered merely by using an already-registered Google/Meta account to access an additional product under that same umbrella account, consistent with *Ellis*'s platform/identifier distinction and the statute's own text. This is a modest, textually grounded ask in the same register as this case's other CIMP-Agreement findings — it does not require the Court to invalidate anything, only to confirm what the statute and *Ellis* already say the state cannot require.

---

## SECTION 2 — DuckDuckGo vs. "In-Private" Browsing (CIMP Item 5)

### 2.1 Bottom line

**There is no real technical basis for treating ordinary DuckDuckGo use as equivalent to "in-private browsing" that defeats CIMP monitoring.** DuckDuckGo's privacy protections operate against third-party advertising/tracking companies on the open web; they do nothing to a locally installed, device-level monitoring agent, which sits below the browser-privacy layer entirely. This is confirmed by DuckDuckGo's own documentation, Google's own documentation about what Incognito mode does and does not do, and the basic architecture of how each technology operates.

### 2.2 What browser-native "private/incognito" browsing actually does

Google's own support page for Chrome Incognito mode (support.google.com/chrome, "Browse in Incognito mode") states — quoted directly — that Incognito "limits the information that's saved to your device," and separately, explicitly warns:

> "organizations that manage your network, like your school, employer, or internet service provider, may be able to observe your activity in Incognito."

That is the key admission from the vendor itself: Incognito/private-browsing modes are a **local storage** feature (don't retain history, cookies, cached form data, etc. *on the device* after the session ends) and were never designed to, and do not, hide activity from anything with actual access to the device or its network path — including exactly the category of software CIMP installs (a locally-installed monitoring agent with privileged access to the monitored device). The same limitation applies as a matter of browser architecture to Safari Private Browsing and Firefox Private Windows: all three are local-storage-suppression features, not anti-surveillance tools against software running on the same machine.

### 2.3 What DuckDuckGo's privacy features actually do

DuckDuckGo's own Help Pages (duckduckgo.com/duckduckgo-help-pages) describe the company's privacy model as stopping personal data "from being collected at all" **by companies** — specifically: the search engine "doesn't track you or your searches" and doesn't "save or share your search history," and the browser/browser extension's "3rd-Party Tracker Loading Protection" blocks "hidden trackers from companies like Google and Facebook lurking on other websites before they even get a chance to load," together with related features (Cookie Protection, Link Tracking Protection, Referrer Tracking Protection, Fingerprinting Protection, CNAME Cloaking Protection, Embedded Social Content Tracking Protection). Every one of these protections targets **third-party advertising/analytics companies operating on other websites** — none of them is directed at, or has any effect on, software running locally on the user's own device with OS-level access. DuckDuckGo's documentation contains no claim, anywhere, of protecting against device-level monitoring, employer/parental-control software, or law-enforcement/probation monitoring — because that is not the problem DuckDuckGo is built to solve.

### 2.4 Does DuckDuckGo have a distinct "private/incognito" branded mode?

No, not in the sense CIMP Item 5 uses the phrase. DuckDuckGo's tracker-blocking is **always on** by default in both its search engine and its browser — it is not a special mode the user switches into and out of. The one feature that superficially resembles a "private mode" is the **Fire Button**, described in DuckDuckGo's own Help Pages: a manual, one-tap, on-device data-erase tool that "burns" recent local browsing data (open tabs, history, cookies, cached site data, granted permissions) after the fact — it is a retroactive cleanup action, not a session-isolation mode like Chrome/Safari/Firefox's incognito/private windows, and it does not need to be invoked (and typically is not invoked) for ordinary browsing. Ordinary use of DuckDuckGo — as a search engine, or as a browser without pressing Fire — does not create, activate, or resemble a distinct "in-private" session at all; it is simply normal browsing with always-on ad-tracker blocking layered on top.

### 2.5 Direct answer to the CIMP-relevant question

**Does using DuckDuckGo have any effect on what a device-level, locally-installed monitoring application (the CIMP type) can observe?** No. A locally installed monitoring agent with access to the operating system, the browser process, or the device's network stack sees the same activity regardless of which search engine or tracker-blocking extension is running on top of the browser — DuckDuckGo's protections operate against a completely different threat model (commercial ad-tech infrastructure external to the device), not against software that already has privileged access to the device itself. Blocking a third-party ad-tracking script from loading on a webpage the user visits has no bearing on, and does not "hide" anything from, a monitoring tool that logs activity at the OS or browser-process level.

### 2.6 How this fits the motion

Item 5's ban on "any form of 'in-private' browsing" is most naturally read — and should be argued as properly limited — to reach only the browser-native private/incognito modes described in § 2.2 above (Chrome Incognito, Safari Private Browsing, Firefox Private Windows, and DuckDuckGo's own Fire Button/session-clearing feature, if and when actually invoked to purge locally stored data), because those are the only things that even arguably interact with what gets saved on the monitored device. Ordinary use of a privacy-respecting *search engine or browser* that merely blocks third-party ad-tracking (DuckDuckGo, in its default operating mode) does not implicate Probation's stated monitoring interest at all — by Google's own admission, even genuine incognito/private modes do not defeat device-level monitoring, so a fortiori a tool that isn't a private-browsing mode in the first place and doesn't even claim to defeat local monitoring cannot be read into that ban without turning Item 5 into a ban on privacy-conscious browsing generally, untethered from Special Condition (a)'s actual monitoring-integrity purpose. This supports the same request already outlined in Finding 4 of the CIMP-Agreement objections memo (Part I.D) — either strike Item 5 as surplusage/ultra vires under *Browder*, or have the Court/Probation confirm on the record that Item 5 reaches only browser-native private/incognito session modes and locally-invoked data-clearing tools, not privacy-respecting tools like DuckDuckGo used in their ordinary, always-on configuration.

---

## Sources Consulted

**Section 1 (SORA/Ellis):**
- People v. Ellis, 2019 NY Slip Op 05183 (N.Y. Ct. App. June 27, 2019) — case summaries/quotes drawn from: FindLaw case page (caselaw.findlaw.com/court/ny-court-of-appeals/1905915.html); New York Appellate Digest, "A Facebook Account Is Not An 'Internet Identifier' Within the Meaning of the Correction Law..." (newyorkappellatedigest.com, June 27, 2019); New York Appellate Lawyer blog, "Sex Offenders Required to Disclose Internet Identifiers, But Not Services on Which They Have Accounts" (newyorkappellatelawyer.com); New York Criminal Lawyer Blog 24/7, "New York Appellate Court Discusses Internet Access for Level 3 Sex Offender" (newyorkcriminallawyer24-7blog.com, Aug. 29, 2019); appellate-litigation.org case note on *The People v. Arthur W. Ellis Jr.*; Mitchell Hamline Sex Offense Litigation & Policy Resource Center case note.
- N.Y. Correction Law §§ 168-a(18), 168-f(4) — verbatim text via New York State Senate official codified-laws site, nysenate.gov/legislation/laws/COR/168-A and /168-F.
- Google Account help documentation: support.google.com/accounts/answer/27441 ("A Google Account gives you access to many Google products").
- Meta Help Center, "Manage connected experiences across your accounts in an Accounts Center," meta.com/help/accounts-center/469011081363524/.
- State v. White, No. 2011-770 (N.H. Dec. 7, 2012) — summary via Technology & Marketing Law Blog (Eric Goldman), blog.ericgoldman.org/archives/2012/12/sex_offender_on.htm.

**Section 2 (DuckDuckGo/private browsing):**
- Google Chrome Help, "Browse in Incognito mode," support.google.com/chrome/answer/95464.
- DuckDuckGo Help Pages: "How does DuckDuckGo protect my privacy?" (duckduckgo.com/duckduckgo-help-pages/company/how-does-duckduckgo-protect-privacy); "DuckDuckGo Web Tracking Protections" (duckduckgo.com/duckduckgo-help-pages/privacy/web-tracking-protections); Fire Button documentation (duckduckgo.com/duckduckgo-help-pages, Fire Button pages).

---

## NOT VERIFIED — DO NOT CITE YET

- **Exact official N.Y.3d reporter citation for *People v. Ellis*.** The neutral citation (2019 NY Slip Op 05183, Ct. App., June 27, 2019, Docket No. 54) is well-confirmed across independent sources; the print reporter volume/page (something in 33 N.Y.3d) was not independently confirmed — conflicting, low-confidence figures appeared in different search snippets. Pull the official reporter citation from Westlaw/Lexis before filing.
- **Primary slip-opinion text of *Ellis*.** Both nycourts.gov (403 Forbidden to automated fetch) and CourtListener (returned an empty/blocked response) could not be retrieved directly in this session. The holding above rests on convergent, consistent secondary-source quotation/paraphrase from six independent outlets, which is strong but not a substitute for reading the primary opinion. Pull the primary text before any filing quotes it directly.
- **Whether any New York case (as opposed to the bare statutory text and *Ellis*'s general reasoning) has ever addressed the specific "same Google/Meta login, new product" scenario.** None was located. The § 1.3 analysis is an extension by direct application of *Ellis* and the statutory text, not an on-point holding — disclose it as such in any drafted argument, exactly as this case's practice requires for analogous extensions (e.g., the Item 9/email-encryption discussion in the CIMP-Agreement memo).
- **"People v. Miller" as a source for any SORA internet-identifier proposition.** Searched extensively; no New York Court of Appeals (or any other court) decision by that name addressing internet-identifier registration was found. Several unrelated "People v. Miller" SORA risk-level-classification cases exist (Third and Fourth Department, various years) but none address internet identifiers. **Do not cite "People v. Miller" for this proposition in any filing.**
