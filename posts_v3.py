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

from content_v3 import F_G4, F_REC_MSB, F_STR, F_SANCTIONS, F_LPEP, F_CHANGES

L_PCMLTFA = "https://laws-lois.justice.gc.ca/eng/acts/P-24.501/FullText.html"
L_PCMLTFR = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-184/FullText.html"
F_AMP_NEW = "https://fintrac-canafe.canada.ca/pen/3-eng"
F_VC_IND = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/indicators-indicateurs/vc_mltf-eng"

POSTS = {}

# ------------------------------------------------------------------ 2026-11-27 FINTRAC supervision priorities (Matos speech)
# Update post. Facts checked 27 November 2026 against FINTRAC's speaking notes of 9 October 2026,
# FINTRAC's FATF statement of 29 September 2026, the FINTRAC modernization page and the AMP changes page.
SP_MATOS = "https://fintrac-canafe.canada.ca/new-neuf/ps-pa/2026-10-09-eng"
SP_RBA = "https://fintrac-canafe.canada.ca/guidance-directives/compliance-conformite/rba/rba-eng"
SP_FATF = "https://fintrac-canafe.canada.ca/new-neuf/statementfatf-declarationgafi-eng"
SP_VSD = "https://fintrac-canafe.canada.ca/guidance-directives/exam-examen/vsdonc/1-eng"
SP_NUMBERS = "https://fintrac-canafe.canada.ca/publications/ar/2025-2026-info-eng"
SP_C4 = "https://laws-lois.justice.gc.ca/eng/AnnualStatutes/2026_4/FullText.html"

