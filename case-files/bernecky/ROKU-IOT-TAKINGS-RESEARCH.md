# Research Memo — Roku Technical Predicate, Comparator Smart Appliances, and Takings Clause Viability

**Case:** United States v. Jeffrey Bernecky, No. 6:18-CR-06018-DGL-MWP (W.D.N.Y.)
**Re:** As-applied challenge to the PO's total-app-lock on Bernecky's browser-less Roku TV under Special Condition (a) (CIMP)
**Status:** Research memo only — not for filing. Feeds into the CIMP-Agreement analysis in `CIMP-AGREEMENT-OBJECTIONS-MEMO.md` and the device-restriction argument already outlined in Part I.C of the pending motion.

---

## 1. Roku Technical Findings

### 1.1 Does stock Roku have a general web browser? — No, confirmed by Roku itself

Roku's own official support documentation states directly that Roku streaming players and Roku TVs "provide access to stream video and music from the internet" but the platform "does not provide the ability to browse the internet on your television." (Official Roku Support, "Does my Roku streaming device have an internet web browser?", https://support.roku.com/article/can-i-browse-the-internet — quoted verbatim via an independent technical review that pulled the same official language: Android Authority, "Does Roku have a web browser?", https://www.androidauthority.com/does-roku-have-a-web-browser-3259796/.)

