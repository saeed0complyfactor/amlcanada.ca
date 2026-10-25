"""Guides (articles) for site-v3, rendered by build_v3.guide_page.

Each guide answers one question people search for and points to one service.
Regulatory statements were checked on 11 October 2026 against the sources listed
with each guide. Re-check before updating, and change "updated" when you do.
"""
from content_v3 import (B_FEE, B_FW, B_REG, B_RPS, F_24, F_EFT, F_G4, F_LCTR, F_LVCTR, F_MSB, F_REG, F_REC_MSB,
                        F_STR, F_TRAVEL, F_UPD, MSB_ACTIVITIES, REPORTS_TABLE, RQ_MSB)

# Official sources used only by the guides (checked 11 October 2026).
L_PCMLTFA = "https://laws-lois.justice.gc.ca/eng/acts/P-24.501/FullText.html"
L_RPAA = "https://laws-lois.justice.gc.ca/eng/acts/R-7.36/FullText.html"
L_RPAR = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2023-229/FullText.html"
L_PCMLTFR = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-184/FullText.html"
F_SANC = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/sanctions/sanctions-eng"
F_SANC_NOTICE = "https://fintrac-canafe.canada.ca/notices-avis/avs/2024-08-02-eng"
F_LPEP = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/Guide5/5-eng"
F_CHG = "https://fintrac-canafe.canada.ca/businesses-entreprises/changes-changements-eng"
F_AMP_NEW = "https://fintrac-canafe.canada.ca/pen/3-eng"
F_MSB_REGISTRY = "https://fintrac-canafe.canada.ca/msb-esm/reg-eng"
F_CAM = "https://fintrac-canafe.canada.ca/guidance-directives/exam-examen/cam/cams-eng"
F_EXAM = "https://fintrac-canafe.canada.ca/guidance-directives/exam-examen/05-2005/4-eng"
F_AMP = "https://fintrac-canafe.canada.ca/pen/2-eng"
F_AMP_LIST = "https://fintrac-canafe.canada.ca/pen/4-eng"
# Checked 16 October 2026.
F_F2R = "https://fintrac-canafe.canada.ca/reporting-declaration/info/f2r-eng"
F_API = "https://fintrac-canafe.canada.ca/reporting-declaration/info/api/api-eng"
F_DIR = "https://fintrac-canafe.canada.ca/obligations/directives-eng"
F_RBA = "https://fintrac-canafe.canada.ca/guidance-directives/compliance-conformite/rba/rba-eng"
B_FAQ = "https://www.bankofcanada.ca/2026/08/frequently-asked-questions-about-retail-payments-supervision/"
B_CRIT = "https://www.bankofcanada.ca/2026/06/criteria-for-registering-payment-service-providers/"
B_RPT = "https://www.bankofcanada.ca/2026/06/reminder-psp-reporting-obligations-under-rpaa/"
B_ACQ = "https://www.bankofcanada.ca/2024/08/acquisitions-of-control-and-prescribed-changes/"
B_SG = "https://www.bankofcanada.ca/wp-content/uploads/2024/02/safeguarding-end-user-funds.pdf"
B_SG_GLANCE = "https://www.bankofcanada.ca/wp-content/uploads/2025/02/Safeguarding-of-end-user-funds-At-a-glance.pdf"
B_SG_FAQ = B_FAQ + "#safeguarding"
FIN_STABLE = "https://www.canada.ca/en/department-finance/programs/financial-sector-policy/canadas-stablecoin-framework.html"
CSA_21_332 = ("https://www.osc.ca/en/securities-law/instruments-rules-policies/2/21-332/"
              "csa-staff-notice-21-332-crypto-asset-trading-platforms-pre-registration-undertakings-changes")
CSA_21_333 = ("https://www.osc.ca/en/securities-law/instruments-rules-policies/2/21-333/"
              "csa-staff-notice-21-333-crypto-asset-trading-platforms-terms-and-conditions-trading-value")
# Checked 22 October 2026.
BC_MSBA = "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/23019"
BC_BILL19 = "https://www.bclaws.gov.bc.ca/civix/document/id/bills/billsprevious/4th42nd:gov19-3"
BCFSA_SP = "https://bcbudget.gov.bc.ca/2026/sp/pdf/agency/bcfsa.pdf"
NP_11_204 = "https://www.osc.ca/en/securities-law/instruments-rules-policies/1/11-204/unofficial-consolidation-national-policy-11-204"

PUBLISHED = "2026-10-11"
GUIDES = {}

# ------------------------------------------------------------------ 1. how to register an MSB
GUIDES["how-to-register-msb-canada.html"] = dict(
    modified="2026-10-25",
    title="How to Register an MSB in Canada: FINTRAC Guide | AML Canada",
    desc="How to register an MSB with FINTRAC, step by step: who must register, what FINTRAC asks for, criminal record checks, approval times and renewal.",
    crumb="How to register an MSB",
    h1="How to register an MSB in Canada",
    lede="A money services business must register with FINTRAC before it starts operating, and renew every two years. FINTRAC doesn't charge a fee, and it says the majority of complete applications are processed within three months.",
    label="Guide · MSB registration",
    also=["buy-or-register-msb-canada.html"],
    service="msb-registration.html",
    takeaways=["Register with FINTRAC before you start operating. FINTRAC doesn't charge a fee.",
               "Criminal record checks are needed for the CEO, president, directors and 20%+ owners.",
               "Answer FINTRAC's clarification requests within 30 days.",
               "Registration lasts two years. Report changes within 30 days."],
    sections=[
        ("need-to-register", "Step 1: Check whether you need to register", f"""          <p>In Canada, a money services business (MSB) is a business that provides certain money services. If you have a place of business in Canada and you provide any of these, you must register with FINTRAC, the Financial Transactions and Reports Analysis Centre of Canada, before you start:</p>
          {MSB_ACTIVITIES}
          <p>If you have no place of business in Canada but you direct and provide these services to people or entities in Canada, you're a foreign MSB, and you must register too. Our <a href="foreign-msb-registration-canada.html">foreign MSB guide</a> covers that case.</p>
          <p>Registering or being licensed with a province doesn't replace FINTRAC registration. Quebec has its own licence for money-services businesses, issued by Revenu Québec, which is needed in addition to FINTRAC registration.</p>
          <p>If your business holds funds for users or transfers funds electronically for them, check the Retail Payment Activities Act as well. Many payment businesses need to register with the Bank of Canada as payment service providers, separately from FINTRAC. Our <a href="rpaa-registration-guide.html">RPAA guide</a> explains who is covered.</p>"""),
        ("gather", "Step 2: Gather what FINTRAC asks for", f"""          <p>FINTRAC's registration asks for:</p>
          <ul>
            <li>details of the business, including its <a href="incorporation-canada.html">incorporation</a>, ownership and senior management;</li>
            <li>bank account information;</li>
            <li>your compliance officer;</li>
            <li>how many employees you have, and every location you operate from;</li>
            <li>estimated annual transaction totals for each money service you offer;</li>
            <li>any agents or mandataries that provide services on your behalf;</li>
            <li>for a foreign MSB, a representative for service who lives in Canada;</li>
            <li>documents confirming the business exists and how it's owned and controlled;</li>
            <li>criminal record checks.</li>
          </ul>
          <p>If you use agents or mandataries, you must also check that they're eligible before you engage them, including reviewing their criminal record checks. This has applied since October 1, 2025. For agents engaged before that date, MSBs have until October 1, 2027, according to <a href="{F_MSB}" rel="noopener">FINTRAC</a>.</p>"""),
        ("criminal-record-checks", "Step 3: Order criminal record checks early", f"""          <p>FINTRAC needs criminal record checks for the chief executive officer, the president, the directors, and anyone who owns or controls 20% or more of the business, directly or indirectly. A sole proprietor provides one for themselves.</p>
          <p>Each check must come from a competent authority in the person's country of residence and be issued no more than six months before you apply. If a check isn't in English or French, it needs a translation attested by a certified translator, as <a href="{F_REG}" rel="noopener">FINTRAC's registration page</a> sets out. When owners and directors live in different countries, this is often the step that takes longest, so start it first.</p>"""),
        ("submit", "Step 4: Submit and answer FINTRAC's questions", f"""          <p>Once everything is gathered and checked, you submit your registration to FINTRAC. FINTRAC may send clarification requests before it decides. You have 30 days to answer each one, and if you don't, FINTRAC may deny the application (<a href="{L_PCMLTFA}" rel="noopener">PCMLTFA section 11.14</a>). Once you're registered, the same 30-day rule applies, and FINTRAC may revoke a registration if a request goes unanswered.</p>
          <p>Complete, consistent information is the best way to avoid back-and-forth. The transaction estimates, locations, ownership and documents should all tell the same story.</p>
          <p><a href="{F_REG}" rel="noopener">FINTRAC says</a> the majority of complete applications are processed within three months, and more complex ones can take longer. In our experience it has ranged from about a week to seven months, depending mostly on how complete the application is and on FINTRAC's workload. Our <a href="msb-registration.html">MSB registration service</a> covers preparing and submitting the application.</p>"""),
        ("program", "Step 5: Have your compliance program ready", """          <p>Registration allows you to operate. Your obligations under the law start at the same time. From the day you start, you need a compliance program with five elements: a compliance officer, written policies and procedures, a risk assessment, an ongoing training program, and an effectiveness review at least every two years. You also need to identify clients, keep records, generally for at least five years, and report to FINTRAC.</p>
          <p>It helps to build the program while the registration is in progress, so it's in place when you're registered. Our <a href="compliance-programs.html">compliance program documents</a> are written for this.</p>"""),
        ("stay-registered", "Step 6: Stay registered", f"""          <p>MSB registration is valid for two years and must be renewed before it expires. Between renewals, tell FINTRAC within 30 days when your registration information changes: a new address, new owners or directors, a new compliance officer, or a change in the services you offer. FINTRAC explains how on its <a href="{F_UPD}" rel="noopener">update and renewal page</a>.</p>"""),
    ],
    faqs=[("Does FINTRAC charge to register an MSB?", "No. FINTRAC doesn't charge a registration fee. Your costs are your own time, criminal record checks, any certified translations, and professional help if you use it."),
          ("Is there an MSB licence in Canada?", "At the federal level, Canada requires registration with FINTRAC under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act. When people search for an MSB licence in Canada, they usually mean FINTRAC registration. Quebec is the exception: Revenu Québec issues a separate licence for money-services businesses."),
          ("Can I register an MSB without a Canadian office?", "Yes, as a foreign MSB, if you direct and provide money services to people in Canada. You'll need a representative for service who lives in Canada."),
          ("Do I need a compliance program before registering?", "You need it in place to operate, and FINTRAC asks for your compliance officer when you register. It makes sense to build both together."),
          ("How long is MSB registration valid?", "Two years. Changes to your registration information must be reported within 30 days."),
          ("How long does FINTRAC take to approve an MSB registration?", "FINTRAC says the majority of complete applications are processed within three months. In our experience it has ranged from about a week to seven months.")],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("Money services businesses", F_MSB), ("Update, renew or cancel your registration", F_UPD),
             ("Compliance program requirements", F_G4), ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA),
             ("Revenu Québec, Money-services business licence", RQ_MSB)],
    related=["msb-registration-cost-canada.html", "foreign-msb-registration-canada.html", "buying-an-msb-canada.html"],
)

# ------------------------------------------------------------------ 2. cost
GUIDES["msb-registration-cost-canada.html"] = dict(
    title="How Much Does MSB Registration Cost in Canada? | AML Canada",
    desc="What it costs to register a money services business in Canada: FINTRAC's fee (none), the other costs of registering, and what professional help costs.",
    crumb="MSB registration cost",
    h1="How much does MSB registration cost in Canada?",
    lede="FINTRAC doesn't charge a fee to register a money services business. The costs come from criminal record checks, translations, documents and the compliance program you need to operate.",
    label="Guide · Costs",
    service="pricing.html",
    takeaways=["FINTRAC registration itself is free.",
               "Budget for criminal record checks, certified translations and documents.",
               "You need a compliance program in place before you operate.",
               "Our fixed fees: US$3,500 registration; US$3,500 program documents."],
    sections=[
        ("fintrac-fee", "FINTRAC's fee: none", f"""          <p><a href="{F_REG}" rel="noopener">FINTRAC</a> doesn't charge a fee to register a money services business, or to renew. If anyone tells you there's a government fee for FINTRAC MSB registration, ask what it's for.</p>"""),
        ("other-costs", "The other costs of registering", f"""          <p>Criminal record checks are one of the main outside costs. FINTRAC needs one for the CEO, the president, each director and anyone owning or controlling 20% or more, and each must be issued within six months before you apply. Costs vary by country and by provider.</p>
          <p>Any check or document that isn't in English or French needs a translation attested by a certified translator. You'll also need corporate documents showing the business exists and how it's owned and controlled.</p>
          <p>If you don't have a Canadian company yet, there are government incorporation fees, currently CA$200 federally online or CA$300 in Ontario online. Where provincial licensing applies, there are fees for that too: Quebec licenses money-services businesses separately through <a href="{RQ_MSB}" rel="noopener">Revenu Québec</a>, which sets its own fees.</p>
          <p>Then there's time: gathering and checking everything, and answering FINTRAC's clarification requests within 30 days. Our <a href="how-to-register-msb-canada.html">step-by-step registration guide</a> shows where the time goes.</p>"""),
        ("operating-costs", "What it costs to operate once registered", """          <p>To operate, an MSB needs a compliance program: a compliance officer, policies and procedures, a risk assessment, training and an effectiveness review at least every two years. It also has to report to FINTRAC and keep records. These are ongoing costs, whether you staff them in-house or outsource them. Our <a href="compliance-programs.html">compliance program documents</a> cover the written part at a fixed fee.</p>"""),
        ("our-fees", "What professional help costs with us", """          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Service</th><th scope="col">Fee</th></tr></thead>
            <tbody>
              <tr><th scope="row"><a href="incorporation-canada.html">Canadian company incorporation</a></th><td>US$1,500, fixed (government fees separate)</td></tr>
              <tr><th scope="row"><a href="msb-registration.html">FINTRAC MSB registration</a></th><td>US$3,500, fixed</td></tr>
              <tr><th scope="row"><a href="compliance-programs.html">PCMLTFA compliance program (14 documents)</a></th><td>US$3,500, fixed</td></tr>
              <tr><th scope="row"><a href="outsourced-compliance-officer.html">Outsourced compliance officer</a></th><td>US$1,500 per 10 hours</td></tr>
              <tr><th scope="row"><a href="canadian-address.html">Canadian business address</a></th><td>US$200 per month</td></tr>
              <tr><th scope="row"><a href="msb-for-sale.html">Registered MSB to acquire</a></th><td>From €28,000</td></tr>
            </tbody>
          </table></div>
          <p>All fees are on our <a href="pricing.html">pricing page</a>. Every engagement starts with a consultation and a written scope, so you know the fee before any work begins.</p>"""),
        ("buy-or-register", "Registering vs buying a registered MSB", """          <p>Some businesses buy a company that's already registered instead of registering a new one. It costs more up front. It still needs due diligence, updates to FINTRAC within 30 days of changes like new owners and directors, criminal record checks for the new people, and a compliance program that fits the new owners. Our guide to <a href="buying-an-msb-canada.html">buying an MSB</a> covers what to check.</p>"""),
    ],
    faqs=[("Is FINTRAC MSB registration free?", "Yes. FINTRAC doesn't charge to register or renew."),
          ("How much does it cost to set up an MSB in Canada?", "Registration is free, but budget for criminal record checks, certified translations, documents and a compliance program. Our fixed fees are US$3,500 for registration and US$3,500 for compliance program documents."),
          ("Does Quebec charge for an MSB licence?", "Yes. Quebec licenses money-services businesses separately through Revenu Québec, which sets its own fees.")],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("Update, renew or cancel your registration", F_UPD), ("Compliance program requirements", F_G4),
             ("Revenu Québec, Money-services business licence", RQ_MSB)],
    related=["how-to-register-msb-canada.html", "buying-an-msb-canada.html", "outsourced-vs-in-house-compliance-officer.html"],
)

# ------------------------------------------------------------------ 3. foreign MSB
GUIDES["foreign-msb-registration-canada.html"] = dict(
    title="Foreign MSB Registration in Canada (FMSB) | AML Canada",
    desc="When a business outside Canada, including EU, UK and UAE payment firms, must register with FINTRAC as a foreign MSB, and when RPAA registration applies too.",
    crumb="Foreign MSB registration",
    modified="2026-10-18",
    checked="18 October 2026",
    also=["buy-or-register-msb-canada.html", "canadian-address.html", "rpaa-registration.html"],
    h1="Foreign MSB registration in Canada",
    lede="A business with no office in Canada may still have to register with FINTRAC. It does if it directs and provides money services to people or entities in Canada.",
    label="Guide · Foreign MSB",
    service="msb-registration.html",
    takeaways=["A licence from your home country doesn't cover serving people in Canada.",
               "Foreign MSBs that direct and provide services to Canada must register first.",
               "Marketing to Canadians, a .ca domain or Canadian listings can count.",
               "You need a representative for service who lives in Canada.",
               "Foreign payment service providers may need Bank of Canada RPAA registration too."],
    sections=[
        ("what-is", "What is a foreign MSB?", f"""          <p>A foreign money services business (FMSB) has no place of business in Canada but directs and provides money services to people or entities in Canada. The money services are the same ones that apply to Canadian MSBs:</p>
          {MSB_ACTIVITIES}
          <p>A foreign MSB must register with FINTRAC before it starts providing these services to Canada. A business with a place of business in Canada, such as a physical location, is a domestic MSB under <a href="{F_MSB}" rel="noopener">FINTRAC's definitions</a>, and registers as one. Our <a href="how-to-register-msb-canada.html">guide to registering an MSB</a> covers the steps for both.</p>"""),
        ("directing", "What counts as directing services at Canada", """          <p>FINTRAC looks at whether your business targets people in Canada. Examples it gives include marketing aimed at people in Canada, operating a .ca domain name, and being listed in a Canadian business directory. If your website, ads or partnerships are built to attract Canadian customers, assume you're in scope and get it confirmed.</p>"""),
        ("home-licence", "Licensed in the EU, UK or UAE? That doesn't cover Canada", """          <p>Payment and e-money firms licensed in Lithuania, Cyprus or elsewhere in the EU, firms authorized in the UK, and firms licensed in the UAE often look at Canada next. Their existing licence or registration doesn't carry over. Whether you must register with FINTRAC depends on what you do for people in Canada: if you direct and provide money services to people or entities in Canada, you register as a foreign MSB, whatever licences you hold elsewhere.</p>
          <p>Your home-country AML program is a useful starting point, but it won't map onto Canadian requirements on its own. FINTRAC's reporting types, thresholds, record-keeping rules and the <a href="how-to-register-msb-canada.html">registration process</a> are Canadian. Plan to adapt your policies and procedures, risk assessment and training to the PCMLTFA before you start serving Canadian clients.</p>"""),
        ("psp", "Payment service providers: RPAA registration too", f"""          <p>FINTRAC registration isn't the only federal regime. The Retail Payment Activities Act (RPAA), supervised by the Bank of Canada, covers payment service providers that perform payment functions for end users, such as holding funds, initiating or transmitting electronic funds transfers, or providing clearing and settlement. A PSP outside Canada is covered when it directs retail payment activities at people or entities in Canada and performs them for end users in Canada (RPAA s.5).</p>
          <p>A foreign payment firm can therefore need both: foreign MSB registration with FINTRAC and PSP registration with the Bank of Canada. Our <a href="rpaa-registration-guide.html">guide to the RPAA</a> explains who it applies to, and our <a href="rpaa-registration.html">RPAA registration service</a> covers the application. See the <a href="{B_RPS}" rel="noopener">Bank of Canada's retail payments supervision pages</a> for the source.</p>"""),
        ("route", "Register as a foreign MSB, or set up in Canada?", """          <p>The route follows where your business will operate:</p>
          <ul>
            <li><strong>No place of business in Canada.</strong> You serve Canadian clients from abroad and register with FINTRAC as a foreign MSB, with a representative for service in Canada.</li>
            <li><strong>A place of business in Canada.</strong> If you'll have a physical location in Canada, you're a domestic MSB under FINTRAC's definitions. Most firms in this position <a href="incorporation-canada.html">incorporate a Canadian company</a> and register it.</li>
            <li><strong>Acquiring a registered company.</strong> Some buyers take over a Canadian company that is already registered with FINTRAC. That is a corporate acquisition, and the target needs proper due diligence. See our guide to <a href="buying-an-msb-canada.html">buying an MSB in Canada</a>.</li>
          </ul>
          <p>Choosing the wrong route is expensive to unwind, so confirm it before you file. We can help in a <a href="contact.html">consultation</a>.</p>"""),
        ("representative", "Your representative for service in Canada", f"""          <p>A foreign MSB must name a representative for service who resides in Canada and is authorized to accept notices from FINTRAC on its behalf. The representative doesn't take over your obligations. The foreign business itself stays responsible for complying with Canada's anti-money laundering law.</p>
          <p>If the representative's name or address for service changes, you must tell FINTRAC within 30 days. If you don't, FINTRAC must deny the application or revoke the registration (<a href="{L_PCMLTFA}" rel="noopener">PCMLTFA subsection 11.13(2)</a>).</p>
          <p>The representative is a person. Having a Canadian business address is a separate matter from the representative requirement. Some foreign MSBs want one for banking, partners or customers. We offer a <a href="canadian-address.html">Canadian business address</a>, and you can ask us about the representative requirement in your consultation.</p>"""),
        ("obligations", "Obligations once registered", """          <p>Foreign MSBs carry substantially the same obligations as Canadian ones: a compliance program, client identification, record keeping, reporting to FINTRAC, the travel rule for funds and virtual currency transfers, and renewing their registration every two years, with changes reported within 30 days. Our <a href="fintrac-reporting-requirements.html">FINTRAC reporting guide</a> sets out which reports apply.</p>
          <p>Many foreign MSBs don't have an experienced compliance person in Canada. Some appoint an <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> who works with FINTRAC's requirements.</p>"""),
        ("checks", "Criminal record checks from abroad", """          <p>FINTRAC needs criminal record checks for the CEO, president, directors and anyone owning or controlling 20% or more, issued in each person's country of residence within six months before you apply. Checks that aren't in English or French need a translation attested by a certified translator. For international ownership, this is usually the longest step.</p>"""),
    ],
    faqs=[("Do foreign companies need to register with FINTRAC?", "Yes, if they direct and provide money services to people or entities in Canada. They register as foreign MSBs before they start."),
          ("Does an EU, UK or UAE licence let us serve Canadian clients?", "No. Registration with FINTRAC depends on what you do for people in Canada, not on licences held elsewhere. If you direct and provide money services to people in Canada, you register as a foreign MSB."),
          ("Do foreign payment companies also need Bank of Canada registration?", "Often, yes. A payment service provider outside Canada is covered by the RPAA when it directs retail payment activities at people or entities in Canada and performs them for end users in Canada. Many need both FINTRAC and Bank of Canada registration."),
          ("Does a foreign MSB need a Canadian address?", "FINTRAC requires a representative for service who resides in Canada. A Canadian business address is a separate thing that some foreign MSBs also want for banking, partners and customers."),
          ("What if our representative for service changes?", "Tell FINTRAC within 30 days. If the new name or address isn't provided in time, FINTRAC must deny the application or revoke the registration."),
          ("Can a foreign MSB outsource its compliance officer?", "Many do. The foreign business stays responsible for its obligations, but an experienced compliance officer in Canada can carry the day-to-day work.")],
    sources=[("FINTRAC, Money services businesses", F_MSB), ("Register your MSB or FMSB", F_REG), ("Travel rule", F_TRAVEL), ("Update, renew or cancel your registration", F_UPD),
             ("Bank of Canada, Retail payments supervision", B_RPS),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA)],
    related=["how-to-register-msb-canada.html", "rpaa-registration-guide.html", "buying-an-msb-canada.html"],
)

# ------------------------------------------------------------------ 4. reporting
GUIDES["fintrac-reporting-requirements.html"] = dict(
    title="FINTRAC Reporting for MSBs: STR, LCTR, EFTR, LVCTR | AML Canada",
    desc="Which reports a money services business must file with FINTRAC, when each applies, the $10,000 threshold, the 24-hour rule and the deadline for each report.",
    crumb="FINTRAC reporting",
    also=["compliance-programs.html", "training.html"],
    h1="FINTRAC reporting for MSBs: which report, and when",
    lede="Money services businesses report suspicious transactions, large cash, international transfers, large virtual currency receipts and listed person property to FINTRAC. Each report has its own trigger and deadline.",
    label="Guide · Reporting",
    service="outsourced-compliance-officer.html",
    takeaways=["STRs have no minimum amount and are due as soon as practicable.",
               "LCTR, EFTR and LVCTR apply at $10,000 or more.",
               "The 24-hour rule adds up transactions you know are linked.",
               "Threshold reports are due within 5 working days to 15 calendar days."],
    sections=[
        ("overview", "The reports at a glance", f"""          {REPORTS_TABLE}
          <p>Amounts are in Canadian dollars, or the equivalent in another currency or in virtual currency.</p>"""),
        ("str", "Suspicious transaction reports (STR)", f"""          <p>You must report a transaction, or an attempted one, when you have reasonable grounds to suspect it's related to money laundering, terrorist financing or, since August 19, 2024, a sanctions evasion offence (<a href="{L_PCMLTFA}" rel="noopener">PCMLTFA section 7</a>). A sanctions evasion offence means breaching a sanctions restriction under the United Nations Act, the Special Economic Measures Act or the Justice for Victims of Corrupt Foreign Officials Act. <a href="{F_SANC}" rel="noopener">FINTRAC's sanctions evasion guidance</a> explains how to flag these reports, and its <a href="{F_SANC_NOTICE}" rel="noopener">August 2024 notice</a> announced the change.</p>
          <p>There's no minimum amount. FINTRAC expects the report "as soon as practicable": somewhere between immediately and as soon as possible, with completing the STR taking priority over other tasks.</p>
          <p>Good STRs explain why: what you saw, the indicators, and how the facts fit together. A transaction can need both an STR and another report, for example a suspicious large cash deposit.</p>"""),
        ("lctr", "Large cash transaction reports (LCTR)", f"""          <p>When you receive $10,000 or more in cash, in one transaction or in several that the 24-hour rule adds together, you report it within 15 calendar days. See <a href="{F_LCTR}" rel="noopener">FINTRAC's LCTR guidance</a>.</p>"""),
        ("eftr", "Electronic funds transfer reports (EFTR)", """          <p>International electronic funds transfers of $10,000 or more, sent or finally received, in one transfer or in several that the 24-hour rule adds together, are reported within 5 working days.</p>"""),
        ("lvctr", "Large virtual currency transaction reports (LVCTR)", """          <p>When you receive virtual currency worth $10,000 or more, in one transaction or in several that the 24-hour rule adds together, you report it within 5 working days after the day you receive it. A working day is Monday to Friday, excluding public holidays.</p>"""),
        ("24-hour-rule", "The 24-hour rule", f"""          <p>The 24-hour rule stops threshold reporting being avoided by splitting transactions. When you know that two or more transactions of the same type, totalling $10,000 or more within a 24-hour window, were conducted by the same person or entity, on behalf of the same person or entity, or for the same beneficiary, you report them together. The individual transactions can be any amount.</p>
          <p>FINTRAC uses a static 24-hour window: you set fixed 24-hour periods, for example 9 a.m. one day to 8:59 a.m. the next. If a client gives you $6,000 in cash at 10 a.m. and another $5,000 at 3 p.m. in the same window, you file one LCTR for $11,000. Your systems need to add these up. <a href="{F_24}" rel="noopener">FINTRAC's 24-hour rule guidance</a> has more examples.</p>"""),
        ("listed-property", "Listed person or entity property reports", f"""          <p>If you know or believe property in your possession or control is owned or controlled by a listed person or entity, you must file a Listed Person or Entity Property Report with FINTRAC immediately, and you can't deal with that property. This report replaced the terrorist property report on March 2, 2025. Since October 1, 2025, it also covers persons and entities listed under the Special Economic Measures Act and the Justice for Victims of Corrupt Foreign Officials Act.</p>
          <p>Separately from the FINTRAC report, the law requires you to disclose the property without delay to the Commissioner of the RCMP and the Director of CSIS. See <a href="{F_LPEP}" rel="noopener">FINTRAC's listed person property guidance</a>.</p>"""),
        ("travel-rule", "The travel rule", """          <p>When MSBs send electronic funds or virtual currency transfers, the information about who requested the transfer and the beneficiary must travel with it: names, addresses and account or reference numbers. Received travel-rule information can't be stripped out. The travel rule doesn't involve filing a report. It supports your record keeping and reporting.</p>"""),
        ("getting-it-right", "Getting reporting right", """          <ul>
            <li>Know which reports apply to your services, and test that your systems flag them.</li>
            <li>Track deadlines from the right day, in working days or calendar days as the report requires.</li>
            <li>Document why you did or didn't file an STR.</li>
            <li>Keep the records behind every report, generally for at least five years.</li>
          </ul>
          <p>Your <a href="compliance-programs.html">policies and procedures</a> should set out how each of these is done, and staff who handle transactions need <a href="training.html">training</a> on them. An <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> can handle this reporting.</p>"""),
    ],
    faqs=[("What is the FINTRAC reporting threshold?", "$10,000 for large cash, international electronic funds transfer and large virtual currency transaction reports, including linked transactions that add up to $10,000 within 24 hours. Suspicious transaction reports have no threshold."),
          ("How long do I have to file an EFTR?", "5 working days."),
          ("How long do I have to file an LCTR?", "15 calendar days after the day you receive the cash."),
          ("When is an STR due?", "As soon as practicable, which FINTRAC describes as between immediately and as soon as possible."),
          ("Do I report suspected sanctions evasion to FINTRAC?", "Yes. Since August 19, 2024, suspicious transaction reports also cover transactions you have reasonable grounds to suspect are related to a sanctions evasion offence.")],
    sources=[("FINTRAC, Reporting suspicious transactions", F_STR), ("Report suspected sanctions evasion", F_SANC), ("FINTRAC notice, August 2, 2024", F_SANC_NOTICE), ("Reporting large cash transactions", F_LCTR),
             ("Reporting electronic funds transfers", F_EFT), ("Reporting large virtual currency transactions", F_LVCTR), ("The 24-hour rule", F_24),
             ("Reporting listed person or entity property", F_LPEP), ("Travel rule", F_TRAVEL), ("Record keeping for MSBs", F_REC_MSB),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA)],
    related=["crypto-registration-canada.html", "fintrac-examination-preparation.html", "outsourced-vs-in-house-compliance-officer.html"],
)