POSTS["fintrac-supervision-priorities-2026-msb.html"] = dict(
    checked="27 November 2026",
    title="FINTRAC Supervision Priorities 2026: What MSBs Can Expect | AML Canada",
    desc="FINTRAC's deputy director of supervision on the $85M funding envelope, deeper virtual currency supervision and risk-based programs. What MSBs should check.",
    crumb="FINTRAC supervision priorities",
    h1="FINTRAC supervision priorities after the FATF evaluation: what MSBs can expect",
    lede="FINTRAC plans to put more of its supervision effort into higher-risk sectors, including virtual currencies, and expects every business it supervises to show a clear link between its documented risks and its controls. Tina Matos, FINTRAC's Deputy Director of Supervision and Chief Compliance Officer, set out these priorities in a speech to The Assembly Canada (ACAMS) in Toronto on 9 October 2026. This post explains what she said and what money services businesses (MSBs) should check.",
    label="Update · Regulation",
    service="compliance-programs.html",
    also=["outsourced-compliance-officer.html", "effectiveness-reviews.html"],
    kind="update",
    date="2026-11-27",
    takeaways=["FINTRAC's overall cost-recovered envelope, which Ms. Matos discussed in relation to supervision, is rising by about $25 million this fiscal year to $85 million, and virtual currencies are one of the sectors named for deeper supervision.",
               "Risk will decide where FINTRAC looks, how closely and how it responds, from guidance for lower-risk businesses to stronger enforcement for significant or persistent non-compliance.",
               "FINTRAC wants each business to show a documented link between the risks it has identified and the measures it uses to manage them.",
               "Universal enrolment and the new penalty framework under the Strengthening Canada's Immigration System and Borders Act are part of the plan. Enrolment still depends on regulations that have not been published."],
    sections=[
        ("speech", "What did FINTRAC say about supervision in October 2026?", f"""          <p>On 29 September 2026, FINTRAC published a <a href="{SP_FATF}" rel="noopener">statement</a> on the Financial Action Task Force (FATF) evaluation of Canada's anti-money laundering regime. FINTRAC said the evaluation found it has a strong research and analytics capability and a good understanding of sector vulnerabilities, and that it had recently finalized a new Supervision Framework.</p>
          <p>On 9 October 2026, Tina Matos spoke about what the evaluation means for supervision. Her <a href="{SP_MATOS}" rel="noopener">speaking notes</a>, published by FINTRAC, cover three topics: FINTRAC's main takeaways from the evaluation, how they are shaping its approach to risk-based supervision, and what reporting entities should expect. She said FINTRAC will use the findings to "accelerate and guide" its modernization.</p>
          <p>A speech does not change the law. Your obligations still come from the Proceeds of Crime (Money Laundering) and Terrorist Financing Act and its regulations. The speech is useful because it tells you how the supervisor plans to check them.</p>"""),
        ("funding", "How is FINTRAC's supervision funding changing?", f"""          <p>The Minister of Finance and National Revenue approved an increase in FINTRAC's cost-recovered envelope, which Ms. Matos discussed in relation to supervision. These are the figures FINTRAC has published:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Measure</th><th scope="col">Figure</th><th scope="col">Source</th></tr></thead>
            <tbody>
              <tr><th scope="row">Cost-recovered envelope, 2025-26 base</th><td>Roughly $60 million</td><td><a href="{SP_MATOS}" rel="noopener">Speaking notes</a></td></tr>
              <tr><th scope="row">Increase this fiscal year</th><td>About $25 million, to an overall envelope of $85 million</td><td><a href="{SP_MATOS}" rel="noopener">Speaking notes</a></td></tr>
              <tr><th scope="row">Supervision-related resources over the next two years</th><td>Up 60% ($37 million)</td><td><a href="{SP_FATF}" rel="noopener">FATF statement</a></td></tr>
              <tr><th scope="row">Businesses subject to the Act</th><td>38,000</td><td><a href="{SP_FATF}" rel="noopener">FATF statement</a></td></tr>
            </tbody>
          </table></div>
          <p>The speaking notes give this fiscal year's increase in the cost-recovered envelope. The FATF statement gives the increase in supervision-related resources over two years.</p>
          <p>According to the speaking notes, the increase will be used to:</p>
          <ul>
            <li>deepen supervision in sectors such as financial institutions, virtual currencies and online gaming;</li>
            <li>supervise newer sectors, such as mortgage lenders, leasing and financing companies, and factoring companies;</li>
            <li>implement the new administrative monetary penalty framework and a universal enrolment program;</li>
            <li>support the expansion with a modernized IT platform.</li>
          </ul>
          <p>Ms. Matos said her intention is to focus on key vulnerabilities in higher-risk areas. In 2025-26, more than 55% of FINTRAC's assessment activities focused on MSBs, according to its <a href="{SP_NUMBERS}" rel="noopener">results by the numbers</a> page. Our post on <a href="fintrac-annual-report-2025-26-msb-supervision.html">FINTRAC's 2025-26 annual report</a> has the full figures.</p>"""),
        ("risk-based", "How will FINTRAC decide which businesses to supervise?", f"""          <p>Ms. Matos said FINTRAC will use technology and data to build a fuller picture of risk across all the businesses it supervises. She listed the information it plans to bring together:</p>
          <ul>
            <li>what it learns through examinations;</li>
            <li>the effectiveness of a business's compliance controls;</li>
            <li>reporting and data-quality concerns;</li>
            <li>enforcement history;</li>
            <li>voluntary disclosures of non-compliance;</li>
            <li>intelligence and information from its partners.</li>
          </ul>
          <p>The response will scale with risk. Where risk is lower, FINTRAC may focus on compliance promotion, guidance or monitoring. As risk rises, supervision goes deeper. Where it finds significant or persistent non-compliance, it will use stronger enforcement tools. FINTRAC wants to be "predictable, transparent and fair," according to the speech, and it must be firm when it finds non-compliance.</p>
          <p>Examiners will keep using professional judgement, she said, and will weigh the evidence and the circumstances of each business. Our guide to <a href="fintrac-examination-preparation.html">preparing for a FINTRAC examination</a> covers what examiners usually ask for.</p>"""),
        ("expectations", "What does FINTRAC expect from MSBs?", f"""          <p>Her main request to businesses concerned the risk assessment. Ms. Matos asked every business to know its risks, document them clearly and make sure they drive the compliance program. She said a risk assessment should reflect the realities of the business and be supported by the information available to it.</p>
          <p>She said that businesses in the same sector can have very different risk profiles because of their products, customers, geographic exposure, delivery channels and business models. FINTRAC expects a business to show a "clear and defensible connection" between the risks it has identified and the measures it has put in place, and to update its program as the business and its risks change.</p>
          <p>This matches a change in the law. Since 26 March 2026, the Act has required compliance programs to be reasonably designed, risk-based and effective, according to FINTRAC's <a href="{F_CHANGES}" rel="noopener">modernization page</a>. FINTRAC says it will update its guidance on these expectations. Its current <a href="{SP_RBA}" rel="noopener">risk assessment guidance</a> and <a href="{F_G4}" rel="noopener">compliance program guidance</a> are still published. Our guides explain <a href="fintrac-risk-assessment-msb.html">how to do a FINTRAC risk assessment</a> and the <a href="fintrac-compliance-program-requirements.html">five parts of a compliance program</a>.</p>"""),
        ("enforcement", "What changes with universal enrolment and the new penalties?", f"""          <p>Ms. Matos said universal enrolment "will be a game changer" for FINTRAC. FINTRAC's <a href="{F_CHANGES}" rel="noopener">modernization page</a> says it will require businesses subject to the Act, other than those already required to register, to enrol with FINTRAC. MSBs already register, so the new requirement is aimed at other sectors. It will come into force in line with regulations to be published in the Canada Gazette, Part II, and FINTRAC says it will share details as they become available.</p>
          <p>The new penalty framework is already in force for violations after 26 March 2026. FINTRAC's <a href="{F_AMP_NEW}" rel="noopener">page on the changes</a> lists:</p>
          <ul>
            <li>maximum penalties up to 40 times the previous limits;</li>
            <li>ability to pay as a factor in setting a penalty;</li>
            <li>mandatory compliance agreements for prescribed violations;</li>
            <li>compliance orders as a new enforcement tool.</li>
          </ul>
          <p>FINTRAC will scope each examination's review period so that it falls entirely before or entirely after 26 March 2026, and will apply one set of rules to the whole period. Our <a href="fintrac-penalties-amps.html">guide to FINTRAC penalties</a> explains how amounts are set.</p>"""),
        ("checklist", "What should an MSB check now?", f"""          <p>You can test each point in the speech against your own program:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">What FINTRAC said</th><th scope="col">What to check</th></tr></thead>
            <tbody>
              <tr><th scope="row">The risk assessment should reflect the realities of the business</th><td>It names your actual products, client types, countries, delivery channels and agents, and it was updated when you last added a service.</td></tr>
              <tr><th scope="row">A defensible link between risks and measures</th><td>Each higher-risk factor points to a specific control, such as enhanced due diligence, a monitoring rule or a transaction limit, and you can show the evidence.</td></tr>
              <tr><th scope="row">The program should change as the business changes</th><td>Policies and the risk assessment carry review dates, and changes are recorded with the reason.</td></tr>
              <tr><th scope="row">Data-quality concerns and voluntary disclosures feed FINTRAC's risk picture</th><td>You check your reports for errors and late filing, and you have a process to decide on a <a href="{SP_VSD}" rel="noopener">voluntary self-declaration</a>.</td></tr>
              <tr><th scope="row">Deeper supervision of virtual currencies</th><td>If you deal in virtual currency, your effectiveness review tests your virtual currency reporting and record keeping.</td></tr>
              <tr><th scope="row">Mandatory compliance agreements under the new penalty framework</th><td>Open findings from your last <a href="effectiveness-reviews.html">effectiveness review</a> are fixed and tested before an examiner finds them.</td></tr>
            </tbody>
          </table></div>
          <p>If your risk assessment has not been reviewed since it was written, review it first. Our <a href="compliance-programs.html">compliance program service</a> covers writing and updating these documents for MSBs.</p>"""),
    ],
    faqs=[("Who is Tina Matos?", "Tina Matos is FINTRAC's Deputy Director of Supervision and Chief Compliance Officer. She spoke about FINTRAC's supervision priorities at The Assembly Canada (ACAMS) in Toronto on 9 October 2026, and FINTRAC published her speaking notes."),
          ("How much funding does FINTRAC have for supervision?", "According to the speaking notes, FINTRAC's cost-recovered envelope, discussed in relation to supervision, was roughly $60 million in 2025-26 and rises by about $25 million this fiscal year, to an envelope of $85 million. FINTRAC's FATF statement says supervision-related resources will rise by 60% ($37 million) over the next two years."),
          ("What is FINTRAC universal enrolment?", "Universal enrolment is a requirement added by the Strengthening Canada's Immigration System and Borders Act for businesses subject to the Act, other than those already required to register, to enrol with FINTRAC. MSBs already register. It comes into force in line with regulations still to be published in the Canada Gazette, Part II."),
          ("Does the speech change what MSBs must do?", "No. A speech does not change the law. MSB obligations come from the Proceeds of Crime (Money Laundering) and Terrorist Financing Act and its regulations, which since 26 March 2026 require compliance programs to be reasonably designed, risk-based and effective. The speech explains how FINTRAC plans to supervise those obligations."),
          ("Which sectors will FINTRAC supervise more closely?", "The speaking notes name financial institutions, virtual currencies and online gaming as sectors for deeper supervision, and mortgage lenders, leasing and financing companies and factoring companies as newer sectors FINTRAC will supervise.")],
    sources=[("FINTRAC, Speaking notes for Tina Matos at The Assembly Canada (ACAMS), 9 October 2026", SP_MATOS),
             ("FINTRAC, Statement on the FATF evaluation (29 September 2026)", SP_FATF),
             ("FINTRAC, Results by the numbers 2025-26", SP_NUMBERS),
             ("Strengthening Canada's Immigration System and Borders Act, S.C. 2026, c. 4", SP_C4),
             ("FINTRAC, Modernization and upcoming changes impacting reporting entities", F_CHANGES),
             ("FINTRAC, Administrative monetary penalties: changes following legislative amendments", F_AMP_NEW),
             ("FINTRAC, Risk assessment guidance", SP_RBA),
             ("FINTRAC, Compliance program requirements", F_G4),
             ("FINTRAC, Voluntary self-declaration of non-compliance", SP_VSD)],
    related=["fintrac-annual-report-2025-26-msb-supervision.html", "fintrac-risk-assessment-msb.html", "fintrac-penalties-amps.html"],
)


