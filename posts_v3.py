"""Dated news and analysis posts ("Latest updates") for site-v3.

Posts use the same shape as a guide in guides_v3.py, plus:
  date      ISO date the post was published, e.g. "2026-10-13"
  kind      "update" (always)
The build lists posts newest first under "Latest updates" on guides.html, gives
them Article structured data with that date, and adds them to the sitemap and
llms files. Newest entries go at the TOP of POSTS.

Rules (see AUTOMATION.md): every fact comes from an official source linked in
"sources" (FINTRAC, Bank of Canada, Government of Canada, Revenu Québec, court or
legislation sites). Penalty amounts, names and dates are copied exactly from the
public notice. No speculation about why a business was penalized beyond what the
notice says. No invented statistics, quotes or client stories.
"""

from content_v3 import F_G4, F_REC_MSB, F_STR

L_PCMLTFA = "https://laws-lois.justice.gc.ca/eng/acts/P-24.501/FullText.html"
L_PCMLTFR = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-184/FullText.html"
F_AMP_NEW = "https://fintrac-canafe.canada.ca/pen/3-eng"
F_VC_IND = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/indicators-indicateurs/vc_mltf-eng"

POSTS = {}

# ------------------------------------------------------------------ 2026-11-03 Bank of Canada supervision update
# ------------------------------------------------------------------ 2026-11-03 BoC PSP supervision update recap
# Update post. Facts checked 3 November 2026 against the sources below; session remarks are attributed in the text.
BU1_ACT = "https://laws-lois.justice.gc.ca/eng/acts/R-7.36/FullText.html"
BU1_REGS = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2023-229/FullText.html"
BU1_MILE = "https://www.bankofcanada.ca/regulatory-oversight/retail-payments/retail-payments-supervision-key-milestones/"
BU1_ORIR = "https://www.bankofcanada.ca/wp-content/uploads/2024/02/operational-risk-and-incident-response.pdf"
BU1_INC = "https://www.bankofcanada.ca/wp-content/uploads/2024/02/Incident-notification.pdf"
BU1_SG = "https://www.bankofcanada.ca/wp-content/uploads/2024/02/safeguarding-end-user-funds.pdf"
BU1_SAT = "https://www.bankofcanada.ca/wp-content/uploads/2026/10/safeguarding-end-user-funds_self-assessment-tool.pdf"
BU1_FAQ = "https://www.bankofcanada.ca/2026/08/frequently-asked-questions-about-retail-payments-supervision/"
BU1_ENF = "https://www.bankofcanada.ca/regulatory-oversight/retail-payments/enforcement-decisions/"
BU1_NOV = "https://www.bankofcanada.ca/2026/06/bank-canada-begin-publishing-notices-violation-payment-service-providers/"
BU1_REVIEW = "https://www.bankofcanada.ca/2025/01/reviews-and-appeals/"
BU1_AR = "https://www.bankofcanada.ca/2024/10/annual-reporting/"
BU1_METRICS = "https://www.bankofcanada.ca/2024/10/annual-reporting-of-retail-payment-activity-metrics/"
BU1_CRIT = "https://www.bankofcanada.ca/2026/06/criteria-for-registering-payment-service-providers/"
BU1_ACQ = "https://www.bankofcanada.ca/2024/08/acquisitions-of-control-and-prescribed-changes/"
BU1_CHG = "https://www.bankofcanada.ca/2026/06/reporting-changes-to-registration-information/"
BU1_C3 = "https://laws-lois.justice.gc.ca/eng/AnnualStatutes/2026_3/FullText.html"
BU1_C30 = "https://www.parl.ca/legisinfo/en/bill/45-1/c-30"
BU1_STABLE = "https://gazette.gc.ca/rp-pr/p1/2026/2026-10-24/html/reg1-eng.html"
BU1_CDB = "https://gazette.gc.ca/rp-pr/p1/2026/2026-06-27/html/reg3-eng.html"
BU1_PC = "https://www.payments.ca/connect/membership/payment-service-provider-participation"

