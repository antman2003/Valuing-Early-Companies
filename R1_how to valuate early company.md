# Valuing Early Companies

*A practical guide for startup and early company investors*

---

## Preface

Early‑stage, high‑growth companies often report accounting losses for many years. Heavy investment in product development, customer acquisition, and infrastructure depresses current earnings, even when the underlying economics are attractive. This makes traditional price‑to‑earnings ratios unusable and forces investors to rely on alternative valuation approaches.

This short book grew out of practical questions from founders, early employees, and investors: **“How do we value a company that is growing fast but losing money?”** and **“Which method should I use in my situation?”** The chapters that follow distil ideas from corporate finance, venture capital, and real‑options theory into a pragmatic guide you can apply immediately to real early‑stage and growth companies (see Damodaran, 2012; Koller et al., 2010).

### How to Use This Book

- **If you are a founder or operator**, focus on the intuitive explanations and case studies. You do not need to memorise every formula; instead, aim to understand **which method applies to your stage** and what investors are looking for.
- **If you are an investor**, you can read sequentially or jump directly to the chapters that match your deal flow (for example, market multiples and DCF for later‑stage deals, or VC/Scorecard methods for seed rounds).
- **If you are a student of finance**, treat the book as a bridge between theory and practice. The maths is intentionally kept at a level accessible to motivated beginners, with notation explained around each formula.

Throughout, remember that these methods are **tools for disciplined thinking**, not precise forecasts. Real‑world valuations should blend methods and remain honest about uncertainty.

### Disclaimer

Nothing in this book constitutes personalised investment advice, a recommendation to buy or sell any security, or a guarantee of financial results. All examples are illustrative and simplified. Real companies are more complex, and any investment decision should consider your circumstances, risk tolerance, and local regulations. The author and publisher accept no responsibility for losses or outcomes arising from the use of this material.

---

### Introduction

Early‑stage, high‑growth companies often report accounting losses for many years. Heavy investment in product development, customer acquisition, and infrastructure depresses current earnings, even when the underlying economics are attractive. This makes traditional price‑to‑earnings ratios unusable and forces investors to rely on alternative valuation approaches.

This book reviews **widely used methods** for valuing such firms, organised **method‑by‑method**, from the most common to the more specialised. For each approach we outline how widely it is used, its historical roots, the core mathematics, foundations and key assumptions, a short case study, and its advantages and limitations. The goal is that, after reading, you can recognise **which method fits which type of early high‑growth company** and how to apply it in practice (see Damodaran, 2012; Koller et al., 2010).

---

## Chapter 1 – Market‑Based Revenue and Operating Metrics Multiples

### 1.1 Common usage and popularity

In practice, especially in **public markets and late‑stage private rounds**, revenue and operating‑metric multiples are probably the **most widely used** way to value high‑growth companies with negative earnings (FTI Consulting, n.d.; Damodaran, 2012). Analysts compare a target company to a peer set using metrics such as:

- \( EV/\text{Sales} \) (enterprise value to revenue),
- \( EV/\text{ARR} \) (for SaaS businesses),
- \( EV/\text{GMV} \) for marketplaces,
- value per active user, subscriber, or unit.

These multiples dominate **IPO pricing, M&A discussions and VC exit comparisons**, because they are simple and can be applied even when earnings are deeply negative.

### 1.2 Historical background

Multiples have been used informally for centuries (e.g., “x times annual rent” for property). In equity markets, **price‑to‑earnings (P/E)** emerged early in the 20th century. As growth companies with negative earnings became more common—especially during the **dot‑com boom** and later the **SaaS and platform era**—practitioners shifted toward **revenue‑based multiples** as a more stable anchor (Damodaran, 2012; “Valuation using multiples”, Wikipedia).

### 1.3 Mathematics

The basic multiple logic is:

\[
V_{\text{company}} \approx M_{\text{peer}} \times X_{\text{company}}
\]

where:

- \( X_{\text{company}} \) is a metric such as next‑year revenue, ARR, or GMV,
- \( M_{\text{peer}} \) is an observed multiple for comparable listed firms or recent transactions.

Analysts often adjust \( M_{\text{peer}} \) up or down based on **growth, margins, retention and risk** differentials.

### 1.4 Foundations and key assumptions

The foundations are:

- **Market‑efficiency logic**: the market prices of comparable companies contain information about what similar growth stories are worth.
- **Relative valuation**: instead of estimating intrinsic value directly, you assume “similar companies should trade on similar multiples.”

Key assumptions include:

- A **relevant peer group** with observable multiples exists.
- Differences in growth, profitability, and risk between the target and peers can be **reasonably adjusted**.
- Current multiples are not distorted by extreme **bubbles or panics**.

### 1.5 Case study (stylised)

Imagine a SaaS company with:

- current ARR \( = \$20\text{m} \),
- year‑on‑year ARR growth of \( 60\% \),
- strong net dollar retention (120%),
- negative earnings due to heavy R&D and sales investment.

Comparable listed SaaS companies with similar growth trade at a median of \( 10\times \) forward ARR. If you judge the target slightly riskier than peers, you might apply \( 8\times \):

\[
V_{\text{equity}} \approx 8 \times 20\text{m} = \$160\text{m}
\]

You can then cross‑check this range against other methods.

### 1.6 Advantages and limitations

- **Advantages**
  - **Very popular in practice**; easy to explain to boards and investors.
  - Grounded in **observable market data**, not just internal forecasts.
  - Works even when companies have **large negative earnings** but meaningful revenue or user metrics.

- **Limitations**
  - Quality of results depends heavily on **choice of comparables**.
  - Multiples can be distorted by **sentiment cycles**; what looks fair in a boom can be expensive later.
  - Less informative about **unit economics, capital intensity, or long‑term profitability**.

**When to use:** market‑based multiples are a good **starting point** for any high‑growth company with material revenue or usage metrics, especially when you need a quick benchmark or are close to IPO/M&A markets. Always combine them with at least one **intrinsic** or **scenario‑based** approach.

---

## Chapter 2 – Discounted Cash Flow (DCF) for Early‑Stage High‑Growth Companies

### 2.1 Common usage and popularity

DCF is the **theoretical backbone** of valuation: in corporate finance textbooks and among many professional investors, it is the primary intrinsic valuation framework (Damodaran, 2012; Koller et al., 2010; “Discounted cash flow”, Wikipedia). For early high‑growth companies, classic DCF is often **adapted**:

- Near‑term cash flows may be negative for several years.
- The discount rate is higher to reflect risk.
- More weight is placed on **terminal value** and long‑run economics.

It is perhaps **less commonly used alone** in very early VC deals, but widely used in **later‑stage growth equity, IPO research, and internal strategic planning**.

### 2.2 Historical background

DCF’s roots go back to **Irving Fisher** and the early 20th‑century development of the **time value of money** concept. It became mainstream in corporate valuation through work by **Modigliani and Miller** and later through modern corporate finance textbooks (for example, Brealey, Myers, and Allen; Damodaran, 2012; Koller et al., 2010). For loss‑making growth companies, DCF gained prominence as analysts needed to justify valuations beyond simple multiples.

### 2.3 Mathematics

The standard free cash flow DCF formula is:

\[
V_0 = \sum_{t=1}^{N} \frac{FCF_t}{(1 + r)^t} + \frac{TV_N}{(1 + r)^N}
\]

where:

- \( FCF_t \) = free cash flow in year \( t \),
- \( r \) = required rate of return (cost of capital or VC‑style required return),
- \( TV_N \) = terminal value once the company has reached a more stable phase.

For a growing company, the terminal value is often computed using a Gordon growth model:

\[
TV_N = \frac{FCF_{N+1}}{r - g}
\]

with \( g \) the long‑run growth rate (less than \( r \)).

### 2.4 Foundations and key assumptions

Foundations:

- **Cash‑flow primacy**: value equals the present value of all future free cash flows to capital providers.
- **Time value of money**: future cash flows are less valuable than current ones, discounted at rate \( r \).

Key assumptions:

- Management can articulate a **credible path to profitability** (unit economics, customer lifetime value, reinvestment needs).
- Cash flows can be **forecast at least in scenarios or ranges**.
- A discount rate \( r \) can be chosen to reflect risk (often \( 20\%–40\% \) in VC‑style deals).
- The business eventually reaches a **stable growth phase** with \( g < r \).

### 2.5 Case study (stylised)

Suppose a platform business has heavy upfront investment and expects the following free cash flows (FCF, in \$m):