# ------------------------------------------------------------------ 2026-11-25 Auditor General audit of FINTRAC
# Update post. Facts checked 25 November 2026 against the OAG report (HTML summary and full PDF),
# the OAG news release, FINTRAC's statement of 29 October 2026 and the FINTRAC pages below.
OG_REPORT = "https://www.canada.ca/en/auditor-general/our-work/audit-reports/21-auditor-general-202610-fintrac-activities-combat-money-laundering.html"
OG_PDF = "https://www.canada.ca/content/dam/oag-bvg/audit-reports/documents/21-ag-202610-fintrac-activities-combat-money-laundering.PDF"
OG_NR = "https://www.canada.ca/en/auditor-general/media-room/news-release-weak-oversight-slow-financial-intelligence-limited-fintrac-effectiveness.html"
OG_STMT = "https://fintrac-canafe.canada.ca/new-neuf/statement-declaration-26-10-29-eng"
OG_RENEW = "https://fintrac-canafe.canada.ca/msb-esm/register-inscrire/respond-eng"
OG_STR = F_STR

POSTS["auditor-general-fintrac-audit-2026-msb-lessons.html"] = dict(
    checked="25 November 2026",
    title="Auditor General Audit of FINTRAC: What MSBs Should Know | AML Canada",
    desc="The Auditor General's audit of FINTRAC found weak oversight and about 2,500 MSB registration requests waiting. What it means for MSBs and what to check now.",
    crumb="Auditor General audit of FINTRAC",
    h1="Auditor General audit of FINTRAC: what MSBs should know",
    lede="The Auditor General of Canada tabled an audit of FINTRAC on 29 October 2026 that found weak compliance oversight, slow financial intelligence and about 2,500 money services business registration requests still waiting to be processed. FINTRAC agreed with every recommendation. This post sets out the findings that affect MSBs and the checks they point to.",
    label="Update · Regulation",
    service="outsourced-compliance-officer.html",
    also=["msb-registration.html", "compliance-programs.html"],
    kind="update",
    date="2026-11-25",
    takeaways=["The audit concluded that FINTRAC did not effectively oversee compliance or produce financial intelligence during the period from 1 January 2023 to 28 February 2026.",
               "About 2,500 MSB registration requests were waiting at publication, and FINTRAC's new registration system is expected in 2027-28.",
               "FINTRAC agreed to build procedures to verify what businesses in higher-risk sectors report in self-attestations and risk questionnaires.",
               "FINTRAC plans to publish guidance on avoiding stereotypes and implicit bias in suspicious transaction reports in 2027-28."],
    sections=[
        ("findings", "What did the Auditor General find in its audit of FINTRAC?", f"""          <p>Auditor General Karen Hogan's report, <a href="{OG_REPORT}" rel="noopener">FINTRAC's Activities to Combat Money Laundering</a>, was tabled in the House of Commons on 29 October 2026. It concludes that FINTRAC "did not effectively carry out its role in overseeing compliance with Canada's anti-money laundering laws or in producing financial intelligence." The audit covered 1 January 2023 to 28 February 2026.</p>
          <p>These are the main findings, as set out in the report and the <a href="{OG_NR}" rel="noopener">OAG news release</a>:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Area</th><th scope="col">Finding</th></tr></thead>
            <tbody>
              <tr><th scope="row">Financial intelligence</th><td>FINTRAC took an average of about 4 months to provide intelligence when law enforcement flagged a concern. Half of surveyed recipients said it arrived too late to be useful.</td></tr>
              <tr><th scope="row">Proactive intelligence</th><td>The share FINTRAC generated on its own initiative fell from 38% in 2021-22 to 23% in 2024-25.</td></tr>
              <tr><th scope="row">Supervision</th><td>About 36,000 reporting entities were under FINTRAC's supervision by the end of the audit period. FINTRAC relied more on light-touch assessments, which gave lower assurance of compliance.</td></tr>
              <tr><th scope="row">MSB registration</th><td>About 2,500 registration, renewal and other MSB requests were waiting at publication, two years after a cyber-incident took the system offline.</td></tr>
              <tr><th scope="row">Public reporting</th><td>FINTRAC's reporting focused on activities and outputs, with little on outcomes, which made it hard to tell whether FINTRAC was achieving its mandate.</td></tr>
            </tbody>
          </table></div>
          <p>The audit also found that FINTRAC had a "formal, well-organized approach" to its supervision work.</p>"""),
        ("registration", "What does the audit say about the MSB registration backlog?", f"""          <p>After the March 2024 cyber-incident, FINTRAC had no backup system to speed up a return to normal operations, so it relied on a temporary process that needed much more manual work. The <a href="{OG_PDF}" rel="noopener">full report</a> gives this timeline:</p>
          <ul>
            <li>17 May 2024, 10 weeks after the incident: FINTRAC began offering workarounds for MSB registration.</li>
            <li>April 2025: a temporary measure let businesses with expired registrations keep operating if they had applied for renewal. The auditors note this also meant some businesses kept operating that may no longer meet the rules.</li>
            <li>August 2025, 17 months after the incident: FINTRAC set up a special team to clear the backlog.</li>
            <li>At publication: about 2,500 MSB requests were waiting, and FINTRAC was resolving about 150 cases a week.</li>
          </ul>
          <p>The auditors note that new businesses could not register and that renewal delays caused problems for banks that check an MSB's registry status before opening a business account. FINTRAC is building a new permanent system, expected in the 2027-28 fiscal year. The report also mentions the universal enrolment of all reporting entities that the government signalled in its 2024 Fall Economic Statement, and says MSB registration would continue to apply alongside it.</p>
          <p>FINTRAC's <a href="{OG_RENEW}" rel="noopener">renewal page</a> still says you must renew before the expiry date and that "the majority of complete applications are processed within three months." Neither the report nor FINTRAC's renewal page says whether the April 2025 measure is still in place, so do not rely on it. File early and keep proof of what you sent and when. Our guides cover <a href="msb-registration-renewal-canada.html">MSB registration renewal</a>, <a href="check-fintrac-msb-registration.html">how to check a registration</a> and <a href="msb-bank-account-canada.html">what banks check before opening an MSB account</a>.</p>"""),
        ("self-attestations", "Why do self-attestations and risk questionnaires matter more now?", f"""          <p>As the number of supervised businesses grew, FINTRAC did more self-attestations and risk questionnaires. The auditors say these "relied largely on reporting entities providing accurate and honest information" and that FINTRAC had limited ability to verify the answers without a deeper assessment. In the report, a self-attestation gives FINTRAC low confidence that a business complies. A resource-intensive examination gives high confidence.</p>
          <p>The auditors recommended that FINTRAC develop procedures to verify information from businesses in higher-risk sectors. FINTRAC agreed. Its response says answers to self-assessments, risk questionnaires and information demands, "including responses that deviate from expectations or demonstrate other red flags," already inform decisions on risk, follow-up supervision or enforcement. It says it will strengthen its existing approach, including a formal procedure to standardize these verification activities.</p>
          <p>For an MSB, every answer on a questionnaire should match a document you could produce. That means a current compliance program, risk assessment, training records and the last effectiveness review. Our guide to <a href="fintrac-examination-preparation.html">preparing for a FINTRAC examination</a> lists what examiners ask for.</p>"""),
        ("scorecards", "FINTRAC reporting scorecards", f"""          <p>The report says FINTRAC introduced scorecards in 2025. They are generated automatically from the transaction reports a business has submitted and give feedback on whether the information was complete and accurate. The auditors found that the scorecards did not clearly explain what needed fixing. In one case, a business with more than 210 flagged reports could not understand the error codes. When it asked, FINTRAC said it was aware that issues had been incorrectly flagged.</p>
          <p>FINTRAC agreed to check scorecards before sending them and to explain any non-compliance it identifies. Its response says the scorecards were a pilot and that most businesses made corrections or started changes before meeting a FINTRAC official. If you receive one, check each flagged report against your records, ask FINTRAC about any code you cannot match and keep a record of the corrections you make. Our <a href="fintrac-reporting-requirements.html">FINTRAC reporting guide</a> covers the report types and deadlines.</p>"""),
        ("str", "What does the audit mean for suspicious transaction reports?", f"""          <p>The auditors found that FINTRAC gave reporting entities indicators for spotting suspicious transactions but no specific guidance on avoiding stereotypes or implicit bias when they file suspicious transaction reports. They point out that Canada's National Risk Assessment identified this risk in 2023 and again in 2025. FINTRAC agreed. Its response says it will look at where guidance may be updated to discourage overreporting of suspicious transaction reports, such as those that contain stereotypes and implicit bias, and that guidance would be published in the 2027-28 fiscal year.</p>
          <p>Until then, FINTRAC's <a href="{OG_STR}" rel="noopener">STR guidance</a> sets the test. It asks for a "holistic assessment of facts, context" and indicators, and it says a fact "cannot be an opinion." Your grounds for suspicion should be explained so that another person with similar knowledge would likely reach the same conclusion from the same information. Build that test into your STR review step, and keep the review short enough that reports still go in "as soon as practicable," as the guidance requires.</p>"""),
        ("response", "FINTRAC's response to the audit", f"""          <p>In a <a href="{OG_STMT}" rel="noopener">statement on 29 October 2026</a>, FINTRAC pointed to the recent FATF evaluation. It quoted the FATF finding that its intelligence was used in 94% of law enforcement investigations into money laundering and criminal possession offences, and that 40% of urgent cases led to a disclosure in less than 10 days. It said it produced 7,214 disclosure packages from 3,007 unique disclosures in 2025-26, and that a $37 million increase in supervision-related resources over two years will strengthen its oversight of the 38,000 businesses subject to the Act. The audit's figure of about 36,000 is a count at the end of its audit period, 28 February 2026.</p>
          <p>Our post on the <a href="fintrac-annual-report-2025-26-msb-supervision.html">FINTRAC 2025-26 annual report</a> covers its supervision and penalty figures for the same year.</p>"""),
        ("checklist", "What should an MSB check after the audit?", f"""          <p>Each finding points to a control an MSB can test now.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Audit finding</th><th scope="col">What to check</th></tr></thead>
            <tbody>
              <tr><th scope="row">About 2,500 MSB requests waiting</th><td>Renewals and changes are filed early, with proof of submission on file for your bank.</td></tr>
              <tr><th scope="row">Self-reported answers to be verified</th><td>Every questionnaire answer is backed by a current document.</td></tr>
              <tr><th scope="row">Scorecards on report quality</th><td>Someone owns scorecard follow-up and logs each correction.</td></tr>
              <tr><th scope="row">STR bias guidance coming in 2027-28</th><td>STR narratives rest on facts, context and indicators, and a reviewer checks them without delaying filing past "as soon as practicable."</td></tr>
            </tbody>
          </table></div>
          <p>The compliance officer appointed under your compliance program should own each of these checks and record when each was done. Businesses without in-house compliance staff can fill that role with an <a href="outsourced-compliance-officer.html">outsourced compliance officer</a>.</p>"""),
    ],
    faqs=[("When was the Auditor General's audit of FINTRAC published?", "The Auditor General of Canada tabled FINTRAC's Activities to Combat Money Laundering in the House of Commons on 29 October 2026. The audit covered 1 January 2023 to 28 February 2026."),
          ("How many MSB registration requests are waiting at FINTRAC?", "The audit says about 2,500 registration, renewal and other requests from money services businesses were waiting to be processed at publication, and that FINTRAC was resolving about 150 cases a week."),
          ("When will FINTRAC's new MSB registration system be ready?", "FINTRAC expects to implement its new MSB registration system in the 2027-28 fiscal year and says it will look for ways to speed up development. In the meantime it has deployed an updated secure document transfer system."),
          ("Did FINTRAC accept the Auditor General's recommendations?", "Yes. FINTRAC agreed with all eight recommendations, including verifying self-reported information from higher-risk sectors, checking scorecards before sending them and publishing guidance on bias in suspicious transaction reports."),
          ("Should an MSB still renew its registration before the expiry date?", "Yes. FINTRAC's renewal page says you must renew before the expiry date and that it is your responsibility to renew on time. Most complete applications are processed within three months.")],
    sources=[("Office of the Auditor General of Canada, FINTRAC's Activities to Combat Money Laundering (29 October 2026)", OG_REPORT),
             ("Office of the Auditor General of Canada, full report (PDF)", OG_PDF),
             ("Office of the Auditor General of Canada, News release (29 October 2026)", OG_NR),
             ("FINTRAC, Statement on the Office of the Auditor General audit (29 October 2026)", OG_STMT),
             ("FINTRAC, Answer clarification requests, update, renew or cancel your registration", OG_RENEW),
             ("FINTRAC, Reporting suspicious transactions to FINTRAC", OG_STR)],
    related=["msb-registration-renewal-canada.html", "fintrac-examination-preparation.html", "fintrac-annual-report-2025-26-msb-supervision.html"],
)

