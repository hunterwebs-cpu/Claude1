# Finding: Phone Lockscreen "This device belongs to your organization"

**Status: CONFIRMED** — verified directly from the client-supplied photo (Google
Drive, "Computer Rules" folder, uploaded 2026-08-11, file `1786398322445.jpg`), and
the underlying technical claim independently verified via WebSearch against Android's
own developer documentation.

## What the photo shows

Jeff's phone lockscreen (carrier: US Mobile), dated Sun, August 9, reads, directly
beneath the standard Android fingerprint-unlock icon:

> **"This device belongs to your organization"**

No company name is displayed — this is the generic, unbranded default version of the
message.

## What this actually is (verified)

This is **not** a custom message the CIMP monitoring vendor wrote to assert
ownership. It is Android's own built-in, non-customizable system text that
automatically appears on the lock screen whenever a Device Policy Controller app is
granted **"Device Owner" mode** — Android Enterprise's "fully managed device" tier,
the single most privileged level of device-management control Android's OS offers to
any app.

**The critical fact:** Android's own developer documentation states that fully
managed / Device Owner mode "can be used only on organization-owned (company-owned)
devices that are used for work." (Source: Android Developers, "Device control |
Android Enterprise," https://developer.android.com/work/dpc/device-management —
confirmed via WebSearch of Google's own documentation, corroborated by independent
MDM-vendor explainer sources describing the same mode.) A DPC app *can* customize the
lock-screen text with an actual company name and contact number for lost-device
recovery (e.g., "This phone belongs to [Company], call [number] if found") — the
generic, unbranded version Jeff's phone displays suggests no such customization was
configured, but the underlying enrollment mode itself is the same either way.

## Why this matters more than the message itself

The message is a symptom, not the injury. The real fact worth arguing is the
**enrollment method**: to install and run its monitoring software, whoever configured
Jeff's phone (Probation's CIMP vendor, presumably) used — or defaulted to — the one
Android management tier Google's own documentation reserves for devices an
organization actually owns. Device Owner mode grants sweeping technical control
substantially beyond passive monitoring: remote wipe, self-protection against
uninstallation, control over what other apps may be installed, and other
enterprise-management capabilities — a materially broader toolkit than what "install
any application as necessary to surveil all activity" (Special Condition (a)'s actual
text) requires or authorizes.

## How this should be used

Fold into the existing Part I.D ultra vires theory (Item 3 / device-authorization
discussion) as an additional, concrete fact — not a new constitutional theory. The
Takings Clause angle was already researched and correctly rejected (see
`ROKU-IOT-TAKINGS-RESEARCH.md`); this finding does not revive it. The point is
narrower and stronger: Special Condition (a) authorizes installing monitoring
software, not enrolling Jeff's personally-owned phone in the specific Android
management tier the platform itself defines as being for organization-owned
hardware. The method exceeds the authorization, evidenced by the device's own
operating system now telling him it "belongs to" someone else.

## NOT VERIFIED

- Which specific MDM/DPC product the CIMP vendor uses, and whether the generic
  (unbranded) lock-screen text reflects a deliberate configuration choice or simply
  that no organization name was ever entered into the enrollment profile.
- Whether Device Owner mode was strictly necessary to accomplish CIMP's monitoring
  goal, or whether a less privileged Android management tier (e.g., "Profile Owner"/
  work-profile mode, which coexists with a personal profile and does not carry the
  same "this device belongs to your organization" messaging or full-device control)
  would have sufficed. This is worth raising as a question in the motion — is full
  Device Owner enrollment "necessary," per Special Condition (a)'s own language, or
  merely convenient for the vendor — but should not be asserted as a settled fact
  without more information.