- Years 1–3: \(-10, -8, -5\) (losses while scaling),
- Years 4–6: \(3, 10, 18\) (unit economics improve),
- Year 7 onwards: stabilisation at \( FCF_7 = 25 \) with long‑run growth \( g = 3\% \),
- Required return \( r = 20\% \).

The present value is:

\[
V_0 = \sum_{t=1}^{6} \frac{FCF_t}{(1 + 0.20)^t} + \frac{TV_6}{(1 + 0.20)^6}
\]

with:

\[
TV_6 = \frac{FCF_7}{r - g} = \frac{25}{0.20 - 0.03}
\]

This simple example highlights that **most of the value** may come from years 4+ and the terminal value, not the early losses.

### 2.6 Advantages and limitations

- **Advantages**
  - **Conceptually rigorous** and widely accepted in finance theory.
  - Forces detailed thinking about **drivers**: customers, pricing, margins, and reinvestment.
  - Can reflect **multiple stages**: early hyper‑growth, transition, and mature steady state.

- **Limitations**
  - Requires long‑horizon forecasts that are **highly uncertain** for early‑stage firms.
  - Small changes in terminal growth \( g \) or discount rate \( r \) can **dramatically change** the result.
  - Easy to produce a precise‑looking model that hides the **fragility of assumptions**.

**When to use:** adapted DCF is most useful when you have **some operating history**, a reasonably clear **path to profitability**, and want to understand the **economic engine** of the business. It is an excellent complement to multiples, especially for Series C+ or pre‑IPO companies.

---

## Chapter 3 – Venture Capital (VC) Method

### 3.1 Common usage and popularity

The VC method is **ubiquitous in early‑stage venture capital** (see, for example, Esinli, n.d.; “Venture capital method”, Wikipedia‑style summaries). Rather than modelling many years of detailed cash flows, investors:

- Focus on a **target exit value** in 5–10 years.
- Apply a **required return** (often 25–40%+ per year).
- Work backwards to a current valuation that makes sense for the fund.

It is particularly common in **Seed, Series A and B** rounds where outcome uncertainty is high and exit comparables are a natural reference point.

### 3.2 Historical background

The method was formalised in venture capital practice from the 1980s onward, as funds needed a simple framework to align **fund math** (portfolio returns, loss rates) with individual deal valuations (Sahlman, 1990). It is closely related to the idea that **a few large winners must pay for many failures** in a VC portfolio.

### 3.3 Mathematics

Steps:

1. Estimate potential exit revenue in year \( T \).
2. Apply an exit multiple (e.g., \( EV/\text{Sales} \)) to get the **exit enterprise value**.
3. Deduct debt and add cash to obtain the **exit equity value** \( V_{\text{exit}} \).
4. Apply a **probability of success** (often implicitly folded into a high required return).
5. Discount back at the **target annual return** \( R \).

If \( V_{\text{exit}} \) is the expected equity value at time \( T \), the VC’s post‑money valuation is:

\[
V_{\text{post}} = \frac{\mathbb{E}[V_{\text{exit}}]}{(1+R)^T}
\]

The **pre‑money valuation** is:

\[
V_{\text{pre}} = V_{\text{post}} - I
\]

where \( I \) is the amount invested in the round.

### 3.4 Foundations and key assumptions

Foundations:

- **Exit‑focused thinking**: the value of the investment is driven by the distribution of exit outcomes.
- **Portfolio logic**: most startups fail; required returns must cover many zeros.

Key assumptions:

- Investors can form a **plausible view** of exit timing and exit multiples.
- The required return \( R \) adequately compensates for **failure risk and illiquidity**.
- Dilution through future funding rounds is modelled or reflected in the target ownership stake.

### 3.5 Case study (stylised)

Assume:

- Target exit in 7 years.
- Expected exit equity value \( \mathbb{E}[V_{\text{exit}}] = \$500\text{m} \) (after considering a mix of success and failure scenarios).
- VC requires \( R = 30\% \) per year.

Then:

\[
V_{\text{post}} = \frac{500}{(1+0.30)^7}
\]

If the result is, say, about \$70m, and the VC plans to invest \$14m, then:

\[
V_{\text{pre}} = 70 - 14 = \$56\text{m}
\]

The VC would target roughly \( 14/70 = 20\% \) ownership post‑money.

