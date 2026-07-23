<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Free Federal Sentencing Calculators | Surviving the Feds</title>
  <meta name="description" content="Free federal sentencing calculators: guideline range, FSA First Step Act time credits, BOP security level, USSC sentencing statistics, and printable guideline reference sheets. Built by someone who served 20 years inside." />
  <meta name="theme-color" content="#0A0B0E" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="Free Federal Sentencing Calculators | Surviving the Feds" />
  <meta property="og:description" content="Federal sentencing guideline calculator, FSA time credits calculator, BOP security level estimator, and USSC sentencing statistics — all free, built by someone who lived it." />
  <meta property="og:image" content="https://survivingthefeds.com/assets/img/logo.png" />
  <meta property="og:url" content="https://survivingthefeds.com/calculators.php" />

  <!-- Canonical -->
  <link rel="canonical" href="https://survivingthefeds.com/calculators.php" />
  <!-- Schema: SoftwareApplication for each tool -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Free Federal Sentencing Calculators",
    "description": "Free calculators for people facing federal sentencing: guideline range calculator, FSA First Step Act time credits calculator, BOP security level estimator, and USSC sentencing statistics viewer.",
    "url": "https://survivingthefeds.com/calculators.php",
    "publisher": {
      "@type": "Organization",
      "name": "Surviving the Feds",
      "url": "https://survivingthefeds.com"
    },
    "hasPart": [
      {
        "@type": "SoftwareApplication",
        "name": "Federal Sentencing Guideline Range Calculator",
        "applicationCategory": "CalculatorApplication",
        "description": "Enter your adjusted offense level and criminal history points to get your estimated federal sentencing guideline range from the official U.S. Sentencing Commission table.",
        "url": "https://survivingthefeds.com/start-here.php#guideline",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
      },
      {
        "@type": "SoftwareApplication",
        "name": "FSA First Step Act Time Credits Calculator",
        "applicationCategory": "CalculatorApplication",
        "description": "Check FSA eligibility and estimate First Step Act time credits plus good time credits to find an earliest release date.",
        "url": "https://survivingthefeds.com/start-here.php#fsa",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
      },
      {
        "@type": "SoftwareApplication",
        "name": "BOP Security Level Designation Calculator",
        "applicationCategory": "CalculatorApplication",
        "description": "Estimate your Bureau of Prisons security level designation using the 7 scoring factors BOP uses — minimum, low, medium, or high security.",
        "url": "https://survivingthefeds.com/start-here.php#bop",
        "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
      }
    ]
  }
  </script>

  <!-- FAQ Schema for AI / featured snippet -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "How do I calculate my federal sentencing guideline range?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Your federal sentencing guideline range is determined by two numbers: your total adjusted offense level (1–43) and your criminal history category (I–VI). Enter both into the Federal Sentencing Guideline Range Calculator above to get your estimated range from the official U.S. Sentencing Commission sentencing table. Your attorney calculates the offense level by adding a base offense level for your charge, then applying enhancements and reductions including a 2–3 point reduction for acceptance of responsibility if you plead guilty."
        }
      },
      {
        "@type": "Question",
        "name": "How much time can you get off with the First Step Act (FSA)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Under the First Step Act (18 U.S.C. § 3632), eligible inmates earn 10–15 days of time credits for every 30 days they participate in evidence-based recidivism reduction (EBRR) programs. Minimum and low-risk inmates earn 15 days per 30 days; medium and high-risk inmates earn 10 days per 30. Credits are capped at 365 days. These are applied to early placement in prerelease custody (halfway house or home confinement) or to reduce supervised release by up to 12 months. Use the FSA Time Credits Calculator above to estimate the specific numbers for your sentence."
        }
      },
      {
        "@type": "Question",
        "name": "What determines your BOP security level?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Bureau of Prisons assigns a security level — minimum, low, medium, or high — based on a point system using 7 factors: (1) severity of the current offense, (2) prior violence history, (3) number of prior commitments, (4) immigration/detainer status, (5) escape history, (6) voluntary surrender, and (7) age. Scores 0–11 without public safety factors generally result in minimum security. Public safety factors (sex offense, 10+ year sentence, STG affiliation) can bump a minimum score to low. Use the BOP Security Level Calculator to estimate your designation."
        }
      },
      {
        "@type": "Question",
        "name": "What percentage of federal defendants get below the guideline range?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Nationally, about 53% of federal defendants are sentenced below their guideline range (FY2022 USSC data). However, the reasons and rates vary significantly by offense type: drug cases see 52% below range (largely through 5K1.1 cooperation motions), fraud cases see 40% below range (35% by judicial variance alone), and child pornography cases see 57% below range because many judges consider the guidelines overstacked. Use the Sentencing Statistics tool to see data specific to your offense type and offense level."
        }
      }
    ]
  }
  </script>
  <?php require '_head.php'; ?>