POSTS["bank-of-canada-psp-supervision-update-november-2026.html"] = dict(
    checked="3 November 2026",
    title="Bank of Canada PSP Supervision Update, 2 Nov 2026 | AML Canada",
    desc="What PSPs heard at the Bank of Canada PSP supervision update on 2 November 2026: priorities, safeguarding, enforcement, AI, fees, policy and 14 audience Q&As.",
    crumb="BoC supervision update, Nov 2026",
    h1="Bank of Canada PSP supervision update, 2 November 2026: what PSPs heard",
    lede="At its Bank of Canada PSP supervision update on 2 November 2026, the Bank told payment service providers (PSPs) that it expects full compliance with the Retail Payment Activities Act (RPAA) now, after its first year of supervision. Staff covered assessments, safeguarding, enforcement, AI risk, PSP Connect, annual reporting, cost recovery and policy, then answered 14 audience questions.",
    label="Update · RPAA",
    service="rpaa-compliance-program.html",
    kind="update",
    date="2026-11-03",
    takeaways=["Bank staff said every PSP should already comply, and an assessment starts with a request for information that asks for evidence of practice.",
               "As of 3 November 2026, all 13 published RPAA notices of violation carry a $0 penalty and concern late registration. Staff said penalties with amounts will follow.",
               "The next annual report is due March 31, 2027 for the 2026 calendar year, and staff signalled stricter enforcement for late filers.",
               "Assessment fees and the new digital wallet payment function were not in force on 3 November 2026. Bank staff said they expect fees to start in 2027."],
    sections=[
        ("glance", "What did the Bank of Canada cover at its 2 November 2026 PSP supervision update?", f"""          <p>The Bank of Canada held a virtual RPAA supervision update for PSPs on 2 November 2026, a little over a year after the operational risk, safeguarding and reporting requirements took effect on September 8, 2025, according to its <a href="{BU1_MILE}" rel="noopener">supervision milestones page</a>. Statuses below are as of 3 November 2026.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Segment</th><th scope="col">Main point</th><th scope="col">Next step or date</th></tr></thead>
            <tbody>
              <tr><th scope="row">Supervision priorities</th><td>Six recurring framework gaps</td><td>Assessments open with a request for information</td></tr>
              <tr><th scope="row">Safeguarding</th><td>Evidence for each account and a traceable ledger</td><td>Self-assessment tool, October 2026</td></tr>
              <tr><th scope="row">Enforcement</th><td>13 notices of violation, all $0, all for late registration</td><td>Penalties with amounts to be published</td></tr>
              <tr><th scope="row">AI</th><td>No new rules</td><td>Map AI use to your framework</td></tr>
              <tr><th scope="row">PSP Connect</th><td>Shared messages, several admins</td><td>New metrics screens</td></tr>
              <tr><th scope="row">Annual reporting</th><td>92% filed; section 4 errors</td><td>Due March 31, 2027</td></tr>
              <tr><th scope="row">Cost recovery</th><td>Fees not in force</td><td>Interim bill expected spring 2027</td></tr>
              <tr><th scope="row">Policy</th><td>Digital wallets, stablecoins, consumer-driven banking, Real-Time Rail</td><td>Finance Canada sets timing</td></tr>
            </tbody>
          </table></div>"""),
        ("priorities", "What are the Bank of Canada's supervision priorities for PSPs?", """          <p>Bank staff said every PSP should already comply with the operational risk and incident response requirements, and that supervision is risk-based and centred on end-user impact. Staff listed six areas where some PSPs fell short:</p>
          <ul>
            <li>yearly framework approval by the senior officer and any board (RPAR section 5);</li>
            <li>indicators for each integrity, confidentiality and availability objective;</li>
            <li>a yearly assessment of every third-party provider that supports a payment function;</li>
            <li>prescribed incident plan items, such as escalation and transaction status;</li>
            <li>monitoring for anomalous events;</li>
            <li>procedures another person could repeat.</li>
          </ul>
          <p>Staff walked through the assessment cycle: document request, review and questions, then findings in writing and a wrap-up meeting. Staff said "assessment readiness starts before an assessment begins." Our guide to <a href="rpaa-compliance-frameworks.html">RPAA compliance frameworks</a> covers each requirement.</p>"""),
        ("safeguarding", "What did the Bank say about safeguarding end-user funds?", f"""          <p>Bank staff said a safeguarding account holds end-user funds only, and a PSP should have evidence for each account that no right of set-off or compensation applies. Other points:</p>
          <ul>
            <li>Trust arrangements need trust documents and a legal opinion, described in the Bank's <a href="{BU1_FAQ}" rel="noopener">supervision FAQ</a>.</li>
            <li>Insurance or guarantee cover still requires segregation.</li>
            <li>Funds not placed on receipt are logged as a shortfall, under paragraphs 2.7 to 2.9 of the <a href="{BU1_SG}" rel="noopener">safeguarding guideline</a>.</li>
            <li>Staff called daily shortfall checks a best practice.</li>
          </ul>
          <p>The Bank's October 2026 <a href="{BU1_SAT}" rel="noopener">self-assessment tool</a> says it is voluntary and that completing it does not show compliance. Our <a href="rpaa-safeguarding-end-user-funds.html">safeguarding guide</a> explains the rules.</p>"""),
        ("enforcement", "How is the Bank of Canada enforcing the RPAA?", f"""          <p>Bank staff described a graduated approach that usually starts with supervision and escalates when that fails or a case is serious. As of 3 November 2026, the Bank's <a href="{BU1_ENF}" rel="noopener">enforcement decisions list</a> shows 13 notices of violation, each with a $0 penalty, all for operating before registering as RPAA section 23 requires.</p>
          <p>Warning letters stay private. Under RPAA paragraph 76(2)(b), a compliance agreement can halve a penalty, and section 101 lets the regulations set penalties of up to $10 million per violation. According to staff, future notices will sometimes carry a dollar penalty, and those will be posted too. Late 2026 annual reports drew warning letters, and staff said the 2027 cycle will likely involve different tools.</p>"""),
        ("ai", "Are there AI-specific RPAA requirements for PSPs?", """          <p>No. Bank staff said existing RPAA and RPAR expectations continue to apply as AI evolves, so AI use sits inside the risk management and incident response framework a PSP already has. Staff named shadow AI, prompt injection, AI-made impersonation and shared model providers as risks. They stressed a named owner for each use case, narrow permissions, human reviewers who can stop an action, and logs that can reconstruct events.</p>"""),
        ("psp-connect", "What has changed in PSP Connect?", """          <p>Bank staff said portal messages are now visible to all of a PSP's authorized users, while automated messages still go to the primary contact. A PSP can have more than one organization admin to add and remove users. A bug that blocked registration information change submissions is fixed, and a fix for copying earlier answers into a change report is in progress.</p>"""),
        ("annual-report", "What did the first RPAA annual report cycle show?", f"""          <p>The first annual report drew filings from 92% of PSPs registered by late March 2026, Bank staff said, and the Bank followed up with the other 8% because not filing is a violation. Most errors were in section 4: blank fields, all-end-user totals lower than Canadian-only totals, and a misread electronic funds transfer definition.</p>
          <p>Under RPAR section 18, the 2026 report must reach the Bank by March 31, 2027. Staff said the new form flags incomplete or inconsistent entries and accepts figures pasted in bulk from a spreadsheet such as Excel. One staff member said: "The value of the information really depends on it being complete and accurate." See the Bank's <a href="{BU1_METRICS}" rel="noopener">metrics guidance</a> and our <a href="rpaa-annual-report.html">RPAA annual report guide</a>.</p>"""),
        ("fees", "When will PSPs pay RPAA assessment fees?", f"""          <p>Not yet. As of 3 November 2026, the RPAA's assessment fee sections (99 and 100) are not in force, and Bank staff said they expect cost recovery to start in 2027, subject to change. The <a href="{BU1_C30}" rel="noopener">Spring Economic Update 2026 Implementation Act</a>, which received Royal Assent on June 18, 2026, moves these powers into the Bank of Canada Act on a date to be set by order.</p>
          <p>On staff's timeline, a first invoice in spring 2027 would use the 2026 annual report figures, and its amount would come off the spring 2028 invoice. Staff did not say which figures will set the bill.</p>"""),
        ("policy", "Which policy changes affect PSPs next?", f"""          <p>Bank staff said the Department of Finance leads legislation and timing. Status as of 3 November 2026:</p>
          <ul>
            <li><strong>Digital wallets.</strong> The <a href="{BU1_C3}" rel="noopener">Budget 2025 Implementation Act, No. 1</a> (S.C. 2026, c. 3, s. 604) would add a payment function for maintaining an end user's tokenized payment instrument or private key. It is not yet in force.</li>
            <li><strong>Stablecoins.</strong> Proposed <a href="{BU1_STABLE}" rel="noopener">Stablecoin Regulations</a> appeared in the Canada Gazette, Part I, on October 24, 2026.</li>
            <li><strong>Consumer-driven banking.</strong> Proposed <a href="{BU1_CDB}" rel="noopener">regulations</a> appeared on June 27, 2026, for a framework overseen by the Bank.</li>
            <li><strong>Real-Time Rail.</strong> Payments Canada requires RPAA registration for <a href="{BU1_PC}" rel="noopener">PSP membership</a>. Staff said the rail should launch soon, phased through 2027.</li>
          </ul>"""),
        ("questions", "What did PSPs ask the Bank, and what did staff answer?", f"""          <p>These are the audience questions as read out, with light grammar cleanup.</p>
          <h3>When can we expect all applicants to be reviewed?</h3>
          <p>There is no set timeline, staff said, since each file passes to the Department of Finance, which coordinates the national security review, once the Bank is done. Sending a complete file the first time cuts delays.</p>
          <h3>What happens if PSPs that should be registered don't register? Is there any action the Bank of Canada can take? What should PSPs do if they see competitors in their vertical not registered as a PSP?</h3>
          <p>Staff said operating unregistered is a very serious violation and has drawn notices of violation. Concerns can go through the Bank's general inquiries form, though the Bank won't report back.</p>
          <h3>What operational threshold constitutes a material impact that requires an immediate incident report to the Bank?</h3>
          <p>Staff said an incident is reportable when it materially affects an end user, another PSP or a clearing house, whatever the root cause, and the <a href="{BU1_INC}" rel="noopener">incident notification guideline</a> gives examples. Notify the Bank and affected parties within 48 hours; see our <a href="rpaa-incident-reporting.html">incident reporting guide</a>.</p>
          <h3>As PSPs increasingly adopt AI for fraud detection, AML monitoring and risk management, how does the Bank view the balance between innovation, model risk, data protection and regulatory oversight?</h3>
          <p>Staff said the RPAA aims to support responsible innovation, while a PSP using AI stays answerable for the results. The Bank looks at outcomes and does not prescribe technologies.</p>
          <h3>What is the review and appeals process following a refusal of a registration application?</h3>
          <p>Request a review within 30 days after service, and appeal the review decision to the Federal Court within 30 days, according to the Bank's <a href="{BU1_REVIEW}" rel="noopener">reviews and appeals page</a>.</p>
          <h3>How does the Bank plan to align RPAA requirements with other Canadian regimes, such as FINTRAC and provincial money services business rules, to avoid duplicate obligations?</h3>
          <p>Staff said the mandates differ, and talks with FINTRAC and others have started, possibly toward a memorandum of understanding. Our <a href="rpaa-vs-fintrac-msb-registration.html">RPAA vs FINTRAC guide</a> compares them.</p>
          <h3>What are the biggest lessons that the Bank has learned so far? Have there been any surprises?</h3>
          <p>Staff said early compliance problems came as no surprise. They added that registration is activity-based and does not mean a PSP showed compliance before it was registered.</p>
          <h3>What will be the significant changes in oversight and regulation over the next 12 months?</h3>
          <p>Staff expect no major RPAA shifts, and named the assessment fee formula as the main new item.</p>
          <h3>Are there any examples, templates or best practice formats that the Bank of Canada recommends for documenting annual testing plans and procedures?</h3>
          <p>No. Staff said one format wouldn't suit every business model, so PSPs should follow the <a href="{BU1_ORIR}" rel="noopener">operational risk guideline</a>.</p>
          <h3>Is a payment facilitator between a merchant and acquirer subject to holding funds requirements if it settles to the merchant immediately? What if settlement occurs the next business day or once a week?</h3>
          <p>Staff said it depends on the facts: funds sent on with an immediate transfer instruction are generally not held, while funds kept for a predetermined future settlement date typically are. The Bank's <a href="{BU1_CRIT}" rel="noopener">registration criteria</a> explain the test.</p>
          <h3>How should PSPs handle changes in control, new owners or new key persons, and does the Bank need advance notice or approval?</h3>
          <p>An acquisition of control needs registration under a new application before closing (<a href="{BU1_ACQ}" rel="noopener">Bank policy</a>). Staff said new key persons need advance notice through PSP Connect and no approval.</p>
          <h3>What level of detail does the Bank expect in an incident report, and how does it want post-incident reviews handled?</h3>
          <p>Staff said to notify within 48 hours, add interim notices, and finish with a final notice giving the root cause and fixes. Staff expect a post-incident review.</p>
          <h3>For smaller or less complex PSPs, what would the Bank of Canada consider sufficient evidence to demonstrate compliance with the annual RPAA testing requirement?</h3>
          <p>Staff said scope and frequency can be proportionate and risk-based, and smaller PSPs still need thorough, documented testing.</p>
          <h3>What are the biggest challenges in moving from policy objectives on paper to operational frameworks that work in practice for both incumbents and innovators? How do you ensure that oversight supports innovation rather than slowing it down?</h3>
          <p>Staff said the two can coexist when rules stay workable, and the Bank coordinates with Finance and other regulators to limit duplication.</p>"""),
    ],
    faqs=[("What did the Bank of Canada say at its November 2026 PSP supervision update?", "At its 2 November 2026 update, the Bank said PSPs should already comply with the RPAA. Staff covered framework gaps, safeguarding, enforcement, AI, PSP Connect, annual reports, assessment fees and policy."),
          ("Has the Bank of Canada fined any PSPs under the RPAA?", "As of 3 November 2026, the Bank had published 13 notices of violation, all with a $0 penalty for late registration. Staff said penalties with amounts will follow."),
          ("When is the next RPAA annual report due?", "The 2026 report is due by March 31, 2027, under section 18 of the Retail Payment Activities Regulations."),
          ("Do PSPs pay RPAA assessment fees yet?", "No, not as of 3 November 2026. Bank staff said they expect fees from 2027, with interim bills in spring 2027, subject to change."),
          ("Is a registered PSP considered compliant by the Bank of Canada?", "No. Bank staff said registration brings a PSP into supervision. Compliance is checked afterwards through reporting and assessments.")],
    sources=[("Bank of Canada, Retail payments supervision key milestones", BU1_MILE),
             ("Bank of Canada, Operational risk and incident response guideline", BU1_ORIR),
             ("Bank of Canada, Incident notification guideline", BU1_INC),
             ("Bank of Canada, Safeguarding end-user funds guideline", BU1_SG),
             ("Bank of Canada, Safeguarding end-user funds: self-assessment tool", BU1_SAT),
             ("Bank of Canada, Retail payments supervision FAQ", BU1_FAQ),
             ("Bank of Canada, Enforcement decisions", BU1_ENF),
             ("Bank of Canada, Publishing notices of violation", BU1_NOV),
             ("Bank of Canada, Reviews and appeals", BU1_REVIEW),
             ("Bank of Canada, Annual reporting (supervisory policy)", BU1_AR),
             ("Bank of Canada, Annual reporting of retail payment activity metrics", BU1_METRICS),
             ("Bank of Canada, Criteria for registering payment service providers", BU1_CRIT),
             ("Bank of Canada, Acquisitions of control and prescribed changes", BU1_ACQ),
             ("Bank of Canada, Reporting changes to registration information", BU1_CHG),
             ("Retail Payment Activities Act", BU1_ACT),
             ("Retail Payment Activities Regulations", BU1_REGS),
             ("Budget 2025 Implementation Act, No. 1, S.C. 2026, c. 3", BU1_C3),
             ("Parliament of Canada, Bill C-30 (Spring Economic Update 2026 Implementation Act)", BU1_C30),
             ("Canada Gazette, Part I, Proposed Stablecoin Regulations", BU1_STABLE),
             ("Canada Gazette, Part I, Proposed Consumer-Driven Banking Regulations", BU1_CDB),
             ("Payments Canada, Payment service provider participation", BU1_PC)],
    related=["rpaa-compliance-frameworks.html", "rpaa-annual-report.html", "rpaa-safeguarding-end-user-funds.html"],
)