### 3.6 Advantages and limitations

- **Advantages**
  - Matches how many **VC funds actually think** about deals.
  - Links **fund return targets** directly to deal pricing.
  - Easy to communicate: “If this becomes a \$X exit, at Y% ownership and Z% required return, this is what we can pay today.”

- **Limitations**
  - Highly sensitive to **exit multiple and timing** assumptions.
  - Often treats probability of success **implicitly**, which can obscure risk analysis.
  - Less informative about **operational levers** (unit economics, burn, etc.).

**When to use:** the VC method is ideal for **early funding rounds** where the key question is, “Given our required return and a plausible exit, what stake and valuation make sense?” It should be cross‑checked against **multiples** and, when possible, a basic **DCF**.

---

## Chapter 4 – First Chicago Method (Scenario‑Weighted Valuation)

### 4.1 Common usage and popularity

The First Chicago method is widely referenced in **venture capital and private equity**, particularly when valuation needs to reflect **highly skewed outcomes** (“First Chicago method”, Wikipedia). It is less common than simple multiples or VC method, but still well‑known among sophisticated investors.

### 4.2 Historical background

The approach was developed and popularised by the investment bank **First Chicago Corporation**, which used it to value venture investments by combining **scenario analysis** with more traditional DCF or multiple‑based valuations (“First Chicago method”, Wikipedia).

### 4.3 Mathematics

Practitioners define a small set of scenarios, for example:

- a **success** scenario,
- a **base‑case** scenario,
- a **failure** scenario.

Each scenario \( s \) has an associated valuation \( V_s \) (from DCF or multiples) and probability \( p_s \). The estimated value is:

\[
V_0 = \sum_{s} p_s \, V_s
\]

### 4.4 Foundations and key assumptions

Foundations:

- **Scenario thinking**: value is an average of distinct possible futures, not a single forecast.
- **Risk‑adjusted expectations**: probabilities weight each outcome.

Key assumptions:

- A small set of **discrete scenarios** can approximate the underlying uncertainty.
- Probabilities \( p_s \) can be assigned in a way that is at least **internally consistent**.
- Within each scenario, valuation relies on standard **DCF or multiples**, inheriting their assumptions.

### 4.5 Case study (stylised)

Suppose you value a fintech startup using three scenarios (equity values in \$m):

- Success: \( V_{\text{high}} = 600 \) with \( p_{\text{high}} = 0.25 \),
- Base: \( V_{\text{base}} = 150 \) with \( p_{\text{base}} = 0.50 \),
- Failure: \( V_{\text{low}} = 0 \) with \( p_{\text{low}} = 0.25 \).

Then:

\[
V_0 = 0.25 \times 600 + 0.50 \times 150 + 0.25 \times 0 = 150 + 75 = 225
\]

So a **scenario‑weighted value** of \$225m might be compared to market multiples and VC‑style required returns.

### 4.6 Advantages and limitations

- **Advantages**
  - Makes **uncertainty explicit** by listing good, base, and bad outcomes.
  - Encourages discussion of **downside risk**, not only upside.
  - Integrates easily with DCF and multiples.

- **Limitations**
  - Scenario probabilities are **judgement‑based** and can be biased.
  - Using only a few scenarios may **oversimplify** a richer distribution of outcomes.
  - Still relies on the quality of underlying **DCF or multiple** inputs.

**When to use:** First Chicago is useful when you want a **structured discussion of upside and downside**, for example in investment committees or board meetings, especially for companies with **binary regulatory or product risks**.

---

## Chapter 5 – Qualitative Early‑Stage Methods: Scorecard and Berkus

### 5.1 Common usage and popularity

These methods are popular in **angel investing and very early seed rounds**, particularly when there is **little or no revenue** and almost no financial history (Berkus, 2016; Payne, 2011). They are less used by institutional growth investors but common among experienced angels and accelerators.

### 5.2 Historical background

The **Berkus method** was introduced by angel investor **Dave Berkus**, who proposed allocating fixed dollar amounts to key qualitative milestones (idea, prototype, team, strategic relationships, etc.) (Berkus, 2016). The **Scorecard method** evolved as angels sought a more structured way to compare new deals with **recent local financings** (Payne, 2011; Allied Venture Partners, n.d.).

### 5.3 Mathematics

