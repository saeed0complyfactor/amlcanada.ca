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

PUBLISHED = "2026-10-11"
GUIDES = {}

# ------------------------------------------------------------------ 1. how to register an MSB
GUIDES["how-to-register-msb-canada.html"] = dict(
    title="How to Register an MSB in Canada: FINTRAC Guide | AML Canada",
    desc="How to register an MSB with FINTRAC, step by step: who must register, what FINTRAC asks for, criminal record checks, approval times and renewal.",
    crumb="How to register an MSB",
    h1="How to register an MSB in Canada",
    lede="A money services business must register with FINTRAC before it starts operating, and renew every two years. FINTRAC doesn't charge a fee, and it says the majority of complete applications are processed within three months.",
    label="Guide · MSB registration",
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
    also=["canadian-address.html", "rpaa-registration.html"],
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
          <p>Quebec also licenses money-services businesses through Revenu Québec. We'll tell you when you need separate advice on these rules.</p>"""),
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
    title="Buying an MSB in Canada: What to Check | AML Canada",
    desc="Due diligence for buying a FINTRAC-registered MSB in Canada: registry checks, eligibility, deal structure, FINTRAC updates within 30 days and red flags.",
    crumb="Buying an MSB",
    h1="Buying an MSB in Canada: what to check",
    lede="Buying a company that's already registered with FINTRAC as a money services business needs the same care as any acquisition, plus checks specific to FINTRAC and, for payment businesses, the Bank of Canada.",
    label="Guide · Acquisition",
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
    faqs=[("Can you buy a FINTRAC-registered MSB?", "Yes. You can acquire a company that's already registered. Changes to its registration information, such as new owners and directors, must be reported to FINTRAC within 30 days."),
          ("Does the registration transfer if I buy the assets?", "As general information, registration belongs to the registered entity. In a share purchase the company keeps it. A new or different company that buys the assets needs its own registration."),
          ("How much does a registered MSB cost?", "It varies by company. AML Canada's registered MSBs for acquisition start from €28,000."),
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


# Dated posts (Latest updates) render with the same template; newest first.
from posts_v3 import POSTS  # noqa: E402

for _k, _v in POSTS.items():
    _v.setdefault("kind", "update")
GUIDES = {**POSTS, **GUIDES}