# ------------------------------------------------------------------ 5. RPAA
GUIDES["rpaa-registration-guide.html"] = dict(
    title="What Is the RPAA? Retail Payment Activities Act | AML Canada",
    desc="The Retail Payment Activities Act explained: what it covers, the five payment functions, who is excluded, foreign PSPs, and how it differs from FINTRAC.",
    crumb="RPAA explained",
    h1="What is the RPAA?",
    lede="The Retail Payment Activities Act is the federal law under which the Bank of Canada supervises payment service providers. It sets rules on operational risk, incidents and the safeguarding of users' funds.",
    label="Guide · RPAA",
    service="rpaa-registration.html",
    also=["rpaa-compliance-program.html"],
    takeaways=["The RPAA applies to payment service providers performing retail payment activities.",
               "Foreign PSPs are covered when they direct activities at Canada and serve end users here.",
               "Banks, credit unions and some other institutions are excluded.",
               "The RPAA sits alongside FINTRAC rules, and many businesses need both."],
    sections=[
        ("what-is", "What the RPAA is", f"""          <p>The <a href="{L_RPAA}" rel="noopener">Retail Payment Activities Act</a> (RPAA) brought payment service providers (PSPs) under federal supervision for the first time. Payment processors, digital wallets and money transfer apps are typical examples. The Bank of Canada supervises them, with a focus on three things: managing operational risk, responding to incidents, and protecting the funds PSPs hold for their users.</p>
          <p>The Act defines a PSP as an individual or entity that performs payment functions as a service or business activity that isn't incidental to another service or business activity. A retail payment activity is a payment function performed in relation to an electronic funds transfer in Canadian or another currency.</p>"""),
        ("payment-functions", "The five payment functions", """          <p>The Act lists five payment functions. A PSP performs one or more of them for end users:</p>
          <ul>
            <li>keeping an account for one or more end users that's used for electronic funds transfers;</li>
            <li>holding funds for an end user until they're withdrawn or sent to someone else;</li>
            <li>starting an electronic funds transfer when an end user asks for it;</li>
            <li>authorizing an electronic funds transfer, or transmitting, receiving or facilitating the instruction for one;</li>
            <li>clearing or settlement services.</li>
          </ul>"""),
        ("scope", "Who the Act covers", f"""          <p>The RPAA applies to retail payment activities performed by a PSP with a place of business in Canada. It also applies to a PSP outside Canada that directs retail payment activities at individuals or entities in Canada and performs them for end users in Canada (RPAA section 5).</p>
          <p>A new PSP must register with the Bank before it performs any retail payment activities, according to the <a href="{B_CRIT}" rel="noopener">Bank's registration criteria</a>. Registered PSPs are listed on the Bank's public registry.</p>"""),
        ("exclusions", "What's excluded", """          <p>Sections 6 to 10 of the Act set out exclusions. Some institutions are outside the RPAA, including banks, authorized foreign banks, provincially regulated credit unions and caisses populaires, insurance companies, federal trust and loan companies, and provincially regulated trust companies.</p>
          <p>Some activities are excluded too, including payments made with closed-loop instruments such as gift cards that can be used only with the issuing merchant or a group of merchants, cash withdrawals at ATMs, and certain securities and financial contract transactions. An agent of a registered PSP that is acting within its authority and is on the PSP's list of agents isn't separately covered.</p>"""),
        ("registration", "Registration, review and fees", f"""          <p>The Bank charges a one-time, non-refundable application fee. It was CA$2,500 when registration opened in November 2024, and it's set by <a href="{L_RPAR}" rel="noopener">regulation</a> and adjusted for inflation each January. We confirm the current amount before you apply. The Bank plans to charge registered PSPs annual assessment fees to recover the cost of supervision, but it hasn't started yet. Its <a href="{B_FAQ}" rel="noopener">FAQ</a> says it will begin charging them in due course, once the fee formula is finalized.</p>
          <p>Application information is shared with the Department of Finance and with FINTRAC. If the Minister of Finance considers it necessary for national security reasons, the Minister can order a full review of an application, and the Bank can't register the applicant while that review is under way. Our <a href="rpaa-registration.html">RPAA registration service</a> covers the application itself.</p>"""),
        ("after", "Ongoing obligations", f"""          <p>Since September 8, 2025, PSPs must have a risk management and incident response framework, and those that hold end-user funds must <a href="rpaa-safeguarding-end-user-funds.html">safeguard them</a>, either in a trust account or in a segregated account with insurance or a guarantee.</p>
          <p>When a PSP becomes aware of an incident with a material impact, it must notify the Bank and the affected end users, PSPs or clearing houses without delay (RPAA section 18). The Bank's <a href="{B_RPT}" rel="noopener">reporting reminder</a> says the initial notice to the Bank is due no later than 48 hours after the PSP determines the incident is material. PSPs also give notice at least five business days before a significant change or new activity, and file an annual report by March 31. Our <a href="rpaa-compliance-program.html">RPAA compliance program</a> covers these frameworks.</p>"""),
        ("fintrac", "RPAA and FINTRAC", """          <p>The two regimes sit side by side. The RPAA deals with operational risk and safeguarding under the Bank of Canada. FINTRAC deals with money laundering, terrorist financing and sanctions evasion under the PCMLTFA. A payment business that also remits or transmits funds usually needs to <a href="how-to-register-msb-canada.html">register with FINTRAC as an MSB</a> as well as with the Bank.</p>"""),
    ],
    faqs=[("What does RPAA stand for?", "The Retail Payment Activities Act, the law under which the Bank of Canada supervises payment service providers."),
          ("How much is the Bank of Canada's RPAA fee?", "A one-time, non-refundable application fee. It was CA$2,500 when introduced in November 2024 and is adjusted for inflation each January, so we confirm the current amount before you apply. Annual assessment fees aren't charged yet."),
          ("Do foreign PSPs have to register under the RPAA?", "Yes, if they direct retail payment activities at individuals or entities in Canada and perform them for end users in Canada."),
          ("When does a PSP have to notify the Bank of an incident?", "Without delay, and no later than 48 hours after it determines that the incident has a material impact. Affected end users, PSPs and clearing houses must also be notified."),
          ("How long does RPAA registration take?", "In our experience, generally about 2 to 8 months, including the national security review.")],
    sources=[("Retail Payment Activities Act", L_RPAA), ("Retail Payment Activities Regulations", L_RPAR), ("Bank of Canada, Retail payments supervision", B_RPS),
             ("Supervisory framework", B_FW), ("Retail payments supervision FAQ", B_REG), ("Registration application fee", B_FEE),
             ("Criteria for registering PSPs", B_CRIT), ("PSP reporting obligations", B_RPT)],
    related=["how-to-register-msb-canada.html", "fintrac-reporting-requirements.html", "msb-registration-cost-canada.html"],
)

# ------------------------------------------------------------------ 6. crypto
GUIDES["crypto-registration-canada.html"] = dict(
    title="Crypto Business Registration in Canada (FINTRAC) | AML Canada",
    desc="How crypto exchanges and virtual currency dealers register with FINTRAC as MSBs, and what follows: LVCTRs, the travel rule, record keeping and provincial rules.",
    crumb="Crypto registration",
    also=["compliance-programs.html"],
    h1="Registering a crypto business with FINTRAC",
    lede="Crypto exchanges and virtual currency dealers register with FINTRAC as money services businesses, whether they're based in Canada or serve Canadians from abroad.",
    label="Guide · Virtual currency",
    service="msb-registration.html",
    takeaways=["Dealing in virtual currency is a money service: register with FINTRAC first.",
               "Foreign crypto businesses serving Canada register as foreign MSBs.",
               "Report virtual currency receipts of $10,000+ within 5 working days.",
               "Trading platforms also deal with provincial securities regulators."],
    sections=[
        ("register", "Crypto businesses register as MSBs", """          <p>Dealing in virtual currency is one of the money services FINTRAC lists, so crypto exchanges and virtual currency dealers register with FINTRAC as money services businesses before they start. A crypto business outside Canada that directs and provides these services to people in Canada registers as a <a href="foreign-msb-registration-canada.html">foreign MSB</a>. The <a href="how-to-register-msb-canada.html">registration steps</a> are the same as for any MSB.</p>"""),
        ("lvctr", "Large virtual currency transaction reports", f"""          <p>When you receive virtual currency worth $10,000 or more, you file a large virtual currency transaction report (LVCTR) within 5 working days after the day you receive it. Under the 24-hour rule, this includes several receipts within a 24-hour window that total $10,000 or more, when you know they were made by or for the same person or entity, or for the same beneficiary. See <a href="{F_LVCTR}" rel="noopener">FINTRAC's LVCTR guidance</a>. Suspicious transaction reports apply too, with no minimum amount. Our <a href="fintrac-reporting-requirements.html">FINTRAC reporting guide</a> covers both.</p>"""),
        ("travel-rule", "The travel rule for virtual currency", """          <p>When you send a virtual currency transfer, you must include the requester's name, address and account or reference number, and the beneficiary's name, address and account or reference number. When you receive transfers, you must take reasonable measures to make sure that information is included. You can't strip received travel-rule information out of a transfer.</p>"""),
        ("records", "Record keeping", """          <p>For virtual currency transfers of $1,000 or more, MSBs keep detailed records, including the date, the type and amount of virtual currency, client and beneficiary details, transaction hashes, sending and receiving addresses, and the exchange rates used. Records are generally kept for at least five years.</p>"""),
        ("provincial", "Provincial rules", f"""          <p>FINTRAC registration is federal. Crypto trading platforms are also regulated by provincial securities regulators. A platform operating in Canada is expected to register with them or, while it seeks registration, file a pre-registration undertaking, under <a href="{CSA_21_332}" rel="noopener">CSA Staff Notice 21-332</a>. Platforms that let clients trade stablecoins, which securities regulators call value-referenced crypto assets, are expected to follow the terms in <a href="{CSA_21_333}" rel="noopener">CSA Staff Notice 21-333</a>.</p>
          <p>Quebec also licenses money-services businesses through Revenu Québec. British Columbia has passed its own Money Services Businesses Act, which isn't in force yet; see <a href="ontario-vs-bc-msb-registration.html">Ontario vs B.C. MSB registration</a>. We'll tell you when you need separate advice on these rules.</p>"""),
        ("changes", "Changes in 2025 and 2026", f"""          <p>Since October 1, 2025, regulations strengthening the MSB registration framework have been in force, including obligations when MSBs engage agents or mandataries.</p>
          <p>Bill C-12, which received Royal Assent on March 26, 2026, raised the maximum administrative monetary penalty for violations after that date to $4 million per violation for a person and $20 million for an entity. It also requires compliance agreements after penalties, adds compliance orders, and requires compliance programs to be reasonably designed, risk-based and effective. FINTRAC lists these on its <a href="{F_CHG}" rel="noopener">changes page</a>.</p>
          <p>The Budget 2025 Implementation Act, which also received Royal Assent on March 26, 2026, created the Stablecoin Act. It isn't in force yet. Under the <a href="{FIN_STABLE}" rel="noopener">federal stablecoin framework</a>, stablecoin issuers will register with the Bank of Canada, which will supervise them, and FINTRAC says they will also register with it as MSBs dealing in virtual currency.</p>"""),
        ("program", "Your compliance program", """          <p>A crypto MSB needs the same five-part compliance program as any MSB, written for crypto risks: wallet screening, blockchain analytics, travel rule handling and virtual currency reporting. Our <a href="compliance-programs.html">14-document program</a> includes a Travel Rule Policy and Procedure.</p>"""),
    ],
    faqs=[("Do crypto exchanges need to register in Canada?", "Yes. Dealing in virtual currency is a money service, so crypto exchanges and dealers register with FINTRAC as MSBs. Trading platforms also deal with provincial securities regulators."),
          ("What is an LVCTR?", "A large virtual currency transaction report, filed within 5 working days when you receive virtual currency worth $10,000 or more, including linked receipts that the 24-hour rule adds together."),
          ("Does the travel rule apply to crypto in Canada?", "Yes. MSBs must include requester and beneficiary information when they send virtual currency transfers, and take reasonable measures to check it's included when they receive them."),
          ("Is the Stablecoin Act in force?", "Not yet. It received Royal Assent on March 26, 2026, and will come into force once its regulations are made.")],
    sources=[("FINTRAC, Money services businesses", F_MSB), ("Reporting large virtual currency transactions", F_LVCTR), ("The 24-hour rule", F_24), ("Travel rule", F_TRAVEL),
             ("Record keeping for MSBs", F_REC_MSB), ("FINTRAC, Changes to legislation and regulations", F_CHG), ("Administrative monetary penalties: changes", F_AMP_NEW),
             ("Department of Finance, Canada's stablecoin framework", FIN_STABLE), ("CSA Staff Notice 21-332", CSA_21_332), ("CSA Staff Notice 21-333", CSA_21_333),
             ("Revenu Québec, Money-services business licence", RQ_MSB)],
    related=["fintrac-reporting-requirements.html", "foreign-msb-registration-canada.html", "how-to-register-msb-canada.html"],
)

# ------------------------------------------------------------------ 7. effectiveness review checklist
GUIDES["fintrac-effectiveness-review-checklist.html"] = dict(
    title="FINTRAC Two-Year Effectiveness Review Checklist | AML Canada",
    desc="A checklist for the two-year AML effectiveness review FINTRAC requires: what to test, who can do it, the 30-day report to a senior officer and common gaps.",
    crumb="Effectiveness review checklist",
    also=["compliance-programs.html"],
    h1="The two-year effectiveness review: a checklist",
    lede="FINTRAC requires every reporting entity to review its compliance program at least every two years. The review should test how the program works in practice as well as what's written down.",
    label="Guide · Effectiveness review",
    service="effectiveness-reviews.html",
    takeaways=["Review every part of your compliance program at least every two years.",
               "An internal or external auditor does it, or you, if you have no auditor.",
               "If you're an entity, report the findings to a senior officer within 30 days.",
               "Test whether procedures are followed, as well as whether documents exist."],
    sections=[
        ("requirement", "What FINTRAC requires", f"""          <p>Every business FINTRAC regulates must institute and document a plan to review the effectiveness of its compliance program, and carry out the review at least every two years. The plan must include all the elements of the program: policies and procedures, risk assessment and training. The requirements are in <a href="{F_G4}" rel="noopener">FINTRAC's compliance program guidance</a>.</p>
          <p>The review is done by an internal or external auditor or, if you don't have an auditor, by yourself. FINTRAC's best-practice advice is that whoever does it shouldn't be directly involved in the compliance program activities being reviewed, so the review stays impartial. Some businesses use an <a href="effectiveness-reviews.html">external effectiveness review</a> for that reason.</p>"""),
        ("checklist", "The checklist", """          <h3>Policies and procedures</h3>
          <ul>
            <li>Are they written, current, and approved by a senior officer (if you're an entity)?</li>
            <li>Do they reflect the services you offer today, including anything launched since the last review?</li>
            <li>Do they cover identification, beneficial ownership, politically exposed persons, third-party determination, ongoing monitoring, record keeping, reporting, ministerial directives and the travel rule where it applies?</li>
          </ul>
          <h3>Risk assessment</h3>
          <ul>
            <li>Does it cover your clients and business relationships, products, services and delivery channels, geography, and new developments and technologies?</li>
            <li>Does it assess sanctions evasion risk alongside money laundering and terrorist financing risk?</li>
            <li>Does it take account of the risks the latest National Risk Assessment identifies for your sector?</li>
            <li>Has it been updated for new products, markets or agents?</li>
            <li>Do your controls follow from it, with enhanced measures for high risk?</li>
          </ul>
          <h3>Training</h3>
          <ul>
            <li>Is there a written, <a href="training.html">ongoing training program</a> and plan?</li>
            <li>Did the people who need training, including agents, receive it, and are there records?</li>
            <li>Does the content match your risks and your staff's roles?</li>
          </ul>
          <h3>The program in practice</h3>
          <ul>
            <li>Sample client files: was identity verified the way your procedures say?</li>
            <li>Sample transactions: were reportable transactions reported on time, including under the 24-hour rule?</li>
            <li>Review unusual-activity decisions: were STR decisions documented either way?</li>
            <li>Check that records can be produced, and are kept for the required period.</li>
            <li>Check that findings from the last review were fixed.</li>
          </ul>
          <p>If your policies or risk assessment need rewriting after the review, our <a href="compliance-programs.html">compliance program documents</a> can replace them.</p>"""),
        ("report", "Reporting the results", """          <p>If you're an entity, you must report in writing to a senior officer no later than 30 days after the review is completed. The report covers the findings of the review, the updates made to your policies and procedures during the reporting period, and the status of putting those updates in place. Keep the report. It's one of the first things an examiner may ask for, as our <a href="fintrac-examination-preparation.html">examination guide</a> explains.</p>"""),
        ("common-gaps", "Common gaps", """          <ul>
            <li>A review that checks documents exist but never tests whether they're followed.</li>
            <li>The same review copied from the previous cycle.</li>
            <li>A risk assessment that hasn't changed since launch, though the business has.</li>
            <li>No assessment of sanctions evasion risk.</li>
            <li>Findings from the last review still open.</li>
            <li>No written report to a senior officer, or one sent late.</li>
          </ul>"""),
    ],
    faqs=[("How often is an AML effectiveness review required?", "At least every two years."),
          ("Who can do the effectiveness review?", "An internal or external auditor, or yourself if you don't have an auditor. FINTRAC suggests it shouldn't be someone directly involved in the activities being reviewed."),
          ("What happens after the review?", "If you're an entity, report the findings in writing to a senior officer within 30 days, along with the updates made to policies and procedures and how far they've been put in place.")],
    sources=[("FINTRAC, Compliance program requirements", F_G4), ("Risk assessment guidance", F_RBA), ("The 24-hour rule", F_24), ("Report suspected sanctions evasion", F_SANC)],
    related=["fintrac-examination-preparation.html", "fintrac-reporting-requirements.html", "outsourced-vs-in-house-compliance-officer.html"],
)

# ------------------------------------------------------------------ 8. examination preparation
GUIDES["fintrac-examination-preparation.html"] = dict(
    title="Preparing for a FINTRAC Examination: What to Expect | AML Canada",
    desc="How FINTRAC examinations work, from the notification letter to the findings letter, what FINTRAC asks for, and how to prepare your program, records and team.",
    crumb="FINTRAC examination",
    h1="Preparing for a FINTRAC examination",
    lede="A FINTRAC examination usually starts with a call to your compliance officer and a letter asking for documents. Examinations can be done remotely or on site, and findings can lead to follow-up or a penalty.",
    label="Guide · Examination",
    service="effectiveness-reviews.html",
    takeaways=["The examination starts on the date FINTRAC notifies you.",
               "The notification letter requests your program documents and records.",
               "Reports filed after the notification date are treated as not reported.",
               "Penalties for violations after March 26, 2026 can be much higher."],
    sections=[
        ("how-it-works", "How a FINTRAC examination works", f"""          <p><a href="{F_CAM}" rel="noopener">FINTRAC's assessment manual</a> describes three phases: planning and scoping, examination and assessment, and drawing conclusions and closing out. Examinations can be done remotely (a desk examination) or at your place of business (an on-site examination).</p>
          <p>It usually starts with a call to your compliance officer, confirmed in a notification letter. The letter is FINTRAC's formal request for information: your compliance program documents and, where relevant, lists of transactions and records. FINTRAC treats the date it notifies you as the start of the examination.</p>"""),
        ("timing", "Why the notification date matters", f"""          <p>A reportable transaction that hasn't been reported by the start of the examination is treated as not reported, and can lead to a finding of failure to submit a report, according to <a href="{F_EXAM}" rel="noopener">FINTRAC's examination guidance</a>. Filing it after you've been notified doesn't change that. FINTRAC also says it won't generally accept certain documents or records once an examination has started.</p>
          <p>Fix late or missing reports before FINTRAC calls. A regular <a href="fintrac-effectiveness-review-checklist.html">effectiveness review</a> helps you find them.</p>"""),
        ("first-steps", "What to do first", """          <ol>
            <li>Read the letter carefully and note every deadline. Missing one is itself a risk.</li>
            <li>Gather your compliance program: policies and procedures, risk assessment, training program and records, and your last effectiveness review and its report to a senior officer.</li>
            <li>Pull the records requested, completely and in the format asked for.</li>
            <li>Brief the people involved, especially your compliance officer and anyone FINTRAC may interview.</li>
            <li>Be accurate. Don't create documents after the fact to fill gaps; explain what exists and what you're fixing.</li>
          </ol>"""),
        ("after", "After the examination", f"""          <p>FINTRAC may send a findings letter to your compliance officer, covering the findings discussed at the exit meeting and listing deficient records. The outcome can be no further action, follow-up, a recommended enforcement action, or a notice of violation with a penalty. If an action plan is requested, it's typically due within 30 calendar days.</p>
          <p>Administrative monetary penalties aren't automatic. FINTRAC considers the nature and extent of the problem, its root cause, mitigating and aggravating factors, and your compliance history. If you receive a notice of violation, you can make written representations within 30 days. When a penalty is imposed, FINTRAC must make public the name of the person or entity, the nature of the violation and the amount (<a href="{L_PCMLTFA}" rel="noopener">PCMLTFA section 73.22</a>). Past notices are on FINTRAC's <a href="{F_AMP_LIST}" rel="noopener">public list of penalties</a>.</p>"""),
        ("bill-c-12", "Changes under Bill C-12", f"""          <p>Bill C-12, the Strengthening Canada's Immigration System and Borders Act, received Royal Assent on March 26, 2026. For violations that happen after that date, the maximum penalty is $4 million per violation for a person and $20 million for an entity. A business that receives a penalty must also enter into a compliance agreement with FINTRAC. If it refuses or doesn't comply, FINTRAC's Director must make a compliance order, which is made public.</p>
          <p>The amendments also require compliance programs to be reasonably designed, risk-based and effective. Violations that happened entirely before March 26, 2026 stay under the earlier penalty policy. FINTRAC explains the transition on its <a href="{F_AMP_NEW}" rel="noopener">penalty changes page</a>.</p>"""),
        ("prepare", "Preparing before FINTRAC calls", """          <ul>
            <li>Keep your program current and approved by a senior officer.</li>
            <li>Make sure every reportable transaction has been reported, and late reports are dealt with.</li>
            <li>Keep training records and your last effectiveness review ready to send.</li>
            <li>Close the findings from your last review or examination.</li>
          </ul>
          <p>An <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> can help keep these up to date, and an <a href="effectiveness-reviews.html">effectiveness review</a> tests them before FINTRAC does.</p>"""),
    ],
    faqs=[("How much notice does FINTRAC give before an examination?", "FINTRAC's assessment manual says the notification letter usually arrives 30 to 45 days before the examination date, sometimes longer for larger businesses."),
          ("Can FINTRAC examinations be done remotely?", "Yes. Examinations can be desk examinations done remotely, or on-site at your place of business."),
          ("Does every deficiency lead to a penalty?", "No. FINTRAC says penalties aren't an automatic response. It considers the nature, extent and root cause of the problem and your compliance history."),
          ("What are the maximum FINTRAC penalties now?", "For violations after March 26, 2026, up to $4 million per violation for a person and $20 million for an entity, under amendments made by Bill C-12.")],
    sources=[("FINTRAC assessment manual", F_CAM), ("FINTRAC examinations: what to expect", F_EXAM), ("Administrative monetary penalties policy", F_AMP),
             ("Administrative monetary penalties: changes", F_AMP_NEW), ("Public notices of penalties", F_AMP_LIST), ("FINTRAC, Changes to legislation and regulations", F_CHG),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA)],
    related=["fintrac-effectiveness-review-checklist.html", "fintrac-reporting-requirements.html", "outsourced-vs-in-house-compliance-officer.html"],
)

