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