# ------------------------------------------------------------------ 2026-10-30 Necosmart penalty
P_NECO = "https://fintrac-canafe.canada.ca/pen/amps/pen-2026-05-14-eng"
P_NECO_NR = "https://fintrac-canafe.canada.ca/new-neuf/nr/2026-05-14-eng"
POSTS["fintrac-penalty-necosmart-virtual-currency-msb.html"] = dict(
    checked="30 October 2026",
    title="FINTRAC Penalizes Necosmart $693,742.50: MSB Lessons | AML Canada",
    desc="FINTRAC penalized Edmonton MSB Necosmart $693,742.50 for missed suspicious transaction reports, unapplied EDD and record gaps. Crypto MSB lessons.",
    crumb="Necosmart penalty",
    h1="FINTRAC penalizes Necosmart $693,742.50: what virtual currency MSBs can learn",
    lede="FINTRAC imposed a $693,742.50 administrative monetary penalty on 13010431 Canada Inc., also operating as Necosmart, a money services business in Edmonton, Alberta, for 5 violations found during a compliance examination. Two of the violations involve controls the business had written down but did not carry out.",
    label="Update · Penalties",
    service="compliance-programs.html",
    also=["outsourced-compliance-officer.html", "effectiveness-reviews.html"],
    date="2026-10-30",
    takeaways=["Necosmart failed to submit 4 suspicious transaction reports. In 3 of them it had spotted some indicators but did not take further measures, such as a holistic review.",
               "FINTRAC found that enhanced due diligence steps and risk mitigation measures in its documents were not carried out in practice.",
               "Its policies and procedures were incomplete and not tailored to how the business operated.",
               "FINTRAC counted 94 record keeping deficiencies in its virtual currency exchange transaction tickets."],
    sections=[
        ("summary", "What FINTRAC found", f"""          <p>FINTRAC published the <a href="{P_NECO}" rel="noopener">public notice</a> on May 14, 2026. It says FINTRAC imposed a penalty of $693,742.50 on 13010431 Canada Inc., also operating as Necosmart, a money services business in Edmonton, Alberta, on March 27, 2026, for 5 violations found during a compliance examination. The <a href="{P_NECO_NR}" rel="noopener">news release</a> refers to the business's virtual currency exchange transaction tickets, so the lessons are most relevant to MSBs that deal in virtual currency.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">#</th><th scope="col">Violation</th><th scope="col">Provision</th><th scope="col">Class</th></tr></thead>
            <tbody>
              <tr><th scope="row">1</th><td>Failure to submit 4 suspicious transaction reports</td><td>Act, section 7</td><td>Very serious</td></tr>
              <tr><th scope="row">2</th><td>Written compliance policies and procedures inadequate, incomplete and not tailored to operations</td><td>Act, subsection 9.6(1); Regulations, paragraph 156(1)(b)</td><td>Serious</td></tr>
              <tr><th scope="row">3</th><td>Enhanced measures for high-risk clients not adequately developed and applied</td><td>Act, subsection 9.6(3); Regulations, section 157</td><td>Serious</td></tr>
              <tr><th scope="row">4</th><td>Risk assessment did not adequately assess and document inherent risks</td><td>Act, subsection 9.6(2); Regulations, paragraph 156(1)(c)</td><td>Serious</td></tr>
              <tr><th scope="row">5</th><td>Prescribed records not kept: 94 deficiencies in virtual currency exchange transaction tickets</td><td>Act, section 6; Regulations, paragraph 36(j)</td><td>Minor</td></tr>
            </tbody>
          </table></div>
          <p>The notice does not break the total down by violation. It also does not say whether the penalty has been paid or appealed.</p>"""),
        ("str", "Spotting a red flag starts the review", f"""          <p>FINTRAC found that Necosmart failed to submit 4 suspicious transaction reports despite indicators of potential money laundering or terrorist financing. The indicators listed in the notice include:</p>
          <ul>
            <li>activity inconsistent with the client's financial standing, usual pattern or occupation (the notice gives student and unemployed as examples)</li>
            <li>transactions of an atypical size or type for the client</li>
            <li>an unknown source of funds for large virtual currency purchases</li>
            <li>transactions that were unnecessarily complex for their stated purpose</li>
            <li>inconsistent identification documents or identifiers</li>
            <li>activity involving locations of concern</li>
          </ul>
          <p>In 3 of the 4 cases, Necosmart had identified some of these indicators. According to FINTRAC, it then failed to take additional measures, including a holistic review of the activity, to decide whether the reasonable grounds to suspect threshold had been reached.</p>
          <p>FINTRAC's <a href="{F_STR}" rel="noopener">suspicious transaction report guidance</a> says indicators can bring suspicious activity to light, and that your holistic assessment of facts, context and indicators is what lets you decide whether you have reasonable grounds to suspect. Once you reach that threshold, you must submit the report as soon as practicable. There is no dollar threshold. FINTRAC also publishes <a href="{F_VC_IND}" rel="noopener">indicators for virtual currency transactions</a>, including an unknown source of funds used to buy large amounts of virtual currency.</p>
          <p>Each alert that names an indicator should lead to a documented follow-up: what you checked, what you concluded and why. When the answer is yes, the report goes to FINTRAC. Our guide to <a href="fintrac-reporting-requirements.html">FINTRAC reporting requirements</a> covers the timing for each report type. If no one on staff owns this review, an <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> can take it on.</p>"""),
        ("practice", "Written controls have to happen in practice", f"""          <p>Two of the violations concern measures that were documented and then not performed. On enhanced measures, FINTRAC gave three examples:</p>
          <ul>
            <li>Necosmart's mandatory enhanced due diligence for higher-risk clients included confirming the address with proof from the last three months. This was not evidenced in the client files FINTRAC reviewed.</li>
            <li>Its enhanced due diligence reviews were meant to cover the client's previous 3 to 6 months of transactions. FINTRAC found it reviewed only the previous month.</li>
            <li>Measures it had documented, such as scanning crypto wallets, were not being carried out.</li>
          </ul>
          <p>On the risk assessment, FINTRAC found that Necosmart did not adequately assess all inherent risks, such as those tied to high-risk jurisdictions and occupations, and that certain documented mitigating measures were not carried out.</p>
          <p><a href="{F_G4}" rel="noopener">FINTRAC's compliance program guidance</a> says your written enhanced measures must include the extra steps you will take to verify identity, keep client and beneficial ownership information updated, and conduct ongoing monitoring at a frequency suited to the risk. Your risk assessment must consider your clients and their activity patterns and locations, your products, services and delivery channels, and where you operate.</p>
          <p>One simple test is to take each enhanced measure in your manual and pull a high-risk client file that shows it was done. If a step is not realistic for your team, update the procedure and the risk assessment together, check that the remaining measures still address the risk, and have the change approved. Our <a href="compliance-programs.html">compliance program service</a> writes procedures around the steps your staff will carry out.</p>"""),
        ("policies", "Policies have to fit the business you run", """          <p>FINTRAC found that Necosmart's policies and procedures were inadequate, incomplete and not tailored to its operations in practice. It named deficiencies in five areas: suspicious transaction reporting, client identification and know your client processes, ongoing monitoring of business relationships, third party determination, and record keeping.</p>
          <p>The Regulations require written compliance policies and procedures that are kept up to date and, for an entity, approved by a senior officer. A manual written for a different business model may not cover what a virtual currency business needs, such as how wallets are screened, how exchange tickets are recorded and how alerts are escalated. Our guide to <a href="fintrac-compliance-program-requirements.html">FINTRAC compliance program requirements</a> walks through each element.</p>"""),
        ("records", "Virtual currency exchange tickets need every field", f"""          <p>FINTRAC reviewed Necosmart's virtual currency exchange transaction tickets for the examination period and found 94 record keeping deficiencies. The news release describes this as a failure to keep a record of sufficient occupation and transactional information.</p>
          <p>FINTRAC's <a href="{F_REC_MSB}" rel="noopener">MSB record keeping guidance</a> says you must keep a ticket for every virtual currency exchange transaction, whatever the amount. Each ticket includes the date. For transactions equivalent to $1,000 or more, it also includes the requester's name and address and, for a person, their date of birth and occupation. Every ticket records the amounts and types of funds and virtual currencies involved, the payment method, the exchange rates used and their source, details of every account involved, reference numbers, transaction identifiers such as a hash, and every sending and receiving address. You keep these records for at least five years.</p>
          <p>The guidance also asks for descriptive occupation entries, such as "retail clothing store manager" instead of "manager". A vague occupation field makes it harder to judge whether activity fits the client, and activity inconsistent with occupation was one of the indicators in Necosmart's unreported cases.</p>"""),
        ("checklist", "A self-check for virtual currency MSBs", """          <ul>
            <li>Every alert that names an indicator has a dated written review and a decision.</li>
            <li>Suspicious transaction reports go to FINTRAC as soon as practicable once the threshold is reached.</li>
            <li>Each enhanced due diligence step in the manual appears in a sample of high-risk client files.</li>
            <li>The risk assessment covers high-risk jurisdictions and occupations, and every mitigating measure it lists is in use.</li>
            <li>Policies describe the business as it runs today and carry a senior officer's approval.</li>
            <li>A sample of exchange tickets has every required field, including occupation, transaction hash and wallet addresses.</li>
          </ul>
          <p>An independent <a href="effectiveness-reviews.html">effectiveness review</a> runs tests like these against real files. Our <a href="fintrac-examination-preparation.html">examination preparation guide</a> explains what examiners usually ask for.</p>"""),
        ("context", "Where this penalty fits", f"""          <p>The penalty was imposed on March 27, 2026, the day after amendments raising FINTRAC's maximum penalties came into force. FINTRAC's <a href="{F_AMP_NEW}" rel="noopener">notice on the changes</a> says the regime that applies depends on the examination period and the date each violation occurred, and that the former policy and amounts continue for violations that occurred entirely before March 26, 2026. The Necosmart notice does not state the examination period.</p>
          <p>Our guide to <a href="fintrac-penalties-amps.html">FINTRAC penalties</a> explains the violation classes, the amounts and the appeal process. This post is general information, not legal advice.</p>"""),
    ],
    faqs=[("How much was the Necosmart FINTRAC penalty?", "FINTRAC imposed $693,742.50 on 13010431 Canada Inc., also operating as Necosmart, on March 27, 2026, for 5 violations found during a compliance examination. FINTRAC published the notice on May 14, 2026."),
          ("Which of Necosmart's violations was the most serious?", "The most serious was the failure to submit suspicious transaction reports under section 7 of the Act, which FINTRAC's notice says the regulations classify as very serious. Three violations were serious and the record keeping violation was minor."),
          ("Is spotting a red flag enough to file a suspicious transaction report?", "An indicator on its own does not settle it. FINTRAC expects a holistic assessment of the facts, context and indicators to decide whether you have reasonable grounds to suspect. Once you do, you must submit the report as soon as practicable, and there is no dollar threshold."),
          ("What is a virtual currency exchange transaction ticket?", "It is a record an MSB must keep for every virtual currency exchange transaction, whatever the amount. It covers the date, the funds and virtual currencies involved, exchange rates, transaction identifiers and sending and receiving addresses, plus client details such as occupation for transactions of $1,000 or more.")],
    sources=[("FINTRAC, Administrative monetary penalty on 13010431 Canada Inc.", P_NECO),
             ("FINTRAC, News release: FINTRAC imposes an administrative monetary penalty on 13010431 Canada Inc.", P_NECO_NR),
             ("FINTRAC, Reporting suspicious transactions to FINTRAC", F_STR),
             ("FINTRAC, Money laundering and terrorist financing indicators: virtual currency transactions", F_VC_IND),
             ("FINTRAC, Compliance program requirements", F_G4),
             ("FINTRAC, Record keeping requirements for money services businesses", F_REC_MSB),
             ("FINTRAC, Administrative monetary penalties: changes following legislative amendments", F_AMP_NEW),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations", L_PCMLTFR)],
    related=["fintrac-penalties-amps.html", "crypto-registration-canada.html", "fintrac-compliance-program-requirements.html"],
)