# ------------------------------------------------------------------ 9. buying an MSB
GUIDES["buying-an-msb-canada.html"] = dict(
    modified="2026-10-25",
    checked="25 October 2026",
    title="Buying an MSB in Canada: What to Check | AML Canada",
    desc="Due diligence for buying a FINTRAC-registered MSB in Canada: registry checks, eligibility, deal structure, FINTRAC updates within 30 days and red flags.",
    crumb="Buying an MSB",
    h1="Buying an MSB in Canada: what to check",
    lede="Buying a company that's already registered with FINTRAC as a money services business needs the same care as any acquisition, plus checks specific to FINTRAC and, for payment businesses, the Bank of Canada.",
    label="Guide · Acquisition",
    also=["buy-or-register-msb-canada.html"],
    service="msb-for-sale.html",
    takeaways=["Check the registration on FINTRAC's public registry before you agree a price.",
               "New owners and managers must not be ineligible under the PCMLTFA.",
               "Tell FINTRAC about changes, like new owners and directors, within 30 days.",
               "A PSP registered under the RPAA must re-register before control changes."],
    sections=[
        ("why", "Why some businesses buy", """          <p>Some businesses acquire a Canadian company that's already registered with FINTRAC as a money services business, instead of <a href="how-to-register-msb-canada.html">registering a new one</a>. They start from an established entity with a registration history. It costs more up front, and the due diligence matters as much as the price.</p>
          <p>AML Canada sells registered MSBs. Our current companies are listed on <a href="msb-for-sale.html">MSB for sale</a>. The checks below apply whichever seller you buy from.</p>"""),
        ("registry", "Check the public registry", f"""          <p>Start with <a href="{F_MSB_REGISTRY}" rel="noopener">FINTRAC's MSB registry</a>. Search by name or registration number and confirm the status is Registered. The other statuses are Revoked, Expired and Ceased. The listing also shows the services the business is registered for, its addresses, and its registration and expiry dates.</p>
          <p>Compare the listed services with what you plan to offer. Adding services later means updating the registration. Note the expiry date too: registration lasts two years and must be renewed before it expires. A Registered listing means the business met the legal requirements to register. FINTRAC says it isn't an endorsement.</p>"""),
        ("eligibility", "Check that the new owners are eligible", f"""          <p>Section 11.11 of the <a href="{L_PCMLTFA}" rel="noopener">PCMLTFA</a> makes some persons and entities ineligible to register. They include:</p>
          <ul>
            <li>persons and entities subject to sanctions under the United Nations Act, the Special Economic Measures Act or the Justice for Victims of Corrupt Foreign Officials Act, or listed under the Criminal Code;</li>
            <li>persons and entities convicted of money laundering, terrorist financing or PCMLTFA offences, or of certain other Criminal Code, drug, customs and tax offences;</li>
            <li>corporations whose director, CEO, president or 20%+ owner has been convicted on indictment of an offence under the PCMLTFA or its predecessor Act;</li>
            <li>since Bill C-12, persons and entities that still haven't paid a FINTRAC penalty, with interest, 30 days after all proceedings on the violation have ended.</li>
          </ul>
          <p>If a registered business becomes ineligible, its registration is revoked from that day. If a change of ownership makes the business ineligible, for example under the corporation rule above, the registration you're paying for ends. FINTRAC also needs criminal record checks for the CEO, the president, each director and anyone owning or controlling 20% or more, so plan for these for the incoming people, especially if they live outside Canada.</p>"""),
        ("structure", "Shares or assets", """          <p>As general information, FINTRAC registration belongs to the registered person or entity. In a share purchase, the company keeps its registration and reports the changes to FINTRAC. If you buy the business's assets into a new or different company, that company needs its own registration before it provides money services.</p>
          <p>A share purchase also brings the company's history with it: past transactions, records, any examination findings and any unpaid penalties. Ask your lawyer about warranties and indemnities that cover this.</p>"""),
        ("due-diligence", "What else to check before you buy", """          <ul>
            <li>Past FINTRAC examinations, findings letters and action plans, and any published penalties.</li>
            <li>The compliance program, the last two effectiveness reviews and their reports to a senior officer.</li>
            <li>Whether reports were filed on time, and whether records exist for the past five years.</li>
            <li>Corporate records: ownership history, directors, and that the company is in good standing.</li>
            <li>Bank accounts and payment partners, and whether they will continue after the change of control.</li>
          </ul>"""),
        ("red-flags", "Red flags", """          <ul>
            <li>A registry status other than Registered, or an expiry date that has already passed.</li>
            <li>A seller who won't share FINTRAC correspondence or examination results.</li>
            <li>Registered services or transaction estimates that don't match what the business has done.</li>
            <li>No compliance program, or one that was never put into practice.</li>
            <li>Owners or directors who may fall within the ineligibility rules.</li>
          </ul>"""),
        ("rpaa-quebec", "Bank of Canada and Quebec", f"""          <p>If the company is also registered with the Bank of Canada as a payment service provider, a planned acquisition of control triggers RPAA section 24. The PSP must submit a new application and be registered again before the acquisition closes. The new application gives the Minister of Finance the chance to carry out a national security review. The <a href="{B_ACQ}" rel="noopener">Bank's guidance on acquisitions</a> asks PSPs to allow time for both reviews before closing.</p>
          <p>In Quebec, money-services businesses also need a licence from <a href="{RQ_MSB}" rel="noopener">Revenu Québec</a>. Revenu Québec decides on a licence only after it receives security clearance reports from the Sûreté du Québec on the business and its associated persons, including directors, officers and anyone who directly or indirectly owns or controls it. New reports are required when a change is likely to affect the licence.</p>"""),
        ("after-purchase", "After the purchase", """          <p>A registered MSB must tell FINTRAC within 30 days when its registration information changes. A change of ownership usually means several changes at once: owners, directors, senior management, and often the compliance officer and address.</p>
          <p>The business still needs a compliance program that reflects its new owners, services and risks, a compliance officer with the authority to do the job, reporting to FINTRAC, record keeping, and renewal every two years. Our <a href="compliance-programs.html">compliance program documents</a> can be rewritten for the new owners. FINTRAC registration also doesn't guarantee banking or payment partners, which make their own decisions.</p>"""),
    ],
    faqs=[("Where can I buy a FINTRAC-registered MSB in Canada?", "AML Canada lists registered Canadian MSBs for sale on its <a href=\"msb-for-sale.html\">MSB for sale</a> page, with each company's FINTRAC dates, registered services and status. We also review the company with you and handle the FINTRAC change filings after closing."),
          ("Which companies sell ready-made Canadian MSBs?", "Consultancies, law firms and brokers sell them. Choose one that gives you the company's FINTRAC registration number before you pay a deposit, so you can check its status and services on FINTRAC's registry yourself."),
          ("How do I buy an existing MSB in Canada?", "You buy the shares of a company already registered with FINTRAC. Then you report the new owners, directors and compliance officer to FINTRAC within 30 days, and update the compliance program for your business."),
          ("Can a FINTRAC MSB registration be transferred to a new owner?", "Not on its own. The registration belongs to the company, so it continues when the company's shares are sold. The changes must then be reported to FINTRAC within 30 days."),
          ("Can you buy a FINTRAC-registered MSB?", "Yes. You can acquire a company that's already registered. Changes to its registration information, such as new owners and directors, must be reported to FINTRAC within 30 days."),
          ("Does the registration transfer if I buy the assets?", "As general information, registration belongs to the registered entity. In a share purchase the company keeps it. A new or different company that buys the assets needs its own registration."),
          ("How much does a ready-made Canadian MSB cost?", "AML Canada's registered MSBs start from €28,000. The price depends on the registered services, the company's history and whether it's also registered with the Bank of Canada. Registering a new MSB instead is our fixed fee of US$3,500."),
          ("Should I buy an existing MSB or register a new one?", "Buy if you need a registered company sooner; register if you want a company with only your history. Both routes carry the same obligations afterwards. Our <a href=\"buy-or-register-msb-canada.html\">buy or register</a> page compares them."),
          ("What due diligence should I do before buying a Canadian MSB?", "Check on FINTRAC's registry that the registration is active, covers your services and when it expires. Then review the corporate records, past compliance issues and FINTRAC correspondence, the new owners' eligibility, and whether the company is registered with the Bank of Canada."),
          ("What happens to an RPAA registration when I buy a Canadian MSB or PSP?", "Buying control of an RPAA-registered company is an acquisition of control, so the company must apply again and be re-registered by the Bank of Canada before the purchase closes."),
          ("Do new owners need criminal record checks?", "Yes. FINTRAC requires criminal record checks for the CEO, the president, each director and anyone owning or controlling 20% or more, so plan for them as part of the purchase.")],
    sources=[("FINTRAC, MSB registry", F_MSB_REGISTRY), ("Register your MSB or FMSB", F_REG), ("Update, renew or cancel your registration", F_UPD), ("Money services businesses", F_MSB),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA), ("Bank of Canada, Acquisitions of control", B_ACQ),
             ("Revenu Québec, Money-services business licence", RQ_MSB)],
    related=["how-to-register-msb-canada.html", "msb-registration-cost-canada.html", "foreign-msb-registration-canada.html"],
)

# ------------------------------------------------------------------ 10. outsourced vs in-house
GUIDES["outsourced-vs-in-house-compliance-officer.html"] = dict(
    title="Outsourced vs In-House Compliance Officer (Canada) | AML Canada",
    desc="Should your MSB or fintech appoint an in-house AML compliance officer or outsource the role? What FINTRAC expects of the role, and how to choose.",
    crumb="Outsourced vs in-house",
    also=["training.html"],
    h1="Outsourced or in-house compliance officer?",
    lede="Every business FINTRAC regulates needs a compliance officer. You can appoint the owner or a manager, hire someone, or outsource the role, and FINTRAC's expectations are the same in each case.",
    label="Guide · Compliance officer",
    service="outsourced-compliance-officer.html",
    takeaways=["Every reporting entity must appoint a compliance officer.",
               "The officer needs authority and access to resources and decision-makers.",
               "Small businesses can appoint the owner or operator.",
               "Your business stays responsible, however the role is filled."],
    sections=[
        ("requirement", "What FINTRAC expects of a compliance officer", f"""          <p>Appointing a compliance officer is the first required element of a compliance program. The person must have the necessary authority and access to resources to implement an effective program, and FINTRAC's best practice is that they can communicate directly with the people who make decisions about the business.</p>
          <p>Who it should be depends on size. In a small business, it can be the owner or operator. For a larger business, <a href="{F_G4}" rel="noopener">FINTRAC's guidance</a> suggests someone from a senior level with direct access to senior management, and says that as a best practice the officer shouldn't be directly involved in receiving, transferring or paying funds.</p>"""),
        ("options", "Your three options", """          <h3>1. Appoint the owner or an existing manager</h3>
          <p>Common in small businesses. It works when that person has the time and the knowledge. The risk is that compliance competes with everything else they do.</p>
          <h3>2. Hire an in-house compliance officer</h3>
          <p>Suits larger or fast-growing businesses with steady volumes. You get full-time attention and someone who knows the business from the inside. The costs are a senior salary and the challenge of finding someone experienced with Canadian requirements.</p>
          <h3>3. Use an outsourced compliance officer</h3>
          <p>An experienced compliance professional carries the day-to-day work, or supports the person you appoint, for the hours you need. They aren't in the business every day, so they rely on the information and access you give them. However it's arranged, your business remains responsible for its obligations, and the arrangement should be set out in writing so it's clear who decides and signs off on what.</p>"""),
        ("compare", "Side by side", """          <div class="table-wrap"><table>
            <thead><tr><th scope="col"></th><th scope="col">In-house hire</th><th scope="col">Outsourced</th></tr></thead>
            <tbody>
              <tr><th scope="row">Cost</th><td>A full-time salary and benefits, whatever the workload</td><td>The hours you use; with us, US$1,500 per 10 hours</td></tr>
              <tr><th scope="row">Presence</th><td>In the business every day</td><td>Works to an agreed scope and schedule</td></tr>
              <tr><th scope="row">Knowledge of your business</th><td>Builds over time from the inside</td><td>Depends on what you share and how often</td></tr>
              <tr><th scope="row">Canadian AML experience</th><td>Depends on who you can hire</td><td>Usually works across several FINTRAC-regulated clients</td></tr>
              <tr><th scope="row">Scaling</th><td>Hire more people</td><td>Add hours as volumes grow</td></tr>
              <tr><th scope="row">Often suits</th><td>Larger businesses with steady volumes</td><td>Smaller, new or foreign businesses, or support for an internal officer</td></tr>
            </tbody>
          </table></div>"""),
        ("what-they-do", "What the work involves", """          <p>Whichever option you choose, the work is the same: second-line review of customer onboarding, advice on cases and products, <a href="fintrac-reporting-requirements.html">reporting to FINTRAC</a> on time, keeping policies and the risk assessment current, client risk ratings, <a href="training.html">training</a>, and preparing for the <a href="fintrac-effectiveness-review-checklist.html">effectiveness review</a> and any <a href="fintrac-examination-preparation.html">examination</a>.</p>"""),
        ("choose", "How to choose", """          <ul>
            <li>If no one in the business has AML experience, an outsourced officer can bring it in while you build your own knowledge.</li>
            <li>If you're based outside Canada, consider whether anyone on your team knows Canadian requirements well enough to run the program.</li>
            <li>If volumes are high and steady, an in-house hire, supported by outside reviews, may make sense.</li>
            <li>Some businesses start outsourced and move in-house as they grow.</li>
          </ul>
          <p>Our <a href="outsourced-compliance-officer.html">outsourced compliance officer service</a> sets out how the arrangement works with us.</p>"""),
    ],
    faqs=[("Does every MSB need a compliance officer?", "Yes. Appointing a compliance officer is a required part of every reporting entity's compliance program."),
          ("Can a small business owner be the compliance officer?", "Yes. FINTRAC's guidance says that in a small business the owner or operator can be the compliance officer."),
          ("How much does an outsourced compliance officer cost?", "With us, US$1,500 per block of 10 hours, scaled to your workload.")],
    sources=[("FINTRAC, Compliance program requirements", F_G4)],
    related=["fintrac-reporting-requirements.html", "fintrac-effectiveness-review-checklist.html", "fintrac-examination-preparation.html"],
)

# ------------------------------------------------------------------ 11. first 90 days after registration
GUIDES["first-90-days-aml-compliance-canada.html"] = dict(
    title="First 90 Days of AML Compliance After MSB Registration | AML Canada",
    desc="What a newly registered MSB in Canada should do in its first 90 days: compliance program checks, FINTRAC reporting access, training, agents and deadlines.",
    crumb="First 90 days",
    h1="The first 90 days of AML compliance after FINTRAC registration",
    lede="Once a money services business in Canada is registered with FINTRAC, its obligations apply from the day it starts operating. This guide sets out a practical order for the first three months and the legal deadlines to put in your diary.",
    label="Guide · After registration",
    service="outsourced-compliance-officer.html",
    also=["compliance-programs.html", "training.html"],
    date="2026-10-16",
    takeaways=["Your compliance program must be in place from the day you operate.",
               "Request access to FINTRAC's reporting system before your first report is due.",
               "Train the people who deal with clients, and check agents before you engage them.",
               "Report changes to your registration to FINTRAC within 30 days."],
    sections=[
        ("day-one", "Day one: what applies straight away", f"""          <p>Registration lets a money services business (MSB) operate, and its obligations under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act apply from the same day. <a href="{F_MSB}" rel="noopener">FINTRAC lists them</a>: a compliance program, verifying the identity of clients for certain activities and transactions, keeping records, reporting to FINTRAC, ministerial directives, and the travel rule for electronic funds and virtual currency transfers.</p>
          <p>Nothing in the law happens at 90 days. It's a planning window that gives you time to get the basics working and then test them. The legal deadlines that do apply are listed at the end of this guide. If you haven't registered yet, start with our guide on <a href="how-to-register-msb-canada.html">how to register an MSB</a>.</p>"""),
        ("week-one", "Week 1: confirm the compliance program matches the business", f"""          <p>Your compliance program has five parts, set out in <a href="{F_G4}" rel="noopener">FINTRAC's compliance program guidance</a> and explained in our <a href="fintrac-compliance-program-requirements.html">guide to the requirements</a>:</p>
          <ul>
            <li>a compliance officer responsible for implementing the program;</li>
            <li>written policies and procedures, kept up to date and, if your business is an entity such as a corporation, approved by a senior officer;</li>
            <li>a documented risk assessment;</li>
            <li>a written, ongoing compliance training program and plan;</li>
            <li>a plan for an effectiveness review at least every two years.</li>
          </ul>
          <p>Registration can take months, and products, payment partners or countries can change in that time. In the first week, check that each part describes the business you're running now. If the risk assessment covers services you don't offer, or misses ones you do, update it. FINTRAC requires you to assess the risks of new developments or technologies before you introduce them, so the same check applies to anything you add later.</p>
          <p>Check too that your compliance officer has the authority and the access to senior management to do the job. Our <a href="compliance-programs.html">compliance program documents</a> are written to be in place before you operate.</p>"""),
        ("reporting", "Weeks 1 and 2: get set up to report", f"""          <p>Some FINTRAC reports have short deadlines. Suspicious transaction reports are due as soon as practicable. Electronic funds transfer reports and large virtual currency transaction reports are due within 5 working days, and large cash transaction reports within 15 calendar days. Our <a href="fintrac-reporting-requirements.html">FINTRAC reporting guide</a> explains which reports apply to which services and how the 24-hour rule adds transactions together.</p>
          <p>To file through the <a href="{F_F2R}" rel="noopener">FINTRAC Web Reporting System</a>, you first ask FINTRAC for access by email at F2R@fintrac-canafe.gc.ca. Your reporting entity administrator then creates contacts and attests to their identity before they can complete or submit reports. Request access early, so it isn't the thing that holds up your first report. FINTRAC points businesses with high reporting volumes to its <a href="{F_API}" rel="noopener">API report submission</a> option instead.</p>
          <p>Then test that your systems flag each report you need: a transfer or cash amount at the threshold, linked transactions under the 24-hour rule, and the way staff escalate unusual activity to the compliance officer. An <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> can prepare and file these reports with you.</p>"""),
        ("first-month", "First month: train your people and check your agents", f"""          <p>If you have employees, agents, mandataries or other people authorized to act for you, FINTRAC requires a written, ongoing compliance training program and a documented plan for delivering it. Start with the people who have contact with clients, such as front-line staff and agents, and those who handle funds or virtual currency. Keep a record of who was trained, when and on what. Our <a href="training.html">AML training</a> is built to meet FINTRAC's training requirement.</p>
          <p>If you use agents or mandataries, <a href="{F_MSB}" rel="noopener">FINTRAC</a> requires you to verify that they're eligible before you engage them, and again within 30 days after the second anniversary of the most recent verification. You must not engage an agent who isn't eligible, and you must stop engaging one who becomes ineligible.</p>"""),
        ("months-two-three", "Months 2 and 3: test what you built", f"""          <p>Once clients and transactions are coming in, check that the program works in practice. An internal check at this stage lets you fix problems before they repeat in more files.</p>
          <ul>
            <li>Sample client files. Was identity verified the way your procedures say, and does each client have a recorded risk rating?</li>
            <li>Compare the transactions that met a reporting threshold with the reports you filed, and check the filing dates against the deadlines.</li>
            <li>Pull a sample of records as if FINTRAC had asked for them. FINTRAC's <a href="{F_REC_MSB}" rel="noopener">record keeping guidance</a> says records must be kept for at least five years and in a way that lets you provide them within 30 days of a request.</li>
            <li>Check that your procedures apply the <a href="{F_DIR}" rel="noopener">ministerial directives</a> in force, which require countermeasures for transactions with the jurisdictions they name. They currently cover Russia, Iran and North Korea (DPRK).</li>
            <li>Update your risk assessment before you launch a new product, delivery channel or market.</li>
          </ul>
          <p>Write down what you found and what you changed. That record shows how the program has been kept up to date, and it feeds into your first <a href="fintrac-effectiveness-review-checklist.html">two-year effectiveness review</a>.</p>"""),
        ("deadlines", "Deadlines to put in your diary", f"""          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Obligation</th><th scope="col">Deadline</th></tr></thead>
            <tbody>
              <tr><th scope="row">Changes to your registration information</th><td>Tell FINTRAC within 30 days</td></tr>
              <tr><th scope="row">Registration renewal</th><td>Before it expires (registration is valid for two years)</td></tr>
              <tr><th scope="row">Effectiveness review</th><td>At least every two years; for an entity, report the results in writing to a senior officer within 30 days of finishing</td></tr>
              <tr><th scope="row">Agent eligibility check</th><td>Again within 30 days after the second anniversary of the last check</td></tr>
              <tr><th scope="row">Records requested by FINTRAC</th><td>Provide them within 30 days of the request</td></tr>
              <tr><th scope="row">Stopping MSB services</th><td>Cancel your registration within 30 days</td></tr>
            </tbody>
          </table></div>
          <p>FINTRAC's <a href="{F_UPD}" rel="noopener">update and renewal page</a> says most complete applications are processed within three months of receipt, so start your renewal well before the expiry date.</p>"""),
    ],
    faqs=[("Is there a FINTRAC deadline 90 days after registration?", "No. Ninety days is a planning window. The deadlines that apply include 30 days to report changes to your registration, the deadline for each FINTRAC report, and renewing your registration before it expires after two years."),
          ("When do my FINTRAC obligations start?", "When you start operating as a money services business. Your compliance program, client identification, record keeping and reporting obligations all apply from that day."),
          ("How do I get access to file reports with FINTRAC?", "Email FINTRAC at F2R@fintrac-canafe.gc.ca to request access to the FINTRAC Web Reporting System. Your reporting entity administrator then sets up the people who will prepare and submit reports."),
          ("Who needs AML training in a new MSB?", "If you have employees, agents, mandataries or others authorized to act for you, you need a written, ongoing compliance training program and a documented plan. Start with the people who deal with clients or handle funds or virtual currency."),
          ("How long does an MSB keep records?", "At least five years. When the period starts depends on the type of record, and records must be kept so they can be provided to FINTRAC within 30 days of a request.")],
    sources=[("FINTRAC, Compliance program requirements", F_G4), ("Money services businesses", F_MSB), ("Update, renew or cancel your registration", F_UPD),
             ("FINTRAC Web Reporting System", F_F2R), ("FINTRAC API report submission", F_API), ("Ministerial directives", F_DIR),
             ("Record keeping for MSBs", F_REC_MSB), ("Reporting suspicious transactions", F_STR), ("Reporting electronic funds transfers", F_EFT),
             ("Reporting large virtual currency transactions", F_LVCTR), ("Reporting large cash transactions", F_LCTR)],
    related=["how-to-register-msb-canada.html", "fintrac-reporting-requirements.html", "fintrac-effectiveness-review-checklist.html"],
)


# ------------------------------------------------------------------ 12. compliance program requirements
GUIDES["fintrac-compliance-program-requirements.html"] = dict(
    checked="16 October 2026",
    title="FINTRAC Compliance Program Requirements Explained | AML Canada",
    desc="What a FINTRAC compliance program must include under the PCMLTFA: compliance officer, policies, risk assessment, training and the two-year review.",
    crumb="Compliance program requirements",
    h1="FINTRAC compliance program requirements",
    lede="Every business FINTRAC regulates must establish and implement a compliance program. It has five parts: a compliance officer, written policies and procedures, a risk assessment, an ongoing training program and plan, and a review of the program at least every two years.",
    label="Guide · Compliance programs",
    service="compliance-programs.html",
    also=["training.html", "effectiveness-reviews.html"],
    date="2026-10-16",
    takeaways=["All reporting entities need a compliance program, including MSBs and virtual currency dealers.",
               "Policies and procedures must be written, kept up to date and, for an entity, approved by a senior officer.",
               "Assess the risks of a new development or new technology before you introduce it.",
               "Test the program at least every two years. If your business is an entity, report the results in writing to a senior officer within 30 days."],
    sections=[
        ("what", "What a FINTRAC compliance program is", f"""          <p>A compliance program, sometimes called an AML/ATF program, is the set of people, documents and processes a reporting entity uses to meet its obligations under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA). <a href="{F_G4}" rel="noopener">FINTRAC's compliance program guidance</a> says it forms the basis for meeting all of your reporting, record keeping, client identification and other know-your-client requirements. Every reporting entity must have one, whatever its size.</p>
          <p>FINTRAC's guidance cites subsection 9.6(1) of the PCMLTFA and section 156 of the <a href="{L_PCMLTFR}" rel="noopener">Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations</a> as the legal basis.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Part</th><th scope="col">What the rules require</th></tr></thead>
            <tbody>
              <tr><th scope="row">Compliance officer</th><td>Appoint a person responsible for implementing the program</td></tr>
              <tr><th scope="row">Policies and procedures</th><td>Written, kept up to date and, for an entity, approved by a senior officer</td></tr>
              <tr><th scope="row">Risk assessment</th><td>Assess and document your money laundering, terrorist financing and sanctions evasion risks</td></tr>
              <tr><th scope="row">Training program and plan</th><td>If others act for you, a written, ongoing training program and a documented plan to deliver it</td></tr>
              <tr><th scope="row">Two-year effectiveness review</th><td>A documented plan, and a review that tests the program at least every two years</td></tr>
            </tbody>
          </table></div>"""),
        ("officer", "1. Appoint a compliance officer", f"""          <p>In a small business, the compliance officer can be the owner, the operator or a senior manager. For a larger business, FINTRAC's example is someone at a senior level with direct access to senior management and the board of directors. As a best practice, the compliance officer of a larger business shouldn't be directly involved in receiving, transferring or paying out funds.</p>
          <p>FINTRAC says the officer needs the authority and resources to implement the program, knowledge of how your business works, knowledge of the money laundering, terrorist financing and sanctions evasion risks in your sector, and an understanding of your sector's requirements under the PCMLTFA. They can delegate tasks, but they stay responsible for implementing the program, and your business stays responsible for meeting the requirements.</p>
          <p>FINTRAC's guidance says the compliance officer can be you or another individual. If you're weighing an <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> against an internal appointment, our guide to <a href="outsourced-vs-in-house-compliance-officer.html">outsourced vs in-house compliance officers</a> compares the two options.</p>"""),
        ("policies", "2. Write policies and procedures", f"""          <p>Your policies and procedures must be written, kept up to date when the law or your own processes change, and approved by a senior officer if your business is an entity such as a corporation. Make them available to everyone authorized to act for you, including employees, agents and anyone else who deals with clients or transactions.</p>
          <p>FINTRAC expects them to cover, as they apply to you:</p>
          <ul>
            <li>the compliance program itself;</li>
            <li>know your client, including identity verification, politically exposed persons, heads of international organizations and their family members and close associates, beneficial ownership and third party determination;</li>
            <li>business relationships and ongoing monitoring;</li>
            <li>record keeping;</li>
            <li>transaction reporting;</li>
            <li>the travel rule for electronic funds and virtual currency transfers;</li>
            <li>ministerial directives.</li>
          </ul>
          <p>For each obligation, describe when it's triggered, what must be reported or recorded, the steps you take and the deadlines. Where the law asks for "reasonable measures", write down the steps you'll take. If an industry association gave you a generic set of policies, FINTRAC says you must tailor them to your business.</p>"""),
        ("risk", "3. Assess your risks", f"""          <p>You must assess and document your money laundering, terrorist financing and sanctions evasion risks in the course of your activities. FINTRAC lists the factors to consider:</p>
          <ul>
            <li>your clients, business relationships and any correspondent banking relationships, including their activity patterns and locations;</li>
            <li>your products, services and delivery channels;</li>
            <li>the places where you carry out your activities;</li>
            <li>new developments or technologies, assessed before you introduce them;</li>
            <li>if you are a financial entity, life insurance company or securities dealer, the risks from the activities of your affiliates;</li>
            <li>the risks for your sector in the latest National Risk Assessment of Money Laundering and Terrorist Financing in Canada;</li>
            <li>any other relevant factor, such as employee turnover.</li>
          </ul>
          <p>An MSB that plans to add virtual currency services, for example, must assess the risks of that new service before it launches.</p>
          <h3>Enhanced measures for high risk</h3>
          <p>Where you consider a risk high, you must take enhanced measures and set them out in written policies and procedures. They include extra steps to verify identity, updating client information and monitoring business relationships at a frequency that matches the risk. FINTRAC's examples include getting more information on the client, on their source of funds or source of wealth, or on the reasons for a transaction. FINTRAC's <a href="{F_RBA}" rel="noopener">risk assessment guidance</a> explains how to build the assessment.</p>"""),
        ("training", "4. Train the people who act for you", f"""          <p>If you have employees, agents, mandataries or others authorized to act for you, you need a written, ongoing compliance training program and a documented plan for delivering it. The training should cover your obligations under the PCMLTFA, background on money laundering and terrorist financing, how your business could be used for them, your own policies and procedures, and each person's role when something looks suspicious.</p>
          <p>The plan should say who gets trained, which topics and materials you use, how you deliver the training and how often. FINTRAC says recipients should include anyone who deals with clients, is involved in client transactions or handles cash, funds or virtual currency for you, and those who implement or oversee the program, such as the compliance officer, senior management, IT staff and internal auditors. Keep a record of each session, with the date, the attendees and the topics. A sole proprietor with no employees, agents or other authorized persons doesn't need a training program or plan. Our <a href="training.html">AML training</a> is built around these requirements.</p>"""),
        ("review", "5. Review the program every two years", f"""          <p>An effectiveness review tests whether your policies and procedures, risk assessment, and training program and plan work in practice. You must start each review no later than 24 months from the start of the previous one, and finish the previous review before you start the next. The review must be carried out, and its results documented, by an internal or external auditor, or by you if you have no auditor. Whoever does it should know your requirements under the PCMLTFA. As a best practice, the reviewer shouldn't be directly involved in your compliance program activities.</p>
          <p>You also need a documented plan for the review that covers every part of the program. It should set out the scope, the reasons for the areas you focus on, the period reviewed, your evaluation methods and sample sizes. The review itself should record when it was done, the period covered, who did it, the test results and the conclusions, including any deficiencies, recommendations and action plans. If your business is an entity, you must report the findings, any other updates to your policies and procedures and the status of those updates, in writing to a senior officer within 30 days of finishing the review. Our <a href="fintrac-effectiveness-review-checklist.html">effectiveness review checklist</a> sets out what to test, and an external <a href="effectiveness-reviews.html">effectiveness review</a> gives you an independent view.</p>"""),
        ("check", "A quick self-check", """          <p>These questions follow FINTRAC's guidance. If you answer no to any of them, that part of your program needs work.</p>
          <ul>
            <li>Has your compliance officer been appointed, and do they have the authority and resources to do the job?</li>
            <li>Are your policies and procedures written, kept up to date, approved by a senior officer if your business is an entity, and tailored to your business?</li>
            <li>Do they cover the travel rule and the ministerial directives in force?</li>
            <li>Does your risk assessment describe the products, channels and countries you deal with today?</li>
            <li>Can you show training records for everyone FINTRAC says should be trained, including senior management and the compliance officer?</li>
            <li>Do you know when your next effectiveness review must start?</li>
          </ul>
          <p>If you're about to register, our <a href="compliance-programs.html">compliance program documents</a> are written to be in place before you start operating. If you've just registered, see what to do in your <a href="first-90-days-aml-compliance-canada.html">first 90 days</a>.</p>"""),
    ],
    faqs=[("Who needs a FINTRAC compliance program?", "Every reporting entity under the PCMLTFA must establish and implement one, whatever its size. That includes money services businesses, foreign MSBs and virtual currency dealers."),
          ("Can I use a compliance program template?", "You can start from one, but FINTRAC says generic policies and procedures must be tailored to your business. The level of detail depends on your size, structure, complexity and exposure to money laundering, terrorist financing and sanctions evasion risks."),
          ("Who approves the compliance policies and procedures?", "If your business is an entity, such as a corporation, a senior officer must approve them. They must also be kept up to date when the law or your processes change."),
          ("Does a sole proprietor need a training program?", "No, if you have no employees, agents, mandataries or other people authorized to act for you. You still need the other parts of the program."),
          ("How often must the compliance program be reviewed?", "At least every two years. Each review must start no later than 24 months from the start of the previous one, and an entity must report the results in writing to a senior officer within 30 days of finishing.")],
    sources=[("FINTRAC, Compliance program requirements", F_G4), ("FINTRAC, Risk assessment guidance", F_RBA),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA), ("Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations", L_PCMLTFR), ("Ministerial directives", F_DIR),
             ("Travel rule guidance", F_TRAVEL)],
    related=["first-90-days-aml-compliance-canada.html", "fintrac-effectiveness-review-checklist.html", "outsourced-vs-in-house-compliance-officer.html"],
)