Independent technology-press sources confirm this is a platform-wide characteristic, not model-specific: "None of Roku's streaming sticks, set-top boxes, or branded smart TVs include native web browsers," and Roku "removed" the rudimentary channel-store browsers that existed years ago and no longer allows developers to add them. (smarttvmaster.com, "No Internet Web Browser On Roku," https://smarttvmaster.com/how-to/web-browser-on-roku/.) This confirms the client's framing: "browser-less" describes Roku OS generally, not one idiosyncratic SKU.

### 1.2 Can a stock, unmodified Roku (no other device attached) reach Tor, P2P networks, or comparable illegal-material channels? — No for all three

**Tor:** No official or unofficial Tor browser exists for Roku OS. The only "Tor on a TV" project located (TorTV, https://dyne.org/software/tortv/) targets WDTV boxes on a different, Linux-based OS, and never left alpha. No comparable Roku project exists. The only path anyone proposes for viewing Tor content "on a Roku screen" is mirroring a phone/laptop that is itself running Tor — routing through a *second device*, not the Roku doing anything, and outside the "without connecting any other device" scope of this inquiry.

**P2P/BitTorrent:** No usable, distributable BitTorrent/Gnutella/eDonkey-style client exists for Roku. The most serious attempt found — a hobbyist's effort to cross-compile `ctorrent` for Roku, discussed on Roku's own developer forum (https://forums.roku.com/viewtopic.php?t=4275) — never reached a working state and required toolchain dependencies beyond consumer sideloading. Tools like "TorrenTV" do the P2P work on a separate machine/cloud service and merely *cast* the resulting video to the TV.

**Other channels (image boards, onion sites, encrypted P2P chat):** No source identifies any of these as reachable from stock Roku; each requires either general web rendering (same browser gap as Tor) or a general-purpose OS running arbitrary client software — neither of which Roku provides.

### 1.3 Does Roku lack a general-purpose sideloading mechanism outside the curated Channel Store? — Yes, confirmed, with a nuance worth disclosing

Every public Roku channel must pass a mandatory "certification review" — automated static-analysis and behavior-analysis tooling checking functional/design/performance requirements — before reaching the Channel Store. (Roku Developer Docs, "Certification testing," https://developer.roku.com/dev/docs/certification-testing.) Consumers cannot install arbitrary code through that store.

The only alternative is "Developer Mode," and Roku's own developer documentation (https://developer.roku.com/dev/docs/developer-mode; https://developer.roku.com/dev/docs/developer-setup) shows it is deliberately gated, not incidental:
- Requires a secret physical remote-control button sequence to even reveal the option.
- Requires accepting an SDK license and setting a developer web-server password.
- **Requires a second device**: loading any code onto the Roku requires opening a browser on a *separate* computer/phone on the same local network and pushing a channel `.zip` package to the Roku's IP address through a local web interface — the Roku cannot sideload anything by itself.
- Disables normal automatic OS updates and is a conspicuous, non-default state.
- Violates Roku's consumer Terms of Use (§4.2, per multiple secondary sources).

**This is the key technical fact for the as-applied argument:** reaching Tor, a P2P client, or any unauthorized tool would require (1) deliberately triggering a hidden engineering mode via a non-obvious button sequence, (2) obtaining/writing installable code capable of the function (which, per §1.2, doesn't usably exist for Tor/P2P), and (3) using an entirely separate networked computer to push it on — categorically different from the "ordinary streaming app" risk (Apple TV, YouTube) the PIN lock actually gates.

**NOT VERIFIED — do not cite:** A low-quality SEO source claimed Roku's firmware blocks unsigned code "at the bootloader level." This more technical-sounding claim was not corroborated by any primary or reputable source and should be dropped; the certification-gate + hidden-Developer-Mode + external-device-required + ToS-violation facts above are independently sufficient without it.

---

## 2. Three Comparator Smart Appliances

Chosen to span categories and — deliberately — to include one honest counter-example, because the right test is functional capability, not device category.

### 2.1 Philips Hue smart lighting — no browser, no general internet access
The Hue Bridge talks to bulbs over a private Zigbee mesh separate from home Wi-Fi; "most Hue Bridge functions don't rely on the internet — your bridge just needs a local network connection to connect to the mobile app," with internet used only for remote control/geofencing. (Philips Hue official FAQ, https://www.philips-hue.com/en-us/explore-hue/faq/controls/what-is-the-hue-bridge.) No display, no browser, no general file-transfer capability anywhere in the system.

### 2.2 iRobot Roomba (connected models) — no display, no browser, closed cloud/app architecture
Connected Roombas pair with the iRobot Home app, which "connects to the cloud to enable features like scheduling, cleaning history, and cleaning performance reports." (iRobot Customer Care, https://homesupport.irobot.com/s/article/17735; https://homesupport.irobot.com/app/answers/detail/a_id/9057.) The robot has no screen and no browsing capability; all connectivity is a closed pipe to iRobot's own cloud, mediated by iRobot's own app on a separate device.

### 2.3 Samsung Family Hub refrigerator — the honest counter-example: this one *does* have a real browser
Samsung's own support materials advertise general web browsing: "Ever thought you could browse the internet on your refrigerator? Well with the Samsung Family Hub refrigerator, now you can!" (Samsung Support, https://www.samsung.com/in/support/home-appliances/how-to-access-the-internet-on-your-family-hub-refrigerator/.) Independent review confirms a 21.5" touchscreen with a genuine browser and apps like YouTube. (Digital Trends review; Best Buy Q&A, https://www.bestbuy.com/site/questions/samsung-family-hub-24-2-cu-ft-3-door-french-door-refrigerator-stainless-steel/5728815/question/232e3f10-e472-3c8d-ab0a-6a1913088324.)

**Why this matters:** It empirically proves the client's functional-definition point. Two "smart appliances" (Hue, Roomba) have zero general browsing/file-transfer capability — structurally identical to Roku's posture. A third (Family Hub) is functionally a full internet terminal and should be treated like a computer for CIMP purposes despite being marketed as a "refrigerator." The line that matters is capability, not the marketing category.

---

## 3. Takings Clause Research — Candid Assessment

### 3.1 Bottom line
**No court appears to have addressed a Takings Clause challenge to a supervised-release computer-monitoring condition, compelled software installation, or a probation-officer/vendor-controlled device lock, in any circuit.** Extensive searching found nothing on point. This absence should be disclosed candidly if a Takings theory is even raised — it hasn't lost somewhere and become adverse precedent; it simply doesn't appear to have been tried in this fact pattern, which is itself informative.

### 3.2 Why the doctrine is a poor structural fit
Takings doctrine is built around two paradigms: (1) **physical takings** — permanent physical occupation of property by/for the government's benefit, *Loretto v. Teleprompter Manhattan CATV Corp.*, 458 U.S. 419 (1982) (confirmed via Justia primary source); and (2) **regulatory takings** — a regulation destroys economic value/use to the point of functional equivalence to a physical taking (*Penn Central* balancing). A condition restricting *how* a defendant may use a device he continues to own and possess is neither — he isn't dispossessed, the government isn't occupying the device for its own beneficial use, and the restriction doesn't destroy the device's value.

The forfeiture line confirms this from the opposite direction: even a complete, permanent *transfer of title* through civil forfeiture doesn't trigger Takings Clause scrutiny — "the government may not be required to compensate an owner for property which it has already lawfully acquired under the exercise of governmental authority other than the power of eminent domain." *Bennis v. Michigan*, 516 U.S. 442, 452 (1996) (confirmed via Justia/FindLaw). If losing title outright isn't a taking, a temporary use-restriction on a device the defendant still owns is a weaker candidate still. Courts deciding this exact recurring fact pattern (probation restricting use of a defendant's own device) have consistently reached for liberty/administrative-law doctrine instead — Fourth Amendment special-needs (*Lifshitz*), delegation/ultra vires (*Kunz*, *Birkedahl*, *Matta*, *Browder* — already this case's spine), vagueness (*Reeves*), and § 3583(d) parsimony — never the Takings Clause.

### 3.3 The "ICCP claims to own the device" fact pattern — legal analysis, conditioned on unconfirmed fact
Treating the ownership-screen fact as unconfirmed (per the client's own framing, pending a photo):

- **If it's a software-license/EULA-style or MDM-style "this device is managed by [Company]" assertion** — not a taking at all. The right vehicle is the **ultra vires "exceeds the Judgment's text" theory already used throughout this case**: Special Condition (a) authorizes Probation to "install any application as necessary to surveil all activity," not to have its vendor assert an ownership interest in Bernecky's hardware. This is a *Browder*/*Kunz*-style argument, not a constitutional taking.
- **If read literally as an actual title-transfer claim** — the better doctrinal homes are (1) the same ultra vires theory (no Judgment provision or statute authorizes a vendor to divest Bernecky of title as an incident of CIMP enrollment), (2) a state-law **conversion**/declaratory-judgment theory (a private company unilaterally asserting ownership it has no basis for is a property dispute, not a constitutional one), and only as a backstop (3) **procedural due process** (notice/opportunity-to-contest that specific incident, separate from whether the underlying restriction was authorized at all).

**Recommendation: do not plead a Takings Clause claim.** It is unlikely to survive a threshold screen, there is no supporting authority, and it risks diluting the credibility of the already-verified, proven ultra vires/delegation theory (*Kunz*'s single-device holding, etc.) this case is built on. If the photo confirms an ownership-assertion screen, fold that fact into the existing Part I.D ultra vires argument as one more example of CIMP-vendor overreach — not a new constitutional count.

**NOT VERIFIED:** the underlying fact that ICCP's software displays any device-ownership screen (awaiting client photo); no case was found on either side of a Takings theory in this fact pattern — the absence itself is the finding.

---

## 4. Recommended Fold-In: A Functional Definition of "Internet Capable Device"

Proposed language for the motion:

> For purposes of Special Condition (a) and the CIMP Agreement, an "internet capable device" warranting the full CIMP monitoring/pre-approval regime is a device that provides the user with **general-purpose web browsing capability, a general-purpose application-installation mechanism reachable by an ordinary user, or general-purpose file-transfer/peer-to-peer capability** — i.e., a realistic, ordinary-use pathway to reach arbitrary internet content or exchange arbitrary files. A device whose internet connectivity is limited to a manufacturer-curated application/channel store and a closed cloud service, with no general browser and no ordinary-user path to install software outside that curated store, does not present the same risk profile and should not be subject to restrictions (such as a total app-installation PIN-lock) beyond what is needed to police the specific, identifiable risk the device does present.

Support for each element:
1. **Not result-driven** — tracks a real technical distinction, proven by the Hue/Roomba (closed) vs. Family Hub (open) contrast in §2; the Family Hub example shows the test does real work rather than just waving every gadget through.
2. **Matches Roku's documented architecture** — no browser, certified/curated store only, no usable Tor/P2P path without leaving the curated environment and involving a second device (§§1.1–1.3).
3. **Gives Probation a real, retained tool short of a blanket lock**: under this definition, the legitimate interest (keeping Bernecky off Tor/P2P/browsers) is fully served by a **defined prohibited-app list** (Tor/Orbot-style proxy apps, VPN apps, any browser channel, any P2P/torrent channel) triggering a violation if installed — because on a closed platform like this, the actual channel of concern is nameable and finite. A pre-approval gate on the entire category of "any app at all" is not "reasonably necessary" under § 3583(d) once that's true. Pitch it as a *Kunz*-style right-sizing/narrowing construction, not a demand to strip Probation's authority.
4. **Honest about its limits** — disclose the Family Hub counter-example; the operative line is functional capability, not the "smart appliance" label, and any proposed order should say so explicitly to avoid inviting a broader (and false) "all IoT devices are safe" reading.

**Drafting note:** Present §§1–2 as judicially-noticeable technical background (citable to manufacturer/support sources, same posture as the RFC/encryption discussion elsewhere in this case's CIMP memo — not in a Table of Authorities), and present §4 as the operative ask.

---

## Citation Status Summary

**Confirmed (primary or directly-quoted manufacturer/court source):** Roku's official no-browser position; Roku Developer Docs on certification and Developer Mode mechanics; Philips Hue Bridge architecture; iRobot Roomba cloud/app architecture; Samsung Family Hub browser capability; *Loretto v. Teleprompter Manhattan CATV Corp.*, 458 U.S. 419 (1982); *Bennis v. Michigan*, 516 U.S. 442 (1996).

**NOT VERIFIED — do not cite:** Roku "bootloader-level" unsigned-code-blocking claim (low-quality source only); any case addressing a Takings Clause challenge to a supervised-release monitoring/software-installation condition (none found — absence is the finding); whether ICCP's software actually displays a device-ownership screen (pending client photo).
