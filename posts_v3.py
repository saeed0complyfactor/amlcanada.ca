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

from content_v3 import F_G4, F_REC_MSB, F_STR, F_SANCTIONS, F_LPEP

L_PCMLTFA = "https://laws-lois.justice.gc.ca/eng/acts/P-24.501/FullText.html"
L_PCMLTFR = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-184/FullText.html"
F_AMP_NEW = "https://fintrac-canafe.canada.ca/pen/3-eng"
F_VC_IND = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/indicators-indicateurs/vc_mltf-eng"

POSTS = {}

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