# ------------------------------------------------------------------ 13. RPAA safeguarding
GUIDES["rpaa-safeguarding-end-user-funds.html"] = dict(
    checked="16 October 2026",
    title="RPAA Safeguarding of End-User Funds Explained | AML Canada",
    desc="How payment service providers safeguard end-user funds under the RPAA: trust accounts, insurance or guarantees, the written framework and reviews.",
    crumb="RPAA safeguarding",
    h1="RPAA safeguarding of end-user funds",
    lede="Since September 8, 2025, a payment service provider that holds funds for its users must safeguard them, either in trust in a trust account or in a segregated account backed by insurance or a guarantee. It also needs a written safeguarding framework and an independent review at least every three years.",
    label="Guide · RPAA",
    service="rpaa-compliance-program.html",
    also=["rpaa-registration.html"],
    date="2026-10-16",
    takeaways=["Safeguarding applies only to end-user funds a PSP holds at rest.",
               "Place held funds in a safeguarding account on receipt. Unavoidable processing constraints allow until the next business day.",
               "Use a trust account, or a segregated account with insurance or a guarantee, or a mix of both.",
               "Keep a daily ledger, approve the framework every year and have it reviewed independently every three years."],
    sections=[
        ("who", "Who must safeguard end-user funds", f"""          <p>One of the payment functions in the Retail Payment Activities Act (RPAA) is holding funds on behalf of an end user until they're withdrawn by the end user or transferred to another person or entity. A payment service provider (PSP) that performs it must safeguard those funds. The <a href="{B_FW}" rel="noopener">Bank of Canada's supervisory framework</a> says the requirement came into force on September 8, 2025.</p>
          <p>It only covers funds that are held. The Bank's <a href="{B_SG_GLANCE}" rel="noopener">safeguarding summary</a> explains the difference:</p>
          <ul>
            <li>You hold funds when they sit at rest in an account you own, available for a later withdrawal or transfer, and you owe them to the end user.</li>
            <li>Funds are at rest while you have no instruction to transfer them immediately.</li>
            <li>You stop holding funds when you receive an instruction for immediate withdrawal or transfer, or when a future-dated transfer date arrives.</li>
            <li>Funds you receive together with an instruction to transfer them immediately aren't held.</li>
          </ul>
          <p>For example, if a user tops up a wallet with you and leaves the balance there for a later payment, you're holding those funds from the moment they reach your account. If a user sends funds with an instruction to pay a recipient straight away, those funds aren't held.</p>
          <p>The Bank's <a href="{B_SG}" rel="noopener">safeguarding guideline</a> adds some specific cases. Funds a merchant processor reserves specifically to cover chargebacks or fraud aren't held, and neither are your own funds advanced to a merchant before a card transaction settles. If you have a place of business in Canada, the requirement covers funds you hold for end users anywhere. If you don't, it covers only funds you hold for end users in Canada.</p>
          <p>There's one exception. A PSP that is itself a member of a provincial deposit insurance program doesn't need to safeguard end-user funds it holds as deposits insured under that program. It doesn't apply just because the credit union or other institution holding your account is a member. If you're not sure whether your business holds funds at all, our <a href="rpaa-registration-guide.html">guide to who the RPAA covers</a> explains registration.</p>"""),
        ("segregate", "Segregate funds in a safeguarding account", f"""          <p>The Bank gives safeguarding two objectives: end users should have reliable access to their funds without delay, and their funds should be protected against loss if the PSP becomes insolvent.</p>
          <p>You must keep end-user funds apart from all other funds, including your own, in an account that isn't used for any other purpose. The Bank calls it the safeguarding account. It must be provided by a Canadian financial institution of the kinds the RPAA lists, or by a foreign institution prudentially regulated to standards comparable to Canadian ones. The Bank also expects a written acknowledgement from the account provider that it has no interest in, recourse to or right against the funds for any sum owed to it.</p>
          <p>The Bank's <a href="{B_SG}" rel="noopener">guideline</a> expects funds to go into the safeguarding account on receipt. If processing constraints you can't avoid make that impossible, they must be in the account by the end of the next business day at the latest. In that case you must not use the funds for anything else, be able to explain the delay to the Bank, track the funds and tell end users when their funds might not be protected straight away. The Bank treats funds not safeguarded on receipt as a shortfall, so keep a record of them and report them in your annual report.</p>"""),
        ("means", "Trust account, insurance or guarantee", f"""          <p>Subsection 20(1) of the <a href="{L_RPAA}" rel="noopener">RPAA</a> sets out the ways to protect the funds. You can combine them, for example by holding part of the funds in trust and covering the rest with insurance, or by using more than one provider.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Aspect</th><th scope="col">In trust in a trust account</th><th scope="col">Segregated account with insurance or a guarantee</th></tr></thead>
            <tbody>
              <tr><th scope="row">How it protects funds</th><td>Funds are held in trust for end users</td><td>Coverage must equal or exceed the amount in the safeguarding account</td></tr>
              <tr><th scope="row">What the Bank expects</th><td>Legal advice that a valid express trust exists, and an agreement with the account provider saying the funds are held in trust</td><td>A provider prescribed by the regulations and not affiliated with you, with terms that keep the proceeds out of your estate, payable to end users as soon as feasible and in force after your insolvency</td></tr>
              <tr><th scope="row">Points to watch</th><td>Quebec arrangements follow the Civil Code; get advice before paying expenses out of the trust account</td><td>Monitor coverage so it never falls below the funds held; notify the Bank at least 30 days before a policy or guarantee is cancelled or ends</td></tr>
            </tbody>
          </table></div>"""),
        ("framework", "The written safeguarding framework", f"""          <p>A PSP that holds end-user funds must establish, implement and maintain a written framework. The Bank's <a href="{B_SG}" rel="noopener">safeguarding guideline</a> sets out what it must contain at a minimum:</p>
          <ul>
            <li>A ledger that records the funds you hold for each end user, with their name and contact details, and whether the funds are in the safeguarding account. It must be updated each day.</li>
            <li>Your approach to meeting withdrawal and transfer requests. Funds can be held in cash or in secure and liquid assets, meaning assets that can be turned into cash quickly with little or no loss of value. The Bank's list includes guaranteed investment certificates, government securities and promissory notes rated at least A-, and commercial paper and corporate bonds rated at least AA-. It excludes residential mortgage-backed securities and common shares.</li>
            <li>Procedures for returning funds to each end user if you become insolvent, written so that an insolvency professional could follow them using your records.</li>
            <li>An analysis of the legal and operational risks that could stop the framework working, and how you reduce them.</li>
            <li>A review at least once a year, after any change to how you safeguard funds, and after any change likely to have a material effect on it.</li>
          </ul>
          <p>Unless the PSP is an individual, the framework must name a senior officer responsible for overseeing safeguarding and for compliance with the requirements. The senior officer, and your board of directors if you have one, must approve the framework at least once a year. The senior officer also approves it after each material change.</p>"""),
        ("shortfalls", "Shortfalls and the three-year independent review", f"""          <p>Under the <a href="{L_RPAR}" rel="noopener">Retail Payment Activities Regulations</a>, you must take ongoing measures to find any shortfall, where the funds in trust or covered by insurance or a guarantee add up to less than the funds you hold. Fix a shortfall in a timely manner, investigate its root cause immediately and, as soon as feasible, take measures to stop it happening again. The Bank suggests checking for shortfalls daily as a best practice.</p>
          <p>At least once every three years, an independent review must check whether you comply with the safeguarding requirements. The reviewer can be inside or outside your business, but must be suitably skilled and must have had no role in setting up or running the framework or in finding shortfalls. Report the gaps it finds, and what you did about them, to your senior officer.</p>"""),
        ("indirect", "Using another PSP's account", """          <p>The Bank expects you to have a direct relationship with your safeguarding account provider. If you rely on another, unaffiliated PSP for access to an account at a financial institution, the Bank treats that as an indirect arrangement. It won't accept one as compliant unless you can show you've dealt with the trust law, Quebec Civil Code and insolvency problems it creates.</p>"""),
        ("reporting", "Where safeguarding shows up in your reporting", f"""          <p>Your annual report to the Bank includes information on your safeguarding practices if you hold end-user funds. It must also list each shortfall you found, with the amount, the root cause and the measures you took to prevent it recurring. A change expected to materially affect how you safeguard funds is a significant change, and you must notify the Bank at least five business days before you make it, according to its <a href="{B_FW}" rel="noopener">supervisory framework</a>. Our <a href="rpaa-compliance-program.html">RPAA compliance program</a> sets up the safeguarding framework with your risk management and incident response frameworks, and PSPs that still need to register can start with our <a href="rpaa-registration.html">RPAA registration</a> service.</p>"""),
    ],
    faqs=[("Does every PSP have to safeguard funds under the RPAA?", "No. Only PSPs that hold end-user funds at rest, available for later withdrawal or transfer. Funds received with an instruction to transfer them immediately aren't held."),
          ("Can a PSP use both a trust account and insurance?", "Yes. The Bank says you can safeguard part of the funds in trust and protect the rest with insurance or a guarantee, and you can use more than one provider."),
          ("How quickly must funds go into the safeguarding account?", "On receipt. If processing constraints you can't avoid make that impossible, by the end of the next business day at the latest, and you must tell end users when that can happen."),
          ("How often is the safeguarding framework reviewed?", "You review it at least once a year and after any change to how you safeguard funds, and your senior officer, and your board if you have one, approve it at least once a year. An independent review of your compliance is also needed at least once every three years."),
          ("Is RPAA safeguarding the same as FINTRAC compliance?", "No. Safeguarding is a Bank of Canada requirement under the RPAA. FINTRAC is a separate regulator, and the Bank's registration application asks for any registrations for retail payment activities you hold with FINTRAC.")],
    sources=[("Bank of Canada, Supervisory framework", B_FW), ("Bank of Canada, Guideline on safeguarding end-user funds (December 2024)", B_SG),
             ("Bank of Canada, Safeguarding of end-user funds: At a glance", B_SG_GLANCE), ("Bank of Canada, FAQ on safeguarding end-user funds", B_SG_FAQ),
             ("Retail Payment Activities Act", L_RPAA), ("Retail Payment Activities Regulations", L_RPAR)],
    related=["rpaa-registration-guide.html", "fintrac-compliance-program-requirements.html", "how-to-register-msb-canada.html"],
)


# ------------------------------------------------------------------ 14-17. MSB registration, penalties, travel rule
# Official sources checked 21 October 2026. Justice Laws texts were read directly (Act and Regulations
# "current to 2026-09-30"). FINTRAC pages were read from their most recent public captures because
# fintrac-canafe.canada.ca refused connections that day. Uses constants defined above in guides_v3.py
# (F_REG, F_MSB, F_UPD, F_TRAVEL, F_DIR, F_AMP, F_AMP_NEW, F_AMP_LIST, F_MSB_REGISTRY, L_PCMLTFA, L_PCMLTFR,
# F_CHG, F_G4, F_REC_MSB, F_STR, F_EFT, F_LVCTR).
MS_REGR = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2007-121/FullText.html"
MS_AMPR = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2007-292/FullText.html"
MS_NOELIG = "https://fintrac-canafe.canada.ca/msb-esm/register-inscrire/no-eng"
MS_REVOKED = "https://fintrac-canafe.canada.ca/msb-esm/revoked-revoquee-eng"
MS_REVIEW = "https://fintrac-canafe.canada.ca/raa-rea/1-eng"
MS_PEN = "https://fintrac-canafe.canada.ca/pen/1-eng"
MS_DIR_RUS = "https://fintrac-canafe.canada.ca/obligations/dir-rus-eng"
MS_DIR_IRI = "https://fintrac-canafe.canada.ca/obligations/dir-iri-eng"
MS_DIR_DPRK = "https://fintrac-canafe.canada.ca/obligations/dir-dprk-eng"
MS_NEWS = "https://fintrac-canafe.canada.ca/new-neuf/1-eng"

# ------------------------------------------------------------------ 14. virtual office and MSB registration
GUIDES["virtual-office-msb-registration.html"] = dict(
    checked="21 October 2026",
    title="Can You Use a Virtual Office for MSB Registration? | AML Canada",
    desc="What FINTRAC asks about your place of business and addresses, how foreign MSBs use a representative for service, and what to check before listing an address.",
    crumb="Virtual office and MSB registration",
    h1="Can you use a virtual office for FINTRAC MSB registration?",
    lede="FINTRAC's published guidance doesn't say whether a virtual office is acceptable. It does say what counts as a place of business in Canada, what the registration asks about your addresses, and that FINTRAC can check the information you give it.",
    label="Guide · MSB",
    service="canadian-address.html",
    also=["msb-registration.html"],
    date="2026-10-21",
    takeaways=["FINTRAC's guidance doesn't address virtual offices, so no address type is pre-approved or ruled out.",
               "A physical location, Canadian incorporation, or staff, agents or branches in Canada make you a domestic MSB.",
               "Your place of business address is published on FINTRAC's public MSB registry.",
               "A foreign MSB needs a representative for service who resides in Canada. An address can't fill that role."],
    sections=[
        ("short-answer", "The short answer", f"""          <p>We checked FINTRAC's pages on registering, on who is a money services business (MSB), on updating a registration and on the public registry. None of them mentions virtual offices, mail-forwarding addresses or shared workspaces. FINTRAC doesn't publish a list of acceptable address types, and it doesn't certify addresses.</p>
          <p>So the useful question is narrower: does the address you give FINTRAC describe how your business really operates? The rest of this guide sets out what the law and <a href="{F_REG}" rel="noopener">FINTRAC's registration page</a> ask for, so you can answer that before you file. If you haven't started the application yet, our guide on <a href="how-to-register-msb-canada.html">how to register an MSB</a> covers the full process.</p>"""),
        ("place-of-business", "Your address decides which kind of MSB you are", f"""          <p>The Proceeds of Crime (Money Laundering) and Terrorist Financing Act draws one line. A business with a place of business in Canada that provides money services is an MSB under paragraph 5(h). A business without one, that directs money services at people in Canada and provides them to clients here, is a foreign MSB under paragraph 5(h.1).</p>
          <p><a href="{F_MSB}" rel="noopener">FINTRAC's MSB page</a> says you have a place of business in Canada if any of these apply:</p>
          <ul>
            <li>you are incorporated in Canada;</li>
            <li>you have a physical location in Canada; or</li>
            <li>you have employees, agents or branches in Canada.</li>
          </ul>
          <p>Two things follow. A company incorporated in Canada is a domestic MSB wherever its staff work. And a foreign business that sets up a physical location here stops being a foreign MSB. FINTRAC's guidance doesn't say whether a rented address with no staff on site counts as a physical location. If you're a foreign business, settle that point before you list a Canadian address anywhere. Our <a href="foreign-msb-registration-canada.html">foreign MSB guide</a> explains the foreign route in full.</p>"""),
        ("what-form-asks", "What the registration asks about addresses", f"""          <p>Schedule 1 to the <a href="{MS_REGR}" rel="noopener">Registration Regulations</a> lists the information an application must contain. The address-related items are:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Item</th><th scope="col">Public identifying information?</th></tr></thead>
            <tbody>
              <tr><th scope="row">Address of place of business</th><td>Yes</td></tr>
              <tr><th scope="row">Mailing address of the place of business, if different</th><td>No</td></tr>
              <tr><th scope="row">Telephone number and website</th><td>Yes</td></tr>
              <tr><th scope="row">Whether any money service is provided in a dwelling-house</th><td>No</td></tr>
              <tr><th scope="row">Address and telephone number of every agent, mandatary and branch</th><td>Yes</td></tr>
              <tr><th scope="row">For a foreign MSB, contact details of the representative for service in Canada</th><td>No</td></tr>
            </tbody>
          </table></div>
          <p>The Regulations make the information in Parts A and C of Schedule 1 public. That includes the place of business address, telephone number, website and the agent and branch details. <a href="{F_MSB_REGISTRY}" rel="noopener">FINTRAC's registry</a> shows a business address and website for each listing. FINTRAC's registration page also asks for "detailed information about every location". If you're a corporation, your certificate of incorporation or equivalent record must show the corporation's name, address and directors, so that address should match what you file.</p>"""),
        ("verify", "FINTRAC can check what you tell it", f"""          <p>Subsection 54.1(4) of the <a href="{L_PCMLTFA}" rel="noopener">Act</a> lets FINTRAC verify the information in any registration application. <a href="{F_UPD}" rel="noopener">FINTRAC says</a> it sends a clarification request when information is inconsistent or can't be adequately verified, usually by email to the contact person or the representative for service. You have 30 days to answer. If you don't, FINTRAC may deny the application, or revoke the registration if you're already registered.</p>
          <p>Consistency matters more than the type of address. Your incorporation records, bank account details, website, contact details and the address you list should tell the same story. Once you're registered, a change of address must be reported to FINTRAC within 30 days. Our guide to <a href="msb-registration-refused-revoked.html">denied, revoked and expired registrations</a> covers what happens when these steps are missed.</p>"""),
        ("fmsb", "Foreign MSBs: the representative for service", f"""          <p>A foreign MSB must name a representative for service. Under paragraph 11.12(1)(c.1) of the Act, that's a person who resides in Canada and is authorized to accept notices from FINTRAC on the business's behalf. FINTRAC needs their name, address for service and contact details.</p>
          <p>The representative is an individual, so a business address can't serve as one. The representative also doesn't take on your obligations. <a href="{F_REG}" rel="noopener">FINTRAC states</a> that the foreign MSB, and not its representative, is responsible for meeting the requirements of the Act.</p>
          <p>If the representative's name or address for service changes and you don't tell FINTRAC within 30 days, FINTRAC must deny your application or revoke your registration (subsection 11.13(2)). Here the Act gives FINTRAC no discretion.</p>"""),
        ("notices", "Make sure someone reads the mail", f"""          <p>The <a href="{MS_AMPR}" rel="noopener">Administrative Monetary Penalties Regulations</a> say how FINTRAC can serve documents such as a notice of violation. For an entity, that includes leaving the document at its head office or place of business with a person who appears to be in charge, or sending it by registered mail or courier to the head office or place of business. A document sent by registered mail or courier is deemed served on the tenth day after the date on the postal or courier receipt.</p>
          <p>Deadlines in the Act run from service. A notice of violation, for example, gives you 30 days to pay or make representations. If mail sent to your listed address isn't collected and read, those days can pass before anyone in the business knows. Whatever address you use, decide in writing who checks the mail and how quickly it reaches your compliance officer.</p>"""),
        ("checklist", "Before you list an address", """          <ul>
            <li>Confirm whether you're a domestic or foreign MSB, using FINTRAC's place of business criteria.</li>
            <li>Make sure the address matches your incorporation records, bank details and website.</li>
            <li>Remember the place of business address will be public on the registry.</li>
            <li>If services are provided from a home, say so: the form asks.</li>
            <li>For a foreign MSB, appoint a representative for service who resides in Canada, and diarize the 30-day rule for changes.</li>
            <li>Set up mail handling so FINTRAC notices reach your compliance officer quickly.</li>
          </ul>
          <p>We offer a <a href="canadian-address.html">Canadian business address</a> for US$200 per month. Before you use it, we check with you how it fits your FINTRAC registration, and the scope, including mail handling, is agreed in writing. Our <a href="msb-registration.html">MSB registration service</a> covers the application itself.</p>"""),
    ],
    faqs=[("Does FINTRAC accept a virtual office for MSB registration?", "FINTRAC's published guidance doesn't address virtual offices. It asks for the address of your place of business, can verify what you provide and sends clarification requests when information is inconsistent or can't be verified. The address should reflect how your business actually operates."),
          ("Is my MSB's address made public?", "Yes. The place of business address is part of the identifying information FINTRAC publishes on its MSB registry, along with agent and branch details."),
          ("Can a Canadian business address act as a foreign MSB's representative for service?", "No. The representative for service is a person who resides in Canada and is authorized to accept FINTRAC's notices. A business address is a separate thing."),
          ("Does a Canadian address turn a foreign MSB into a domestic MSB?", "FINTRAC says a physical location in Canada is a place of business, and a business with a place of business in Canada is a domestic MSB. FINTRAC doesn't say whether an address without staff counts, so get this confirmed before you list one."),
          ("Can I register an MSB that operates from home?", "The registration asks whether any money service is provided in a dwelling-house, so it's something you disclose. Your address must still match your other records.")],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("FINTRAC, Money services businesses", F_MSB),
             ("FINTRAC, Answer clarification requests, update, renew or cancel your registration", F_UPD),
             ("FINTRAC, Money Services Business Registry", F_MSB_REGISTRY),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Registration Regulations", MS_REGR),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Administrative Monetary Penalties Regulations", MS_AMPR)],
    related=["foreign-msb-registration-canada.html", "how-to-register-msb-canada.html", "msb-registration-refused-revoked.html"],
)

# ------------------------------------------------------------------ 15. denied, revoked or expired registration
GUIDES["msb-registration-refused-revoked.html"] = dict(
    checked="21 October 2026",
    title="MSB Registration Denied, Revoked or Expired | AML Canada",
    desc="Why FINTRAC denies or revokes MSB registrations, what expiry means, how to ask for a review or appeal, the penalties for operating unregistered and reapplying.",
    crumb="Denied, revoked or expired",
    h1="MSB registration denied, revoked or expired: what happens and what to do",
    lede="FINTRAC can deny an MSB application or revoke a registration for a short list of reasons set out in the Act. A registration that isn't renewed expires. Each outcome has its own deadlines, and operating without a valid registration is an offence.",
    label="Guide · MSB",
    service="msb-registration.html",
    date="2026-10-21",
    takeaways=["Ineligibility revokes a registration automatically, from the day it arises.",
               "Unanswered 30-day clarification requests can lead to denial or revocation.",
               "You have 30 days to ask FINTRAC's Director to review a denial or revocation.",
               "Renew before expiry: a renewal submitted in time keeps you Registered while it's processed."],
    sections=[
        ("statuses", "The four statuses on FINTRAC's registry", f"""          <p><a href="{F_MSB_REGISTRY}" rel="noopener">FINTRAC's MSB registry</a> shows one of four statuses for every business:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Status</th><th scope="col">FINTRAC's meaning</th></tr></thead>
            <tbody>
              <tr><th scope="row">Registered</th><td>Currently registered with FINTRAC</td></tr>
              <tr><th scope="row">Revoked</th><td>No longer registered for not answering a clarification request, not providing assistance to FINTRAC, or being found ineligible</td></tr>
              <tr><th scope="row">Expired</th><td>Didn't renew its registration after two years</td></tr>
              <tr><th scope="row">Ceased</th><td>Told FINTRAC it no longer offers the services</td></tr>
            </tbody>
          </table></div>
          <p>FINTRAC updates the registry monthly, and a downloadable version is available. It also keeps a separate <a href="{MS_REVOKED}" rel="noopener">list of businesses with revoked registrations</a>. Search by name and registration number, and check the expiry date as well as the status.</p>"""),
        ("denied", "Why an application is denied", f"""          <p>The <a href="{L_PCMLTFA}" rel="noopener">Act</a> gives three grounds:</p>
          <ul>
            <li><strong>Ineligibility.</strong> FINTRAC must deny an applicant listed in subsection 11.11(1) (section 11.16).</li>
            <li><strong>Unanswered clarification requests.</strong> FINTRAC may deny an application if the applicant doesn't provide requested clarifications within 30 days (section 11.14).</li>
            <li><strong>A foreign MSB's representative for service.</strong> If the representative's name or address for service changes and FINTRAC isn't told within 30 days, FINTRAC must deny the application (subsection 11.13(2)).</li>
          </ul>
          <p>The ineligible group includes people and entities subject to certain sanctions, listed terrorist entities, and those convicted of money laundering, terrorist financing and a range of other offences, including human smuggling and trafficking offences under sections 117 and 118 of the Immigration and Refugee Protection Act. Since the Bill C-12 amendments of March 26, 2026, it also includes anyone who still hasn't paid a FINTRAC penalty, with interest, 30 days after all proceedings on the violation have ended. Under the <a href="{MS_REGR}" rel="noopener">Registration Regulations</a>, a corporation or other entity is also ineligible if its CEO, president, a director or a 20% owner falls into most of these groups. <a href="{MS_NOELIG}" rel="noopener">FINTRAC's eligibility page</a> lists the offences in plain language.</p>"""),
        ("revoked", "Why a registration is revoked", f"""          <ul>
            <li><strong>Ineligibility.</strong> If a registered business becomes ineligible, its registration is revoked as of the day that happens (subsection 11.11(2)). FINTRAC then sends written notice without delay. No decision by FINTRAC is needed for the revocation to take effect.</li>
            <li><strong>Clarification requests.</strong> A registered business must answer FINTRAC's clarification requests within 30 days, or FINTRAC may revoke (section 11.17).</li>
            <li><strong>Not assisting FINTRAC.</strong> FINTRAC may revoke if a business doesn't give an examiner reasonable assistance, or doesn't provide documents required by a notice served during an examination (section 11.171).</li>
            <li><strong>A foreign MSB's representative for service.</strong> The same 30-day rule as for applications applies, and revocation is mandatory.</li>
          </ul>
          <p>Every decision to deny or revoke must be in writing, with reasons (section 11.18).</p>"""),
        ("review", "Asking for a review, then appealing", f"""          <p>Within 30 days after you receive a denial or revocation, you can apply in writing to FINTRAC's Director for a review and include supporting information (section 11.3). The Director either confirms the decision or substitutes their own, and serves notice with reasons.</p>
          <p>If you disagree with the Director's decision, you can appeal to the Federal Court within 30 days after it's served, or within a longer period the Court allows. If the Director doesn't decide within 90 days after receiving your application for review, you can appeal within 30 days after that 90-day period ends (section 11.4).</p>
          <p><a href="{MS_REVIEW}" rel="noopener">FINTRAC's reviews and appeals page</a> says applications go to its Review and Appeals Unit by mail, or electronically after you email rev-app@fintrac-canafe.gc.ca for a secure link. If a lawyer applies for you, include a letter of authorization. This is general information, and a lawyer can advise on your own case.</p>"""),
        ("expired", "Expiry and renewal", f"""          <p>Registration must be renewed every two years (section 11.19). <a href="{F_UPD}" rel="noopener">FINTRAC says</a> it's your responsibility to renew on time, and that most complete applications are processed within three months.</p>
          <p>Timing matters because of how the registry treats renewals. If you submit a renewal before the expiry date, you stay Registered until FINTRAC processes it, even if the expiry date passes. If you don't submit one before the expiry date, your registration is treated as Expired.</p>
          <p>Virtual currency dealers and foreign MSBs have a specific deadline for their first renewal under section 6.1 of the Registration Regulations. For a corporation, it's the last day of the month of the first anniversary of incorporation that falls after the second anniversary of initial registration. Check the expiry date on your registry listing rather than counting from memory.</p>"""),
        ("changes", "Changes and stopping services", f"""          <p>Tell FINTRAC about any change to your registration information, or newly obtained information that should have been in the application, within 30 days of becoming aware of it (subsection 11.13(1)). If you stop offering the services you're registered for, notify FINTRAC within 30 days using its cessation form (section 11.2). FINTRAC says failing to do either may lead to penalties or criminal charges.</p>"""),
        ("unregistered", "Operating without a valid registration", f"""          <p>Section 77.4 of the Act makes it an offence for a business that must register to knowingly engage in an activity it isn't registered for. As the Act reads today, the maximum is a fine of $2,500,000, up to two years less a day in prison, or both, on summary conviction, and a fine of $5,000,000, up to five years in prison, or both, on indictment. Officers and directors who directed, authorized or took part in an offence can also be found guilty (section 78).</p>
          <p>The same failures can be handled as administrative violations instead. Under the <a href="{MS_AMPR}" rel="noopener">penalty regulations</a>, failing to register, to report changes, to answer clarification requests, to renew or to notify cessation are all serious violations. For violations on or after March 26, 2026, a serious violation can carry up to $4,000,000. FINTRAC can't pursue both a penalty and a prosecution for the same act. Our guide to <a href="fintrac-penalties-amps.html">FINTRAC penalties</a> explains the process.</p>
          <p>There are practical effects too. FINTRAC notes that financial entities must make sure the foreign MSBs they open accounts for are registered with FINTRAC.</p>"""),
        ("reapply", "Applying again", f"""          <p>The registration sections of the Act don't set a waiting period before a new application. Any ineligibility has to be resolved first, such as an unpaid penalty. The application asks whether you've applied before, so be open about the earlier outcome and what has changed.</p>
          <p>Fresh criminal record checks will be needed, issued no more than six months before you apply. Answer every clarification request well within 30 days. Our <a href="msb-registration.html">MSB registration service</a> prepares and submits applications, and our <a href="how-to-register-msb-canada.html">registration guide</a> sets out each step. Some businesses look at <a href="buying-an-msb-canada.html">buying a registered MSB</a> instead, which brings its own checks. If the address on file is part of the problem, see our guide on <a href="virtual-office-msb-registration.html">virtual offices and MSB registration</a>.</p>"""),
    ],
    faqs=[("What happens if my MSB registration expires?", "If you didn't submit a renewal before the expiry date, the registry shows the business as Expired and it isn't registered. Providing money services while unregistered can lead to a penalty or prosecution."),
          ("Can I keep operating while my renewal is processed?", "Yes, if you submitted the renewal before the expiry date. FINTRAC says the business stays Registered until the renewal is processed."),
          ("How do I challenge a FINTRAC revocation?", "Apply in writing to FINTRAC's Director for a review within 30 days of receiving the decision. If you disagree with the Director's decision, you can appeal to the Federal Court within 30 days after it's served."),
          ("Can a business with a revoked registration apply again?", "The Act doesn't set a waiting period, but the reason for revocation must be resolved first. An ineligible applicant must be refused."),
          ("How do I check if an MSB is registered?", "Search FINTRAC's Money Services Business Registry by name or registration number and check the status and expiry date. FINTRAC says registration isn't an endorsement or a licence.")],
    sources=[("FINTRAC, Answer clarification requests, update, renew or cancel your registration", F_UPD), ("FINTRAC, Money Services Business Registry", F_MSB_REGISTRY),
             ("FINTRAC, Money services businesses with revoked registration", MS_REVOKED), ("FINTRAC, Who is not eligible to register", MS_NOELIG),
             ("FINTRAC, Reviews and appeals", MS_REVIEW), ("FINTRAC, Register your MSB or FMSB", F_REG),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Registration Regulations", MS_REGR),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Administrative Monetary Penalties Regulations", MS_AMPR)],
    related=["how-to-register-msb-canada.html", "fintrac-penalties-amps.html", "buying-an-msb-canada.html"],
)