# ------------------------------------------------------------------ 2026-11-23 FINTRAC 2025-26 annual report
# Update post. Facts checked 23 November 2026 against the FINTRAC pages below.
AR_REPORT = "https://fintrac-canafe.canada.ca/publications/ar/2026/1-eng"
AR_NUMBERS = "https://fintrac-canafe.canada.ca/publications/ar/2025-2026-info-eng"
AR_NR = "https://fintrac-canafe.canada.ca/new-neuf/nr/2026-10-26-eng"
AR_OAG = "https://fintrac-canafe.canada.ca/new-neuf/statement-declaration-26-10-29-eng"
AR_FATF = "https://fintrac-canafe.canada.ca/new-neuf/statementfatf-declarationgafi-eng"
AR_VSD = "https://fintrac-canafe.canada.ca/guidance-directives/exam-examen/vsdonc/1-eng"
AR_EXAM = "https://fintrac-canafe.canada.ca/guidance-directives/exam-examen/1-eng"
AR_AMP_POL = "https://fintrac-canafe.canada.ca/pen/2-eng"

POSTS["fintrac-annual-report-2025-26-msb-supervision.html"] = dict(
    checked="23 November 2026",
    title="FINTRAC Annual Report 2025-26: What It Means for MSBs | AML Canada",
    desc="FINTRAC's 2025-26 annual report: 433 MSB examinations and information demands, 82 revocations and $198M+ in MSB penalties. What MSBs should check now.",
    crumb="FINTRAC 2025-26 annual report",
    h1="FINTRAC's 2025-26 annual report: what the supervision figures mean for MSBs",
    lede="FINTRAC published its 2025-26 annual report on 26 October 2026. In the year to 31 March 2026, money services businesses received more than 55% of its assessment activity, 433 targeted examinations and information demands, and 82 registration revocations. This post sets out the supervision and enforcement figures that matter to MSBs and the compliance checks they point to.",
    label="Update · Regulation",
    service="outsourced-compliance-officer.html",
    also=["compliance-programs.html", "effectiveness-reviews.html", "msb-registration.html"],
    kind="update",
    date="2026-11-23",
    takeaways=["More than 55% of FINTRAC's 4,874 assessment and monitoring activities in 2025-26 were directed at money services businesses.",
               "FINTRAC ran 625 targeted examinations and information demands, and 433 of them were on MSBs.",
               "It revoked 82 MSB registrations, up from 12 the year before, and penalized nine MSBs for more than $198 million.",
               "FINTRAC received 294 voluntary self-declarations of non-compliance, many about late reporting caused by human error or systems issues."],
    sections=[
        ("figures", "What does FINTRAC's 2025-26 annual report say about supervision?", f"""          <p>FINTRAC published its <a href="{AR_REPORT}" rel="noopener">2025-26 Annual Report, Safe Canadians, Secure Economy</a> on 26 October 2026. The report covers the year to 31 March 2026. Its supervision chapter describes a new Supervision Framework that FINTRAC finalized, implemented and published during the year, and a focus on higher-risk businesses. The <a href="{AR_NR}" rel="noopener">news release</a> calls the 4,874 assessment and monitoring activities a record.</p>
          <p>These are the supervision figures FINTRAC reports in its <a href="{AR_NUMBERS}" rel="noopener">results by the numbers</a> page and in the report itself:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Measure (2025-26)</th><th scope="col">Figure</th></tr></thead>
            <tbody>
              <tr><th scope="row">Assessment and monitoring activities, all sectors</th><td>4,874</td></tr>
              <tr><th scope="row">Share of activities focused on MSBs</th><td>More than 55%</td></tr>
              <tr><th scope="row">Targeted examinations and information demands</th><td>625, including 433 on MSBs, 129 on financial entities and 26 on casinos</td></tr>
              <tr><th scope="row">Full-scope examinations</th><td>89, mostly dealers in precious metals and stones (34), real estate (29) and mortgage brokers (9)</td></tr>
              <tr><th scope="row">Self-attestations processed</th><td>812</td></tr>
              <tr><th scope="row">Risk questionnaires administered</th><td>984</td></tr>
              <tr><th scope="row">Voluntary self-declarations of non-compliance received</th><td>294</td></tr>
              <tr><th scope="row">MSB registrations revoked</th><td>82, up from 12 the previous year</td></tr>
              <tr><th scope="row">Notices of violation, all sectors</th><td>35, for more than $247 million</td></tr>
              <tr><th scope="row">Non-compliance cases disclosed to law enforcement</th><td>31, of which 28 involved MSBs</td></tr>
            </tbody>
          </table></div>"""),
        ("msb-focus", "Why did MSBs get most of FINTRAC's attention?", f"""          <p>The report says the 2025 Assessment of Money Laundering and Terrorist Financing Risks in Canada rated MSBs as having very high vulnerability, so FINTRAC "focused significant resources" on the sector, particularly on virtual asset service providers. The MSB work included:</p>
          <ul>
            <li>full-scope examinations of larger, more traditional MSBs;</li>
            <li>targeted assessments of crowdfunding platforms and payment service providers;</li>
            <li>information demands on high-risk virtual asset service providers.</li>
          </ul>
          <p>FINTRAC also says that, when it assessed virtual currency dealers, it found instances of exposure to dark markets related to the buying, selling and distribution of illegal fentanyl.</p>
          <p>The report describes a move from an audit approach to an assessment approach, with "more complex, lengthy and in-depth examinations" of larger businesses in higher-risk sectors. After an examination, FINTRAC monitors the business's action plan, and an action item closes only once the business can show it has taken all appropriate corrective measures. Our guide to <a href="fintrac-examination-preparation.html">preparing for a FINTRAC examination</a> covers what examiners ask for.</p>"""),
        ("registry", "What happened to MSB registrations in 2025-26?", f"""          <p>The registry grew in 2025-26 even as revocations rose. According to the annual report, 1,401 new MSBs registered and 625 renewed in 2025-26. FINTRAC denied 23 new registrations, 91 businesses ceased their registrations and 605 registrations expired, a figure that includes registrations that expired and were then renewed. As of 31 March 2026, 3,396 MSBs were registered, up from 2,778 a year earlier.</p>
          <p>FINTRAC revoked 82 registrations. The report says MSBs must respond in a timely manner to FINTRAC's demands for information "or their registrations are revoked," and that people convicted of certain offences are ineligible to register. FINTRAC publishes the names of revoked MSBs.</p>
          <p>The 82 figure covers the fiscal year. FINTRAC's 6 November 2026 statement gave a separate count of 161 revocations since the start of calendar year 2026, which we covered in our post on the <a href="ofac-sanctions-canadian-msbs-iran-fintrac.html">OFAC sanctions on Canadian MSBs</a>. Our guide to <a href="msb-registration-refused-revoked.html">refused and revoked MSB registrations</a> explains the process.</p>"""),
        ("penalties", "How large were FINTRAC's penalties?", f"""          <p>FINTRAC issued 35 notices of violation in 2025-26, up 52% from the previous year, for more than $247 million. The report calls it "by far the largest amount in FINTRAC's history." By number of notices of violation, the most penalized sectors were financial entities (12), MSBs (8), casinos (5) and real estate (5). FINTRAC's <a href="{AR_NUMBERS}" rel="noopener">results by the numbers</a> page compares the last five fiscal years:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Fiscal year</th><th scope="col">Notices of violation</th><th scope="col">Amount</th></tr></thead>
            <tbody>
              <tr><th scope="row">2025-26</th><td>35</td><td>More than $247 million</td></tr>
              <tr><th scope="row">2024-25</th><td>23</td><td>$25 million</td></tr>
              <tr><th scope="row">2023-24</th><td>12</td><td>$26 million</td></tr>
              <tr><th scope="row">2022-23</th><td>6</td><td>$1 million</td></tr>
              <tr><th scope="row">2021-22</th><td>15</td><td>$3.5 million</td></tr>
            </tbody>
          </table></div>
          <p>In its section on MSBs, the report says nine MSBs were penalized for more than $198 million, for violations that include compliance program deficiencies, failing to register and failing to report large virtual currency transactions. The report does not explain why this differs from the eight MSBs in its count of most penalized sectors. It names three MSB cases:</p>
          <ul>
            <li>Xeltox Enterprises Ltd. (operating as Cryptomus) received a $176 million penalty in October 2025, the largest in FINTRAC's history. Among other violations, FINTRAC found it failed to submit suspicious transaction reports where there were reasonable grounds to suspect links to trafficking in child sexual abuse material, fraud, ransomware payments and sanctions evasion.</li>
            <li>Peken Global Limited (also operating as KuCoin), a foreign MSB, received a $19,552,000 penalty in July 2025 for failing to register, failing to report large virtual currency transactions on 2,952 occasions and failing to report suspicious transactions on 33 occasions.</li>
            <li>MP Technology Services Ltd., a subsidiary of MoonPay Inc. and a foreign MSB, received a $536,853.35 penalty in November 2025 for four violations, including failing to report suspicious transactions with direct or indirect exposure to darknet marketplaces, sanctioned entities and child sexual abuse material.</li>
          </ul>
          <p>The report adds that the Strengthening Canada's Immigration System and Borders Act, passed in March 2026, raised penalties by up to 40 times and gave FINTRAC power to issue compliance orders. Failing to comply with an order can bring a penalty of up to $30 million or 3% of the business's global revenues. Our <a href="fintrac-penalties-amps.html">guide to FINTRAC penalties</a> explains how amounts are set under the <a href="{AR_AMP_POL}" rel="noopener">AMP policy</a>.</p>"""),
        ("self-declaration", "What is a voluntary self-declaration of non-compliance?", f"""          <p>A business that finds its own gaps can tell FINTRAC in writing. FINTRAC received 294 of these declarations in 2025-26. The report says many related to late reporting caused by human error or systems issues, or to fixing past non-compliance in recently onboarded sectors.</p>
          <p>FINTRAC's <a href="{AR_VSD}" rel="noopener">self-declaration page</a> says a declaration should include the business's name and contact details, the number and type of reports affected and the period involved, the reason for the problem, and a plan with measures and timelines to fix it and submit any outstanding reports. FINTRAC says it will work with the business to resolve the issue when the problem is not a repeat of an earlier declaration and the declaration was not made after the business was notified of an upcoming assessment activity.</p>"""),
        ("checklist", "What should an MSB check after reading the report?", f"""          <p>The report shows where FINTRAC spent its supervision effort in 2025-26. Here is a control an MSB can test against each finding.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">What the report shows</th><th scope="col">What to check</th></tr></thead>
            <tbody>
              <tr><th scope="row">433 targeted examinations and information demands on MSBs</th><td>Your compliance program documents, risk assessment, training records and last effectiveness review are current and can be produced quickly.</td></tr>
              <tr><th scope="row">Registrations revoked when MSBs do not answer information demands in time</th><td>Someone monitors the email address on your registration and answers FINTRAC by the deadline. Our <a href="fintrac-revocation-response-plan.html">revocation response plan</a> sets out the steps.</td></tr>
              <tr><th scope="row">Penalties for unreported suspicious and large virtual currency transactions</th><td>Your monitoring flags exposure to darknet markets, sanctioned entities and fraud, and your reports are filed on time.</td></tr>
              <tr><th scope="row">Failure to register was among the MSB violations</th><td>Every service you offer, including virtual currency and payment services, is covered by your registration.</td></tr>
              <tr><th scope="row">Action plan items close only when corrective measures are shown</th><td>Past examination findings have documented fixes and evidence that the fixes work.</td></tr>
              <tr><th scope="row">294 self-declarations, many about late reporting</th><td>You have a process to find reporting errors and decide whether to self-declare before an assessment is announced.</td></tr>
            </tbody>
          </table></div>
          <p>If your business has no dedicated compliance staff, an <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> can run these checks and handle FINTRAC correspondence. FINTRAC's <a href="{AR_EXAM}" rel="noopener">examination pages</a> describe what to expect if you are selected.</p>"""),
        ("outlook", "What comes next for FINTRAC supervision?", f"""          <p>In its <a href="{AR_FATF}" rel="noopener">statement on the FATF evaluation</a> of 29 September 2026, FINTRAC said its supervision-related resources will rise by 60% ($37 million) over the next two years, to strengthen oversight of the 38,000 businesses subject to the Act. In its <a href="{AR_OAG}" rel="noopener">statement on the Auditor General's audit</a> of 29 October 2026, FINTRAC said it will use the recommendations of the Office of the Auditor General and the FATF evaluation to strengthen its supervision.</p>
          <p>The annual report also says FINTRAC is strengthening its penalty framework to implement the higher amounts and compliance orders.</p>"""),
    ],
    faqs=[("When did FINTRAC publish its 2025-26 annual report?", "FINTRAC published its 2025-26 Annual Report, Safe Canadians, Secure Economy, on 26 October 2026. It covers the fiscal year that ended on 31 March 2026."),
          ("How many MSB registrations did FINTRAC revoke in 2025-26?", "FINTRAC revoked 82 money services business registrations in 2025-26, up from 12 the previous year. It publishes the names of revoked MSBs."),
          ("How many FINTRAC examinations focused on MSBs?", "Of the 625 targeted examinations and information demands FINTRAC carried out in 2025-26, 433 were on money services businesses. More than 55% of all its assessment activities were directed at MSBs."),
          ("How much did FINTRAC penalize MSBs in 2025-26?", "FINTRAC imposed administrative monetary penalties on nine money services businesses for more than $198 million, for violations including compliance program deficiencies, failing to register and failing to report large virtual currency transactions."),
          ("How many MSBs were registered with FINTRAC at 31 March 2026?", "FINTRAC's annual report says 3,396 money services businesses were registered as of 31 March 2026, up from 2,778 a year earlier.")],
    sources=[("FINTRAC, 2025-26 Annual Report, Safe Canadians, Secure Economy", AR_REPORT),
             ("FINTRAC, Results by the numbers 2025-26", AR_NUMBERS),
             ("FINTRAC, News release: 2025-26 Annual Report (26 October 2026)", AR_NR),
             ("FINTRAC, Statement on the FATF evaluation (29 September 2026)", AR_FATF),
             ("FINTRAC, Statement on the Office of the Auditor General audit (29 October 2026)", AR_OAG),
             ("FINTRAC, Voluntary self-declaration of non-compliance", AR_VSD),
             ("FINTRAC, Administrative monetary penalties policy", AR_AMP_POL),
             ("FINTRAC, Examinations", AR_EXAM)],
    related=["fintrac-examination-preparation.html", "msb-registration-refused-revoked.html", "fintrac-penalties-amps.html"],
)