</head>
<body>

<?php $stf_page = 'calculators'; require '_nav.php'; ?>

  <main>

    <!-- ========================================================= HERO -->
    <section class="section" style="padding-top: clamp(72px, 8vw, 120px); padding-bottom: clamp(48px, 5vw, 80px);">
      <div class="container">
        <span class="eyebrow">Free Federal Sentencing Tools</span>
        <h1 style="font-size: clamp(2.2rem, 5vw, 3.6rem); line-height: 1.12; max-width: 18ch; margin: 20px 0 20px;">Federal Sentencing Calculators — Built for the people who need them.</h1>
        <p class="lead" style="max-width: 660px; margin-bottom: 0;">The tools attorneys use and charge thousands for. Built free — no login, no account, no charge.</p>
      </div>
    </section>

    <!-- ===================================================== TOOLS GRID -->
    <section class="section section--alt" id="tools">
      <div class="container">
        <div class="sec-head" data-reveal>
          <span class="eyebrow">The Calculators</span>
          <h2>Five tools. Every number that matters at sentencing.</h2>
          <p class="lead">The federal sentencing system runs on numbers — offense levels, criminal history points, sentence months, time credits. These calculators let you work through those numbers before your attorney does, so you can ask better questions and understand the answers.</p>
        </div>

        <!-- Tool 08: Guideline Range -->
        <article class="calc-tool-card" id="tool-guideline" data-reveal>
          <div class="calc-tool-body">
            <div class="calc-tool-head">
              <h2 class="calc-tool-title">Federal Sentencing Guideline Range Calculator</h2>
              <span class="calc-tool-tag">§5A Sentencing Table</span>
            </div>
            <p class="calc-tool-desc">The U.S. Sentencing Commission publishes a 43×6 table that every federal judge starts with. Your offense level (1–43) on one axis, your criminal history category (I–VI) on the other — the intersection is your guideline range in months. This calculator does that lookup instantly.</p>
            <div class="calc-tool-answers">
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What is my guideline range in months?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> How many criminal history points do I have?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> How does acceptance of responsibility change the level?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What does my range look like in years instead of months?</div>
            </div>
            <div class="calc-tool-note">
              <strong>How to use it:</strong> Ask your attorney for the "total adjusted offense level" and "criminal history points" — or estimate them yourself. The calculator accepts both inputs and shows the official range. Err on the high side when estimating — assume a higher level until your attorney confirms the actual calculation.
            </div>
            <a class="btn btn--primary calc-tool-cta" href="start-here.php#guideline">
              Use Calculator →
            </a>
          </div>
        </article>

        <!-- Tool 09: Sentencing Statistics -->
        <article class="calc-tool-card" id="tool-stats" data-reveal>
          <div class="calc-tool-body">
            <div class="calc-tool-head">
              <h2 class="calc-tool-title">Federal Sentencing Statistics — USSC Data</h2>
              <span class="calc-tool-tag">USSC FY2022 Data</span>
            </div>
            <p class="calc-tool-desc">The U.S. Sentencing Commission publishes data on every federal sentence. This tool shows you what actually happened at sentencing for people in your offense category — what percentage were sentenced within range, below range through cooperation, below range through judicial variance, and above range. Plus the median sentence.</p>
            <div class="calc-tool-answers">
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What percentage of people in my offense type got below the guideline range?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What was the median sentence for drug trafficking / fraud / firearms cases?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> How much does cooperation (5K1.1) affect outcomes in cases like mine?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What does the data show for defendants at my specific offense level?</div>
            </div>
            <div class="calc-tool-note">
              <strong>Important context:</strong> These are national averages — not predictions. A 38% below-range rate for drug cases means 38% of drug defendants nationally got below range, for many different reasons including cooperation, Fast Track programs, and individual judge decisions. The data helps you understand the landscape, not guarantee a result.
            </div>
            <a class="btn btn--primary calc-tool-cta" href="start-here.php#stats">
              View Statistics →
            </a>
          </div>
        </article>

        <!-- Tool 10: FSA Time Credits -->
        <article class="calc-tool-card" id="tool-fsa" data-reveal>
          <div class="calc-tool-body">
            <div class="calc-tool-head">
              <h2 class="calc-tool-title">FSA Time Credits Calculator — First Step Act</h2>
              <span class="calc-tool-tag">18 U.S.C. § 3632</span>
            </div>
            <p class="calc-tool-desc">The First Step Act of 2018 created a system where eligible inmates earn time credits for participating in evidence-based programming. Minimum and low-risk inmates earn 15 days per 30 days of programming. Medium and high-risk earn 10 days per 30. Credits are capped at 365 days and can be applied to reduce time in custody or supervised release. This calculator checks eligibility first — many offense types are excluded by law.</p>
            <div class="calc-tool-answers">
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> Is my offense eligible for FSA time credits?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> How many days of FSA credits can I earn on my sentence?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What is my earliest possible release date with FSA + good time credits?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> How does my PATTERN risk level affect how much I earn?</div>
            </div>
            <div class="calc-tool-note">
              <strong>Good time credits are separate:</strong> Under 18 U.S.C. § 3624(b), every eligible federal inmate earns 54 days per year of the sentence regardless of FSA eligibility. This calculator shows both — the total picture of what can reduce actual custody time.
            </div>
            <a class="btn btn--primary calc-tool-cta" href="start-here.php#fsa">
              Use Calculator →
            </a>
          </div>
        </article>

        <!-- Tool 07: BOP Security Level -->
        <article class="calc-tool-card" id="tool-bop" data-reveal>
          <div class="calc-tool-body">
            <div class="calc-tool-head">
              <h2 class="calc-tool-title">BOP Security Level Designation Calculator</h2>
              <span class="calc-tool-tag">Bureau of Prisons Form BP-337</span>
            </div>
            <p class="calc-tool-desc">The Bureau of Prisons designates every inmate to a security level — minimum, low, medium, or high — using a point system called the Security Designation and Custody Classification form (BP-337). Seven factors are scored: offense severity, prior violence history, prior federal commitments, immigration detainer, escape history, voluntary surrender, and age. This calculator walks through all seven and estimates the result.</p>
            <div class="calc-tool-answers">
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> Will I be designated to a minimum security camp or a low / medium / high security prison?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What factors are pushing my security level higher than it should be?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> Does an ICE detainer affect my security designation?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What is a Public Safety Factor and how does it affect designation?</div>
            </div>
            <div class="calc-tool-note">
              <strong>Voluntary surrender helps:</strong> Defendants who self-surrender score significantly lower on the surrender factor than those taken into custody. This is one of the few designation factors you can still influence at the time of sentencing — discuss it with your attorney.
            </div>
            <a class="btn btn--primary calc-tool-cta" href="start-here.php#bop">
              Use Calculator →
            </a>
          </div>
        </article>

        <!-- Tool 11: Reference Sheets -->
        <article class="calc-tool-card" id="tool-refsheets" data-reveal>
          <div class="calc-tool-body">
            <div class="calc-tool-head">
              <h2 class="calc-tool-title">Printable Federal Sentencing Guideline Reference Sheets</h2>
              <span class="calc-tool-tag">7 Major Guidelines</span>
            </div>
            <p class="calc-tool-desc">The federal sentencing guidelines are notoriously complex — but for each offense type, the structure is knowable. These reference sheets break down seven major guidelines: fraud (§2B1.1), drug trafficking (§2D1.1), child pornography (§2G2.2), immigration reentry (§2L1.2), firearms (§2K2.1), money laundering (§2S1.1), and robbery (§2B3.1). Each sheet shows how the score is built, a worked example at a realistic offense level, and specific questions to ask your attorney — on STF letterhead.</p>
            <div class="calc-tool-answers">
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What enhancements apply to my fraud / drug / firearms case?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What questions should I ask my attorney about the sentencing calculation?</div>
              <div class="calc-tool-q"><span class="calc-q-mark">?</span> What does a worked example look like for someone in a situation like mine?</div>
            </div>
            <div class="calc-tool-note">
              <strong>Print it and bring it to the visit:</strong> These sheets are designed to print on a single page — bring them to your next attorney meeting and work through the questions together. Understanding the calculation is how you verify your attorney is fighting for every point.
            </div>
            <a class="btn btn--primary calc-tool-cta" href="start-here.php#refsheets">
              Open Reference Sheets →
            </a>
          </div>
        </article>

      </div>
    </section>

    <!-- ======================================================= DISCLAIMER -->
    <section class="section">
      <div class="container">
        <div class="narrow" style="margin: 0 auto;" data-reveal>
          <span class="eyebrow">Before you use these tools</span>
          <h2 style="font-size: 1.8rem; margin: 16px 0 20px;">These calculators are informational. Your attorney does the official calculation.</h2>
          <p class="lead">The guideline range calculator uses the official U.S. Sentencing Commission sentencing table — the same table your attorney and the judge will use. But the actual calculation for your specific case depends on case-specific facts that only your attorney knows: what the factual basis says, how the PSR calculates the offense level, whether any departures or variances apply, and what enhancements the government is pursuing.</p>
          <p style="color: var(--muted); margin-top: 18px; font-size: 1rem; line-height: 1.75;">Use these tools to understand the system and ask better questions — not to predict your outcome. The number that matters most is the one in the plea agreement and the PSR, confirmed by your attorney. <strong style="color: var(--text);">Always err on the high side when estimating.</strong></p>
        </div>
      </div>
    </section>

    <!-- ================================================= ROUTING PATHS -->
    <section class="section section--routing section--alt">
      <div class="container">
        <span class="eyebrow">More from Surviving the Feds</span>
        <div class="routing-paths">
          <a class="route-path" href="start-here.php" data-reveal>
            <span class="route-num">→</span>
            <div class="route-body">
              <strong>The Command Center</strong>
              <span>All tools, guides, and situation-specific answers in one place. Start here if this is all new.</span>
            </div>
            <svg class="route-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <a class="route-path" href="is-my-lawyer-any-good.php" data-reveal data-delay="1">
            <span class="route-num">→</span>
            <div class="route-body">
              <strong>Is My Lawyer Any Good?</strong>
              <span>Seven questions that separate the attorneys who fight from the ones who fold. Free.</span>
            </div>
            <svg class="route-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <a class="route-path" href="books.php" data-reveal data-delay="2">
            <span class="route-num">→</span>
            <div class="route-body">
              <strong>The Books</strong>
              <span>Pretrial to post-conviction — the complete map, written by someone who served 20 years and learned every piece of it.</span>
            </div>
            <svg class="route-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
        </div>
      </div>
    </section>

  </main>

  <!-- ============================================================ FOOTER -->

<?php require '_footer.php'; ?>

  <script>
    document.getElementById('year').textContent = new Date().getFullYear();
  </script>
</body>
</html>