# ------------------------------------------------------------------ 16. FINTRAC administrative monetary penalties
GUIDES["fintrac-penalties-amps.html"] = dict(
    checked="21 October 2026",
    title="FINTRAC Penalties (AMPs): How They Work in 2026 | AML Canada",
    desc="FINTRAC administrative monetary penalties explained: the amounts in force since March 26, 2026, violation classes, notices, appeals and public naming.",
    crumb="FINTRAC penalties (AMPs)",
    h1="FINTRAC administrative monetary penalties (AMPs) explained",
    lede="FINTRAC can impose administrative monetary penalties for breaches of the anti-money laundering law. Amendments in force since March 26, 2026 raised the maximum amounts up to 40 times and added compliance agreements and compliance orders.",
    label="Guide · FINTRAC",
    service="outsourced-compliance-officer.html",
    also=["effectiveness-reviews.html"],
    date="2026-10-21",
    takeaways=["For violations on or after March 26, 2026, the cap is $4 million per violation for a person and $20 million for an entity.",
               "Each violation is classed as minor, serious or very serious, and the class sets the range.",
               "You have 30 days to pay or make representations, and paying means accepting the violation.",
               "Imposed penalties are made public, and a compliance agreement now follows every prescribed violation."],
    sections=[
        ("what", "What an AMP is", f"""          <p>An administrative monetary penalty (AMP) is a civil penalty for not complying with the Proceeds of Crime (Money Laundering) and Terrorist Financing Act and its regulations. FINTRAC has been able to impose them since December 30, 2008. Under the <a href="{L_PCMLTFA}" rel="noopener">Act</a>, penalties are meant to encourage compliance rather than to punish (section 73.11). A violation isn't an offence (section 73.23), and due diligence is a defence (section 73.24).</p>
          <p>FINTRAC can also refer non-compliance to law enforcement as a criminal offence. It can't do both for the same act or omission (section 73.12). <a href="{F_AMP}" rel="noopener">FINTRAC's policy</a> says that after an assessment it may take no further action, follow up, issue a penalty, or disclose information to law enforcement.</p>"""),
        ("amounts", "Penalty amounts in force today", f"""          <p>The Strengthening Canada's Immigration System and Borders Act (Bill C-12) received Royal Assent on March 26, 2026. It amended the Act and the <a href="{MS_AMPR}" rel="noopener">Administrative Monetary Penalties Regulations</a> the same day. The new framework applies to violations committed on or after that day. Violations committed before it stay under the former rules, according to the Act's transitional provisions and <a href="{F_AMP_NEW}" rel="noopener">FINTRAC's notice on the changes</a>.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Class</th><th scope="col">Range per violation before March 26, 2026</th><th scope="col">Range per violation from March 26, 2026</th></tr></thead>
            <tbody>
              <tr><th scope="row">Minor</th><td>$1 to $1,000</td><td>$1 to $40,000</td></tr>
              <tr><th scope="row">Serious</th><td>$1 to $100,000</td><td>$1 to $4,000,000</td></tr>
              <tr><th scope="row">Very serious</th><td>$1 to $100,000 (person); $1 to $500,000 (entity)</td><td>$1 to $20,000,000, with a $4,000,000 cap for a person</td></tr>
            </tbody>
          </table></div>
          <p>Section 73.1 of the Act now caps each prescribed violation at $4,000,000 for a person and $20,000,000 for an entity. The total for all violations on one notice is capped at the greater of $4,000,000 or 3% of a person's gross global income, or the greater of $20,000,000 or 3% of an entity's gross global revenue. For an entity in an affiliated group, the group's revenue is used.</p>
          <p>FINTRAC says it scopes each examination so the review period falls entirely under one framework.</p>"""),
        ("classes", "Minor, serious and very serious", f"""          <p>The schedule to the penalty regulations classifies each violation. Some examples:</p>
          <ul>
            <li><strong>Very serious:</strong> failing to report a suspicious transaction; failing to comply with a ministerial directive; failing to keep a compliance program that is reasonably designed, risk-based and effective; and the compliance program elements in section 156 of the Regulations, such as the compliance officer, policies, risk assessment, training and the two-year review.</li>
            <li><strong>Serious:</strong> MSB registration failures, including not registering, not reporting changes, not answering clarification requests, not renewing and not notifying cessation.</li>
            <li><strong>Minor:</strong> most record keeping, client identification and threshold reporting items, and the travel rule obligations.</li>
          </ul>
          <p>Bill C-12 moved certain compliance program violations from serious to very serious, as <a href="{F_CHG}" rel="noopener">FINTRAC's changes page</a> notes. <a href="{MS_PEN}" rel="noopener">FINTRAC publishes harm done guides</a> for seven groups of violations: compliance program, threshold reports (large cash, electronic funds transfer and casino disbursement), suspicious transaction reports, know your client, record keeping, MSB registration, and other compliance measures.</p>"""),
        ("calculation", "How the amount is set", f"""          <p>Section 73.11 of the Act lists the criteria: the non-punitive purpose, the harm done by the violation, and, new since March 26, 2026, the ability of the person or entity to pay. The regulations add the history of compliance. If FINTRAC asks for information on your ability to pay, your later representations can generally rely only on what you gave before its deadline (section 73.111).</p>
          <p>FINTRAC's published policy works in two steps. First, it assesses harm: how far the violation interferes with the Act's objectives or FINTRAC's mandate, including resulting harm such as unreported transactions caused by a gap in procedures. For a complete failure to meet a requirement, the base penalty is typically the maximum for that violation. Second, it adjusts for compliance history and the non-punitive purpose. FINTRAC says it's updating this policy, with an updated approach to calculating penalties under the new framework.</p>"""),
        ("process", "From notice of violation to final decision", """          <ol>
            <li><strong>Notice of violation.</strong> It names the violations, the proposed penalty and how it was calculated. FINTRAC must start proceedings within two years after it becomes aware of the subject matter.</li>
            <li><strong>Pay, or make representations.</strong> You have 30 days after service, or a longer period FINTRAC specifies. Paying means you're deemed to have committed the violation, and proceedings end.</li>
            <li><strong>No response.</strong> You're deemed to have committed the violation, and FINTRAC imposes the proposed penalty.</li>
            <li><strong>Director's decision.</strong> If you make written representations, the Director decides on a balance of probabilities and may impose the proposed penalty, a lesser one or none.</li>
            <li><strong>Federal Court.</strong> For a serious or very serious violation, or a compliance order violation, you can appeal within 30 days after the decision is served. If no decision comes within 90 days after your representations are complete, you can appeal within the following 30 days.</li>
          </ol>
          <p>Decisions on minor violations can't be appealed, unless a series of minor violations on one notice counts as serious. The current regulations set that threshold at $400,000 in total. Penalties not paid on time accrue interest and are a debt to the Crown.</p>"""),
        ("agreements", "Compliance agreements and compliance orders", """          <p>After proceedings on a prescribed violation end, FINTRAC must require a compliance agreement (section 73.16). It sets out the measures you'll take and a deadline. FINTRAC can extend the deadline by up to one year if you're making substantial progress. If you don't sign within six months, you're deemed to have refused.</p>
          <p>If you refuse, or miss the deadline, the Director must make a compliance order and make it public (section 73.17). The order requires you to publish the measures you're taking. Breaching it is a compliance order violation, capped at the greater of $5,000,000 or 3% of gross global income for a person, and the greater of $30,000,000 or 3% of gross global revenue for an entity.</p>"""),
        ("public", "Public naming", f"""          <p>When a violation is deemed committed, or the Director decides one was committed, FINTRAC must publish the name of the person or entity, the nature of the violation and the penalty amount, and it may include its reasons (section 73.22). Notices stay on <a href="{F_AMP_LIST}" rel="noopener">FINTRAC's public notice page</a> for five years. For an MSB, an unpaid penalty also has a registration effect: 30 days after proceedings end, it makes the business ineligible to register, as our guide to <a href="msb-registration-refused-revoked.html">revoked registrations</a> explains.</p>"""),
        ("reduce", "Lowering your risk", """          <p>Most violations trace back to gaps an internal check would find. Test your program with a regular <a href="fintrac-effectiveness-review-checklist.html">effectiveness review</a>, fix late or missing reports before FINTRAC calls, and prepare as our <a href="fintrac-examination-preparation.html">examination guide</a> describes. An <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> can keep reporting and records current, and an external <a href="effectiveness-reviews.html">effectiveness review</a> gives an independent view. Payment businesses should also check their <a href="fintrac-travel-rule-ministerial-directives.html">travel rule and directive procedures</a>, since breaching a directive is very serious.</p>"""),
    ],
    faqs=[("What is the maximum FINTRAC penalty now?", "For violations on or after March 26, 2026, up to $4 million per violation for a person and $20 million for an entity. The total on one notice can reach the greater of those amounts or 3% of gross global income or revenue."),
          ("Does paying a FINTRAC penalty mean admitting the violation?", "Yes. Under the Act, paying the penalty in a notice of violation means you're deemed to have committed the violation, and the proceedings end."),
          ("Can I appeal a FINTRAC penalty?", "First make written representations to FINTRAC's Director within 30 days of the notice. You can then appeal the Director's decision to the Federal Court within 30 days for serious, very serious and compliance order violations."),
          ("Will FINTRAC publish my business's name?", "Yes, when a violation is deemed committed or the Director decides one was committed. FINTRAC publishes the name, the nature of the violation and the penalty, and notices stay online for five years."),
          ("Does FINTRAC consider whether a business can afford the penalty?", "Since March 26, 2026, the Act lists ability to pay as one of the criteria for setting the amount, along with the harm done and the purpose of encouraging compliance.")],
    sources=[("FINTRAC, Administrative monetary penalties: changes following legislative amendments", F_AMP_NEW), ("FINTRAC, Administrative monetary penalties policy", F_AMP),
             ("FINTRAC, Penalties for non-compliance", MS_PEN), ("FINTRAC, Public notice of administrative monetary penalties", F_AMP_LIST),
             ("FINTRAC, Reviews and appeals", MS_REVIEW), ("FINTRAC, Modernization and upcoming changes", F_CHG),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Administrative Monetary Penalties Regulations", MS_AMPR)],
    related=["fintrac-examination-preparation.html", "fintrac-effectiveness-review-checklist.html", "msb-registration-refused-revoked.html"],
)

# ------------------------------------------------------------------ 17. travel rule and ministerial directives
GUIDES["fintrac-travel-rule-ministerial-directives.html"] = dict(
    checked="21 October 2026",
    title="Travel Rule Canada and FINTRAC Ministerial Directives | AML Canada",
    desc="The travel rule in Canada for funds and virtual currency transfers, what to do when information is missing, and the Russia, Iran and North Korea directives.",
    crumb="Travel rule and directives",
    h1="The travel rule and ministerial directives: what Canadian MSBs must do",
    lede="Canada's travel rule requires money services businesses to send originator and beneficiary information with funds and virtual currency transfers, and to check it arrives with transfers they receive. Ministerial directives add stricter measures for transactions connected to Russia, Iran and North Korea.",
    label="Guide · FINTRAC",
    service="compliance-programs.html",
    also=["outsourced-compliance-officer.html"],
    date="2026-10-21",
    takeaways=["Include names, addresses and account or reference numbers with transfers you send.",
               "Take reasonable measures to get missing information, then follow written risk-based procedures.",
               "Three ministerial directives are in force: Russia, Iran and North Korea (DPRK).",
               "Directive transactions are high risk at any amount, and Iran-connected transactions must all be reported."],
    sections=[
        ("what", "What the travel rule is", f"""          <p>The travel rule is the requirement to make sure specific information goes with an electronic funds transfer (EFT) or a virtual currency transfer. It comes from section 9.5 of the <a href="{L_PCMLTFA}" rel="noopener">Act</a> and sections 124 and 124.1 of the <a href="{L_PCMLTFR}" rel="noopener">Regulations</a>. <a href="{F_TRAVEL}" rel="noopener">FINTRAC's guidance</a> applies it to financial entities, money services businesses (MSBs), foreign MSBs and casinos.</p>
          <p>Information you receive under the travel rule can't be removed from a transfer. The travel rule isn't a separate record keeping requirement, though following it helps you meet your record keeping and reporting obligations. The EFTs covered are international EFTs, and EFTs within Canada sent as SWIFT MT-103 messages or their equivalent.</p>"""),
        ("eft", "Electronic funds transfers", f"""          <p>The rule applies to the EFTs you must keep a record of. For an MSB, section 36 of the Regulations requires records when it initiates an EFT of $1,000 or more, sends an international EFT of $1,000 or more initiated by someone else, or is the final recipient of an international EFT of $1,000 or more. <a href="{F_REC_MSB}" rel="noopener">FINTRAC's record keeping guidance</a> has the detail.</p>
          <p>When you initiate an EFT, include:</p>
          <ul>
            <li>the name, address and account number or other reference number, if any, of the person or entity who requested the transfer;</li>
            <li>the beneficiary's name and address; and</li>
            <li>if applicable, the beneficiary's account number or other reference number.</li>
          </ul>
          <p>When you receive an EFT, as an intermediary or as the final recipient, take reasonable measures to make sure that information is included. If you pass an EFT on, include the information you received or obtained.</p>"""),
        ("vc", "Virtual currency transfers", """          <p>MSBs keep records when they transfer $1,000 or more in virtual currency at a client's request, or receive $1,000 or more in virtual currency for remittance to a beneficiary. For those transfers, you must send the name, address and account or other reference number, if any, of both the person who requested the transfer and the beneficiary. For transfers you receive, take reasonable measures to make sure the same information is included. Crypto businesses can read this with our guide to <a href="crypto-registration-canada.html">crypto registration with FINTRAC</a>.</p>"""),
        ("missing", "When the information is missing", f"""          <p>If a transfer arrives without the required information, you must take reasonable measures to obtain it. FINTRAC describes reasonable measures as steps taken to achieve an outcome even if they don't achieve it, such as asking the client, searching open sources, retrieving information you already hold, or consulting commercially available information.</p>
          <p>You also need written, risk-based policies and procedures for what happens when those measures fail. FINTRAC says they must cover when you allow, suspend or reject the transfer, and what follow-up measures you take. Write the steps down in your procedures and keep a record of what you did for each case. If the circumstances give you reasonable grounds to suspect money laundering, terrorist financing or sanctions evasion, the usual <a href="{F_STR}" rel="noopener">suspicious transaction reporting</a> duty applies as well.</p>
          <p>Under the penalty regulations, the travel rule obligations are minor violations. For violations on or after March 26, 2026, a minor violation can carry up to $40,000 each. Our <a href="fintrac-penalties-amps.html">guide to FINTRAC penalties</a> explains the classes.</p>"""),
        ("directives", "What a ministerial directive is", f"""          <p>Part 1.1 of the Act, in force since June 19, 2014, lets the Minister of Finance issue directives requiring reporting entities to apply countermeasures to transactions coming from or going to designated foreign jurisdictions or entities. <a href="{F_DIR}" rel="noopener">FINTRAC's directives page</a> says FINTRAC informs reporting entities when one is issued, that each directive stays in force until revoked, suspended or amended, and that directives are reviewed at least every three years. Every MSB and foreign MSB must comply (section 11.43).</p>"""),
        ("in-force", "The three directives in force", f"""          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Directive</th><th scope="col">In force since</th><th scope="col">Latest change</th></tr></thead>
            <tbody>
              <tr><th scope="row"><a href="{MS_DIR_RUS}" rel="noopener">Russia</a></th><td>February 24, 2024</td><td>FINTRAC guidance updated March 22, 2025</td></tr>
              <tr><th scope="row"><a href="{MS_DIR_IRI}" rel="noopener">Iran</a></th><td>July 25, 2020</td><td>Directive amended February 15, 2024 and November 15, 2025; guidance updated June 23, 2026</td></tr>
              <tr><th scope="row"><a href="{MS_DIR_DPRK}" rel="noopener">North Korea (DPRK)</a></th><td>December 9, 2017</td><td>FINTRAC guidance updated March 22, 2025</td></tr>
            </tbody>
          </table></div>
          <p>For any transaction originating from or bound for one of these countries, whatever the amount, each directive requires you to:</p>
          <ul>
            <li>treat it as high risk;</li>
            <li>verify the identity of any person or entity requesting or benefiting from it;</li>
            <li>apply customer due diligence with particular attention to sanctions evasion risk, including the source of funds or virtual currency, the purpose of the transaction, and the beneficial ownership or control of any entity involved; and</li>
            <li>keep a record of it, even below the usual record keeping thresholds.</li>
          </ul>
          <p>The Iran and North Korea directives also require policies and procedures to assess the sanctions evasion risk associated with that country. The Iran directive goes further: every Iran-connected transaction must be reported to FINTRAC. Below-threshold EFTs and virtual currency receipts go on the usual EFT or large virtual currency transaction report, marked "IR2020" in the ministerial directive field. Transfers within Canada go on a suspicious transaction report, also marked "IR2020", with the suspicion and action taken sections left blank.</p>"""),
        ("connection", "Deciding whether a transaction is connected", """          <p>FINTRAC's guidance gives examples of a connection: an origin or destination address in the country, transactions involving the country's government representatives, and use of the Russian ruble or Iranian rial. For Iran, it also lists funds from the sale of an asset in Iran and online transactions traced to an IP address geolocated in Iran. A transfer routed through a third country is caught when details such as the account or third-party information point back to the country.</p>
          <p>A client's passport or nationality alone isn't a connection, and neither is a past history of sending funds there, if nothing else about the transaction points to the country.</p>"""),
        ("program", "Building it into your program", f"""          <p>Your policies and procedures should cover the travel rule and the ministerial directives, as <a href="{F_G4}" rel="noopener">FINTRAC's compliance program guidance</a> expects. They should also say how you learn of new directives and how you decide a transaction is connected. Your risk assessment should record your exposure to these countries. Failing to comply with a directive is a very serious violation, and knowingly contravening one can also be prosecuted under section 74 of the Act. FINTRAC also publishes advisories on countries identified by the Financial Action Task Force. The most recent on its <a href="{MS_NEWS}" rel="noopener">news page</a> is dated July 15, 2026.</p>
          <p>Our <a href="compliance-programs.html">14-document compliance program</a> includes a Travel Rule Policy and Procedure, and our guide to <a href="fintrac-compliance-program-requirements.html">compliance program requirements</a> covers the rest. An <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> can handle directive reviews and reporting. If you're still registering, check our guide on <a href="virtual-office-msb-registration.html">addresses and MSB registration</a> and what to do if a registration is <a href="msb-registration-refused-revoked.html">denied or revoked</a>.</p>"""),
    ],
    faqs=[("What is the travel rule in Canada?", "It requires financial entities, MSBs, foreign MSBs and casinos to include the requester's and beneficiary's names, addresses and account or reference numbers with electronic funds and virtual currency transfers, and to take reasonable measures to check that information arrives with transfers they receive."),
          ("Does the travel rule apply to crypto in Canada?", "Yes. MSBs and foreign MSBs must include travel rule information with virtual currency transfers they're required to keep records of, generally $1,000 or more, and take reasonable measures for transfers they receive."),
          ("What should I do if a transfer arrives without originator information?", "Take reasonable measures to obtain it, such as asking the client. If that fails, follow your written risk-based procedures on whether to allow, suspend or reject the transfer, and record your follow-up."),
          ("Which countries do FINTRAC ministerial directives cover?", "Three directives are in force: Russia (since February 24, 2024), Iran (since July 25, 2020, amended in 2024 and 2025) and North Korea (since December 9, 2017)."),
          ("Do MSBs have to report every transaction connected to Iran?", "Yes. Under the Iran directive, every transaction originating from or bound for Iran must be reported to FINTRAC, whatever the amount, using the report types FINTRAC's guidance sets out.")],
    sources=[("FINTRAC, Travel rule for electronic funds and virtual currency transfers", F_TRAVEL), ("FINTRAC, Ministerial directives and transaction restrictions", F_DIR),
             ("FINTRAC, Guidance on the Ministerial Directive on Russia", MS_DIR_RUS), ("FINTRAC, Guidance on the Ministerial Directive on Iran", MS_DIR_IRI),
             ("FINTRAC, Guidance on the Ministerial Directive on the DPRK", MS_DIR_DPRK), ("FINTRAC, Record keeping for MSBs", F_REC_MSB),
             ("FINTRAC, Compliance program requirements", F_G4), ("FINTRAC news", MS_NEWS),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", L_PCMLTFA),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Regulations", L_PCMLTFR),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Administrative Monetary Penalties Regulations", MS_AMPR)],
    related=["fintrac-reporting-requirements.html", "crypto-registration-canada.html", "fintrac-compliance-program-requirements.html"],
)



# ------------------------------------------------------------------ apostille guides
# Official sources used by the apostille guides (checked 21 October 2026).
AG_GAC = "https://international.canada.ca/en/global-affairs/services/document-authentication"
AG_GAC_REQ = "https://international.canada.ca/en/global-affairs/services/document-authentication/requirements"
AG_GAC_FAQ = "https://international.canada.ca/en/global-affairs/services/document-authentication/faq"
AG_GAC_GLOSS = "https://international.canada.ca/en/global-affairs/services/document-authentication/glossary"
AG_GAC_UPD = "https://international.canada.ca/en/global-affairs/services/document-authentication/updates"
AG_GAC_PORTAL = "https://apostille-gac.powerappsportals.com/en/search-document/"
AG_HCCH = "https://www.hcch.net/en/instruments/conventions/status-table/?cid=41"
AG_ON = "https://www.ontario.ca/page/authenticate-document-use-outside-canada"
AG_ON_NOTARY = "https://www.ontario.ca/page/information-notaries-public-ontario"
AG_ON_FEES = "https://www.ontario.ca/page/cost-time-required-to-register-change-search-for-business-name-corporation-not-for-profit"
AG_BC_FEES = "https://www2.gov.bc.ca/gov/content/governments/government-id/guide-to-the-authentication-of-documents/fees"
AG_BC_REG = "https://www2.gov.bc.ca/gov/content/governments/government-id/guide-to-the-authentication-of-documents/process/registries-online-docs"
AG_AB = "https://www.alberta.ca/document-authentication-other-jurisdictions-countries"
AG_SK = "https://www.saskatchewan.ca/government/notarized-documents-legislation-maps/authenticating-notarized-documents"
AG_QC_ABOUT = "https://www.quebec.ca/en/justice-and-civil-status/services/apostille/about"
AG_QC_APPLY = "https://www.quebec.ca/en/justice-and-civil-status/services/apostille/applying"
AG_F_MSB_REGISTRY = "https://fintrac-canafe.canada.ca/msb-esm/reg-eng"
AG_B_REGISTRY = "https://www.bankofcanada.ca/regulatory-oversight/retail-payments/psp-registry/"

GUIDES["apostille-canada-guide.html"] = dict(
    checked="21 October 2026",
    title="How to Get an Apostille in Canada (2026 Guide) | AML Canada",
    desc="How to get an apostille in Canada: which authority issues it in each province, when to notarize first, translations, and official fees and processing times.",
    crumb="Apostille in Canada",
    h1="How to get an apostille in Canada (2026 guide)",
    lede="Since January 11, 2024, Canadian public documents going to Apostille Convention countries get an apostille. Who issues it depends on where the document was issued or notarized: Global Affairs Canada, or one of five provinces.",
    label="Guide · Apostille",
    service="apostille-notarization-canada.html",
    date="2026-10-21",
    takeaways=["The Apostille Convention has applied in Canada since January 11, 2024.",
               "Alberta, British Columbia, Ontario, Quebec and Saskatchewan apostille their own documents. Global Affairs Canada handles federal documents and the rest of Canada.",
               "A document notarized in Alberta, Ontario or Saskatchewan goes to that province, wherever it was issued.",
               "Global Affairs Canada charges no fee. Provincial fees run from CA$16 to CA$66.50 per document."],
    sections=[
        ("what", "What an apostille does", f"""          <p>An apostille is a certificate that confirms the signature and seal of a public official on a document are genuine. Countries that belong to the Apostille Convention accept it without any further step, according to the <a href="{AG_GAC_GLOSS}" rel="noopener">Global Affairs Canada glossary</a>. Before the Convention, a Canadian document usually had to be authenticated in Canada and then legalized by the destination country's embassy or consulate. The apostille replaces that chain with a single certificate.</p>
          <p>Canada acceded to the Convention on May 12, 2023, and it entered into force for Canada on January 11, 2024, according to the <a href="{AG_HCCH}" rel="noopener">Hague Conference status table</a>. An apostille doesn't validate what a document says. It confirms where the document came from.</p>"""),
        ("step-1", "Step 1: Confirm what the destination needs", f"""          <p>Whether you need an apostille is decided by the law of the country where the document will be used. Canadian law doesn't require it. <a href="{AG_GAC_FAQ}" rel="noopener">Global Affairs Canada</a> and Ontario's Official Documents Services both tell applicants to check with the receiving institution or the destination country's embassy or consulate first. Neither office can advise on what a foreign authority wants.</p>
          <p>Ask how recent the document must be, whether a certified copy is acceptable and whether any translation also needs an apostille. Quebec advises applicants to make sure the issue date meets the requesting entity's requirements and to use recent documents where possible.</p>"""),
        ("step-2", "Step 2: Find the right authority", f"""          <p>Canada has six competent authorities: the federal government and five provinces. The <a href="{AG_GAC_REQ}" rel="noopener">Global Affairs Canada requirements</a> split the work like this:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Where the document comes from</th><th scope="col">Who issues the apostille</th></tr></thead>
            <tbody>
              <tr><th scope="row">Government of Canada (federal documents)</th><td>Global Affairs Canada</td></tr>
              <tr><th scope="row">Manitoba, New Brunswick, Newfoundland and Labrador, Northwest Territories, Nova Scotia, Nunavut, Prince Edward Island, Yukon</th><td>Global Affairs Canada, for documents issued or notarized there</td></tr>
              <tr><th scope="row">Alberta, Ontario, Saskatchewan</th><td>The province, for documents issued there and for any document notarized there</td></tr>
              <tr><th scope="row">British Columbia, Quebec</th><td>The province, for documents issued there; a notarized document qualifies only if the original was issued in the province</td></tr>
            </tbody>
          </table></div>
          <p>Global Affairs Canada's online <a href="{AG_GAC_PORTAL}" rel="noopener">eligibility tool</a> tells you where to send a given document. Quebec says it doesn't apostille documents issued by a federal authority, a territory or another province. Global Affairs Canada also notes that some countries accept only its authentication, so confirm the destination accepts a provincial apostille.</p>"""),
        ("step-3", "Step 3: Notarize the document if needed", f"""          <p>Government-issued originals with an original signature or seal can often be apostilled directly. Private documents, and many business records, must be notarized first. Plain photocopies can't be authenticated, but Global Affairs Canada may accept a copy certified by a notary. It also says commissioners for oaths generally aren't authorized to certify copies.</p>
          <p>When a notary signs a document for authentication, <a href="{AG_GAC_REQ}" rel="noopener">Global Affairs Canada</a> expects the notary to:</p>
          <ul>
            <li>have a valid certificate of appointment;</li>
            <li>sign by hand in ink;</li>
            <li>apply a stamp or seal showing their full name and the province or territory of appointment;</li>
            <li>state the type of notarial act and the date;</li>
            <li>show when their appointment expires, if it does.</li>
          </ul>
          <p>Provincial rules add to this. In Ontario the notary must be physically present, and the <a href="{AG_ON_NOTARY}" rel="noopener">Ministry of the Attorney General</a> says documents notarized remotely won't be authenticated or apostilled. Ontario also needs the notary's full signature and seal on the same page. Alberta asks for corporate records and powers of attorney to be notarized by an Alberta notary. Quebec requires an official certificate from a lawyer or notary for private documents, with a signature authentication from the Barreau du Québec or the Chambre des notaires du Québec.</p>"""),
        ("step-4", "Step 4: Arrange translations", f"""          <p>Global Affairs Canada needs a certified translation for any content not in English or French, sent with the original. The translator must belong to a recognized provincial translation association, or a Canadian notary who speaks both languages must attest the translation. Ontario adds that a document in another language must be issued in Canada, notarized by an Ontario notary and accompanied by a translation.</p>"""),
        ("step-5", "Step 5: Submit, pay and wait", f"""          <p>Global Affairs Canada takes requests through its online portal. You then mail or courier the documents, or drop them at its distribution centre in Ottawa, which offers no in-person service. Include a prepaid return envelope or label if you want tracking. Ontario accepts mail-in requests at its Toronto office and in-person requests in Toronto, Ottawa, Sault Ste. Marie, Windsor and Thunder Bay. Alberta and British Columbia take documents by mail or courier, and Quebec by mail.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Authority</th><th scope="col">Fee</th><th scope="col">Published processing time</th></tr></thead>
            <tbody>
              <tr><th scope="row"><a href="{AG_GAC}" rel="noopener">Global Affairs Canada</a></th><td>Free</td><td>Processing requests received 25 business days earlier, plus mailing time; no expedited service</td></tr>
              <tr><th scope="row"><a href="{AG_ON}" rel="noopener">Ontario</a></th><td>CA$16 per notarized document; CA$32 per Ontario government document</td><td>Mail-in within 15 business days; in person about 30 minutes if complete</td></tr>
              <tr><th scope="row"><a href="{AG_BC_FEES}" rel="noopener">British Columbia</a></th><td>CA$20 per document</td><td>2 to 4 weeks, not including mail time</td></tr>
              <tr><th scope="row"><a href="{AG_AB}" rel="noopener">Alberta</a></th><td>CA$25 per document</td><td>At least 7 to 10 business days</td></tr>
              <tr><th scope="row"><a href="{AG_SK}" rel="noopener">Saskatchewan</a></th><td>CA$50 per certificate, signatory or package</td><td>Typically 4 to 7 business days, not including mail time</td></tr>
              <tr><th scope="row"><a href="{AG_QC_APPLY}" rel="noopener">Quebec</a></th><td>CA$66.50 per document</td><td>Varies with volume; on October 9, 2026 Quebec was processing requests received October 8</td></tr>
            </tbody>
          </table></div>
          <p>These are the figures each authority published when we checked on October 21, 2026. Global Affairs Canada also says you don't need to hire a third party to submit a request, and that processing times are the same either way.</p>"""),
        ("after", "After you receive the apostille", f"""          <p>Apostilles from Global Affairs Canada don't expire. Before January 11, 2024, Global Affairs Canada authenticated documents with a red stamp, and a red-stamped document can't be used in a Convention country. You need a new request with a clean version of the document. Global Affairs Canada's <a href="{AG_GAC_UPD}" rel="noopener">verification tool</a> lets a recipient check apostilles it issued and those issued by Alberta, Saskatchewan and British Columbia. Ontario runs its own validity check.</p>"""),
        ("non-convention", "Countries outside the Convention", f"""          <p>For a country that hasn't joined the Convention, the document may need legalization at that country's embassy, high commission or consulate after it's authenticated in Canada. Ontario issues a certificate of authentication for those countries. Alberta and Quebec issue an apostille either way, and both say legalization may still be needed. Global Affairs Canada can forward authenticated documents to an embassy or high commission in Ottawa on request.</p>
          <p>If your documents are corporate records for a foreign bank or regulator, our guide to <a href="apostille-corporate-documents-canada.html">apostilling Canadian corporate documents</a> covers which ones need notarizing. Our <a href="apostille-notarization-canada.html">apostille and notarization service</a> coordinates the process for corporate documents, with notarization by a licensed Ontario partner notary.</p>"""),
    ],
    faqs=[("Who issues apostilles in Canada?", "Global Affairs Canada issues them for federal documents and for documents from Manitoba, New Brunswick, Newfoundland and Labrador, Nova Scotia, Prince Edward Island and the three territories. Alberta, British Columbia, Ontario, Quebec and Saskatchewan issue them for their own documents."),
          ("How much does an apostille cost in Canada?", "Global Affairs Canada charges no fee. Ontario charges CA$16 per notarized document and CA$32 per Ontario government document, British Columbia CA$20, Alberta CA$25, Saskatchewan CA$50 per certificate, signatory or package, and Quebec CA$66.50 per document."),
          ("How long does an apostille take?", "It depends on the authority. On October 21, 2026, Global Affairs Canada was processing requests received 25 business days earlier, plus mailing time. Ontario processes mail-in requests within 15 business days."),
          ("Can I get an apostille on a photocopy?", "Not on a plain photocopy. Global Affairs Canada may authenticate a copy certified by a notary, depending on the document."),
          ("Does an apostille work in every country?", "Only in countries that belong to the Apostille Convention. Other countries may require legalization at their embassy or consulate after the document is authenticated in Canada.")],
    sources=[("Global Affairs Canada, Authentication of documents", AG_GAC), ("Requirements", AG_GAC_REQ), ("Frequently asked questions", AG_GAC_FAQ),
             ("Glossary", AG_GAC_GLOSS), ("Notices and updates", AG_GAC_UPD), ("Document eligibility tool", AG_GAC_PORTAL),
             ("HCCH, Apostille Convention status table", AG_HCCH),
             ("Ontario, Authenticate a document for use outside Canada", AG_ON), ("Ontario, Information for notaries public", AG_ON_NOTARY),
             ("British Columbia, Document authentication fee", AG_BC_FEES), ("Alberta, Documents for other jurisdictions or countries", AG_AB),
             ("Saskatchewan, Authenticating notarized documents", AG_SK), ("Quebec, About apostille", AG_QC_ABOUT),
             ("Quebec, Applying for an apostille", AG_QC_APPLY)],
    related=["apostille-corporate-documents-canada.html", "foreign-msb-registration-canada.html", "how-to-register-msb-canada.html"],
)


GUIDES["apostille-corporate-documents-canada.html"] = dict(
    checked="21 October 2026",
    title="Apostilling Canadian Corporate Documents for Banks | AML Canada",
    desc="Apostilling Canadian corporate documents for foreign banks and regulators: certificates, certified copies, minute book extracts, resolutions and registrations.",
    crumb="Apostille for corporate documents",
    h1="Apostilling Canadian corporate documents for foreign banks and regulators",
    lede="Foreign banks, payment partners and regulators often want Canadian corporate documents with an apostille. Some government certificates can go straight to the authority. Most corporate records must be notarized first.",
    label="Guide · Apostille",
    service="apostille-notarization-canada.html",
    also=["incorporation-canada.html"],
    date="2026-10-21",
    takeaways=["Get the receiving party's document list in writing before ordering anything.",
               "Global Affairs Canada says business and corporate records must be notarized, apart from Corporations Canada certificates of incorporation with an original signature or seal.",
               "Ontario apostilles business registry documents issued since 1991 without notarization.",
               "A copy notarized in Ontario goes to Ontario's Official Documents Services, even if the original is a federal document."],
    sections=[
        ("start", "Start with the receiving party's list", f"""          <p>Each bank, payment partner and regulator sets its own requirements, and the destination country's law decides whether an apostille is needed at all. Global Affairs Canada and Ontario both say they can't advise on what a foreign authority wants. Ask the receiving party to confirm in writing:</p>
          <ul>
            <li>which documents it needs, by name;</li>
            <li>how recent each must be;</li>
            <li>whether it accepts certified or notarized copies;</li>
            <li>whether translations must be apostilled as well;</li>
            <li>whether the country is a member of the Apostille Convention.</li>
          </ul>
          <p>Our general guide to <a href="apostille-canada-guide.html">getting an apostille in Canada</a> covers the steps, authorities and fees for any document.</p>"""),
        ("federal", "Federal corporations: Corporations Canada documents", f"""          <p>Documents issued by the Government of Canada go to Global Affairs Canada. Its <a href="{AG_GAC_PORTAL}" rel="noopener">document eligibility tool</a> treats corporate documents differently by type:</p>
          <ul>
            <li><strong>Certificate of incorporation.</strong> A Corporations Canada certificate with an original signature or seal doesn't need notarizing. One without an original signature or seal must be notarized.</li>
            <li><strong>Certificates of compliance, existence and amendment, and articles of incorporation.</strong> The tool says business or corporate records must be notarized.</li>
          </ul>
          <p>Where notarization is needed, the notary's province decides the route. <a href="{AG_GAC_REQ}" rel="noopener">Global Affairs Canada</a> says a document notarized in Alberta, Ontario or Saskatchewan goes to that province, wherever it was issued. A federal certificate copied and notarized by an Ontario notary is apostilled by Ontario's Official Documents Services, at CA$16 per notarized document.</p>"""),
        ("ontario", "Ontario corporations: Ontario Business Registry documents", f"""          <p>Ontario's <a href="{AG_ON}" rel="noopener">Official Documents Services</a> accepts business registry documents issued since 1991 by the Business and Personal Property Branch or the Ontario Business Registry without notarization. Ontario charges CA$32 to authenticate an Ontario government official document.</p>
          <p>The <a href="{AG_ON_FEES}" rel="noopener">Ontario Business Registry</a> sells a certificate of status online for CA$26, available immediately, and copies of filed documents for CA$3 each. Ontario's guidance says it checks signatures and seals against its records and needs a hard copy; it won't authenticate electronic copies. Confirm with the eligibility portal that the version you order qualifies.</p>"""),
        ("other-provinces", "Companies registered in other provinces", f"""          <p>British Columbia apostilles original documents from B.C. Registries and Online Services, such as a Notice of Articles, incorporation certificate, certificate of good standing and certified true copy. <a href="{AG_BC_REG}" rel="noopener">British Columbia</a> requires notarization if the document has no Registrar's signature, or has no raised seal and you can't provide the online receipt. Alberta asks for corporate records to be notarized by an Alberta notary before it issues an apostille. Quebec apostilles documents issued in Quebec, including authentic acts such as notarized documents.</p>"""),
        ("internal", "Minute book extracts, registers and resolutions", f"""          <p>Your company's own records, such as register extracts, minute book pages and director or shareholder resolutions, are private documents. Global Affairs Canada's tool says business or corporate records, including corporate bylaws, must be notarized. Corporate powers of attorney fall under private legal documents, which must also be notarized.</p>
          <p>Under Ontario's Notaries Act, a notary can witness and attest the signing of a document and certify a true copy, according to the <a href="{AG_ON_NOTARY}" rel="noopener">Ministry of the Attorney General</a>. The notary must be physically present, as remote notarization isn't permitted, and Ontario won't apostille a remotely notarized document. Ontario also needs the notary's signature and seal on the same page, and a name and seal that match its records.</p>"""),
        ("registration", "Evidence of FINTRAC or Bank of Canada registration", f"""          <p>Payment partners often ask an MSB or payment service provider to prove it is registered. FINTRAC's <a href="{AG_F_MSB_REGISTRY}" rel="noopener">Money Services Business Registry</a> is public and shows each business's registration number, status and dates. FINTRAC says it doesn't issue licences or certificates of registration. The Bank of Canada keeps a public <a href="{AG_B_REGISTRY}" rel="noopener">registry of payment service providers</a> and says it doesn't endorse or license them.</p>
          <p>Global Affairs Canada's tool says documents from a Government of Canada department or agency that aren't on its list must be notarized. Ask the receiving party what evidence it will accept before anything is prepared. Our guides to <a href="how-to-register-msb-canada.html">registering an MSB</a> and <a href="foreign-msb-registration-canada.html">foreign MSB registration</a> explain the registration itself.</p>"""),
        ("translation", "Translations", f"""          <p>Some countries want documents translated into their language. Depending on the recipient, you may need an apostille on the original only, or on both the original and the translation, as <a href="{AG_QC_ABOUT}" rel="noopener">Quebec</a> explains. Ask the receiving party which one it needs. For documents going into the Canadian process, Global Affairs Canada needs a certified translation of any content that isn't in English or French.</p>"""),
        ("summary", "Quick reference: where each document goes", f"""          <p>This table covers federal and Ontario corporations, and assumes any notarization is done by an Ontario notary, as with our partner notary. Fees are the government fees published on October 21, 2026.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Document</th><th scope="col">Notarize first?</th><th scope="col">Apostille from</th></tr></thead>
            <tbody>
              <tr><th scope="row">Corporations Canada certificate of incorporation with an original signature or seal</th><td>No</td><td>Global Affairs Canada, free</td></tr>
              <tr><th scope="row">Other Corporations Canada documents, such as certificates of compliance, existence or amendment, and articles</th><td>Yes</td><td>Ontario, CA$16 per notarized document</td></tr>
              <tr><th scope="row">Ontario Business Registry documents issued since 1991, such as a certificate of status</th><td>No</td><td>Ontario, CA$32 per document</td></tr>
              <tr><th scope="row">Minute book extracts, registers, resolutions and bylaws</th><td>Yes</td><td>Ontario, CA$16 per notarized document</td></tr>
              <tr><th scope="row">Corporate power of attorney</th><td>Yes</td><td>Ontario, CA$16 per notarized document</td></tr>
            </tbody>
          </table></div>
          <p>Global Affairs Canada sends documents notarized in Alberta, Ontario or Saskatchewan to that province, which is why a notarized federal document lands with Ontario in this table. Always run the specific document through the <a href="{AG_GAC_PORTAL}" rel="noopener">eligibility tool</a> or the province's guidance, because the version you hold matters.</p>"""),
        ("rejections", "Common reasons documents come back", f"""          <p>The authorities list these reasons on their official pages:</p>
          <ul>
            <li>a plain photocopy, with no original signature or seal;</li>
            <li>an electronic copy (Ontario needs a hard copy, and Global Affairs Canada needs paper);</li>
            <li>a document commissioned by a commissioner for taking affidavits, which Ontario won't authenticate;</li>
            <li>a document notarized remotely, in Ontario;</li>
            <li>a notary's signature and seal on different pages, or a seal that doesn't match the authority's records;</li>
            <li>glued or laminated documents, which Global Affairs Canada can't authenticate;</li>
            <li>a document sent to the wrong competent authority;</li>
            <li>a missing fee or incomplete request form.</li>
          </ul>
          <p>Our <a href="apostille-notarization-canada.html">apostille and notarization service</a> checks each corporate document against these rules before it is notarized by our licensed Ontario partner notary and submitted. If you're still setting up, start with <a href="incorporation-canada.html">company incorporation</a>.</p>"""),
    ],
    faqs=[("Can a certificate of status be apostilled without notarization?", "In Ontario, yes. Ontario's Official Documents Services accepts business registry documents issued since 1991 without notarization. Global Affairs Canada says federal certificates of compliance and existence must be notarized."),
          ("Do minute book extracts and resolutions need notarizing?", "Yes. Global Affairs Canada says business or corporate records must be notarized before authentication."),
          ("Does FINTRAC issue a registration certificate?", "No. FINTRAC says it doesn't issue licences or certificates of registration. Registration details appear in its public Money Services Business Registry."),
          ("Where does a notarized copy of a federal certificate go?", "If an Ontario notary notarized it, to Ontario's Official Documents Services. Global Affairs Canada says documents notarized in Alberta, Ontario or Saskatchewan go to that province."),
          ("Can corporate documents be notarized remotely in Ontario?", "No. Ontario's Notaries Act doesn't permit remote notarization, and Ontario won't apostille documents notarized remotely.")],
    sources=[("Global Affairs Canada, Requirements", AG_GAC_REQ), ("Document eligibility tool", AG_GAC_PORTAL), ("Frequently asked questions", AG_GAC_FAQ),
             ("Ontario, Authenticate a document for use outside Canada", AG_ON), ("Ontario, Information for notaries public", AG_ON_NOTARY),
             ("Ontario Business Registry fees", AG_ON_FEES), ("British Columbia, Registries documents", AG_BC_REG),
             ("Alberta, Documents for other jurisdictions or countries", AG_AB), ("Quebec, About apostille", AG_QC_ABOUT),
             ("FINTRAC, Money Services Business Registry", AG_F_MSB_REGISTRY), ("Bank of Canada, Registry of PSPs", AG_B_REGISTRY)],
    related=["apostille-canada-guide.html", "how-to-register-msb-canada.html", "foreign-msb-registration-canada.html"],
)


# ------------------------------------------------------------------ RPAA guides set (checked 21 October 2026)
# Official sources used only by these four guides. Prefix RP_ avoids clashes with names above.
RP_ACT = "https://laws-lois.justice.gc.ca/eng/acts/R-7.36/FullText.html"
RP_REGS = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2023-229/FullText.html"
RP_PCMLTFA = "https://laws-lois.justice.gc.ca/eng/acts/P-24.501/FullText.html"
RP_AMP = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2007-292/FullText.html"
RP_CRIT = "https://www.bankofcanada.ca/2026/06/criteria-for-registering-payment-service-providers/"
RP_FAQ = "https://www.bankofcanada.ca/2026/08/frequently-asked-questions-about-retail-payments-supervision/"
RP_FW = "https://www.bankofcanada.ca/regulatory-oversight/retail-payments/supervisory-framework/"
RP_FEE = "https://www.bankofcanada.ca/2024/10/registration-application-fee/"
RP_REFUSE = "https://www.bankofcanada.ca/2025/08/refusal-or-revocation-of-registration-under-the-rpaa/"
RP_REG_GUIDE = ("https://www.bankofcanada.ca/wp-content/uploads/2024/01/"
                "How-to-complete-a-registration-application-a-step-by-step-guide.pdf")
RP_MKT = "https://www.bankofcanada.ca/2025/12/supervisory-policy-for-online-marketplaces/"
RP_CS_GATEWAY = "https://www.bankofcanada.ca/2024/08/case-scenarios-about-e-commerce-web-building-tools-and-payment-gateways/"
RP_CS_REMIT = "https://www.bankofcanada.ca/2024/08/case-scenarios-about-remittance-service-providers/"
RP_CS_CRYPTO = "https://www.bankofcanada.ca/2024/10/case-scenarios-about-providers-of-services-backed-by-cryptocurrencies/"
RP_CS_MERCHANT = "https://www.bankofcanada.ca/2023/12/case-scenarios-about-merchants-and-the-incidental-payment-function/"
RP_CS_AGENTS = "https://www.bankofcanada.ca/2023/12/case-scenarios-about-agents-and-mandataries/"
RP_CS_GEO = "https://www.bankofcanada.ca/2023/12/case-scenarios-about-geographic-scope/"
RP_REMIND = "https://www.bankofcanada.ca/2026/06/reminder-psp-reporting-obligations-under-rpaa/"
RP_AR = "https://www.bankofcanada.ca/2024/10/annual-reporting/"
RP_AR_GUIDE = ("https://www.bankofcanada.ca/wp-content/uploads/2026/01/"
               "How-to-complete-an-annual-report-A-step-by-step-guide.pdf")
RP_CHG = "https://www.bankofcanada.ca/2026/06/reporting-changes-to-registration-information/"
RP_NOV = "https://www.bankofcanada.ca/2026/06/bank-canada-begin-publishing-notices-violation-payment-service-providers/"
RP_INC = "https://www.bankofcanada.ca/wp-content/uploads/2024/02/Incident-notification.pdf"
RP_INC_GUIDE = "https://www.bankofcanada.ca/wp-content/uploads/2025/05/how-complete-incident-step-by-step-guide.pdf"


# ------------------------------------------------------------------ RPAA 1. who must register as a PSP
GUIDES["who-must-register-psp-rpaa.html"] = dict(
    checked="21 October 2026",
    title="Who Must Register as a PSP Under the RPAA? | AML Canada",
    desc="Who must register as a payment service provider under the RPAA: the Bank of Canada's four-part test, the incidental test, exclusions and examples.",
    crumb="Who must register as a PSP",
    h1="Who must register as a PSP under the RPAA?",
    lede="You must register with the Bank of Canada if you perform a payment function as a business in its own right, for electronic transfers in Canadian or foreign currency, with a link to Canada, and no exclusion applies. This guide shows how the Bank applies each part of that test to real business models.",
    label="Guide · RPAA",
    service="rpaa-registration.html",
    date="2026-10-21",
    takeaways=["Register if you perform a payment function as a distinct business, for fiat transfers, with a link to Canada, and no exclusion applies.",
               "You can be a PSP without holding funds. Storing a customer's details for future transfers can be enough.",
               "Payments are incidental only when they exist to support another business. Separate fees, user expectations and payment marketing point the other way.",
               "Agents of a registered PSP are covered by it. Third-party providers and agents of excluded banks are not."],
    sections=[
        ("test", "The four-part test", f"""          <p>The Bank of Canada's supervisory policy, <a href="{RP_CRIT}" rel="noopener">Criteria for registering payment service providers</a> (last updated June 29, 2026), sets out a four-part test. You must register if all four parts are true:</p>
          <ol>
            <li>You perform at least one of the five payment functions as a service or business activity that isn't incidental to another service or business activity. That makes you a payment service provider (PSP).</li>
            <li>The payment function relates to an electronic funds transfer (EFT) in Canadian dollars, a foreign currency or a unit that meets prescribed criteria. That makes it a retail payment activity. Cash isn't an EFT.</li>
            <li>You have a place of business in Canada, or you direct retail payment activities at people or entities in Canada and perform them for end users here.</li>
            <li>Neither you nor the activity is excluded.</li>
          </ol>
          <p>Registration must be in place before you perform any retail payment activities (<a href="{RP_ACT}" rel="noopener">RPAA</a> section 23). The Bank's <a href="{RP_FAQ}" rel="noopener">FAQ</a> says every PSP in scope must register for itself, regardless of size or revenue.</p>"""),
        ("functions", "How the Bank reads the five payment functions", """          <p>Section 2 of the Act lists the payment functions. The Bank's policy explains how it reads each one, and some reach further than businesses expect:</p>
          <ul>
            <li><strong>Providing or maintaining an account.</strong> Storing personal or financial information about an identifiable end user for future EFTs counts. You don't need to hold any funds. Collecting data for a single transaction usually doesn't count.</li>
            <li><strong>Holding funds.</strong> Funds are held when they're at rest, available for later withdrawal or transfer, and owed to the end user. Funds in transit aren't held. If you do hold funds, our <a href="rpaa-safeguarding-end-user-funds.html">safeguarding guide</a> explains what follows.</li>
            <li><strong>Initiating an EFT.</strong> You initiate a transfer when you create the first payment instruction by capturing and packaging the payer's or payee's data. This covers push and pull payments.</li>
            <li><strong>Authorizing or transmitting instructions.</strong> This includes enabling consent, confirming funds are available, and providing the platforms or interfaces that carry payment instructions.</li>
            <li><strong>Clearing or settlement.</strong> Clearing includes netting and calculating positions before settlement. Settlement includes posting debits and credits. Software used only for a merchant's accounting or reporting usually doesn't count.</li>
          </ul>
          <p>An end user is the payer or payee, who may not be your direct customer when several PSPs are involved.</p>"""),
        ("incidental", "The incidental test", f"""          <p>A business that performs payment functions only to support another business isn't a PSP. The Act builds this into the PSP definition, and section 3 of the <a href="{RP_REGS}" rel="noopener">Retail Payment Activities Regulations</a> excludes an incidental retail payment activity unless the other business itself consists of performing a payment function.</p>
          <p>The Bank's policy says payment functions may be incidental if they exist only to support your non-payment services or improve the customer's experience of them. You're more likely to be a PSP if payments are a distinct business, especially when you facilitate payments between other buyers and sellers. The Bank weighs three indicators:</p>
          <ul>
            <li>revenue or commercial advantage, including indirect benefits such as data that could later be monetized;</li>
            <li>whether end users reasonably expect to receive a payment service;</li>
            <li>marketing and branding that promote payments.</li>
          </ul>
          <p>The Bank's <a href="{RP_CS_MERCHANT}" rel="noopener">merchant scenarios</a> show where the line falls. An online boot retailer that stores a customer's name and address to speed up checkout maintains an account, but the function is incidental and it doesn't register. If the same retailer lets unaffiliated merchants accept payments through its app for a fee on each transaction, payments become a business line of their own and the retailer must register. The Bank expects businesses to reassess as they change.</p>"""),
        ("models", "How the test applies to common business models", f"""          <p>The Bank's fictional case scenarios are illustrative and aren't legal advice, but they show how it reasons. A selection:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Business model</th><th scope="col">Bank's conclusion</th><th scope="col">Why</th></tr></thead>
            <tbody>
              <tr><th scope="row">Payment gateway that captures card data and relays it to a processor, for a fee per transaction</th><td>PSP</td><td>It initiates EFTs and transmits instructions. Handling funds isn't required (<a href="{RP_CS_GATEWAY}" rel="noopener">gateway scenarios</a>)</td></tr>
              <tr><th scope="row">Website builder whose checkout redirects to another provider's page</th><td>Not a PSP</td><td>No payment function. Adding its own paid gateway would make it a PSP</td></tr>
              <tr><th scope="row">Money transfer operator that sends funds abroad straight away</th><td>PSP</td><td>It stores customer data, initiates EFTs and transmits instructions (<a href="{RP_CS_REMIT}" rel="noopener">remittance scenarios</a>)</td></tr>
              <tr><th scope="row">Remittance firm that also offers a multi-currency wallet</th><td>PSP</td><td>It also holds funds, so the safeguarding rules apply</td></tr>
              <tr><th scope="row">Online marketplace that receives sale proceeds in an account it owns or controls</th><td>PSP</td><td>Even if another PSP handles part of the process. If funds never pass through its account, it generally isn't a PSP (<a href="{RP_MKT}" rel="noopener">marketplace policy</a>)</td></tr>
              <tr><th scope="row">Exchange dealing only in cryptocurrency</th><td>Not a PSP</td><td>No transfer in Canadian or foreign currency takes place (<a href="{RP_CS_CRYPTO}" rel="noopener">crypto scenarios</a>)</td></tr>
              <tr><th scope="row">Crypto exchange that also holds fiat for trading and is subject to securities law</th><td>Doesn't need to register</td><td>Payments are incidental to trading, and the securities exclusions apply</td></tr>
              <tr><th scope="row">Crypto-backed prepaid card that earns interchange fees</th><td>PSP</td><td>The card is a separate revenue stream</td></tr>
              <tr><th scope="row">Counter that exchanges currency for cash only</th><td>Not a PSP</td><td>No EFT is involved</td></tr>
            </tbody>
          </table></div>"""),
        ("foreign", "Place of business and foreign PSPs", f"""          <p>The Bank treats you as having a place of business in Canada if you have a physical location here, including a home office, are incorporated here, or have employees, agents or mandataries here.</p>
          <p>A PSP with no place of business in Canada is still covered if it performs retail payment activities for end users in Canada and directs those activities at Canada (RPAA section 5). To locate end users, the Bank looks at factors such as IP address, shipping or service address and whether the product is localized for Canada. Signs of directing activities at Canada include marketing aimed at Canadians, a .ca domain, offering Canadian dollars or Canadian support, and a target market largely in Canada.</p>
          <p>Marketing only to test demand doesn't trigger registration, but serving end users here does. In the Bank's <a href="{RP_CS_GEO}" rel="noopener">geographic scope scenarios</a>, a foreign payment app that reaches Canadian merchants through an agreement with a Canadian PSP must register, and a foreign app's Canadian subsidiary registers in its own right. A foreign applicant also names an agent or mandatary in Canada authorized to accept notices and orders for it (RPAA paragraph 29(1)(o)).</p>"""),
        ("exclusions", "Exclusions: the details that decide close cases", """          <p>Our <a href="rpaa-registration-guide.html">RPAA overview</a> lists the exclusions in sections 6 to 10 of the Act. These points from the Bank's policy settle most close cases:</p>
          <ul>
            <li><strong>Affiliates of excluded institutions.</strong> Banks, credit unions, insurers and other institutions listed in section 9 are outside the Act. Their affiliates must register unless OSFI or the provincial regulator supervises them on a consolidated basis.</li>
            <li><strong>Merchant instruments.</strong> Instruments usable only at the issuing merchant or within a specific group of merchants are excluded. Wide-use instruments may not be.</li>
            <li><strong>Securities transactions.</strong> Payments that give effect to securities transactions are excluded only when performed by an entity regulated, or exempted from regulation, under Canadian securities law. Its other payments may still be in scope.</li>
            <li><strong>Designated systems.</strong> Payment functions performed using a system designated under the Payment Clearing and Settlement Act are excluded (section 7). Functions you perform outside the system are not.</li>
            <li><strong>Internal transactions.</strong> Transfers between affiliated entities are excluded only when no other PSP is involved (section 8). Payments to unaffiliated customers don't qualify, even if they move through an internal ledger.</li>
          </ul>"""),
        ("agents", "Agents, mandataries and third-party providers", f"""          <p>Section 10 takes an agent or mandatary of a registered PSP outside the Act while it acts within its authority and appears on the list of agents the PSP gave the Bank. The PSP keeps that list up to date and is liable for violations committed by its employees, agents, mandataries and third-party service providers within the scope of their role (section 87).</p>
          <p>The Bank's <a href="{RP_CS_AGENTS}" rel="noopener">agent scenarios</a> draw three lines. A retailer that pays out cash only on behalf of a registered remittance company doesn't register. An agent that also offers payment services to its own customers must register for those services. An agent acting for a bank, which is excluded rather than registered, may have to register itself.</p>
          <p>Third-party service providers, which supply a PSP with a payment-related service under contract, aren't excluded. The PSP discloses them and stays responsible for them. Each affiliated PSP in a group also registers separately, even when its parent is registered.</p>"""),
        ("next", "Before you apply", f"""          <p>Run the four parts for each product line and keep a written record. The Bank's <a href="{RP_REFUSE}" rel="noopener">refusal policy</a> lists, among its grounds, that the RPAA doesn't apply to the applicant. Many businesses that register with the Bank also need FINTRAC registration. Our guide to <a href="rpaa-vs-fintrac-msb-registration.html">RPAA vs FINTRAC MSB registration</a> explains how the two fit together, and our <a href="rpaa-registration.html">RPAA registration service</a> starts with this scoping work before preparing the application.</p>"""),
    ],
    faqs=[("Do I need to register with the Bank of Canada if I don't hold customer funds?", "Possibly. Holding funds is only one of the five payment functions. A payment gateway that captures card data and relays it to a processor is a PSP in the Bank's own example, even though it never handles funds."),
          ("Do crypto exchanges need to register under the RPAA?", "It depends on the model. In the Bank's examples, an exchange dealing only in cryptocurrency doesn't register, and neither does one whose fiat functions are incidental to trading and covered by the securities exclusions. A crypto-backed prepaid card that earns interchange fees is a PSP."),
          ("Does an online marketplace need to register as a PSP?", "Under the Bank's December 2025 policy, a marketplace that receives sale proceeds in an account it owns or controls is a PSP, even if it uses another PSP for part of the process. A marketplace whose funds never pass through its own account generally isn't."),
          ("Do foreign payment companies have to register with the Bank of Canada?", "Yes, if they perform retail payment activities for end users in Canada and direct those activities at Canada. Marketing only to test demand doesn't trigger registration, but serving Canadian end users does."),
          ("Is there a minimum size or revenue for RPAA registration?", "No. The Bank's FAQ says every PSP in scope must register for itself, regardless of size and whether or not the business generates revenue.")],
    sources=[("Bank of Canada, Criteria for registering payment service providers", RP_CRIT), ("Bank of Canada, Supervisory policy for online marketplaces", RP_MKT),
             ("Case scenarios: e-commerce web building tools and payment gateways", RP_CS_GATEWAY), ("Case scenarios: remittance service providers", RP_CS_REMIT),
             ("Case scenarios: services backed by cryptocurrencies", RP_CS_CRYPTO), ("Case scenarios: merchants and the incidental payment function", RP_CS_MERCHANT),
             ("Case scenarios: agents and mandataries", RP_CS_AGENTS), ("Case scenarios: geographic scope", RP_CS_GEO),
             ("Refusal or revocation of registration under the RPAA", RP_REFUSE), ("Retail payments supervision FAQ", RP_FAQ),
             ("Retail Payment Activities Act", RP_ACT), ("Retail Payment Activities Regulations", RP_REGS)],
    related=["rpaa-registration-guide.html", "rpaa-vs-fintrac-msb-registration.html", "rpaa-safeguarding-end-user-funds.html"],
)

# ------------------------------------------------------------------ RPAA 2. annual report
GUIDES["rpaa-annual-report.html"] = dict(
    checked="21 October 2026",
    title="RPAA Annual Report for PSPs: Deadline and Contents | AML Canada",
    desc="The RPAA annual report explained: the March 31 deadline, reporting period, what the Bank of Canada asks for, filing in PSP Connect and late-filing penalties.",
    crumb="RPAA annual report",
    h1="The RPAA annual report for payment service providers",
    lede="Every payment service provider that performs retail payment activities in a calendar year must file an annual report with the Bank of Canada by March 31 of the following year. It covers your risk management and incident response framework, safeguarding, activity metrics and financial results.",
    label="Guide · RPAA",
    service="rpaa-compliance-program.html",
    date="2026-10-21",
    takeaways=["File the report in PSP Connect by March 31 for the previous calendar year.",
               "Financial metrics use your most recent financial year-end. Everything else uses the calendar year.",
               "The form asks for monthly figures on held funds and transfers, so collect them as the year goes.",
               "A late report costs $500 a day for up to 30 days, then $15,000 to $1,000,000."],
    sections=[
        ("who-when", "Who files, and when", f"""          <p>Section 21 of the <a href="{RP_ACT}" rel="noopener">Retail Payment Activities Act</a> (RPAA) requires a payment service provider (PSP) that performs retail payment activities to submit an annual report to the Bank of Canada. Under section 18 of the <a href="{RP_REGS}" rel="noopener">Retail Payment Activities Regulations</a>, a PSP that performs retail payment activities in a calendar year must submit the report for that year no later than March 31 of the following year. The report for 2026 is due by March 31, 2027.</p>
          <p>The Bank's <a href="{RP_FAQ}" rel="noopener">FAQ</a> says the first annual report covered 2025. The Bank makes the form available in PSP Connect ahead of the deadline and, according to its <a href="{RP_AR_GUIDE}" rel="noopener">step-by-step guide</a>, notifies PSPs when it's ready to complete. If you aren't yet sure whether you're a PSP at all, start with <a href="who-must-register-psp-rpaa.html">who must register under the RPAA</a>.</p>"""),
        ("period", "The reporting period", f"""          <p>The reporting year is the calendar year (subsection 19(5) of the regulations). Financial metrics are the exception. The Bank's <a href="{RP_AR}" rel="noopener">annual reporting policy</a> says you give your most recent figures based on your financial year-end. The guide's example: if your year ends on June 30, you report financial metrics as at June 30, 2026 in the 2026 report, due by March 31, 2027.</p>
          <p>Financial metrics are reported in Canadian dollars. If your statements are in another currency, you calculate the Canadian dollar equivalent. You may report unaudited figures if the audit for the year won't be finished before the deadline, or if you don't prepare audited statements for any other purpose.</p>"""),
        ("contents", "What the report contains", f"""          <p>Section 19 of the regulations lists the information. In summary:</p>
          <ul>
            <li><strong>Risk management and incident response framework.</strong> Changes made during the year and plans for maintaining the framework; its objectives, reliability targets and indicators; your operational risks and their causes; how you classified assets and business processes; the controls in place; the resources and roles assigned; how approvals were obtained; training; the reviews, testing and independent reviews carried out; and a description of any incidents.</li>
            <li><strong>Safeguarding, if you hold end-user funds.</strong> Who provides your safeguarding account and who regulates them; any other PSP through which you use an account; any insurer or guarantor and the terms of cover; how you safeguard funds; your safeguarding framework; each shortfall found during the year with its root cause and the measures taken; and any independent review. Our <a href="rpaa-safeguarding-end-user-funds.html">safeguarding guide</a> covers these requirements.</li>
            <li><strong>Size and connections.</strong> The maximum value of end-user funds held at any time; for each month, the average end-of-day value of funds held and the number and value of transfers, broken down by currency and for end users in Canada; the number of end users; and the number of other PSPs you served. A PSP without a place of business in Canada reports the Canadian figures.</li>
            <li><strong>Other information.</strong> Significant changes made, activities started or stopped, changes in your use of third-party providers and agents, your record-keeping practices, and financial metrics including revenues, gross and operating profit or loss, assets, liabilities and equity.</li>
          </ul>
          <p>The current form starts by asking you to confirm or update your registration information. It then has six sections: operational risk and incident management, safeguarding, significant changes and incidents, ubiquity and interconnectedness, financial information, and record-keeping. In the incident section you count every incident in the year by type, including those that weren't material enough to report under section 18.</p>"""),
        ("filing", "How it's filed", f"""          <p>You file through PSP Connect, under Reporting, then Annual Reporting. You can save your progress and return later, and the Bank sends a confirmation of receipt once you submit. Its policy says the form may change from year to year, with instructions when the questions change, and the Bank may ask for more information after it reviews your answers. Section 61 of the Act prohibits giving the Bank false or misleading information, and that includes the annual report.</p>"""),
        ("late", "Late or missing reports", f"""          <p>Missing the deadline is a violation. For a violation of section 21, the regulations (section 48) set the penalty at $500 for each day it continues, for up to 30 days. After 30 days the range is $15,000 to $1,000,000. The Bank's <a href="{RP_REMIND}" rel="noopener">June 2026 reminder</a> says PSPs that don't meet reporting requirements may face enforcement action. On June 12, 2026, the Bank <a href="{RP_NOV}" rel="noopener">announced</a> it would start publishing notices of violation and noting them on the PSP's entry in its public registry.</p>"""),
        ("other-reports", "Other reports during the year", f"""          <p>The annual report sits alongside event-driven filings, all made through PSP Connect:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Report</th><th scope="col">When it's needed</th><th scope="col">Timing</th></tr></thead>
            <tbody>
              <tr><th scope="row">Incident notice</th><td>An incident with a material impact on an end user, another PSP or a designated clearing house (RPAA s.18)</td><td>Without delay, and no later than 48 hours after you determine it's material</td></tr>
              <tr><th scope="row">Significant change or new activity</th><td>A change that could reasonably be expected to have a material impact on operational risks or safeguarding, or a new retail payment activity (RPAA s.22)</td><td>At least five business days before</td></tr>
              <tr><th scope="row">Change to registration information</th><td>Changes such as your name, address, structure, agents or third-party providers (RPAA s.59)</td><td>Within 30 days after the change</td></tr>
              <tr><th scope="row">Change to prescribed information</th><td>Information used for the national security review, such as directors and major shareholders (RPAA s.60)</td><td>As soon as feasible, and some changes 30 or 60 days before they take effect</td></tr>
              <tr><th scope="row">Acquisition of control</th><td>Someone plans to acquire control of the PSP (RPAA s.24)</td><td>A new application, and registration under it, before the acquisition</td></tr>
            </tbody>
          </table></div>
          <p>One change can trigger more than one filing. The Bank's policy on <a href="{RP_CHG}" rel="noopener">reporting changes to registration information</a> gives the example of a PSP that starts holding end-user funds and engages a new third-party provider: it files a significant change notice and a change of registration information. Our guide to <a href="rpaa-incident-reporting.html">RPAA incident reporting</a> covers incident notices in detail.</p>"""),
        ("prepare", "Preparing through the year", f"""          <p>Most of the work is collecting information you already produce, in the form the Bank asks for. A few habits make March easier:</p>
          <ul>
            <li>Record held funds and transfer volumes and values each month, split by currency and between end users in Canada and elsewhere.</li>
            <li>Log every incident, material or not, with its type.</li>
            <li>Keep a shortfall log if you hold end-user funds, with the root cause and fix for each one.</li>
            <li>Date your framework approvals. The regulations require your senior officer and board, if you have one, to approve the risk management and incident response framework at least once a year (section 5).</li>
            <li>Keep the record of each review and test. The regulations also require records sufficient to show you comply (section 40).</li>
          </ul>
          <p>Our <a href="rpaa-compliance-program.html">RPAA compliance program</a> includes a framework for the annual report and change notices, and outsourced compliance officer hours can cover preparing the report itself.</p>"""),
    ],
    faqs=[("When is the RPAA annual report due?", "By March 31 of the year after the reporting year. The report for 2026 is due by March 31, 2027."),
          ("What period does the RPAA annual report cover?", "The previous calendar year. Financial metrics are the exception: you report them as at your most recent financial year-end."),
          ("Do I have to file if I don't hold end-user funds?", "Yes, if you performed retail payment activities during the year. The safeguarding information applies only to PSPs that hold end-user funds."),
          ("What happens if a PSP files its annual report late?", "It's a violation. The penalty is $500 a day for up to 30 days, then $15,000 to $1,000,000, and the Bank has said it will publish notices of violation."),
          ("Do the financial figures have to be audited?", "No, not in every case. You may report unaudited figures if your audit won't be finished before the deadline or if you don't prepare audited statements for any other purpose.")],
    sources=[("Retail Payment Activities Act", RP_ACT), ("Retail Payment Activities Regulations", RP_REGS),
             ("Bank of Canada, Annual reporting (supervisory policy)", RP_AR), ("Bank of Canada, How to complete an annual report: A step-by-step guide", RP_AR_GUIDE),
             ("Bank of Canada, Reminder: PSP reporting obligations under the RPAA", RP_REMIND), ("Bank of Canada, Reporting changes to registration information", RP_CHG),
             ("Bank of Canada, Publishing notices of violation", RP_NOV), ("Retail payments supervision FAQ", RP_FAQ)],
    related=["rpaa-incident-reporting.html", "rpaa-safeguarding-end-user-funds.html", "rpaa-registration-guide.html"],
)

# ------------------------------------------------------------------ RPAA 3. RPAA vs FINTRAC MSB registration
GUIDES["rpaa-vs-fintrac-msb-registration.html"] = dict(
    checked="21 October 2026",
    title="RPAA vs FINTRAC MSB Registration: Do You Need Both? | AML Canada",
    desc="RPAA vs FINTRAC MSB registration compared: regulators, who must register, obligations and penalties, which business models need both, and the order to apply in.",
    crumb="RPAA vs FINTRAC",
    h1="RPAA vs FINTRAC MSB registration: do you need both?",
    lede="Payment service providers register with the Bank of Canada under the RPAA. Money services businesses register with FINTRAC under the PCMLTFA. Many payment businesses are both, and the two registrations are linked: the Bank shares your application with FINTRAC and can refuse it based on what FINTRAC reports.",
    label="Guide · RPAA",
    service="rpaa-registration.html",
    also=["msb-registration.html"],
    date="2026-10-21",
    takeaways=["The RPAA deals with operational risk and safeguarding. The PCMLTFA deals with money laundering and terrorist financing.",
               "A remittance business is usually both a PSP and an MSB. A crypto-only exchange or a cash currency counter can be an MSB without being a PSP.",
               "The Bank sends your application details to FINTRAC, and FINTRAC reports back within 30 days.",
               "If you're an MSB, put the FINTRAC registration in place first or alongside the Bank application."],
    sections=[
        ("two-regimes", "Two laws, two regulators", f"""          <p>The <a href="{RP_ACT}" rel="noopener">Retail Payment Activities Act</a> (RPAA) gives the Bank of Canada the job of supervising payment service providers (PSPs) to check they comply with the Act. Its focus is operational risk, incident response and the safeguarding of end users' funds. The <a href="{RP_PCMLTFA}" rel="noopener">Proceeds of Crime (Money Laundering) and Terrorist Financing Act</a> (PCMLTFA) is Canada's anti-money laundering law, and FINTRAC supervises the businesses it covers, including money services businesses (MSBs).</p>
          <p>The tests are different. You're a PSP because of the payment functions you perform. You're an MSB because of the money services you provide. One business can meet both tests, one test or neither. The Bank's own registration guide says applicants must register with FINTRAC if they are considered an MSB.</p>"""),
        ("compare", "Side-by-side comparison", f"""          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Aspect</th><th scope="col">RPAA (PSP)</th><th scope="col">FINTRAC (MSB)</th></tr></thead>
            <tbody>
              <tr><th scope="row">Regulator</th><td>Bank of Canada</td><td>FINTRAC</td></tr>
              <tr><th scope="row">Law</th><td>Retail Payment Activities Act and its regulations</td><td>PCMLTFA and its regulations</td></tr>
              <tr><th scope="row">Who</th><td>Businesses that perform payment functions for end users as a distinct business, for electronic transfers in Canadian or foreign currency, with a link to Canada. See <a href="who-must-register-psp-rpaa.html">who must register as a PSP</a></td><td>Businesses providing foreign exchange dealing, remitting or transmitting funds, transporting currency or negotiable instruments, issuing or redeeming money orders and similar instruments, dealing in virtual currencies, acquirer services for private ATMs, or a prescribed service (PCMLTFA 5(h)), including foreign MSBs serving Canada (5(h.1))</td></tr>
              <tr><th scope="row">Timing</th><td>Registered before performing any retail payment activities (s.23)</td><td>Registration required (s.11.1), renewed every two years (s.11.19)</td></tr>
              <tr><th scope="row">Fees</th><td>One-time, non-refundable <a href="{RP_FEE}" rel="noopener">application fee</a>, $2,500 from November 1, 2024, indexed each January</td><td>See our <a href="msb-registration-cost-canada.html">MSB registration cost guide</a></td></tr>
              <tr><th scope="row">Main ongoing obligations</th><td>Risk management and incident response framework, incident notices, safeguarding if you hold funds, annual report, change notices</td><td>Compliance program (s.9.6), suspicious transaction reports (s.7) and the other <a href="fintrac-reporting-requirements.html">FINTRAC reports</a>, record keeping (s.6) and identity verification (s.6.1)</td></tr>
              <tr><th scope="row">Penalties</th><td>Up to $1,000,000 for a serious violation and $10,000,000 for a very serious one. Late reports and notices: $500 a day for up to 30 days, then $15,000 to $1,000,000</td><td>Up to $40,000 for a minor violation, $4,000,000 for a serious one and $20,000,000 for a very serious one, subject to caps in s.73.1 of the Act. Failing to register is a serious violation</td></tr>
            </tbody>
          </table></div>
          <p>The RPAA figures come from section 48 of the <a href="{RP_REGS}" rel="noopener">Retail Payment Activities Regulations</a>. The FINTRAC ranges come from section 5 of the <a href="{RP_AMP}" rel="noopener">PCMLTFA Administrative Monetary Penalties Regulations</a>, as amended in 2026. For an individual, the Act caps a single violation at $4,000,000.</p>"""),
        ("models", "Which business models need both", f"""          <p>The Bank's published case scenarios, read with the MSB services listed in the PCMLTFA, show how common models fall:</p>
          <ul>
            <li><strong>Money transfer and remittance apps.</strong> The Bank treats a money transfer operator as a PSP, and one that also offers a multi-currency wallet holds funds as well (<a href="{RP_CS_REMIT}" rel="noopener">remittance scenarios</a>). Remitting or transmitting funds is also an MSB service. Expect to need both.</li>
            <li><strong>Crypto-backed payment cards.</strong> The Bank's <a href="{RP_CS_CRYPTO}" rel="noopener">crypto scenarios</a> treat a crypto-backed prepaid card that earns interchange fees as a PSP. Dealing in virtual currencies is an MSB service. Expect to need both.</li>
            <li><strong>Crypto-only exchanges.</strong> The Bank says an exchange dealing only in cryptocurrency performs no retail payment activity. Dealing in virtual currencies still makes it an MSB. FINTRAC only. Our <a href="crypto-registration-canada.html">crypto registration guide</a> covers that side.</li>
            <li><strong>Cash currency exchange counters.</strong> The Bank's example of a business exchanging currency for cash isn't a PSP, because no electronic transfer is involved. Foreign exchange dealing is an MSB service. FINTRAC only.</li>
            <li><strong>Payment gateways and marketplaces.</strong> These can be PSPs without moving money in the way a remitter does. Whether they're also MSBs depends on what they do with funds, so check the FINTRAC side separately.</li>
          </ul>"""),
        ("sharing", "How the Bank and FINTRAC share information", f"""          <p>The link between the two registrations is written into both Acts:</p>
          <ul>
            <li>The Bank's application asks whether you're registered with FINTRAC (RPAA paragraph 29(1)(l)). Its <a href="{RP_REG_GUIDE}" rel="noopener">step-by-step guide</a> asks for your FINTRAC registration number and issue date.</li>
            <li>Once the Bank considers your application complete, it sends FINTRAC your name, address, structure, agents and description of activities (RPAA section 31).</li>
            <li>Within 30 days, FINTRAC must tell the Bank if, in the past five years, you were found guilty of certain PCMLTFA offences or served with a decision or penalty for a serious or very serious violation, or if you aren't registered under the PCMLTFA (PCMLTFA section 53.6).</li>
            <li>After registration, FINTRAC tells the Bank if it revokes your FINTRAC registration or penalizes you for a serious or very serious violation, and it may share other compliance information relevant to the Bank's role (sections 53.6 and 65.03).</li>
          </ul>
          <p>On the Bank's side, these are grounds to refuse or revoke. The RPAA lets the Bank refuse an applicant that has such a conviction or penalty, or that isn't registered in accordance with section 11.1 of the PCMLTFA (section 48). The same matters are grounds to revoke an existing registration (section 52). The Bank's <a href="{RP_FW}" rel="noopener">supervisory framework</a> states that it can refuse or revoke registration based on information provided by FINTRAC.</p>"""),
        ("order", "Order of operations", """          <p>For a business that needs both, a sensible sequence is:</p>
          <ol>
            <li><strong>Map your activities against both tests.</strong> List each product and the payment functions and money services it involves.</li>
            <li><strong>Put your FINTRAC registration in place first, or file both together.</strong> The Bank asks for your FINTRAC number, and FINTRAC reports to the Bank if you aren't registered.</li>
            <li><strong>Deal with any open FINTRAC issues.</strong> A serious or very serious violation in the past five years is a refusal ground under the RPAA.</li>
            <li><strong>Prepare the Bank application.</strong> Describe the same business in the same way in both, since the Bank passes your application details to FINTRAC.</li>
            <li><strong>Keep both registrations current.</strong> Report changes to each regulator on its own timeline, and renew with FINTRAC every two years.</li>
          </ol>
          <p>Our <a href="msb-registration.html">MSB registration</a> and <a href="rpaa-registration.html">RPAA registration</a> services can be run together, and our guide to <a href="how-to-register-msb-canada.html">registering an MSB with FINTRAC</a> covers the FINTRAC application step by step.</p>"""),
    ],
    faqs=[("What is the difference between a PSP and an MSB in Canada?", "A payment service provider performs payment functions and registers with the Bank of Canada under the RPAA. A money services business provides money services, such as remitting funds or dealing in virtual currencies, and registers with FINTRAC under the PCMLTFA. One business can be both."),
          ("Does RPAA registration replace FINTRAC registration?", "No. They're separate registrations under separate laws. The Bank asks for your FINTRAC registration details in its application."),
          ("Can the Bank of Canada refuse my application because of FINTRAC?", "Yes. The RPAA lets the Bank refuse an applicant that isn't registered under section 11.1 of the PCMLTFA, or that has certain PCMLTFA convictions or serious or very serious violations in the past five years."),
          ("Should I register with FINTRAC or the Bank of Canada first?", "If you're an MSB, have the FINTRAC registration in place first or file both together, because the Bank asks for your FINTRAC number and FINTRAC reports to the Bank if you aren't registered."),
          ("Does a crypto exchange need both registrations?", "Not always. In the Bank's example, an exchange dealing only in cryptocurrency isn't a PSP, but dealing in virtual currencies makes it an MSB. A crypto-backed payment card is a PSP in the Bank's example.")],
    sources=[("Retail Payment Activities Act", RP_ACT), ("Retail Payment Activities Regulations", RP_REGS),
             ("Proceeds of Crime (Money Laundering) and Terrorist Financing Act", RP_PCMLTFA), ("PCMLTFA Administrative Monetary Penalties Regulations", RP_AMP),
             ("Bank of Canada, Supervisory framework", RP_FW), ("Bank of Canada, How to complete a registration application", RP_REG_GUIDE),
             ("Bank of Canada, Registration application fee", RP_FEE), ("Case scenarios: remittance service providers", RP_CS_REMIT),
             ("Case scenarios: services backed by cryptocurrencies", RP_CS_CRYPTO)],
    related=["who-must-register-psp-rpaa.html", "how-to-register-msb-canada.html", "fintrac-compliance-program-requirements.html"],
)

# ------------------------------------------------------------------ RPAA 4. incident reporting
GUIDES["rpaa-incident-reporting.html"] = dict(
    checked="21 October 2026",
    title="RPAA Incident Reporting: The 48-Hour Rule | AML Canada",
    desc="RPAA incident reporting explained: what counts as a material incident, the 48-hour deadline, initial, interim and final notices, and how to notify end users.",
    crumb="RPAA incident reporting",
    h1="RPAA incident reporting and the 48-hour rule",
    lede="When a payment service provider becomes aware of an incident with a material impact, it must notify the Bank of Canada and the affected end users, payment service providers and clearing houses without delay. The Bank expects the first notice no later than 48 hours after the provider decides the incident is material.",
    label="Guide · RPAA",
    service="rpaa-compliance-program.html",
    date="2026-10-21",
    takeaways=["Only incidents with a material impact are reported, but every incident must be investigated and documented.",
               "The 48 hours run from when you determine an incident is material, not from when it started.",
               "File an initial notice and a final notice in PSP Connect, with interim notices as things develop.",
               "Notify affected end users directly. A social media post alone isn't enough."],
    sections=[
        ("law", "What the law requires", f"""          <p>Section 18 of the <a href="{RP_ACT}" rel="noopener">Retail Payment Activities Act</a> (RPAA) says that if a payment service provider (PSP) becomes aware of an incident that has a material impact on an end user, another PSP or a designated clearing house, it must, without delay, notify that individual or entity and the Bank of Canada. The other PSP doesn't have to be one the RPAA applies to. Sections 11 and 12 of the <a href="{RP_REGS}" rel="noopener">Retail Payment Activities Regulations</a> set out the form and content of the notices. The Bank can also order a PSP to give follow-up notices (RPAA section 19).</p>
          <p>The Bank explains how it expects PSPs to comply in its <a href="{RP_INC}" rel="noopener">Incident notification guideline</a> (October 2024) and its <a href="{RP_INC_GUIDE}" rel="noopener">step-by-step guide</a> to the notice form (May 2025).</p>"""),
        ("incident", "What counts as an incident", """          <p>The Act defines an incident as an unplanned event, or series of related events, that results in, or could reasonably be expected to result in, the reduction, deterioration or breakdown of any retail payment activity the PSP performs. The Bank reads this to include any negative impact on the confidentiality, integrity or availability of your retail payment activities, or of the systems, data and information behind them.</p>
          <p>Incidents at your agents, mandataries and third-party service providers count, as do incidents they detect. If one of them has a material impact, you report it.</p>"""),
        ("material", "When an incident has a material impact", f"""          <p>Only material incidents are reportable under section 18. The guideline leaves the judgment to you, based on your business model, the services you offer and other relevant factors. It gives examples, which it says aren't exhaustive:</p>
          <ul>
            <li><strong>Lost funds.</strong> Any amount of an end user's held funds becomes unrecoverably lost or permanently unavailable, for example through theft or a system flaw at the PSP, or because the institution holding the funds fails. Losses caused by the end user's own actions, such as authorized fraud, are not included.</li>
            <li><strong>Outages.</strong> An outage that materially affects the availability of your retail payment activities, such as one caused by a technology failure, loss of a data centre, hosting or third party, or a cyber attack.</li>
            <li><strong>Insolvency.</strong> The PSP becomes subject to an insolvency event listed in the regulations.</li>
            <li><strong>Confidentiality breaches.</strong> Unauthorized access to or disclosure of confidential information that creates a real risk of significant harm, such as financial loss, identity theft, damage to reputation or bodily harm. This covers more than personal information. Weigh how sensitive the information is and how likely it is to be misused.</li>
            <li><strong>Integrity failures.</strong> A compromised ledger or transaction records, a payee receiving a different amount than the payer sent, funds routed to the wrong account, misdirected instructions, or errors in clearing or settlement.</li>
          </ul>
          <p>Incidents that aren't material don't need a section 18 notice. You still have to investigate, respond to and document every incident, and the Bank may ask about them. Your annual report also counts all incidents by type. See our guide to the <a href="rpaa-annual-report.html">RPAA annual report</a>.</p>"""),
        ("clock", "The 48-hour clock", f"""          <p>The guideline sets the deadline as without delay, but no later than 48 hours after the PSP determines the incident is material. The Bank's <a href="{RP_REMIND}" rel="noopener">June 2026 reminder</a> repeats it. If an incident starts out below the threshold and gets worse, the 48 hours run from the point you determine it has become material.</p>
          <p>The notice form asks separately when the incident started, when it was detected and when you became aware it was material. Record all three as they happen. Build your escalation process so that someone with authority makes the materiality decision promptly, since the duty is to notify without delay.</p>"""),
        ("bank", "Notifying the Bank: initial, interim and final notices", """          <p>Notices go to the Bank through PSP Connect, under Reporting, then Incident. The guideline describes three kinds:</p>
          <ul>
            <li><strong>Initial notice</strong>, within the 48 hours, for every material incident.</li>
            <li><strong>Interim notices</strong>, when there are significant developments or useful updates. You can file more than one.</li>
            <li><strong>Final notice</strong>, once the incident is resolved and the root cause is known.</li>
          </ul>
          <p>If the incident is resolved and you have everything, including the root cause, within the 48 hours, one notice can serve as both initial and final. If your systems are so degraded that you can't file online, the Bank accepts notices by phone in exceptional circumstances.</p>
          <p>Under section 11 of the regulations, the notice must give your name and a contact person, a description of the incident and its material impact, and the measures you've taken. The guideline expects dates and times for start, detection, the materiality decision and resolution; how the incident was detected; which retail payment activities were affected; the actual or estimated impact, such as the number of people affected; the impact on systems and data; and the root cause analysis.</p>"""),
        ("others", "Notifying end users, other PSPs and clearing houses", """          <p>Section 12 of the regulations requires you to notify each materially affected individual or entity using the most recent contact information they gave you. If you don't have contact details for everyone affected, you post the notice on your website. The guideline expects these notices within the same 48 hours.</p>
          <ul>
            <li>Email, text message or your app are suitable. A post on social media isn't, although you can use social media as well.</li>
            <li>The notice gives your name, a description of the incident with when it began, its impact on the person notified, and any steps they can take, such as changing a password.</li>
            <li>If an incident at PSP A affects PSP B, A notifies B and its own affected users, and B then notifies its users if the incident is material for them.</li>
            <li>If notifying users within 48 hours could increase the risk of harm or the incident, or isn't feasible, tell the Bank through the incident template. The Bank expects this to be rare.</li>
          </ul>"""),
        ("overlaps", "Privacy law and clearing house rules", """          <p>A breach that is reportable under privacy law is still reportable to the Bank under the RPAA. You can send affected people a single notice if it meets the requirements of every law that applies. Members of clearing and settlement systems may also have reporting duties under the system's rules. Meeting one set of obligations doesn't satisfy the other, and all material incidents still go to the Bank.</p>"""),
        ("after", "After the notice", f"""          <p>The Bank can order follow-up notices, setting who receives them, when, and what they say. It can also send an information request. Normally you have 15 days to answer, but for an ongoing incident that could have a significant adverse impact on end users, other PSPs or certain clearing houses, the regulations allow only 24 hours (section 43).</p>
          <p>The notices depend on your risk management and incident response framework, which must allocate roles for detecting, responding to and recovering from incidents. Our <a href="rpaa-compliance-program.html">RPAA compliance program</a> includes an incident response framework with escalation steps, a materiality assessment and notice templates. If you hold end-user funds, read it with our <a href="rpaa-safeguarding-end-user-funds.html">safeguarding guide</a>, since lost or inaccessible funds are a material incident.</p>"""),
    ],
    faqs=[("How long does a PSP have to report an incident to the Bank of Canada?", "Without delay, and no later than 48 hours after it determines that the incident has a material impact on an end user, another PSP or a designated clearing house."),
          ("Do all incidents have to be reported under the RPAA?", "No. Only incidents with a material impact need a section 18 notice. Every incident must still be investigated, responded to and documented, and all incidents are counted in the annual report."),
          ("How do you submit an RPAA incident notice?", "Through PSP Connect, using the Bank's incident notice form. You file an initial notice, interim notices as needed, and a final notice once the incident is resolved and the root cause is known."),
          ("Does a PSP have to tell customers about an incident?", "Yes, if they're materially affected. Notify them directly using their latest contact details, or post a notice on your website if you don't have contact details for everyone."),
          ("Do incidents at a third-party provider count?", "Yes. Incidents that occur at or are detected by your agents, mandataries or third-party service providers are reportable if they have a material impact.")],
    sources=[("Retail Payment Activities Act", RP_ACT), ("Retail Payment Activities Regulations", RP_REGS),
             ("Bank of Canada, Incident notification guideline (October 2024)", RP_INC), ("Bank of Canada, How to complete an incident notice: A step-by-step guide", RP_INC_GUIDE),
             ("Bank of Canada, Reminder: PSP reporting obligations under the RPAA", RP_REMIND)],
    related=["rpaa-annual-report.html", "rpaa-safeguarding-end-user-funds.html", "who-must-register-psp-rpaa.html"],
)

# ------------------------------------------------------------------ Ontario vs B.C. for crypto MSBs
GUIDES["ontario-vs-bc-msb-registration.html"] = dict(
    checked="22 October 2026",
    title="Ontario vs B.C. MSB Registration for Crypto | AML Canada",
    desc="Ontario vs B.C. MSB registration for crypto startups: why both are FINTRAC-only today, what B.C.'s MSB Act will add, and how to choose.",
    crumb="Ontario vs B.C.",
    h1="Ontario vs B.C. MSB registration: which province suits a crypto startup?",
    lede="Today there's no MSB difference between the two provinces. A money services business in Ontario or British Columbia registers with FINTRAC and nobody else, because B.C.'s Money Services Businesses Act has been passed but isn't in force. That should change: B.C. plans to start provincial registration, and Ontario has no equivalent law.",
    label="Guide · Virtual currency",
    service="msb-registration.html",
    also=["compliance-programs.html"],
    date="2026-10-22",
    takeaways=["For AML purposes, Ontario and B.C. MSBs both register with FINTRAC only, for now.",
               "B.C.'s Money Services Businesses Act received Royal Assent in 2023 and is still not in force. BCFSA's plan targets 2027/28.",
               "The B.C. Act names foreign exchange and remittance. Virtual currency isn't named, so regulations will decide whether crypto-only businesses are covered.",
               "Securities rules for crypto trading platforms follow your clients, so your head office won't keep you out of another province's rules."],
    sections=[
        ("today", "What applies in each province today", f"""          <p>Founders often hear that B.C. already makes crypto businesses register twice, once with FINTRAC and once with the province. It doesn't. As of October 2026, <a href="{BC_MSBA}" rel="noopener">BC Laws</a> shows every operative section of the Money Services Businesses Act as not in force. A crypto MSB with its head office in Vancouver deals with the same AML regulator as one in Toronto.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Question</th><th scope="col">Ontario</th><th scope="col">British Columbia</th></tr></thead>
            <tbody>
              <tr><th scope="row">AML registration as an MSB</th><td>FINTRAC</td><td>FINTRAC</td></tr>
              <tr><th scope="row">Provincial MSB law</th><td>None</td><td>Money Services Businesses Act, SBC 2023, c. 19. Passed, not in force</td></tr>
              <tr><th scope="row">Who would run provincial registration</th><td>Not applicable</td><td>BC Financial Services Authority (BCFSA)</td></tr>
              <tr><th scope="row">Securities regulator for crypto trading platforms with clients in the province</th><td>Ontario Securities Commission (OSC)</td><td>British Columbia Securities Commission (BCSC)</td></tr>
              <tr><th scope="row">Expected change</th><td>None announced</td><td>BCFSA's service plan targets implementation in 2027/28, subject to government direction</td></tr>
            </tbody>
          </table></div>
          <p>BCFSA and the BCSC are different bodies. BCFSA would administer the new MSB registration. The BCSC is B.C.'s securities regulator and already oversees crypto trading platforms with B.C. clients. For the federal side, see our guide to <a href="crypto-registration-canada.html">crypto registration with FINTRAC</a>.</p>"""),
        ("bc-act", "What B.C.'s Money Services Businesses Act will do", f"""          <p>The Act received Royal Assent on May 11, 2023. Section 66 says it comes into force by regulation, and no regulation has done that yet. BCFSA's <a href="{BCFSA_SP}" rel="noopener">2026/27 to 2028/29 service plan</a> sets the targets, subject to government direction: finish implementation readiness, including registration, education and compliance components, in 2026/27, then implement the Act in 2027/28.</p>
          <p>Once it's in force, the <a href="{BC_BILL19}" rel="noopener">text of the Act</a> says:</p>
          <ul>
            <li><strong>Registration.</strong> A person must not carry on the business of providing money services unless registered or exempt (section 5). Banks, insurers and some other institutions are exempt (section 6).</li>
            <li><strong>What counts.</strong> "Money services" means foreign exchange dealing, remitting or transmitting funds by any means, issuing or redeeming money orders, traveller's cheques and similar instruments, and any service added by regulation (section 1).</li>
            <li><strong>Fitness.</strong> The superintendent can refuse an applicant found unfit, for example one that has been refused registration, or had a registration cancelled, under money services or securities legislation in B.C. or another jurisdiction.</li>
            <li><strong>Investigations.</strong> During an investigation, the superintendent can inspect and copy records at the business's premises and compel people to answer questions.</li>
            <li><strong>Penalties.</strong> Administrative penalties of up to $100,000 (section 34). Offences carry fines of up to $200,000, and an individual can also face up to 2 years in prison (section 42).</li>
          </ul>
          <p>Fees, capital rules, reporting forms and the full list of covered services will be set by regulations that haven't been published, so there are no B.C. capital or bond requirements to quote yet.</p>"""),
        ("crypto", "Will B.C. cover crypto businesses?", """          <p>Not on the face of the Act. Unlike the federal law, which lists dealing in virtual currencies as a money service, B.C.'s definition doesn't mention virtual currency. It can be added by regulation, so a crypto-only business won't know where it stands until the regulations appear.</p>
          <p>Many crypto businesses also do things the Act does name. If you convert client funds between Canadian dollars and other currencies, or send fiat payouts, you may be dealing in foreign exchange or remitting funds. Map each product against the B.C. definition as well as the federal one.</p>
          <p>A crypto firm's record with securities regulators could also affect a future B.C. application, because the fitness test looks at refusals and cancellations under securities legislation in any jurisdiction.</p>"""),
        ("securities", "Securities rules follow your clients", f"""          <p>For crypto trading platforms, picking a head office doesn't decide which securities rules apply. Under <a href="{CSA_21_332}" rel="noopener">CSA Staff Notice 21-332</a>, a platform operating in Canada is expected to register with the securities regulators, or file a pre-registration undertaking while it seeks registration. If your clients live in Ontario and B.C., both provinces' securities laws are relevant, wherever you're incorporated. Platforms that offer stablecoins are expected to follow <a href="{CSA_21_333}" rel="noopener">CSA Staff Notice 21-333</a>.</p>
          <p>Firms registering in several provinces don't file a separate application with each. <a href="{NP_11_204}" rel="noopener">National Policy 11-204</a> sets out a process where one principal regulator coordinates the registration. That's a practical reason to think about where your head office sits, but it doesn't take you outside any province's rules.</p>"""),
        ("choose", "How to choose", """          <p>Since the AML side is the same today, base the decision on the business. Go through these points:</p>
          <ol>
            <li><strong>Where are your clients?</strong> Securities rules, and possibly B.C.'s MSB Act, depend on where you do business, not only where you're incorporated.</li>
            <li><strong>Do you touch fiat?</strong> Foreign exchange and remittance are named in the B.C. Act. A B.C. business doing either should plan for BCFSA registration once the regime starts.</li>
            <li><strong>Are you crypto-only?</strong> Watch for B.C. regulations that could add virtual currency to the definition.</li>
            <li><strong>Where are your people, banks and investors?</strong> Talent, banking relationships and investor expectations usually matter more, since the regulatory gap is nil today.</li>
            <li><strong>Will you serve Quebec?</strong> Quebec already licenses money-services businesses through Revenu Québec, separately from FINTRAC.</li>
          </ol>
          <p>An Ontario base may avoid a second provincial registration later, which matters most for a business doing fiat FX or remittance, though how far the B.C. Act reaches businesses outside the province is still unknown. A B.C. base costs nothing extra today. Either way, the work that decides whether you get and keep a FINTRAC registration is the same: an accurate <a href="how-to-register-msb-canada.html">MSB application</a> and a <a href="fintrac-compliance-program-requirements.html">compliance program</a> written for crypto risks. If you're based abroad, our guide to <a href="foreign-msb-registration-canada.html">foreign MSB registration</a> covers that route.</p>"""),
    ],
    faqs=[("Do I need a BCFSA MSB licence in B.C. today?", "No. B.C.'s Money Services Businesses Act was passed in 2023 but isn't in force, so a B.C. money services business currently registers with FINTRAC only."),
          ("When will B.C.'s MSB registration start?", "No date has been set by regulation. BCFSA's 2026/27 to 2028/29 service plan targets implementation in 2027/28, subject to government direction."),
          ("Will B.C.'s MSB Act apply to crypto businesses?", "The Act doesn't name virtual currency. It covers foreign exchange dealing, remittance and money orders, plus services added by regulation, so crypto-only businesses depend on future regulations. Crypto firms that also handle fiat FX or remittance may be covered."),
          ("Is Ontario better than B.C. for a crypto startup?", "For MSB registration there's no difference today: both are FINTRAC-only. Ontario has no plan for provincial MSB registration, while B.C. does, so a business doing fiat FX or remittance avoids a possible second registration in Ontario."),
          ("If my company is in Ontario, can I ignore B.C. rules?", "Not for securities. Crypto trading platforms deal with the securities regulators where their clients are. How far B.C.'s MSB Act will reach outside the province will be clearer once it and its regulations are in force.")],
    sources=[("BC Laws, Money Services Businesses Act, SBC 2023, c. 19", BC_MSBA), ("Bill 19, Money Services Businesses Act, third reading text", BC_BILL19),
             ("BCFSA 2026/27 to 2028/29 Service Plan", BCFSA_SP), ("FINTRAC, Money services businesses", F_MSB),
             ("CSA Staff Notice 21-332", CSA_21_332), ("CSA Staff Notice 21-333", CSA_21_333),
             ("National Policy 11-204, Process for Registration in Multiple Jurisdictions", NP_11_204),
             ("Revenu Québec, Money-services business licence", RQ_MSB)],
    related=["crypto-registration-canada.html", "how-to-register-msb-canada.html", "foreign-msb-registration-canada.html"],
)


# Dated posts (Latest updates) render with the same template; newest first.
from posts_v3 import POSTS  # noqa: E402

for _k, _v in POSTS.items():
    _v.setdefault("kind", "update")
GUIDES = {**POSTS, **GUIDES}
# Newest first everywhere guides are listed; same-day guides keep newest-added first.
# ------------------------------------------------------------------ 25. MSB licence in Canada (2026-10-25)
F_PUBLIC_MSB = "https://fintrac-canafe.canada.ca/public/businesses-entreprises-eng"
GUIDES["msb-licence-canada.html"] = dict(
    modified="2026-10-25",
    checked="25 October 2026",
    title="MSB Licence in Canada: What FINTRAC Registration Is | AML Canada",
    desc="Is there an MSB licence in Canada? FINTRAC registers money services businesses but doesn't license them. What that means, and where licences do apply.",
    crumb="MSB licence in Canada",
    h1="MSB licence in Canada: what FINTRAC registration really is",
    lede="People search for a Canadian \"MSB licence\". What FINTRAC actually gives a money services business is a registration, and the difference matters when you buy, bank or advertise one.",
    label="Guide · MSB registration",
    service="msb-registration.html",
    also=["buy-or-register-msb-canada.html"],
    takeaways=["FINTRAC registers MSBs. It doesn't issue licences or certificates.",
               "Registration is valid for two years and changes are reported within 30 days.",
               "Quebec licenses MSBs separately, and PSPs may also register with the Bank of Canada.",
               "Registration isn't an endorsement and doesn't come with banking."],
    sections=[
        ("answer", "The short answer", f"""          <p>Canada has no federal MSB licence. A money services business registers with FINTRAC before it starts operating, and FINTRAC lists it on its public <a href="{F_MSB_REGISTRY}" rel="noopener">MSB registry</a>. FINTRAC says registration \"does not indicate that FINTRAC endorses or licenses the business\" and only shows that the business has met the legal requirements to register. It also says it doesn't issue licences or certificates of registration.</p>
          <p>\"MSB licence\" is still the phrase most people use, including banks and payment partners. When they say it, they usually mean an active FINTRAC registration for the services the business offers.</p>"""),
        ("who", "Who has to register", f"""          <p>A business that offers any of these services to the public in Canada must register with FINTRAC before it begins, and a business abroad that directs and provides them to people in Canada registers as a <a href="foreign-msb-registration-canada.html">foreign MSB</a>:</p>
{MSB_ACTIVITIES}
          <p>FINTRAC says that even a business already registered or licensed as an MSB elsewhere must still register with FINTRAC. See <a href="{F_MSB}" rel="noopener">FINTRAC's MSB page</a>.</p>"""),
        ("means", "What a registration gives you, and what it doesn't", """          <div class="table-wrap"><table>
            <thead><tr><th scope="col">A FINTRAC registration</th><th scope="col">Means</th></tr></thead>
            <tbody>
              <tr><th scope="row">Is</th><td>Your legal permission to offer the registered money services, once FINTRAC has accepted your application, and a public listing on the MSB registry</td></tr>
              <tr><th scope="row">Lasts</th><td>Two years. You must renew before it expires</td></tr>
              <tr><th scope="row">Requires</th><td>Updates within 30 days when your registration information changes, and a compliance program, compliance officer, reporting and record keeping from the day you operate</td></tr>
              <tr><th scope="row">Isn't</th><td>A licence, a certificate or an endorsement by FINTRAC</td></tr>
              <tr><th scope="row">Doesn't include</th><td>A bank account or payment partners. They make their own decisions</td></tr>
            </tbody>
          </table></div>"""),
        ("licences", "Where licences and other registrations do apply", f"""          <ul>
            <li><strong>Quebec.</strong> Money-services businesses operating in Quebec also need a licence from <a href="{RQ_MSB}" rel="noopener">Revenu Québec</a>, on top of FINTRAC registration.</li>
            <li><strong>Payment service providers.</strong> A business that holds funds for users or transfers funds at their request may also have to register with the Bank of Canada under the <a href="{L_RPAA}" rel="noopener">Retail Payment Activities Act</a>. See <a href="rpaa-vs-fintrac-msb-registration.html">RPAA vs FINTRAC MSB registration</a>.</li>
            <li><strong>Crypto trading platforms.</strong> These also deal with provincial securities regulators. See <a href="crypto-registration-canada.html">crypto registration in Canada</a>.</li>
            <li><strong>British Columbia.</strong> B.C. has passed a Money Services Businesses Act that isn't in force yet. See <a href="ontario-vs-bc-msb-registration.html">Ontario vs B.C.</a></li>
          </ul>"""),
        ("get", "How to get registered", """          <p>You prepare the business information FINTRAC asks for, including the services, owners, directors and compliance officer, gather criminal record checks for the people FINTRAC names, and apply online. FINTRAC says most complete applications are processed within three months. In our experience it has taken from about a week to seven months. FINTRAC charges nothing to register. Our fee to prepare and submit it is a fixed US$3,500. The full steps are in <a href="how-to-register-msb-canada.html">how to register an MSB in Canada</a>.</p>
          <p>The other route is to buy a company that's already registered. See <a href="buy-or-register-msb-canada.html">buy or register an MSB</a> and the companies on <a href="msb-for-sale.html#available">MSB for sale</a>.</p>"""),
        ("advertising", "Describing your registration accurately", f"""          <p>Because registration isn't an endorsement, don't present it as one in your marketing or in what you tell clients and partners. Say that the business is registered with FINTRAC as a money services business and give the registration number, which anyone can check on the registry. FINTRAC also has a <a href="{F_PUBLIC_MSB}" rel="noopener">page for the public</a> on dealing with MSBs.</p>"""),
    ],
    faqs=[("Is there an MSB licence in Canada?", "Not federally. FINTRAC registers money services businesses and says it doesn't issue licences or certificates. Quebec separately licenses money-services businesses through Revenu Québec."),
          ("How long is a FINTRAC MSB registration valid?", "Two years. You must renew it before it expires, and report changes to your registration information within 30 days."),
          ("How much does an MSB licence cost in Canada?", "FINTRAC charges nothing to register. Our fixed fee to prepare and submit a registration is US$3,500. Registered companies for sale start from €28,000."),
          ("Does FINTRAC registration mean the business is approved?", "It means the business met the legal requirements to register. FINTRAC says registration doesn't mean it endorses or licenses the business."),
          ("Do I need a licence from the Bank of Canada too?", "If you hold funds for users or transfer funds at their request, you may need to register as a payment service provider under the RPAA. That's a registration, separate from FINTRAC's.")],
    sources=[("FINTRAC, Money Services Business Registry", F_MSB_REGISTRY), ("FINTRAC, Money services businesses", F_MSB), ("Register your MSB or FMSB", F_REG),
             ("Update, renew or cancel your registration", F_UPD), ("FINTRAC, Conducting transactions with an MSB", F_PUBLIC_MSB),
             ("Revenu Québec, Money-services business licence", RQ_MSB), ("Retail Payment Activities Act", L_RPAA)],
    related=["how-to-register-msb-canada.html", "rpaa-vs-fintrac-msb-registration.html", "msb-registration-cost-canada.html"],
)

# ------------------------------------------------------------------ 26. Ready-made MSB company (2026-10-25)
GUIDES["ready-made-msb-company-canada.html"] = dict(
    modified="2026-10-25",
    checked="25 October 2026",
    title="Ready-Made FINTRAC MSB Company in Canada | AML Canada",
    desc="What a ready-made FINTRAC-registered MSB company is, what should come with it, what drives the price, and the claims to question before you pay a deposit.",
    crumb="Ready-made MSB company",
    h1="Ready-made FINTRAC MSB companies: what you get and what to question",
    lede="A ready-made MSB is a Canadian company that's already registered with FINTRAC, sold through a share purchase. Here's what should come with one, and which sales claims don't hold up.",
    label="Guide · Acquisition",
    service="msb-for-sale.html",
    also=["buy-or-register-msb-canada.html"],
    takeaways=["You buy the company's shares. The registration stays with the company.",
               "Ask for the legal name and MSB registration number before any deposit.",
               "Changes such as new owners and directors go to FINTRAC within 30 days.",
               "A registration doesn't come with a bank account."],
    sections=[
        ("what", "What \"ready-made\" means", """          <p>A ready-made MSB is a Canadian corporation, usually newly incorporated and with no trading history, that a seller has already registered with FINTRAC as a money services business. You acquire it by buying all its shares. The FINTRAC registration belongs to the registered business, so it stays with the company; it can't be moved to a company of yours.</p>
          <p>The appeal is starting from a company already on the FINTRAC registry instead of waiting for a new application. The trade-off is that you take on whatever comes with the company, so the checks come before the price.</p>"""),
        ("included", "What should come with it", """          <ul>
            <li>the certificate and articles of incorporation, the minute book and the share register;</li>
            <li>FINTRAC's registration approval and the company's listing on the public registry (new registrations can take up to a month to appear);</li>
            <li>the share purchase agreement and the share transfer documents;</li>
            <li>the change filings to FINTRAC after closing;</li>
            <li>any compliance documents, reviewed and rewritten for your business. A program written for nobody in particular won't fit yours.</li>
          </ul>"""),
        ("claims", "Claims to question", """          <div class="table-wrap"><table>
            <thead><tr><th scope="col">You may hear</th><th scope="col">What to know</th></tr></thead>
            <tbody>
              <tr><th scope="row">\"Licensed by FINTRAC\"</th><td>FINTRAC registers MSBs and says it doesn't issue licences or endorse businesses. See <a href="msb-licence-canada.html">MSB licence in Canada</a></td></tr>
              <tr><th scope="row">\"Start trading the same day\"</th><td>The new owners, directors and compliance officer are reported within 30 days, and the business needs a compliance program, a compliance officer and banking before it operates</td></tr>
              <tr><th scope="row">\"Bank account included\"</th><td>Registration doesn't guarantee banking. An existing account may not survive a change of control. Ask the bank, not the seller</td></tr>
              <tr><th scope="row">\"The licence transfers to your company\"</th><td>It doesn't. The registration stays with the company whose shares you buy</td></tr>
              <tr><th scope="row">\"PSP included\"</th><td>Bank of Canada registration under the RPAA is separate from FINTRAC registration. If the company has it, it must be re-registered before the purchase closes</td></tr>
            </tbody>
          </table></div>"""),
        ("price", "What drives the price", """          <p>The registered services, how long is left before the registration expires, whether the company has traded and how clean its records are, whether it's also registered with the Bank of Canada, and what's included after closing. Our registered companies start from €28,000. Registering a new MSB instead is our fixed US$3,500, with no FINTRAC fee. See <a href="buy-or-register-msb-canada.html">buy or register</a>.</p>"""),
        ("before-deposit", "Before you pay a deposit", f"""          <ol>
            <li>Get the legal name and MSB registration number, under an NDA if the seller asks.</li>
            <li>Check the status, services and expiry date on <a href="{F_MSB_REGISTRY}" rel="noopener">FINTRAC's registry</a>.</li>
            <li>Confirm that the new owners, directors, CEO and president can provide criminal record checks and aren't ineligible under PCMLTFA s.11.11.</li>
            <li>Ask whether the company is registered with the Bank of Canada, and plan any re-registration.</li>
            <li>Read the share purchase agreement for warranties about the company's history.</li>
          </ol>
          <p>The full checklist is in <a href="buying-an-msb-canada.html">buying an MSB in Canada</a>. The companies we have now are on <a href="msb-for-sale.html#available">MSB for sale</a>.</p>"""),
    ],
    faqs=[("What is a ready-made MSB in Canada?", "A Canadian company already registered with FINTRAC as a money services business, sold by transferring its shares. The registration stays with the company."),
          ("How much does a ready-made MSB cost?", "Our registered companies start from €28,000. The price depends on the registered services, the time left on the registration, the company's history and any Bank of Canada registration."),
          ("Does a ready-made MSB come with a bank account?", "Not reliably. FINTRAC registration doesn't guarantee banking, and an existing account may not continue after a change of control."),
          ("Can I start operating right after the purchase?", "Only once you have a compliance program and compliance officer that fit the new owners, and banking in place. The changes are reported to FINTRAC within 30 days.")],
    sources=[("FINTRAC, Money Services Business Registry", F_MSB_REGISTRY), ("Register your MSB or FMSB", F_REG), ("Update, renew or cancel your registration", F_UPD),
             ("PCMLTFA", L_PCMLTFA), ("Bank of Canada, Acquisitions of control and prescribed changes", B_ACQ)],
    related=["buying-an-msb-canada.html", "msb-licence-canada.html", "fintrac-msb-change-of-ownership.html"],
)

# ------------------------------------------------------------------ 27. FINTRAC change of ownership (2026-10-25)
GUIDES["fintrac-msb-change-of-ownership.html"] = dict(
    modified="2026-10-25",
    checked="25 October 2026",
    title="FINTRAC MSB Change of Ownership: 30-Day Updates | AML Canada",
    desc="What to report to FINTRAC after an MSB changes owners, directors or compliance officer: the 30-day rule, the change form, eligibility and RPAA re-registration.",
    crumb="Change of ownership",
    h1="FINTRAC MSB change of ownership: what to report and when",
    lede="When a registered money services business changes hands, its registration stays with the company, but FINTRAC has to be told about the changes within 30 days.",
    label="Guide · MSB registration",
    service="msb-for-sale.html",
    also=["sell-your-msb.html", "msb-registration.html"],
    takeaways=["Report changes to your registration information within 30 days.",
               "Use FINTRAC's change form; FINTRAC may follow up with questions.",
               "New owners and managers must not be ineligible under s.11.11.",
               "A registered PSP is re-registered by the Bank of Canada before closing."],
    sections=[
        ("rule", "The 30-day rule", f"""          <p>A registered MSB must keep its registration information up to date. When it changes, FINTRAC must be told within 30 days, using its change form: \"Request to update registration information for a money services business or foreign money services business\". See <a href="{F_UPD}" rel="noopener">FINTRAC, Update, renew or cancel your registration</a>.</p>
          <p>A sale usually changes several things at once: the owners, the directors and senior officers, often the compliance officer, and sometimes the address, agents or services. Report them together if you can, and keep a record of what was sent and when.</p>"""),
        ("eligibility", "Eligibility of the new people", f"""          <p>Under section 11.11 of the <a href="{L_PCMLTFA}" rel="noopener">PCMLTFA</a>, some persons and entities can't be registered, for example a corporation whose director, CEO, president or 20%+ owner has been convicted of certain offences. If a change of ownership makes the business ineligible, its registration is revoked. FINTRAC asks for criminal record checks for the CEO, the president, each director and anyone owning or controlling 20% or more, with certified translations for any not in English or French. Start these for the incoming people before closing; checks from abroad take longest.</p>"""),
        ("questions", "If FINTRAC asks questions", """          <p>FINTRAC may send a clarification request about the changes. You have 30 days to respond. If a business doesn't answer, or doesn't report changes in time, its registration can be revoked or denied. For a foreign MSB, FINTRAC says registration will be revoked or denied if a change to the representative for service's name or address isn't reported within 30 days.</p>"""),
        ("rpaa", "If the company is also a registered PSP", f"""          <p>If the company is registered with the Bank of Canada under the Retail Payment Activities Act, a planned acquisition of control is different: the company must apply again and be registered before the acquisition closes (RPAA s.24). Allow time for this, because it can include a national security review. See the <a href="{B_ACQ}" rel="noopener">Bank of Canada's guidance</a>.</p>"""),
        ("order", "A workable order of events", """          <ol>
            <li>Before signing: due diligence, criminal record checks for the incoming people, and any Bank of Canada re-registration.</li>
            <li>Closing: share transfer, new directors and officers appointed, corporate registers updated.</li>
            <li>Within 30 days: FINTRAC change form covering owners, directors, officers, compliance officer and any other changed details.</li>
            <li>Straight after: compliance program, risk assessment and policies updated for the new owners, and staff training if people changed.</li>
            <li>Diary the registration renewal date. Registration must be renewed before it expires.</li>
          </ol>"""),
        ("help", "How we help", """          <p>We prepare and file the FINTRAC change filings for clients who buy one of our <a href="msb-for-sale.html#available">registered MSBs</a> or who <a href="sell-your-msb.html">sell an MSB</a> through us. We also rewrite the <a href="compliance-programs.html">compliance program</a> for the new owners and can act as the <a href="outsourced-compliance-officer.html">compliance officer</a>.</p>"""),
    ],
    faqs=[("How long do I have to tell FINTRAC about a change of ownership?", "30 days from the change, using FINTRAC's change form for MSB registration information."),
          ("Does the MSB need to register again after a share sale?", "No. The registration stays with the company. The changes are reported to FINTRAC within 30 days. A company that buys the business's assets instead needs its own registration."),
          ("What happens if we report late?", "FINTRAC says failing to keep registration information up to date can lead to administrative monetary penalties or other consequences, and registration can be revoked or denied."),
          ("What if the company is registered with the Bank of Canada?", "Then an acquisition of control needs re-registration by the Bank of Canada before closing, under RPAA section 24.")],
    sources=[("FINTRAC, Update, renew or cancel your registration", F_UPD), ("Register your MSB or FMSB", F_REG), ("FINTRAC, Money Services Business Registry", F_MSB_REGISTRY),
             ("PCMLTFA", L_PCMLTFA), ("Bank of Canada, Acquisitions of control and prescribed changes", B_ACQ)],
    related=["buying-an-msb-canada.html", "ready-made-msb-company-canada.html", "msb-registration-refused-revoked.html"],
)


GUIDES = dict(sorted(GUIDES.items(), key=lambda kv: (kv[1].get("date", PUBLISHED), list(GUIDES).index(kv[0])), reverse=True))