# ------------------------------------------------------------------ 2026-11-21 OFAC sanctions on 8 Canadian MSBs
# Update post. Facts checked 21 November 2026 against the FINTRAC, OFAC and US Treasury pages below.
OS_STMT = "https://fintrac-canafe.canada.ca/new-neuf/statement-declaration-2026-11-06-eng"
OS_OFAC = "https://ofac.treasury.gov/recent-actions/20261106"
OS_PR = "https://home.treasury.gov/news/press-releases/sb0686"
OS_SANC = F_SANCTIONS
OS_IRI = "https://fintrac-canafe.canada.ca/obligations/dir-iri-eng"
OS_LPEP = F_LPEP
F_AMP_LIST = "https://fintrac-canafe.canada.ca/pen/4-eng"

POSTS["ofac-sanctions-canadian-msbs-iran-fintrac.html"] = dict(
    checked="21 November 2026",
    title="OFAC Sanctions 8 Canadian MSBs: Compliance Lessons | AML Canada",
    desc="US Treasury sanctioned eight Canadian MSBs on 6 November 2026 in coordination with FINTRAC. What happened, the Iran directive and what MSBs should check.",
    crumb="OFAC sanctions on Canadian MSBs",
    h1="OFAC sanctions eight Canadian MSBs: what money services businesses should check",
    lede="On 6 November 2026, the US Treasury's Office of Foreign Assets Control (OFAC) designated eight money services businesses based in Canada under its Iran sanctions, and FINTRAC said it coordinated with OFAC and FinCEN on the action. For Canadian MSBs, it is a reason to recheck sanctions screening and how Iran-connected transactions are identified and reported.",
    label="Update · Sanctions",
    service="compliance-programs.html",
    also=["outsourced-compliance-officer.html", "effectiveness-reviews.html"],
    kind="update",
    date="2026-11-21",
    takeaways=["OFAC added eight Canadian MSBs in Ontario and British Columbia to its SDN List under Executive Order 13902, for operating in the digital asset sector of the Iranian economy.",
               "The SDN entries list aliases, addresses, Canadian MSB registration numbers and, for four entities, TRX digital currency addresses, so screening on legal names alone can miss a match.",
               "FINTRAC says it has revoked 161 MSB registrations since the start of 2026 and imposed penalties totalling more than $198 million on nine MSBs over the past year.",
               "Canada's Iran ministerial directive already treats every transaction originating from or bound for Iran as high risk and requires it to be reported to FINTRAC."],
    sections=[
        ("what-happened", "What did OFAC and FINTRAC announce on 6 November 2026?", f"""          <p>OFAC designated eight Canadian money services businesses under Executive Order 13902 "for operating in the digital asset sector of the Iranian economy," according to the <a href="{OS_PR}" rel="noopener">US Treasury press release</a>. The action is part of Treasury's Operation Economic Outcast. Treasury says the businesses facilitate the exchange of Iranian rials and other currencies for digital assets, and that the action was coordinated with FinCEN and FINTRAC.</p>
          <p>The same day, FINTRAC published a <a href="{OS_STMT}" rel="noopener">public statement</a> confirming it had coordinated with OFAC and FinCEN "in the imposition of sanctions against eight Canadian money services businesses." FINTRAC added that, under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act, it cannot disclose compliance actions against specific businesses except through a public notice of an administrative monetary penalty.</p>
          <p>The <a href="{OS_OFAC}" rel="noopener">OFAC recent actions notice</a> lists the eight entities added to the Specially Designated Nationals (SDN) List:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Legal name in the SDN entry</th><th scope="col">Also known as (selected)</th><th scope="col">Province</th></tr></thead>
            <tbody>
              <tr><th scope="row">1380079 BC LTD</th><td>Amin Exchange Vancouver; Sarafi Amin</td><td>British Columbia</td></tr>
              <tr><th scope="row">2397639 ONTARIO LTD</th><td>Farah Exchange</td><td>Ontario</td></tr>
              <tr><th scope="row">B GALAXY INC</th><td>Cryptoyal; C Exchange</td><td>Ontario</td></tr>
              <tr><th scope="row">CCC INC</th><td>Ccurrency Exchange; Sarafi C; Parsis Exchange; Salam Exchange</td><td>Ontario</td></tr>
              <tr><th scope="row">DARVISH EXCHANGE</th><td>Kanata MD Inc; Canada Exchange</td><td>Ontario</td></tr>
              <tr><th scope="row">DIVERSE TRADE INC</th><td>Million Exchange; Millionex</td><td>Ontario</td></tr>
              <tr><th scope="row">NIA NATIONS CURRENCY LTD</th><td>NIA Exchange</td><td>British Columbia</td></tr>
              <tr><th scope="row">TOP PC TECHNICIAN INC</th><td>2840711 Ontario Inc; Amin Exchange Toronto</td><td>Ontario</td></tr>
            </tbody>
          </table></div>
          <p>The entries for 1380079 BC LTD and DIVERSE TRADE INC also give addresses in Montreal, Quebec. Each entry lists a Canadian MSB registration number.</p>"""),
        ("treasury-findings", "What does Treasury say these businesses did?", f"""          <p>Treasury says digital asset addresses linked to several of the businesses transacted with sanctioned Iranian exchanges, including Nobitex, Wallex, Ramzinex, Bitpin, Aban Tether Exchange and Shelbit, or with addresses associated with Iran's Islamic Revolutionary Guard Corps.</p>
          <p>Treasury also says several of the businesses worked with an OFAC-sanctioned Canadian drug trafficker, who used couriers to bring bulk cash to money exchange businesses in the Vancouver and Toronto areas that converted it into digital assets to send abroad. It adds that several of the businesses "have changed their business names and addresses in an attempt to evade detection and enforcement actions."</p>
          <p>Treasury's account describes the exchange of rials for virtual currency, cash converted to virtual currency for transfer abroad, and changes of business name and address. These are Treasury's statements. FINTRAC's statement does not describe the conduct of any of the eight businesses, and none of them appears on FINTRAC's <a href="{F_AMP_LIST}" rel="noopener">public notice list of penalties</a> as of 21 November 2026.</p>"""),
        ("fintrac-numbers", "What did FINTRAC say about MSB enforcement?", f"""          <p>FINTRAC's statement gave these figures, which go beyond the eight businesses:</p>
          <ul>
            <li>Since the beginning of 2026, FINTRAC has revoked the registrations of 161 money services businesses, "more than the last three years combined."</li>
            <li>Over the past year, it imposed administrative monetary penalties on nine MSBs for more than $198 million, for violations that include failing to register and failing to report large virtual currency transactions.</li>
            <li>Over the past year, it disclosed 28 cases of MSB non-compliance to law enforcement.</li>
            <li>Since Bill C-12 passed in March 2026, operating without a valid MSB registration can bring, on conviction on indictment, a fine of up to $5,000,000, up to five years in prison, or both.</li>
          </ul>
          <p>Our guides on <a href="fintrac-penalties-amps.html">FINTRAC penalties</a> and <a href="msb-registration-refused-revoked.html">refused and revoked MSB registrations</a> explain how penalties and revocations work.</p>"""),
        ("canadian-rules", "Which Canadian rules apply to Iran-connected transactions?", f"""          <p>An OFAC designation is a US measure. Your obligations to FINTRAC come from Canadian law. The sanctions evasion and listed property reports below depend on Canadian sanctions laws and lists, so a match on the SDN List alone does not trigger them. The Iran directive and suspicious transaction reporting for money laundering or terrorist financing can still apply.</p>
          <h3>The ministerial directive on Iran</h3>
          <p>The directive came into force on July 25, 2020 and was amended on February 15, 2024 and November 15, 2025, according to <a href="{OS_IRI}" rel="noopener">FINTRAC's Iran directive guidance</a>. For every transaction originating from or bound for Iran, whatever the amount, you must treat it as high risk and verify the identity of the client who requests or benefits from it. Your due diligence must establish the source of the funds or virtual currency, the purpose of the transaction and the beneficial ownership or control of any entity involved. You must also keep a record and report the transaction to FINTRAC. FINTRAC's examples of a connection include virtual currency or currency exchange transactions involving the Iranian rial, and online transactions traced to an IP address geolocated in Iran. Our <a href="fintrac-travel-rule-ministerial-directives.html">ministerial directives guide</a> covers the "IR2020" reporting field.</p>
          <h3>Suspicious transaction reports for sanctions evasion</h3>
          <p>You must report completed and attempted transactions when there are reasonable grounds to suspect they relate to a sanctions evasion offence, according to <a href="{OS_SANC}" rel="noopener">FINTRAC's sanctions evasion guidance</a>. FINTRAC defines that offence by reference to orders and regulations under the United Nations Act, the Special Economic Measures Act and the Sergei Magnitsky Law, and points to the Consolidated Canadian Autonomous Sanctions List and the UN Security Council list. Suspicions of money laundering or terrorist financing are reportable on their own terms; see our <a href="fintrac-reporting-requirements.html">FINTRAC reporting guide</a>.</p>
          <h3>Listed person or entity property reports</h3>
          <p>If you must disclose property of a listed person or entity under the Criminal Code, the United Nations Act, the Special Economic Measures Act or the Sergei Magnitsky Law, you must also send FINTRAC a Listed Person or Entity Property Report immediately, according to <a href="{OS_LPEP}" rel="noopener">FINTRAC's guidance</a>. Property includes virtual currency.</p>"""),
        ("checklist", "What should an MSB check in its program now?", f"""          <p>Your risk assessment sets how far each of these checks needs to go.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">What the case shows</th><th scope="col">What to check</th></tr></thead>
            <tbody>
              <tr><th scope="row">SDN entries list aliases, addresses, MSB registration numbers and, for four entities, TRX addresses</th><td>If you screen against the SDN List, for example because of US banking or counterparty exposure, your tool matches on all of these identifiers, is updated when lists change, and covers TRX addresses if you support that network.</td></tr>
              <tr><th scope="row">Exchange of rials for virtual currency</th><td>Staff can spot an Iran connection, and every such transaction gets the directive's identification, due diligence, record keeping and reporting steps.</td></tr>
              <tr><th scope="row">Bulk cash converted to virtual currency for transfer abroad</th><td>Your monitoring flags cash-to-virtual-currency patterns, and your large cash and large virtual currency transaction reports are filed on time.</td></tr>
              <tr><th scope="row">Name and address changes</th><td>Know-your-client and counterparty files are refreshed, and changes to a business client's name, address or ownership trigger a new review.</td></tr>
              <tr><th scope="row">FINTRAC's guidance covers sanctions evasion risk</th><td>Your written risk assessment covers sanctions evasion risk, as <a href="{F_G4}" rel="noopener">FINTRAC's compliance program guidance</a> expects.</td></tr>
            </tbody>
          </table></div>
          <p>Our guide to the <a href="fintrac-risk-assessment-msb.html">MSB risk assessment</a> explains the risk factors FINTRAC expects you to document. A <a href="compliance-programs.html">compliance program review</a> can test whether these controls work in practice.</p>"""),
        ("us-exposure", "Why does a US designation matter to a Canadian MSB?", f"""          <p>Treasury's press release says US persons are generally prohibited from dealing with designated persons, and that entities owned 50% or more by blocked persons are also blocked. It adds that non-US persons are prohibited from causing US persons to violate US sanctions, and that financial institutions and others "may risk exposure to sanctions" for certain transactions with designated persons. Each SDN entry also notes "secondary sanctions risk" under section 2 of Executive Order 13902.</p>
          <p>If your business uses US banks, US dollar settlement or US-based service providers, those providers may be US persons subject to these prohibitions. Whether and how US sanctions apply to a specific business is a legal question, so get advice from a sanctions lawyer if any of your clients or counterparties appear on the SDN List. This post is general information, not legal advice.</p>"""),
    ],
    faqs=[("Which Canadian MSBs did OFAC sanction in November 2026?", "On 6 November 2026, OFAC added 1380079 BC Ltd, 2397639 Ontario Ltd, B Galaxy Inc, CCC Inc, Darvish Exchange, Diverse Trade Inc, NIA Nations Currency Ltd and Top PC Technician Inc to its SDN List under Executive Order 13902."),
          ("Did FINTRAC take part in the OFAC sanctions?", "FINTRAC said in a public statement on 6 November 2026 that it coordinated with OFAC and FinCEN in the imposition of sanctions against eight Canadian money services businesses."),
          ("Do Canadian MSBs have to report transactions connected to Iran?", "Yes. Under the ministerial directive on Iran, every transaction originating from or bound for Iran must be treated as high risk and reported to FINTRAC, whatever the amount."),
          ("Do MSBs have to report suspected sanctions evasion to FINTRAC?", "Yes. FINTRAC requires a suspicious transaction report when there are reasonable grounds to suspect a transaction relates to a sanctions evasion offence under Canada's United Nations Act, Special Economic Measures Act or Sergei Magnitsky Law."),
          ("How many MSB registrations has FINTRAC revoked in 2026?", "FINTRAC said on 6 November 2026 that it had revoked the registrations of 161 money services businesses since the beginning of 2026, more than the previous three years combined.")],
    sources=[("FINTRAC, Public Statement: Sanctions on Canadian Money Services Businesses (6 November 2026)", OS_STMT),
             ("OFAC, Recent actions: Iran-related designations (6 November 2026)", OS_OFAC),
             ("US Treasury, Operation Economic Outcast press release (6 November 2026)", OS_PR),
             ("FINTRAC, Report suspected sanctions evasion", OS_SANC),
             ("FINTRAC, Guidance on the Ministerial Directive on Iran", OS_IRI),
             ("FINTRAC, Reporting listed person or entity property", OS_LPEP),
             ("FINTRAC, Compliance program requirements (Guide 4)", F_G4),
             ("FINTRAC, Public notice of administrative monetary penalties", F_AMP_LIST)],
    related=["fintrac-travel-rule-ministerial-directives.html", "fintrac-risk-assessment-msb.html", "msb-registration-refused-revoked.html"],
)



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
            <li>Funds not placed on receipt are logged as a shortfall, under paragraphs 2.7 and 4.8 of the <a href="{BU1_SG}" rel="noopener">safeguarding guideline</a>.</li>
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