- **Berkus method (simplified)**: assign up to a fixed amount (e.g., \$0.5–1m each) to categories such as:
  - sound idea,
  - prototype or MVP,
  - quality management team,
  - strategic relationships,
  - product rollout or early traction.

  The valuation is the **sum** of these assigned amounts.

- **Scorecard method (simplified)**:
  1. Start from a **median valuation** of comparable funded startups in the same region and stage (e.g., \$6m pre‑money).
  2. Score the target on factors like team, market, product, competition, and need for additional capital.
  3. Apply **weighted multipliers** to adjust the baseline up or down (e.g., if the team is above average, multiply by 1.2; if market size is below average, multiply by 0.8).

### 5.4 Foundations and key assumptions

Foundations:

- **Qualitative drivers matter early**: team quality, market size, and product strength are leading indicators of success.
- **Deal benchmarks** in the ecosystem give a reasonable starting point.

Key assumptions:

- Recent deals in the same region and sector provide a **representative baseline** valuation.
- Qualitative factors can be **scored consistently** across companies.
- These scores correlate with future economic outcomes.

### 5.5 Case study (stylised)

Imagine a pre‑revenue AI startup. Recent seed‑stage AI deals in the region price at a median of \$8m pre‑money. You apply the Scorecard method:

- Team: above average (1.2×),
- Market: very large (1.3×),
- Product: early but promising (1.0×),
- Competition: intense (0.9×),
- Need for capital: high (0.9×).

The composite multiplier might be around \( 1.2 \times 1.3 \times 1.0 \times 0.9 \times 0.9 \approx 1.27 \). The indicated valuation is then:

\[
V_{\text{pre}} \approx 8\text{m} \times 1.27 \approx \$10.2\text{m}
\]

### 5.6 Advantages and limitations

- **Advantages**
  - Works when there is **almost no financial data**.
  - Focuses attention on **team, market and traction**, which often matter most at this stage.
  - Simple and intuitive for angels and founders.

- **Limitations**
  - Highly **subjective**; results vary widely between investors.
  - Dependent on **recent deal benchmarks**, which may be inflated or depressed.
  - Provides a **rough range**, not a detailed intrinsic valuation.

**When to use:** scorecard and Berkus‑type methods are best for **very early, pre‑revenue companies** where any DCF or multiple‑based valuation would be pure guesswork. They give a **sanity range** rather than a precise answer.

---

## Chapter 6 – Real Options and the Datar–Mathews Approach

### 6.1 Common usage and popularity

Real options and the Datar–Mathews method are less widely used than the previous approaches; they are most common among **quantitatively oriented investors** and in **capital‑intensive, R&D‑heavy sectors** (e.g., biotech, deep tech, energy) (Datar & Mathews, 2004; “Datar–Mathews method for real option valuation”, Wikipedia). They are powerful when managerial **flexibility to abandon or expand** is a major source of value.

### 6.2 Historical background

Real options theory extends financial option pricing (e.g., **Black–Scholes**) to real investment projects. The **Datar–Mathews method** provides a practical Monte‑Carlo‑based framework to value startup opportunities as options on future cash flows or exit values (Datar & Mathews, 2004).

### 6.3 Mathematics

The Datar–Mathews approach:

- Simulates many possible future business outcomes (e.g., exit equity values) using probability distributions for key drivers.
- Computes the **net present value (NPV)** of each simulated path.
- Truncates negative NPVs at zero, because the investor can abandon or avoid follow‑on funding.
- Values the opportunity as the **average of positive NPVs** (similar to a call option).

If \( NPV_i \) is the NPV of scenario \( i \), the option value is:

\[
V_0 = \frac{1}{N} \sum_{i=1}^{N} \max(NPV_i, 0)
\]

### 6.4 Foundations and key assumptions

Foundations:

- **Option‑like payoff**: downside is limited to invested capital; upside can be very large.
- **Managerial flexibility**: the ability to abandon, delay, or expand projects adds value.

Key assumptions:

- Key drivers (market size, adoption, pricing, margins) can be modeled as **stochastic variables**.
- Management will act **rationally**, abandoning poor paths and doubling down on promising ones.
- Simulated distributions are **calibrated to realistic ranges**, not arbitrary guesses.

### 6.5 Case study (stylised)

Consider a deep‑tech startup where:

- There is a significant chance of **technical failure** (zero value).
- If technical milestones are achieved, potential exit values range from modest to very large.

By simulating thousands of future paths for revenues, margins and exit multiples, you obtain a distribution of NPVs. Many simulations are negative (projects you would rationally abandon), while a minority are highly positive. Truncating at zero and averaging the positives yields an **option value** that can guide whether the **initial investment** is attractive relative to its cost.

### 6.6 Advantages and limitations

- **Advantages**
  - Explicitly captures **asymmetric payoff and managerial flexibility**.
  - Well‑suited to **R&D‑intensive or platform** businesses with highly skewed outcomes.
  - Provides a rich view of the **full distribution** of outcomes.

- **Limitations**
  - Requires **quantitative modelling skills** and good data to calibrate.
  - Can appear “black box” to decision‑makers unfamiliar with option theory.
  - Sensitive to assumptions about volatility, correlations and decision rules.

**When to use:** real options analysis is most useful for **large, staged investments** with major technical or regulatory risk, where the ability to **stop, defer, or expand** materially changes value (e.g., drug development, major infrastructure, deep‑tech platforms).

---

## Chapter 7 – Summary and Practical Takeaways

After reviewing these methods, you can think of valuation for early high‑growth companies as choosing the **right tool for the specific case**, then cross‑checking results:

- **Very early, pre‑revenue**: start with **Scorecard/Berkus** to get a rough range, informed by local deal benchmarks. Use qualitative factors (team, market, technology) as the main drivers.
- **Early revenue but still loss‑making**: combine **revenue/metric multiples** (for a quick market check) with a **simple DCF** based on unit economics and a credible path to profitability.
- **Later‑stage high‑growth (pre‑IPO or growth equity)**: lean more on **adapted DCF** (to capture long‑term economics) and use **market multiples** to ensure the valuation is consistent with trading comps.
- **VC portfolio decisions in seed/Series A**: use the **VC method** and, where helpful, **First Chicago** scenarios to connect exit distributions and required fund returns to today’s price.
- **Deep‑tech or staged R&D projects**: consider **real options / Datar–Mathews** to value the flexibility to abandon or expand.

Across all cases:

- **Blend methods, don’t rely on one number.** Use at least one **relative** (multiples) and one **intrinsic or scenario‑based** approach.
- **Be explicit about assumptions.** Document growth, margins, discount rates, exit multiples, and probabilities; test how sensitive value is to each.
- **Focus on education and transparency.** These frameworks are tools to reason about value under uncertainty, not guarantees of investment success or personalised financial advice.

---

## References

- Allied Venture Partners. (n.d.). *How to Value Your Early‑Stage Startup — Scorecard Method*. Retrieved from `https://www.allied.vc/guides/how-to-value-your-early-stage-startup`
- Berkus, D. (2016). *The Berkus Method: Valuing Startups*. Various blog posts and angel investing materials.
- Datar, V., & Mathews, S. (2004). *A Practical Method for Real Options Valuation Using Monte Carlo Simulation*. R&D Management, 34(1), 1–15.
- Damodaran, A. (2012). *Investment Valuation: Tools and Techniques for Determining the Value of Any Asset* (3rd ed.). John Wiley & Sons.
- Esinli. (n.d.). *How to Value a Startup With No Revenue: 5 Methods That Actually Work*. Retrieved from `https://esinli.com/`
- FTI Consulting. (n.d.). *Navigating the Complexities of Valuing Early‑Stage Companies*. Retrieved from `https://www.fticonsulting.com/`
- Koller, T., Goedhart, M., & Wessels, D. (2010). *Valuation: Measuring and Managing the Value of Companies*. John Wiley & Sons.
- Payne, B. (2011). *The Scorecard Valuation Method for Startups*. Angel Capital Association whitepaper.
- Sahlman, W. (1990). *The Structure and Governance of Venture‑Capital Organizations*. Journal of Financial Economics, 27(2), 473–521.
- “Datar–Mathews method for real option valuation.” *Wikipedia, The Free Encyclopedia*.
- “Discounted cash flow.” *Wikipedia, The Free Encyclopedia*.
- “First Chicago method.” *Wikipedia, The Free Encyclopedia*.
- “Valuation using multiples.” *Wikipedia, The Free Encyclopedia*.