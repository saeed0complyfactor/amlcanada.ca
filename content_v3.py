"""Long-form service content for site-v3 (rendered by build_v3.deep_page).

Fees come from the owner (11 October 2026). Regulatory statements were checked on
11 October 2026 against the FINTRAC, Justice Laws, Bank of Canada, Corporations Canada
and Ontario pages listed in each page's sources; re-check them before each update.
"""

CHECKED = "11 October 2026"

F_MSB = "https://fintrac-canafe.canada.ca/msb-esm/msb-eng"
F_REG = "https://fintrac-canafe.canada.ca/msb-esm/register-inscrire/reg-ins-eng"
F_UPD = "https://fintrac-canafe.canada.ca/msb-esm/register-inscrire/respond-eng"
F_G4 = "https://fintrac-canafe.canada.ca/guidance-directives/compliance-conformite/Guide4/4-eng"
F_STR = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/str-dod/str-dod-eng"
F_LCTR = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/lctr-doie/lctr-doie-eng"
F_EFT = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/eft-dt/eft-dt-eng"
F_LVCTR = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/lvctr/lvctr-eng"
F_24 = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/24hour/1-eng"
F_LPEP = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/Guide5/5-eng"
F_SANCTIONS = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/sanctions/sanctions-eng"
F_CHANGES = "https://fintrac-canafe.canada.ca/businesses-entreprises/changes-changements-eng"
L_PCMLTFA = "https://laws-lois.justice.gc.ca/eng/acts/P-24.501/"
B_RPS = "https://www.bankofcanada.ca/regulatory-oversight/retail-payments/"
B_FW = "https://www.bankofcanada.ca/regulatory-oversight/retail-payments/supervisory-framework/"
B_REG = "https://www.bankofcanada.ca/2026/08/frequently-asked-questions-about-retail-payments-supervision/"
B_FEE = "https://www.bankofcanada.ca/2024/10/registration-application-fee/"
B_REGISTRY = "https://www.bankofcanada.ca/regulatory-oversight/retail-payments/psp-registry/"
B_CRIT = "https://www.bankofcanada.ca/2026/06/criteria-for-registering-payment-service-providers/"
B_REPORTING = "https://www.bankofcanada.ca/2026/06/reminder-psp-reporting-obligations-under-rpaa/"
B_ACQ = "https://www.bankofcanada.ca/2024/08/acquisitions-of-control-and-prescribed-changes/"
L_RPAR = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2023-229/"
F_REGISTRY = "https://fintrac-canafe.canada.ca/msb-esm/reg-eng"
F_REGISTRY_CSV = "https://fintrac-canafe.canada.ca/msb-esm/reg-eng.csv"
F_NOT_ELIGIBLE = "https://fintrac-canafe.canada.ca/msb-esm/register-inscrire/no-eng"

WHATSAPP = "https://wa.me/18078060444?text=" + "Hi%2C%20I%27m%20interested%20in%20a%20registered%20MSB%20%28amlcanada.ca%29"
TELEGRAM = "https://t.me/sabbasi_1"

# Registered MSBs currently offered for acquisition (confirmed by the owner 25 October 2026).
# Names and registration numbers are withheld until an NDA; only month-level dates are shown.
# Facts below come from FINTRAC's public MSB registry (checked 25 October 2026) and the
# incorporation records. To mark one sold, set status="Sold" (keep the row for 60 days).
LISTINGS = [
    dict(slug="ontario-2026-09", province="Ontario", suffix="Ltd.", incorporated="September 2026",
         registered="October 2026", expiry="September 2029", status="Available",
         services="Foreign exchange, money transferring, virtual currency, PSP"),
    dict(slug="bc-2026-01", province="British Columbia", suffix="Inc.", incorporated="January 2026",
         registered="June 2026", expiry="January 2029", status="Available",
         services="Foreign exchange, money transferring, virtual currency, PSP"),
    dict(slug="bc-2026-02", province="British Columbia", suffix="Inc.", incorporated="February 2026",
         registered="June 2026", expiry="February 2029", status="Available",
         services="Foreign exchange, money transferring, virtual currency, PSP"),
]


def listings_html():
    rows = "\n".join(f"""              <tr id="{l['slug']}">
                <th scope="row"><span class="redact" aria-hidden="true">Withheld company</span> {l['suffix']}<span class="sr-only">Company name shared under NDA</span><br><span class="listing-sub">{l['province']}</span></th>
                <td>Incorporated {l['incorporated']}<br>Registered {l['registered']}<br>Expires {l['expiry']}</td>
                <td>{l['services']}</td>
                <td><span class="redact" aria-hidden="true">N300000000</span><span class="sr-only">Registry number shared under NDA</span></td>
                <td><span class="listing-status">{l['status']}</span><br><a href="contact.html?need=acquire&amp;entity={l['slug']}">Ask about this MSB</a></td>
              </tr>""" for l in LISTINGS)
    return f"""          <p>These Canadian companies are registered with FINTRAC as money services businesses and are for sale now. None has traded. Names and registration numbers are shared under NDA, and you can then check each one yourself on <a href="{F_REGISTRY}" rel="noopener">FINTRAC's public MSB registry</a> before paying anything.</p>
          <div class="table-wrap"><table class="listing-table">
            <thead><tr><th scope="col">Company</th><th scope="col">FINTRAC dates</th><th scope="col">Registered services (as listed by FINTRAC)</th><th scope="col">Registry no.</th><th scope="col">Status</th></tr></thead>
            <tbody>
{rows}
            </tbody>
          </table></div>
          <p>Price from €28,000, depending on the company. Bank of Canada (RPAA) status, banking and the full corporate file are reviewed with you before you commit. Message us on <a href="{WHATSAPP}" rel="noopener">WhatsApp</a> or <a href="{TELEGRAM}" rel="noopener">Telegram</a>, or <a href="contact.html?need=acquire">book a consultation</a>.</p>"""


RULES_HTML = f"""          <ol>
            <li><strong>It's a registration, not a licence.</strong> FINTRAC registers money services businesses under the PCMLTFA. It doesn't issue licences, and a registration isn't an endorsement. Quebec is the only province that licenses money services businesses separately. <a href="{F_MSB}" rel="noopener">FINTRAC</a></li>
            <li><strong>You buy the company, not the registration.</strong> The registration belongs to the registered business, so it continues when the company's shares are sold. It can't be moved to another company. <a href="{F_REG}" rel="noopener">FINTRAC</a></li>
            <li><strong>Changes go to FINTRAC within 30 days.</strong> New owners, directors and other changes to the registration information must be reported within 30 days. <a href="{F_UPD}" rel="noopener">FINTRAC</a></li>
            <li><strong>New owners must be eligible.</strong> A business can't be registered if, for example, a director, the chief executive officer, the president or a 20% owner has certain criminal convictions (PCMLTFA s.11.11). <a href="{F_NOT_ELIGIBLE}" rel="noopener">FINTRAC</a></li>
            <li><strong>Bank of Canada registration is separate.</strong> If the company is registered as a payment service provider under the RPAA, buying control needs Bank of Canada re-registration before the purchase closes. <a href="{B_ACQ}" rel="noopener">Bank of Canada</a></li>
          </ol>"""

REGISTRY_HOWTO = f"""          <ol>
            <li>Open <a href="{F_REGISTRY}" rel="noopener">FINTRAC's MSB registry</a>. It's updated monthly, and a full <a href="{F_REGISTRY_CSV}" rel="noopener">CSV download</a> is available.</li>
            <li>Search by the company's legal name or its MSB registration number.</li>
            <li>Check that the status is Registered, and check the registered services and the expiry date.</li>
            <li>Make sure the legal name and incorporation number match the share purchase agreement.</li>
          </ol>
          <p>A newly registered company can take up to a month to appear, because the registry is updated monthly. In that case, ask the seller for FINTRAC's registration approval email.</p>"""

MSB_ACTIVITIES = """<ul>
            <li>foreign exchange dealing;</li>
            <li>remitting or transmitting funds;</li>
            <li>issuing or redeeming money orders, traveller's cheques or similar negotiable instruments;</li>
            <li>dealing in virtual currency;</li>
            <li>crowdfunding platform services;</li>
            <li>armoured car services;</li>
            <li>cheque cashing;</li>
            <li>acquirer services for private automated banking machines.</li>
          </ul>"""

REPORTS_TABLE = """<div class="table-wrap"><table>
            <thead><tr><th scope="col">Report</th><th scope="col">When it applies</th><th scope="col">Deadline</th></tr></thead>
            <tbody>
              <tr><th scope="row">Suspicious transaction report (STR)</th><td>Reasonable grounds to suspect a transaction is related to money laundering, terrorist financing or, since August 19, 2024, sanctions evasion. No minimum amount.</td><td>As soon as practicable</td></tr>
              <tr><th scope="row">Large cash transaction report (LCTR)</th><td>You receive cash of $10,000 or more, in one transaction or in two or more that the 24-hour rule requires you to add together.</td><td>15 calendar days</td></tr>
              <tr><th scope="row">Electronic funds transfer report (EFTR)</th><td>You initiate, or finally receive, an international electronic funds transfer of $10,000 or more, in one transfer or in two or more that the 24-hour rule requires you to add together.</td><td>5 working days</td></tr>
              <tr><th scope="row">Large virtual currency transaction report (LVCTR)</th><td>You receive virtual currency worth $10,000 or more, in one transaction or in two or more that the 24-hour rule requires you to add together.</td><td>5 working days</td></tr>
              <tr><th scope="row">Listed person or entity property report</th><td>Property you know or believe is owned or controlled by a terrorist group or a listed person or entity. Since October 1, 2025, this includes persons listed under the Special Economic Measures Act and the Sergei Magnitsky Law. Called the terrorist property report until March 2, 2025. You must also disclose the property to the RCMP and CSIS without delay.</td><td>Immediately</td></tr>
            </tbody>
          </table></div>"""

PCMLTFA_DOCS = ["AML/ATF Compliance Policy",
                "KYC and Customer Due Diligence Procedure",
                "Ongoing Monitoring Procedure",
                "Business-Wide Risk Assessment",
                "Sanctions and Watchlist Screening Policy and Procedure",
                "Ministerial Directive Compliance Policy",
                "Travel Rule Policy and Procedure",
                "Applicable FINTRAC Reporting Procedures",
                "Procedural Registers",
                "Records Retention Policy",
                "Staff AML Training Policy",
                "Compliance Testing and Effectiveness Review Plan",
                "Risk Appetite Policy",
                "Fraud Risk Management Policy"]

DEEP = {}

# ------------------------------------------------------------------ outsourced compliance officer
DEEP["outsourced-compliance-officer.html"] = dict(
    guides=['outsourced-compliance-officer-how-it-works.html', 'second-line-of-defence-aml-canada.html', 'outsourced-vs-in-house-compliance-officer.html', 'msb-compliance-officer-requirements-canada.html', 'choosing-outsourced-compliance-officer-canada.html', 'msb-onboarding-file-review-checklist.html'],
    name="Outsourced compliance officer",
    title="Outsourced AML Compliance Officer (MLRO) Canada | AML Canada",
    desc="An outsourced Canadian AML compliance officer (MLRO): onboarding reviews, FINTRAC reporting, policies and risk assessments. US$1,500 per month for 10 hours.",
    service_type="Outsourced AML compliance officer (MLRO)",
    offers=[("1500", "USD", "Outsourced compliance officer, 10 hours per month")],
    kicker="Outsourced AML compliance officer (MLRO) in Canada",
    h1="A Canadian compliance officer, without the full-time hire.",
    lede="An outsourced AML compliance officer, or MLRO, for businesses FINTRAC regulates. US$1,500 per month for 10 hours, scaled as you grow.",
    hero_price="US$1,500 / month · 10 hours",
    label="Compliance officer · On duty",
    need="officer",
    intro=("Every business FINTRAC regulates has to appoint a compliance officer. For many growing businesses, the right person is experienced, part-time and already working in Canada.",
           ["AML Canada provides an outsourced compliance officer, also known as an MLRO (money laundering reporting officer) or CAMLO, for money services businesses, virtual currency dealers, payment companies and foreign businesses entering Canada. We carry the day-to-day anti-money laundering and anti-terrorist financing work for you: second-line review of customer onboarding, advice on difficult cases, regulatory reporting to FINTRAC, and keeping your policies and risk assessments current.",
            "The fee is US$1,500 per month for 10 hours. Start with the hours you need now and add further 10-hour blocks to your month as your customers, products and markets grow.",
            "Your business stays responsible for its obligations under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA). We do the work behind them on time and keep a record of what was done."]),
    facts=[("Fee", "US$1,500", "per month for 10 hours"),
           ("Hours", "Scalable", "add 10-hour blocks as you grow"),
           ("Reports", "STR · EFTR · LVCTR", "LCTR and the others that apply to you"),
           ("Based", "In Canada", "working alongside your team")],
    fee=dict(amount="US$1,500", unit="per month · 10 hours · scalable",
             note="How your hours are used each month is set out in your written scope.",
             items=["All AML and compliance obligations under your program",
                    "Second-line review of customer onboarding",
                    "Advice on cases, products and regulatory questions",
                    "Regulatory reporting: STR, EFTR, LVCTR, LCTR and others",
                    "Policy and procedure maintenance",
                    "Business risk assessment",
                    "Client risk assessments",
                    "Hours that scale as your business grows"]),
    guide=[
        ("role", "What an outsourced compliance officer does", f"""          <p>Under the PCMLTFA, a business that FINTRAC regulates must appoint a compliance officer who is responsible for implementing its compliance program. FINTRAC's guidance says that person needs the authority and the access to resources to do the job. For a larger business, FINTRAC's guidance suggests someone from a senior level with direct access to senior management and the board.</p>
          <p>An outsourced compliance officer fills that role, or supports the person who holds it, from outside the business. FINTRAC's guidance doesn't specifically address external appointments, so we document the compliance officer's authority, access to senior management and sign-off responsibilities in writing. The arrangement is common for money services businesses, virtual currency dealers, payment companies and foreign businesses entering Canada, which need experienced compliance judgment without a full-time senior hire.</p>
          <p>The work is ongoing. Customers are onboarded every day, transactions need watching, reports have deadlines measured in days, and the rules and your business both change. We do that work with your team, inside your systems.</p>"""),
        ("scope", "What's included", f"""          <p>The scope covers your AML and compliance obligations as a whole. This is the work most often involved.</p>
          <h3>Second-line customer onboarding review</h3>
          <p>Your front line collects customer information. As the second line, we review it: how identity was verified, beneficial ownership, politically exposed person and head of international organization determinations, third-party determinations, sanctions and listed person screening results, and the customer's risk rating. We approve or escalate files, apply enhanced measures where the risk is high, and sample completed files to check that the process holds up.</p>
          <h3>Advisory</h3>
          <p>Questions don't wait for a review cycle. A new product, a new market, a new agent, a payment partner's due diligence questionnaire, a bank asking about your program, or a letter from FINTRAC. We give you a clear answer, explain the reasoning, and record the decision so you can show it later.</p>
          <h3>Regulatory reporting</h3>
          <p>We prepare and file the reports your business has to make to FINTRAC, including suspicious transaction reports, electronic funds transfer reports, large virtual currency transaction reports, large cash transaction reports and listed person or entity property reports. Each one has its own threshold and deadline:</p>
          {REPORTS_TABLE}
          <p>Amounts are in Canadian dollars. For large cash and large virtual currency transactions, FINTRAC's 24-hour rule means two or more transactions that total $10,000 or more within a static 24-hour window are reported together when you know they were conducted by or on behalf of the same person or entity, or are for the same beneficiary. Electronic funds transfers and casino disbursements have their own aggregation rules.</p>
          <h3>Policy maintenance</h3>
          <p>Your compliance policies and procedures have to be kept up to date. We update them when the regulations change, when FINTRAC publishes new guidance, and when your business launches something new, and we keep a record of what changed and why.</p>
          <h3>Business risk assessment</h3>
          <p>Your program rests on a documented assessment of your money laundering, terrorist financing and sanctions evasion risks: your clients and business relationships, your products, services and delivery channels, where you operate, and new technologies. We write it, keep it current and check that your controls follow from it.</p>
          <h3>Client risk assessments</h3>
          <p>Every client gets a risk rating that drives how closely you monitor them. We set the methodology, review ratings and apply enhanced measures to high-risk clients.</p>"""),
        ("how", "How the engagement runs", """          <ol>
            <li><strong>Consultation.</strong> Your business, your customers, your volumes and what you already have in place.</li>
            <li><strong>Written scope.</strong> What we'll do, how many hours to start with, and how we'll report the time to you.</li>
            <li><strong>Set-up.</strong> Access to the systems we need, such as your onboarding and screening tools and your FINTRAC reporting account, and a handover of open items.</li>
            <li><strong>Ongoing work.</strong> Onboarding reviews, reporting, advice and maintenance, with regular check-ins with your management.</li>
            <li><strong>Scaling.</strong> As volumes grow, add blocks of hours, or hand the work to an in-house compliance officer we help you hire and train.</li>
          </ol>"""),
        ("hours", "How many hours you might need", """          <p>It depends on how many customers you onboard, how many alerts and reports you generate, how many products and markets you serve, and whether you deal in cash or virtual currency. A business preparing to launch needs far fewer hours than one onboarding hundreds of customers a month.</p>
          <p>We estimate a starting number of hours with you in the consultation, then adjust once your volumes are clear. The monthly fee covers 10 hours, and you add 10-hour blocks when you need more, so the cost follows your workload.</p>"""),
        ("responsibility", "Your responsibilities, and ours", """          <p>Your business remains the reporting entity even when we do the work, and your senior management stays accountable for the program. We document decisions, send escalations to the right people and keep you informed of what was done in your name.</p>
          <ul>
            <li>You provide access, information and timely decisions.</li>
            <li>We carry out the agreed work, flag risks early and keep records you can show an examiner.</li>
            <li>We agree in writing who signs off on what, including reports and policy changes.</li>
          </ul>"""),
        ("fractional", "A fractional compliance officer", """          <p>"Fractional" usually means a part-time compliance officer from outside your business who is paid for the hours used. That's how our service works: US$1,500 per month for 10 hours, with further 10-hour blocks added as your customers, products and markets grow. You get an experienced officer without the cost of a full-time senior hire, and the arrangement can later be handed to an in-house officer we help you hire and train.</p>"""),
        ("exam", "What FINTRAC checks about your compliance officer", """          <p>An appointment has to be real. In an examination, FINTRAC verifies four things about the compliance officer: appointment, authority, knowledge and duties. Its compliance assessment manual says the focus is whether the officer is fulfilling their duties to implement a sound compliance program, judged by whether the areas examined are put into practice. Examiners may also confirm that the officer has direct access to senior management or the board, and timely access to information from all business lines.</p>
          <p>An external officer has that access only if you grant it, so we put it in writing at the start, together with who signs off on reports, policy changes and client decisions. Our guide to <a href="msb-compliance-officer-requirements-canada.html">FINTRAC compliance officer requirements</a> lists the documents to keep on file.</p>"""),
        ("mlro", "MLRO, CAMLO, compliance officer or CCO?", """          <p>The titles differ by country and by firm. In the UK and Europe the role is usually called the MLRO, or money laundering reporting officer. Canada's PCMLTFA framework uses "compliance officer". Some Canadian firms also use "CAMLO" (chief anti-money laundering officer) or "chief compliance officer" for the same appointed role. If you're entering Canada from abroad and looking for an MLRO, the Canadian compliance officer is the equivalent role, with Canada's own reports, thresholds and deadlines.</p>"""),
    ],
    sources=[("FINTRAC, Compliance program requirements", F_G4), ("Reporting suspicious transactions", F_STR),
             ("Reporting suspected sanctions evasion", F_SANCTIONS), ("Reporting listed person or entity property", F_LPEP),
             ("Reporting electronic funds transfers", F_EFT), ("Reporting large virtual currency transactions", F_LVCTR),
             ("Reporting large cash transactions", F_LCTR), ("The 24-hour rule", F_24)],
    for_title="When it helps",
    for_items=[("Before you launch", "A compliance officer in place from the day you start operating."),
               ("When a bank or partner asks", "Someone who can answer due diligence questions about your program."),
               ("When volumes outgrow your team", "Extra capacity for onboarding reviews, reporting and maintenance.")],
    arts=["scan", "address", "many"],
    faqs=[("Can a business outsource its compliance officer in Canada?", "Many businesses use an outside compliance officer, or outside support for the person they appoint. FINTRAC's guidance doesn't specifically address external appointments. Your business stays responsible for its obligations, and the compliance officer needs the authority and access to senior management to do the job, so we set out authority, access and sign-off in writing."),
          ("What does an outsourced compliance officer cost?", "US$1,500 per month for 10 hours. You can add further 10-hour blocks each month as your business grows."),
          ("What is an MLRO in Canada?", "MLRO means money laundering reporting officer, a title used mainly in the UK and Europe. The Canadian equivalent under the PCMLTFA is the compliance officer, which some Canadian firms call the CAMLO (chief anti-money laundering officer)."),
          ("Does the compliance officer have to live in Canada?", "Section 156 of the regulations and FINTRAC's compliance program guidance set no residency requirement for the compliance officer. A foreign MSB must separately name a person who resides in Canada and is authorized to accept notices from FINTRAC."),
          ("What does FINTRAC check about an outsourced compliance officer?", "The same as for any compliance officer: appointment, authority, knowledge and duties, judged by whether the compliance program is actually put into practice. Examiners may also confirm, where applicable, that the officer has direct access to senior management or the board and timely access to information from all business lines, which an external officer has only if you grant it in writing."),
          ("Which FINTRAC reports do you handle?", "Suspicious transaction reports, electronic funds transfer reports, large virtual currency transaction reports, large cash transaction reports, and listed person or entity property reports, whichever apply to your business."),
          ("Do you work with foreign money services businesses?", "Yes. We work with businesses based outside Canada that serve people in Canada."),
          ("Can we start small?", "Yes. Start with 10 hours a month, and add further 10-hour blocks when your volumes grow."),
          ("Is a fractional compliance officer the same as an outsourced one?", "In practice, yes. \"Fractional\" usually means a part-time compliance officer from outside your business who is paid for the hours used. Our service works that way: US$1,500 per month for 10 hours, with more hours added as your volumes grow.")],
    related=["compliance-programs.html", "msb-registration.html", "effectiveness-reviews.html"],
)

# ------------------------------------------------------------------ MSB registration
DEEP["msb-registration.html"] = dict(
    name="MSB registration",
    title="FINTRAC MSB Registration in Canada | AML Canada",
    desc="FINTRAC registration for money services businesses, foreign MSBs and virtual currency (crypto) dealers. Fixed fee US$3,500, prepared and submitted with you.",
    service_type="FINTRAC money services business registration",
    timing="1 week to 7 months",
    offers=[("3500", "USD", "FINTRAC MSB registration, fixed fee")],
    kicker="FINTRAC MSB registration in Canada",
    h1="MSB registration with FINTRAC, from first assessment to decision.",
    lede="For money services businesses, foreign MSBs and virtual currency dealers. Fixed fee US$3,500.",
    hero_price="Fixed fee · US$3,500",
    label="MSB · Registration prepared",
    need="register",
    intro=("Money services businesses (MSBs) must register with FINTRAC before they start operating, and so must foreign businesses that serve people in Canada.",
           ["FINTRAC, the Financial Transactions and Reports Analysis Centre of Canada, registers money services businesses under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA). It's how foreign exchange dealers, money transfer businesses, virtual currency dealers and others become allowed to operate in Canada.",
            "We work out whether and how registration applies to you, gather and check everything FINTRAC asks for, support you through submission and FINTRAC's questions, and prepare your compliance program at the same time.",
            "Our fee is a fixed US$3,500. FINTRAC itself doesn't charge to register."]),
    facts=[("FINTRAC fee", "None", "FINTRAC doesn't charge to register"),
           ("When", "Before you operate", "registration comes first"),
           ("Typical approval", "1 week to 7 months", "in our experience"),
           ("Valid for", "2 years", "then renewed")],
    fee=dict(amount="US$3,500", unit="fixed fee · one time",
             note="Covers your registration. Compliance program documents are a separate fixed fee of US$3,500.",
             items=["Assessment of which of your activities are money services",
                    "Registration information gathered and checked with you",
                    "Ownership, corporate and criminal record check requirements coordinated, including certified translations",
                    "Submission, and answers to FINTRAC's follow-up questions",
                    "Foreign MSB requirements, including your representative for service in Canada",
                    "Coordination with your compliance program"]),
    guide=[
        ("who-must-register", "Who has to register", f"""          <p>A business with a place of business in Canada must register with FINTRAC before it provides any of these money services:</p>
          {MSB_ACTIVITIES}
          <p>Registering or being licensed with a province doesn't replace FINTRAC registration. Whether your own activities are covered depends on how your business works, which is the first thing we confirm with you.</p>
          <p>An MSB that holds funds for its users or transfers funds at their request may also need to register with the Bank of Canada under the Retail Payment Activities Act. We cover that in <a href="rpaa-registration.html">RPAA registration</a>.</p>
          <p>Prefer a company that's already registered? Compare the two routes on our <a href="buy-or-register-msb-canada.html">buy or register an MSB</a> page.</p>"""),
        ("foreign-msb", "Foreign MSB registration", """          <p>A foreign MSB has no place of business in Canada but directs and provides money services to people or entities in Canada. It registers with FINTRAC before it starts and names a representative for service who resides in Canada; our <a href="foreign-msb-registration-canada.html">foreign MSB guide</a> covers the details.</p>"""),
        ("application", "What FINTRAC asks for", """          <p>FINTRAC's registration asks for:</p>
          <ul>
            <li>details of the business, including its incorporation, ownership and senior management;</li>
            <li>bank account information;</li>
            <li>your compliance officer;</li>
            <li>how many employees you have, and every location you operate from;</li>
            <li>estimated annual transaction totals for each money service you offer;</li>
            <li>any agents or mandataries that provide services on your behalf;</li>
            <li>for a foreign MSB, a representative for service who lives in Canada;</li>
            <li>documents confirming the business exists and how it's owned and controlled;</li>
            <li>criminal record checks.</li>
          </ul>
          <p>Criminal record checks are needed for the chief executive officer, the president, the directors and anyone who owns or controls 20% or more, directly or indirectly. Each must be issued no more than six months before you apply. A criminal record check that isn't in English or French needs a translation attested by a certified translator (PCMLTFA s.11.12(1.1)).</p>
          <p>If FINTRAC asks for clarification, the answer is due within 30 days of the request, or FINTRAC can deny the application (PCMLTFA s.11.14). Registered businesses face the same 30-day limit, or FINTRAC can revoke the registration (s.11.17). Transaction estimates, locations, ownership and documents that tell the same story are the best way to avoid back-and-forth. Our guide on <a href="how-to-register-msb-canada.html">how to apply to FINTRAC</a> covers each step.</p>"""),
        ("licence", "MSB licence or registration?", """          <p>People often search for an "MSB licence". At the federal level, Canada requires registration with FINTRAC, not a licence, and FINTRAC doesn't endorse the businesses it registers. Quebec is the exception: a business operating in Quebec that offers currency exchange, funds transfers, cheque cashing, traveller's cheques, money orders or bank drafts, or ATMs or crypto ATMs also needs a licence from Revenu Québec under the Money-Services Businesses Act. Our guide <a href="msb-licence-canada.html">Is there an MSB licence in Canada?</a> explains how to describe your registration accurately.</p>"""),
        ("how", "How registration works with us", """          <ol>
            <li><strong>Assessment.</strong> Which of your services are money services, whether you're an MSB or a foreign MSB, and what follows from that.</li>
            <li><strong>Preparation.</strong> A checklist of everything FINTRAC needs, and help gathering and checking it. Criminal record checks from several countries often take longest, so we start them first.</li>
            <li><strong>Submission.</strong> Your registration, submitted to FINTRAC with your approval.</li>
            <li><strong>Follow-up.</strong> Answers to FINTRAC's questions, within its deadlines, until your registration is decided.</li>
            <li><strong>Compliance program.</strong> Prepared at the same time as your registration, so you can operate once you're registered.</li>
          </ol>"""),
        ("how-long", "How long registration takes", """          <p>FINTRAC says most complete applications are processed within three months. In our experience it has ranged from about 1 week to 7 months. The main factors are how complete and consistent the application is, how quickly criminal record checks arrive, and FINTRAC's workload at the time.</p>"""),
        ("after", "After you register", """          <p>Registration is valid for two years and has to be renewed before it expires. Changes to your registration information must be reported to FINTRAC within 30 days.</p>
          <p>After registration, an MSB also needs a compliance program, client identification, record keeping and reporting to FINTRAC. Since October 1, 2025, an MSB must also check that its agents and mandataries are eligible, including by reviewing criminal record checks, before engaging them.</p>
          <p>FINTRAC's public MSB registry lists registered businesses and is updated monthly, so clients, banks and partners can confirm your status. Our guide shows <a href="check-fintrac-msb-registration.html">how to check FINTRAC MSB registration</a>.</p>
          <p>Knowingly operating without the required registration is an offence. Section 77.4 of the PCMLTFA makes it an offence for a business that must register to knowingly engage in an activity it isn't registered for, and officers and directors can also be found guilty (section 78). Our guide on <a href="msb-registration-refused-revoked.html">refused and revoked registrations</a> sets out the penalties.</p>"""),
        ("crypto", "Virtual currency dealers", """          <p>Dealing in virtual currency is a money service, so crypto exchanges and dealers register with FINTRAC as MSBs, including foreign ones that serve people in Canada. Registered dealers also report virtual currency transactions of $10,000 or more within five working days. Provincial securities rules can also apply to some crypto trading platforms; we'll tell you if that's something you need separate advice on.</p>"""),
    ],
    sources=[("FINTRAC, Money services businesses", F_MSB), ("Register your MSB or FMSB", F_REG),
             ("Update, renew or cancel your registration", F_UPD), ("Reporting large virtual currency transactions", F_LVCTR),
             ("PCMLTFA, sections 11.1 to 11.17", L_PCMLTFA), ("Bank of Canada, Retail payments", B_RPS)],
    for_title="Common starting points",
    for_items=[("Launching a new MSB", "A company and a product ready, with FINTRAC registration needed before going live."),
               ("Adding a money service", "An existing business adding foreign exchange, transfers or virtual currency."),
               ("Entering from abroad", "A business outside Canada that will serve people in Canada.")],
    arts=["one", "many", "address"],
    faqs=[("How much does MSB registration cost?", "FINTRAC doesn't charge a registration fee. Our fee to prepare and support your registration is a fixed US$3,500."),
          ("How long does FINTRAC registration take?", "FINTRAC says most complete applications are processed within three months. In our experience it has ranged from about 1 week to 7 months, depending mostly on how complete the application is, how quickly criminal record checks arrive, and FINTRAC's workload."),
          ("Can a company outside Canada register as an MSB?", "Yes. A foreign business that directs and provides money services to people in Canada registers as a foreign MSB and must name a representative for service who resides in Canada."),
          ("Do I need a compliance program before I register?", "You need one to operate. FINTRAC asks for your compliance officer when you register, and your obligations start as soon as you begin. We prepare your program at the same time as your registration. Program documents are a separate fixed fee of US$3,500."),
          ("How often do I renew?", "Every two years. Changes to your registration information have to be reported within 30 days."),
          ("Do crypto businesses register with FINTRAC?", "Yes. Dealing in virtual currency is a money service, so crypto dealers and exchanges register as MSBs."),
          ("Is there an MSB licence in Canada?", "At the federal level, Canada requires registration with FINTRAC, not a licence. When people search for an MSB licence in Canada, they usually mean FINTRAC registration. Quebec is the exception: a business operating in Quebec that offers currency exchange, funds transfers, cheque cashing, traveller's cheques, money orders or bank drafts, or ATMs or crypto ATMs also needs a licence from Revenu Québec."),
          ("How do I check if a business is registered with FINTRAC?", "Search FINTRAC's public MSB registry by name or registration number and confirm the status is Registered. The other statuses are Revoked, Expired and Ceased. FINTRAC updates the registry monthly, so a newly registered business may not appear yet.")],
    related=["compliance-programs.html", "outsourced-compliance-officer.html", "rpaa-registration.html"],
)

# ------------------------------------------------------------------ compliance program
DEEP["compliance-programs.html"] = dict(
    name="Compliance programs",
    title="FINTRAC Compliance Program (AML, PCMLTFA) | AML Canada",
    desc="FINTRAC compliance program documents under the PCMLTFA: policies and procedures, risk assessment, training and review plans. Fixed fee US$3,500.",
    service_type="PCMLTFA AML compliance program documents",
    offers=[("3500", "USD", "FINTRAC PCMLTFA compliance program documents, fixed fee")],
    kicker="FINTRAC compliance program for your business",
    h1="An AML compliance program built around your products, customers and team.",
    lede="FINTRAC and PCMLTFA compliance program documents for the businesses FINTRAC regulates. Fixed fee US$3,500.",
    hero_price="Fixed fee · US$3,500",
    label="Program · 5 of 5 parts",
    need="programme",
    intro=("Every business FINTRAC regulates must have a compliance program, sometimes called an AML/ATF program. Since March 2026 the PCMLTFA requires programs to be reasonably designed, risk-based and effective.",
           ["Under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA), a compliance program brings together a compliance officer, written policies and procedures, a risk assessment, an ongoing training program and a regular review of how well it all works.",
            "We write your program documents around your products, your customers and the way your team works, in language your staff can follow.",
            "You receive 14 documents, from the AML/ATF Compliance Policy to the Fraud Risk Management Policy, for a fixed fee of US$3,500."]),
    facts=[("Documents", "14", "in one fixed fee"),
           ("Required parts", "5", "in every program"),
           ("Review", "Every 2 years", "at a minimum"),
           ("Policies", "Kept current", "and approved by a senior officer")],
    fee=dict(amount="US$3,500", unit="fixed fee · program documents",
             note="Keeping the program current afterwards can be covered by outsourced compliance officer hours.",
             items=PCMLTFA_DOCS),
    guide=[
        ("documents", "The 14 documents you receive", """          <p>Your fixed fee covers a complete set of PCMLTFA compliance program documents for your business:</p>
          <ol class="doc-list">
""" + "\n".join(f"            <li>{d}</li>" for d in PCMLTFA_DOCS) + """
          </ol>
          <p>Together they cover the policies, procedures, risk assessment, training and review planning behind the five required parts of a FINTRAC compliance program, plus your risk appetite and fraud risk management.</p>"""),
        ("program-elements", "The five elements of a FINTRAC compliance program", """          <p>FINTRAC's guidance sets out five required elements:</p>
          <ol>
            <li><strong>A compliance officer</strong>, appointed to be responsible for implementing the program. See <a href="msb-compliance-officer-requirements-canada.html">FINTRAC compliance officer requirements</a>.</li>
            <li><strong>Written policies and procedures</strong>, kept up to date and, for an entity, approved by a senior officer. See <a href="fintrac-compliance-program-requirements.html#policies">what FINTRAC expects them to cover</a>.</li>
            <li><strong>A risk assessment</strong> of the business's money laundering, terrorist financing and sanctions evasion risks, documented. See <a href="fintrac-risk-assessment-msb.html">how to do a FINTRAC risk assessment</a>.</li>
            <li><strong>A written, ongoing compliance training program</strong>, with a plan for delivering it, if you have employees, agents or others authorized to act for you. See <a href="fintrac-training-requirements.html">FINTRAC training requirements</a>.</li>
            <li><strong>A review of effectiveness</strong> of the policies and procedures, risk assessment and training program, at least every two years. See our <a href="fintrac-effectiveness-review-checklist.html">effectiveness review checklist</a>.</li>
          </ol>
          <p>Our guide to <a href="fintrac-compliance-program-requirements.html">FINTRAC compliance program requirements</a> explains what FINTRAC expects in each part.</p>"""),
        ("policies", "What your policies and procedures cover", """          <ul>
            <li>knowing your client: verifying identity, beneficial ownership, and politically exposed persons and heads of international organizations;</li>
            <li>third-party determinations and business relationships;</li>
            <li>ongoing monitoring, and the enhanced measures you apply to high-risk clients;</li>
            <li>sanctions and listed person screening;</li>
            <li>reporting to FINTRAC, including suspicious transactions, and the 24-hour rule;</li>
            <li>record keeping;</li>
            <li>ministerial directives, and how you'll apply new ones;</li>
            <li>travel rule information for funds and virtual currency transfers, where it applies.</li>
          </ul>
          <p>The exact list depends on the kind of business you are and the services you offer, which is why we start with how you operate.</p>"""),
        ("risk-assessment", "Your risk assessment", """          <p>The rest of your program depends on the risk assessment. It looks at your money laundering, terrorist financing and sanctions evasion risks: your clients and business relationships, your products, services and delivery channels, the places you operate in and deal with, new developments and technologies, and the risks for your sector set out in Canada's latest National Risk Assessment of Money Laundering and Terrorist Financing. Higher-risk clients and products get closer controls.</p>"""),
        ("without", "What happens without one", """          <p>FINTRAC can impose administrative monetary penalties for breaches of the anti-money laundering law. For violations on or after March 26, 2026, the cap is $4 million per violation for a person and $20 million for an entity. FINTRAC can also disclose non-compliance to law enforcement for investigation as a criminal offence, but the same act or omission can't be dealt with both as a violation and as an offence (PCMLTFA s.73.12). Our guide to <a href="fintrac-penalties-amps.html">FINTRAC penalties (AMPs)</a> explains how they work.</p>"""),
        ("bank", "If your bank or payment partner has asked for your program", """          <p>Banks and payment partners usually want to see that your program exists, fits your business, has a named compliance officer, and is followed day to day. If you've been asked and don't have one, or aren't sure yours will stand up, book a consultation. We'll tell you what's missing and how quickly it can be put right.</p>"""),
        ("keeping-current", "Keeping it current", """          <p>A program written once and left on a shelf goes out of date as your business and the rules change. We can keep it current through outsourced compliance officer hours, and test it in your two-year effectiveness review.</p>"""),
    ],
    sources=[("FINTRAC, Compliance program requirements", F_G4), ("Changes to the PCMLTFA and regulations", F_CHANGES),
             ("Money services businesses", F_MSB), ("The 24-hour rule", F_24)],
    for_title="Who it's for",
    for_items=[("Newly registered businesses", "Putting a program in place for the first time."),
               ("Growing businesses", "New products, new markets or more volume than the program was written for."),
               ("Businesses after a review or examination", "Closing the gaps that were found.")],
    arts=["one", "programme", "scan"],
    faqs=[("What does an AML compliance program include in Canada?", "Five parts: a compliance officer, written policies and procedures, a risk assessment, an ongoing training program and plan if you have employees, agents or others acting for you, and an effectiveness review at least every two years."),
          ("Who needs a FINTRAC compliance program?", "Every reporting entity under the PCMLTFA must establish and implement one, whatever its size. That includes money services businesses, foreign MSBs and virtual currency dealers."),
          ("Can the owner be the compliance officer?", "Yes, if your business is small. FINTRAC's guidance says the owner or operator of a small business can be the compliance officer, and a sole proprietor can appoint themselves. In a larger business, FINTRAC's best practice is an officer who isn't directly involved in receiving, transferring or paying funds."),
          ("Is a FINTRAC compliance program the same as an RPAA compliance program?", "No. A FINTRAC compliance program covers money laundering, terrorist financing and sanctions evasion under the PCMLTFA. An RPAA compliance program covers operational risk and safeguarding under the Bank of Canada. Many payment businesses need both."),
          ("How much does a compliance program cost?", "A fixed US$3,500 for 14 PCMLTFA compliance program documents, from the AML/ATF Compliance Policy to the Fraud Risk Management Policy."),
          ("Do you use templates?", "We use a consistent structure, and the content is written for your products, customers and team. A program that doesn't describe how your business works won't hold up in an examination."),
          ("Does the fee include the effectiveness review?", "No. The program includes a plan for your review. The review itself is a separate, scoped piece of work."),
          ("Can you keep the program up to date afterwards?", "Yes, through outsourced compliance officer hours at US$1,500 per month for 10 hours."),
          ("Our bank has asked for our AML program. What now?", "Book a consultation. We'll look at what you have, tell you what's missing and agree a written scope to close the gaps.")],
    related=["outsourced-compliance-officer.html", "effectiveness-reviews.html", "msb-registration.html"],
)

# ------------------------------------------------------------------ Canadian address
# Address roles and limits added 23 November 2026 (seo-run REVERSE-address-incorporation-apostille).
# Checked 23 November 2026 against the pages below; FINTRAC wording reused from virtual-office-msb-registration.html.
CA_CBCA_19 = "https://laws-lois.justice.gc.ca/eng/acts/C-44/section-19.html"
CA_CBCA_20 = "https://laws-lois.justice.gc.ca/eng/acts/C-44/section-20.html"
CA_CC_NEXT = "https://ised-isde.canada.ca/site/corporations-canada/en/business-corporations/next-steps-following-incorporation-your-business"
CA_OBCA = "https://www.ontario.ca/laws/statute/90b16"
CA_CRA_ADDR = "https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/maintain-business/change-address.html"
CA_CRA_RES = ("https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/"
              "businesses-international-non-resident-taxes/residency-a-corporation.html")

DEEP["canadian-address.html"] = dict(
    name="Canadian business address",
    checked="23 November 2026",
    modified="2026-11-23",
    title="Canadian Business Address for Foreign Companies | AML Canada",
    desc="A Canadian business address for foreign MSBs and companies entering Canada, for your setup, banking and partners. US$200 per month, terms agreed in writing.",
    service_type="Canadian business address",
    offers=[("200", "USD", "Canadian business address, per month")],
    h1="A Canadian business address for foreign companies and MSBs.",
    lede="A Canadian business address for your setup, banking and partners, for foreign MSBs and companies entering Canada. US$200 per month.",
    hero_price="US$200 · per month",
    label="Business address · Canada",
    need="address",
    intro=("Setting up in Canada from abroad is easier with a Canadian base for your business.",
           ["We provide a Canadian business address for companies entering the Canadian market, including foreign money services businesses, to use for your setup, your banking and your partners.",
            "It costs US$200 per month. What's included, such as how mail is handled, is confirmed with you in writing before anything starts."]),
    facts=[("Fee", "US$200", "per month"),
           ("For", "Foreign MSBs", "and companies entering Canada"),
           ("Use", "Setup and banking", "and your partners"),
           ("Scope", "In writing", "including mail handling")],
    fee=dict(amount="US$200", unit="per month",
             note="Often combined with MSB registration and an outsourced compliance officer.",
             items=["A Canadian business address",
                    "For your setup, banking and partners",
                    "Scope, including mail handling, confirmed in writing",
                    "Checked against your FINTRAC registration before you use it"]),
    guide=[
        ("why", "Why a Canadian address helps", """          <p>Canadian banks, payment partners and customers often look for a Canadian presence, and a Canadian business address gives your setup a stable base. For a Canadian-based MSB, FINTRAC registration asks for every location you operate from.</p>"""),
        ("registration", "How the address fits your FINTRAC registration", """          <p>A foreign MSB registers with FINTRAC through a representative for service: a person who resides in Canada and accepts FINTRAC's notices on the business's behalf. That's a separate requirement from your business address.</p>
          <p>If you're a foreign MSB, a physical location in Canada can change your status to a domestic MSB. We'll confirm how the address fits your registration before you use it.</p>"""),
        ("which-address", "Which Canadian address do you need?", f"""          <p>A company in Canada can have several addresses, and each one does a different job. It helps to know which ones you need before you choose an address.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Address</th><th scope="col">What it is</th></tr></thead>
            <tbody>
              <tr><th scope="row">Registered office</th><td>A federal corporation must at all times have a registered office in the province named in its articles (<a href="{CA_CBCA_19}" rel="noopener">CBCA s. 19(1)</a>). <a href="{CA_CC_NEXT}" rel="noopener">Corporations Canada</a> calls it the official address for communications with your corporation. It's public, and a change must be filed within 15 days. An Ontario corporation needs a registered office in Ontario (<a href="{CA_OBCA}" rel="noopener">Business Corporations Act, s. 14(1)</a>).</td></tr>
              <tr><th scope="row">Records office</th><td>A federal corporation keeps its articles, by-laws, minutes, resolutions and securities register at its registered office or another place in Canada the directors designate (<a href="{CA_CBCA_20}" rel="noopener">CBCA s. 20(1)</a>). Records can be kept outside Canada only if they can be inspected electronically from the registered office or another place in Canada (s. 20(5.1)).</td></tr>
              <tr><th scope="row">CRA physical address</th><td>The <a href="{CA_CRA_ADDR}" rel="noopener">CRA</a> says the physical address is the business or head office address, where day-to-day activities take place. It can't be a rural route number or a P.O. box.</td></tr>
              <tr><th scope="row">Mailing address</th><td>The CRA says your mailing address can be different from your physical address, for example your accountant's. The CRA also needs your books and records address if it's different. FINTRAC's MSB registration asks for a mailing address if it differs from the place of business.</td></tr>
              <tr><th scope="row">Place of business given to FINTRAC</th><td>An MSB lists the address of its place of business, and FINTRAC's registration asks for detailed information about every location. That address is published on <a href="{F_REGISTRY}" rel="noopener">FINTRAC's public MSB registry</a>.</td></tr>
              <tr><th scope="row">Representative for service (foreign MSB)</th><td>Not an address. It's a person who resides in Canada and is authorized to accept notices from FINTRAC on the business's behalf.</td></tr>
            </tbody>
          </table></div>
          <p>Tell us which of these you need an address for. What our address covers is confirmed with you in writing before you use it. Our guide on <a href="virtual-office-msb-registration.html">using a virtual office for MSB registration</a> covers the FINTRAC side in more detail.</p>"""),
        ("limits", "What a Canadian address doesn't do", f"""          <ul>
            <li><strong>It doesn't incorporate or register your company.</strong> <a href="incorporation-canada.html">Incorporation</a> is a separate filing with Corporations Canada or a province.</li>
            <li><strong>It isn't FINTRAC approval.</strong> FINTRAC doesn't publish a list of acceptable address types, and it doesn't certify addresses. It can verify what you tell it, and the address you list should describe how your business really operates.</li>
            <li><strong>It isn't a representative for service.</strong> A foreign MSB still needs a person who resides in Canada for that role.</li>
            <li><strong>It doesn't, on its own, make your company resident in Canada for tax.</strong> The <a href="{CA_CRA_RES}" rel="noopener">CRA</a> says a corporation incorporated in Canada after April 26, 1965 is deemed resident. Otherwise, a company is generally resident where its central management and control is actually exercised, which is usually where the board meets. Tax treatment depends on your facts, so take advice from a tax professional.</li>
            <li><strong>It doesn't guarantee a bank account.</strong> We can't promise that a bank will open an account for you.</li>
          </ul>"""),
        ("how", "How it works", """          <ol>
            <li><strong>Consultation.</strong> Your plans for Canada and how you'll use the address.</li>
            <li><strong>Written scope.</strong> What's included, including mail handling.</li>
            <li><strong>Registration check.</strong> How the address fits your FINTRAC registration, if you have one or are applying.</li>
            <li><strong>Start.</strong> Your address is ready to use with your banks and partners.</li>
            <li><strong>Monthly.</strong> US$200 per month while you use it.</li>
          </ol>"""),
    ],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("Money services businesses", F_MSB),
             ("FINTRAC, Money Services Business Registry", F_REGISTRY),
             ("Canada Business Corporations Act, s. 19", CA_CBCA_19), ("CBCA, s. 20", CA_CBCA_20),
             ("Corporations Canada, Next steps following incorporation", CA_CC_NEXT),
             ("Ontario Business Corporations Act", CA_OBCA),
             ("CRA, Change a business address", CA_CRA_ADDR), ("CRA, Residency of a corporation", CA_CRA_RES)],
    for_title="Who uses it",
    for_items=[("Foreign money services businesses", "Companies outside Canada that serve customers in Canada."),
               ("Companies opening Canadian operations", "Businesses establishing a presence before hiring locally."),
               ("Start-ups preparing to launch", "Founders who need their Canadian setup in order early.")],
    arts=["address", "one", "register"],
    faqs=[("How much is a Canadian business address?", "US$200 per month."),
          ("Can I use the address on my FINTRAC registration?", "It depends on how you're registered. A foreign MSB registers with a representative for service who resides in Canada, and a physical location in Canada can change a foreign MSB into a domestic MSB. We confirm how the address fits your registration before you use it."),
          ("Is the address my representative for service?", "No. A foreign MSB's representative for service is a person who resides in Canada, which is a separate requirement. Ask us about it in your consultation."),
          ("What happens to mail sent to the address?", "How mail is handled is set out in your written scope."),
          ("Can a P.O. box be my Canadian business address?", "Not as your physical address with the CRA. The CRA says the physical address must be where day-to-day activities take place and can't be a rural route number or a P.O. box. Your mailing address can be different."),
          ("Does a Canadian address make my company tax resident in Canada?", "Not on its own. The CRA says a corporation incorporated in Canada after April 26, 1965 is deemed resident, and other companies are generally resident where their central management and control is exercised. Take advice from a tax professional on your facts.")],
    related=["msb-registration.html", "msb-for-sale.html", "outsourced-compliance-officer.html"],
)

# ------------------------------------------------------------------ MSB for sale
DEEP["msb-for-sale.html"] = dict(
    name="MSB for sale",
    modified="2026-10-25",
    checked="25 October 2026",
    title="Canadian MSB for Sale: Buy a Ready-Made MSB | AML Canada",
    desc="Buy a ready-made Canadian MSB: FINTRAC-registered companies for sale now, from €28,000. Check each one on FINTRAC's registry before you pay.",
    service_type="Acquisition of a FINTRAC-registered money services business",
    offers=[("28000", "EUR", "Registered Canadian MSB for acquisition, starting price")],
    kicker="MSB for sale in Canada: ready-made and FINTRAC-registered",
    h1="A registered Canadian MSB, ready to take over.",
    lede="Buy a ready-made MSB: a Canadian company already registered with FINTRAC as a money services business. From €28,000.",
    hero_price="From €28,000",
    label="MSB · Registered · For sale",
    need="acquire",
    intro=("Buying a company that's already registered with FINTRAC is one way into Canada, if the company's records are clean and the change of ownership is reported on time.",
           ["We sell ready-made MSBs: Canadian companies already registered with FINTRAC as money services businesses, starting from €28,000. The price depends on the company, the services it's registered for and its history.",
            "The registration belongs to the registered business, so the purchase is of the company's shares. A new entity would need its own registration.",
            "We take you through choosing the right company, checking it before you commit, the change of ownership, and the updates FINTRAC has to receive afterwards."]),
    facts=[("Price", "From €28,000", "depending on the company"),
           ("FINTRAC updates", "30 days", "to report changes"),
           ("Registration", "2 years", "then renewed"),
           ("Due diligence", "First", "before you commit")],
    fee=dict(amount="€28,000", unit="starting price · acquisition",
             note="Compliance program, compliance officer and Canadian address are available alongside, at their own fees.",
             items=["A Canadian company registered with FINTRAC as an MSB",
                    "Company records and registration history reviewed with you",
                    "Eligibility of the new owners and directors checked",
                    "Support through the change of ownership",
                    "Updates to FINTRAC within 30 days, including new owners and directors",
                    "Guidance on what the new owners need to provide"]),
    guide=[
        ("available", "Canadian MSBs for sale now", listings_html()),
        ("how", "How to buy an MSB in Canada", """          <ol>
            <li><strong>Consultation.</strong> Your plans: the services you'll offer, your customers and your timeline.</li>
            <li><strong>Matching.</strong> A company registered for the money services you need.</li>
            <li><strong>Due diligence.</strong> Corporate records, registration status and history, and the eligibility of the new owners and directors, reviewed before you commit.</li>
            <li><strong>Bank of Canada.</strong> If the company is also registered under the Retail Payment Activities Act, re-registration before the purchase closes.</li>
            <li><strong>Change of ownership.</strong> The transfer of the company's shares to you.</li>
            <li><strong>FINTRAC updates.</strong> Changes to the registration information, such as owners, directors and compliance officer, reported within 30 days.</li>
          </ol>"""),
        ("check", "What to check before you buy", """          <ul>
            <li>that the registration is active and covers the services you plan to offer;</li>
            <li>when the registration is next due for renewal;</li>
            <li>the company's corporate records, ownership history and any past compliance issues;</li>
            <li>that the new owners and directors are eligible. Under PCMLTFA s.11.11, a business can't be registered if, for example, a director, the chief executive officer, the president or a 20% owner has certain criminal convictions, or if a FINTRAC penalty remains unpaid;</li>
            <li>that the chief executive officer, the president, the directors and anyone owning or controlling 20% or more can provide criminal record checks, with a certified translation for any that aren't in English or French;</li>
            <li>whether the company is also registered with the Bank of Canada as a payment service provider;</li>
            <li>whether provincial requirements apply where you'll operate. Quebec, for example, licenses money services businesses separately.</li>
          </ul>
          <p>Every check is in our <a href="buying-an-msb-canada.html">MSB due-diligence checklist</a>.</p>"""),
        ("registry", "How to check an MSB on FINTRAC's registry", REGISTRY_HOWTO),
        ("rules", "Rules buyers get wrong", RULES_HTML),
        ("rpaa", "If the company is also registered with the Bank of Canada", """          <p>Some MSBs are also registered with the Bank of Canada as payment service providers under the Retail Payment Activities Act. Buying control of such a company is an acquisition of control, so the company must apply again and be re-registered by the Bank before the purchase closes (RPAA s.24). The changes are then reported to FINTRAC within 30 days.</p>"""),
        ("after", "After the purchase", """          <p>The obligations come with the company. The business needs a compliance officer and a compliance program that reflect its new owners and services, and it must report to FINTRAC, keep records and renew its registration every two years. FINTRAC registration doesn't guarantee a bank account or payment partners, which make their own decisions.</p>"""),
        ("compare", "Buying an MSB or registering a new one", """          <div class="table-wrap"><table>
            <thead><tr><th scope="col"></th><th scope="col">Register a new MSB</th><th scope="col">Buy a registered MSB</th></tr></thead>
            <tbody>
              <tr><th scope="row">Our fee</th><td>US$3,500, fixed</td><td>From €28,000</td></tr>
              <tr><th scope="row">Starting point</th><td>A new or existing company of yours</td><td>A company already registered</td></tr>
              <tr><th scope="row">Main wait</th><td>Preparing the application and FINTRAC's review</td><td>Due diligence, the change of ownership and any Bank of Canada re-registration</td></tr>
              <tr><th scope="row">Afterwards</th><td colspan="2">The same obligations: compliance program, reporting, record keeping and renewal</td></tr>
            </tbody>
          </table></div>
          <p>Our <a href="buy-or-register-msb-canada.html">buy or register an MSB</a> page compares the two routes in full.</p>"""),
    ],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("Update, renew or cancel your registration", F_UPD), ("Money services businesses", F_MSB),
             ("FINTRAC MSB registry", F_REGISTRY), ("Who is not eligible to register", F_NOT_ELIGIBLE),
             ("PCMLTFA, section 11.11", L_PCMLTFA), ("Bank of Canada, Acquisitions of control and prescribed changes", B_ACQ)],
    for_title="Who buys",
    for_items=[("Foreign payment businesses", "Entering Canada through an existing registered company."),
               ("Groups adding a Canadian entity", "A registered company to sit alongside existing operations."),
               ("Founders who prefer an existing company", "A company with a registration history they can review before committing.")],
    arts=["one", "register", "many"],
    faqs=[("What is a ready-made MSB?", "A Canadian corporation, usually newly incorporated and with no trading history, that is already registered with FINTRAC as a money services business. You buy all its shares, and the registration stays with the company."),
          ("Is this an MSB licence for sale?", "There's no federal MSB licence. What's for sale is a company holding a FINTRAC MSB registration, which is often called an MSB licence and is renewed every two years. Quebec licenses money services businesses separately."),
          ("How much does a registered MSB cost?", "Acquisitions start from €28,000. The price depends on the company, the services it's registered for and its history."),
          ("Does the FINTRAC registration stay with the company?", "The registration belongs to the registered business, so the purchase is of the company's shares; a new entity would need its own registration. After the purchase, FINTRAC must be told about changes to the registration information, such as new owners and directors, within 30 days."),
          ("Do the new owners need criminal record checks?", "FINTRAC asks for criminal record checks for the chief executive officer, the president, the directors and anyone owning or controlling 20% or more of the business. Any check that isn't in English or French needs a translation attested by a certified translator."),
          ("What if the company is registered with the Bank of Canada too?", "Then it must apply again and be re-registered by the Bank before the purchase closes. We check this during due diligence."),
          ("Does it come with a bank account?", "FINTRAC registration doesn't guarantee banking or payment partners. We discuss what each company has in place before you commit."),
          ("Can a buyer outside Canada acquire an MSB?", "Yes. Foreign buyers can acquire a registered Canadian company, subject to the same FINTRAC requirements."),
          ("Which MSBs are available right now?", "The companies listed on this page: one Ontario and two British Columbia companies, all registered with FINTRAC for foreign exchange, money transferring and virtual currency, with no trading history. Names and registration numbers are shared under NDA."),
          ("How can I verify a company before I pay?", "Ask for its legal name and MSB registration number, then search FINTRAC's public MSB registry and check that the status is Registered and the services and expiry date match what you've been told.")],
    related=["buy-or-register-msb-canada.html", "msb-registration.html", "outsourced-compliance-officer.html"],
)

# ------------------------------------------------------------------ buy or register an MSB (hub)
DEEP["buy-or-register-msb-canada.html"] = dict(
    name="Buy or register an MSB",
    modified="2026-10-25",
    checked="25 October 2026",
    title="How to Open an MSB in Canada: Buy or Register | AML Canada",
    desc="Two ways to open an MSB in Canada: register your own with FINTRAC for US$3,500, or buy a registered company from €28,000. For founders in Canada and abroad.",
    service_type="FINTRAC money services business registration or acquisition",
    timing="1 week to 7 months (new registration)",
    offers=[("3500", "USD", "New FINTRAC MSB registration, fixed fee"), ("28000", "EUR", "Ready-made FINTRAC-registered Canadian MSB, starting price")],
    kicker="Open an MSB in Canada: buy one or register your own",
    h1="Two ways to a FINTRAC-registered MSB.",
    lede="Buy a Canadian company already registered with FINTRAC from €28,000, or register your own for a fixed US$3,500. For crypto, foreign exchange, remittance and payment businesses, in Canada or abroad.",
    hero_price="From US$3,500 · ready-made from €28,000",
    label="MSB · Buy or register",
    need="acquire",
    intro=("There are two ways to open a money services business (MSB) in Canada: register a company of your own with FINTRAC, or buy one that's already registered. We do both.",
           ["To register a new MSB, we prepare and submit the FINTRAC registration for your company, new or existing, for a fixed US$3,500. FINTRAC doesn't charge to register. See <a href=\"msb-registration.html\">MSB registration</a>.",
            "To buy a ready-made MSB, you acquire the shares of a Canadian company already registered with FINTRAC, from €28,000, and we report the change of ownership to FINTRAC within 30 days. See <a href=\"msb-for-sale.html\">MSB for sale</a>.",
            "Both routes cover the same money services, such as foreign exchange dealing, remitting or transmitting funds, and dealing in virtual currency. Both can be handled without travelling to Canada. Most of our MSB clients are outside Canada, in places such as the UAE, India, Cyprus, Germany, Turkey and Ukraine."]),
    facts=[("New registration", "US$3,500", "fixed fee, no FINTRAC fee"),
           ("Ready-made MSB", "From €28,000", "depending on the company"),
           ("FINTRAC review", "1 week to 7 months", "in our experience"),
           ("Capital", "No minimum", "for FINTRAC registration")],
    fee=dict(amount="US$3,500", unit="new registration · fixed fee",
             note="Or buy a registered company from €28,000. Compliance program, compliance officer, incorporation and Canadian address are available with either route, at their own fees.",
             items=["Advice on which route fits your services, markets and timeline",
                    "New route: assessment, application prepared, submitted and followed up with FINTRAC",
                    "Ready-made route: a company registered for the services you need, reviewed with you before you commit",
                    "Ownership, director and criminal record check requirements coordinated, including certified translations",
                    "FINTRAC updates within 30 days after a change of ownership",
                    "Foreign MSB requirements, including your representative for service in Canada"]),
    guide=[
        ("answer", "The short answer", """          <p>Registering a new MSB costs our fixed fee of US$3,500, with no FINTRAC fee, and FINTRAC's review has taken from about a week to seven months in our experience. Buying a ready-made MSB starts from €28,000 and skips the new application, but you take on the company's history, so due diligence comes first. Either way, the business needs a compliance officer and a compliance program before it operates.</p>"""),
        ("compare", "Ready-made or new: side by side", """          <div class="table-wrap"><table>
            <thead><tr><th scope="col"></th><th scope="col">Register a new MSB</th><th scope="col">Buy a ready-made MSB</th></tr></thead>
            <tbody>
              <tr><th scope="row">Our fee</th><td>US$3,500, fixed. FINTRAC charges nothing</td><td>From €28,000, depending on the company</td></tr>
              <tr><th scope="row">Company</th><td>Yours, new or existing. We can <a href="incorporation-canada.html">incorporate one</a> for US$1,500</td><td>A Canadian company already registered with FINTRAC</td></tr>
              <tr><th scope="row">Main wait</th><td>Preparing the application and FINTRAC's review. FINTRAC says most complete applications are processed within three months</td><td>Due diligence, the share transfer and, if the company is also a registered PSP, Bank of Canada re-registration before closing</td></tr>
              <tr><th scope="row">History</th><td>A clean start</td><td>The company's registration history and records come with it</td></tr>
              <tr><th scope="row">Suits</th><td>Founders who want their own structure from day one</td><td>Founders who want a company already on the FINTRAC registry</td></tr>
              <tr><th scope="row">Afterwards</th><td colspan="2">The same obligations: compliance program, compliance officer, reporting, record keeping and renewal every two years</td></tr>
            </tbody>
          </table></div>"""),
        ("ready-made", "Buying a ready-made MSB", f"""          <p>A FINTRAC registration belongs to the registered business, so you buy the company's shares rather than the registration itself. Before you commit, check that the registration is active and covers the services you plan to offer, when it's next due for renewal, and the company's records and compliance history. You can confirm any company's status on <a href="{F_REGISTRY}" rel="noopener">FINTRAC's public MSB registry</a>.</p>
          <p>The companies currently available are listed on <a href="msb-for-sale.html#available">MSB for sale</a>. The price depends on the company, the services it's registered for and its history. After the purchase, new owners, directors and the compliance officer are reported to FINTRAC within 30 days. Every check is in our <a href="buying-an-msb-canada.html">MSB due-diligence checklist</a>.</p>"""),
        ("new", "Registering a new MSB", """          <p>We work out which of your services are money services, gather and check everything FINTRAC asks for, submit the application with your approval and answer FINTRAC's questions until it's decided. If FINTRAC asks for clarification, the answer is due within 30 days. Criminal record checks from several countries usually take longest, so we start them first. Our guide on <a href="how-to-register-msb-canada.html">how to register an MSB in Canada</a> covers each step.</p>"""),
        ("abroad", "Setting up from outside Canada", """          <ul>
            <li><strong>MSB or foreign MSB.</strong> A business with a place of business in Canada registers as an MSB. A business abroad that directs and provides money services to people in Canada registers as a foreign MSB and names a representative for service who resides in Canada. See our <a href="foreign-msb-registration-canada.html">foreign MSB guide</a>.</li>
            <li><strong>Directors.</strong> Ontario corporations don't need resident Canadian directors. Federal corporations need at least 25% resident Canadian directors, or at least one if there are fewer than four.</li>
            <li><strong>Criminal record checks.</strong> FINTRAC asks for them for the chief executive officer, the president, the directors and anyone owning or controlling 20% or more. Any check that isn't in English or French needs a translation attested by a certified translator.</li>
            <li><strong>Address and documents.</strong> We provide a <a href="canadian-address.html">Canadian business address</a> and can arrange <a href="apostille-notarization-canada.html">notarization and apostilles</a> for Canadian corporate documents you need abroad.</li>
            <li><strong>No travel.</strong> Registration is filed online and we work by video call and email, so you don't need to come to Canada.</li>
          </ul>"""),
        ("activities", "Crypto, foreign exchange, remittance and payments", """          <ul>
            <li><strong>Crypto.</strong> Dealing in virtual currency is a money service. Crypto MSBs also report virtual currency receipts of $10,000 or more and follow the travel rule. Trading platforms may also deal with provincial securities regulators. See <a href="crypto-registration-canada.html">crypto registration in Canada</a>.</li>
            <li><strong>Foreign exchange and remittance.</strong> Foreign exchange dealing and remitting or transmitting funds are money services. If you buy a ready-made MSB, choose one registered for these services, or plan the registration update with us.</li>
            <li><strong>Payments.</strong> A business that holds funds for its users or transfers funds at their request may also need to register with the Bank of Canada under the Retail Payment Activities Act. See <a href="rpaa-vs-fintrac-msb-registration.html">RPAA vs FINTRAC MSB registration</a>.</li>
            <li><strong>Quebec.</strong> Quebec licenses money services businesses separately through Revenu Québec.</li>
          </ul>"""),
        ("banking", "Banking: what to expect", """          <p>FINTRAC registration doesn't come with a bank account and doesn't guarantee one. Banks and payment partners make their own decisions, and they look closely at your compliance program, your compliance officer and where your customers are. With a ready-made MSB, we tell you what each company has in place before you commit.</p>"""),
        ("not-for", "Who this isn't for", """          <ul>
            <li>Businesses that need a licence to take deposits or lend. FINTRAC registration isn't a banking licence.</li>
            <li>Anyone hoping a registration alone will open bank accounts or payment rails.</li>
            <li>Owners or directors who can't provide criminal record checks, or who have the convictions that make a business ineligible under PCMLTFA s.11.11.</li>
            <li>Anyone not ready to run a compliance program from the day they operate.</li>
          </ul>"""),
        ("after", "After you're registered", """          <p>Registration is valid for two years and must be renewed before it expires, and changes to your registration information are reported within 30 days. From the day you operate you need a compliance officer, a written <a href="compliance-programs.html">compliance program</a>, client identification, record keeping and reporting to FINTRAC. We can act as your <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> and prepare your program at the same time as the registration or purchase.</p>"""),
    ],
    sources=[("FINTRAC, Money services businesses", F_MSB), ("Register your MSB or FMSB", F_REG), ("Update, renew or cancel your registration", F_UPD),
             ("FINTRAC MSB registry", F_REGISTRY), ("PCMLTFA", L_PCMLTFA), ("Bank of Canada, Acquisitions of control and prescribed changes", B_ACQ),
             ("Bank of Canada, Retail payments", B_RPS)],
    for_title="Which route people choose",
    for_items=[("Foreign payment and crypto businesses", "Often buy a ready-made MSB to start from a company already on the FINTRAC registry."),
               ("Founders with their own structure", "Usually register a new MSB in a company they own, incorporated in Ontario or federally."),
               ("Groups adding Canada", "Choose either route, depending on timing and whether they want a company with history.")],
    arts=["register", "one", "address"],
    faqs=[("Can a foreigner own an MSB in Canada?", "Yes. Owners and directors can live outside Canada. A business abroad that serves people in Canada registers as a foreign MSB and names a representative for service who resides in Canada."),
          ("Do I need a Canadian resident director?", "Not for an Ontario corporation. A federal corporation needs at least 25% resident Canadian directors, or at least one if it has fewer than four."),
          ("How much does it cost to buy or register an MSB in Canada?", "Registering a new MSB is our fixed fee of US$3,500, and FINTRAC charges nothing. Ready-made MSBs start from €28,000, depending on the company."),
          ("How long does each route take?", "FINTRAC says most complete applications are processed within three months. In our experience new registrations have taken from about a week to seven months. A ready-made purchase depends on due diligence, the share transfer and any Bank of Canada re-registration, and we give you a timeline for the specific company."),
          ("Is there a minimum capital requirement for an MSB?", "FINTRAC registration has no minimum capital requirement. Banks and payment partners may set their own expectations."),
          ("Is an MSB a licence?", "It's a registration with FINTRAC, often called an MSB licence. It's renewed every two years."),
          ("Does the FINTRAC registration transfer with the company?", "The registration belongs to the registered business, so buying the company's shares keeps it. New owners, directors and other changes are reported to FINTRAC within 30 days."),
          ("Can I use a ready-made MSB for crypto?", "Choose a company registered for dealing in virtual currency, or plan the registration update with us. Crypto trading platforms may also deal with provincial securities regulators."),
          ("Does a ready-made MSB come with a bank account?", "FINTRAC registration doesn't guarantee banking. We tell you what each company has in place before you commit."),
          ("Can the whole process be done remotely?", "Yes. Registration is filed online and we work by video call and email. You don't need to travel to Canada."),
          ("Do I also need Bank of Canada registration?", "If you hold funds for users or transfer funds at their request, you may also need to register as a payment service provider under the RPAA.")],
    related=["msb-registration.html", "msb-for-sale.html", "outsourced-compliance-officer.html"],
)

# ------------------------------------------------------------------ RPAA registration
DEEP["rpaa-registration.html"] = dict(
    name="RPAA registration",
    title="RPAA PSP Registration with the Bank of Canada | AML Canada",
    desc="Register as a payment service provider (PSP) with the Bank of Canada under the RPAA. Fixed fee US$3,500, plus the Bank's own application fee.",
    service_type="Bank of Canada RPAA payment service provider registration",
    timing="Often 2 to 8 months (not guaranteed)",
    offers=[("3500", "USD", "RPAA PSP registration with the Bank of Canada, fixed fee (excludes the Bank's application fee)")],
    h1="RPAA registration with the Bank of Canada.",
    lede="Retail Payment Activities Act (RPAA) registration for payment service providers. Fixed fee US$3,500, plus the Bank's application fee.",
    hero_price="Fixed fee · US$3,500",
    label="PSP · RPAA · Registered",
    need="rpaa",
    intro=("Payment service providers that perform retail payment activities for people and businesses in Canada must register with the Bank of Canada under the Retail Payment Activities Act (RPAA).",
           ["Payment processors, digital wallets, money transfer apps and similar businesses fall under the Bank's supervision. A new payment service provider (PSP) must be registered before it starts retail payment activities, so plan your launch around the Bank's review.",
            "We confirm whether the RPAA applies to you, prepare the application with you, and help you answer the Bank's questions during its review.",
            "Our fee is a fixed US$3,500. The Bank of Canada charges its own one-time application fee, which you pay directly to the Bank."]),
    facts=[("Our fee", "US$3,500", "fixed, one time"),
           ("Bank of Canada fee", "CA$2,500", "when introduced; indexed each January"),
           ("Typical timing", "2 to 8 months", "often, not guaranteed"),
           ("Before launch", "Registration", "new PSPs wait for the Bank")],
    fee=dict(amount="US$3,500", unit="fixed fee · plus the Bank of Canada application fee",
             note="The Bank's application fee is non-refundable and paid to the Bank. It was CA$2,500 when introduced in November 2024 and is indexed to inflation each January under the Retail Payment Activities Regulations; we confirm the current amount before you apply. RPAA compliance program documents are a separate fixed fee of US$3,500.",
             items=["Assessment of whether the RPAA applies to your activities",
                    "Registration application prepared with you",
                    "Your payment activities, agents, mandataries and third parties described",
                    "Support through the Bank's questions and any national security review",
                    "Coordination with your FINTRAC registration, where you need both"]),
    guide=[
        ("who", "Does the RPAA apply to you?", """          <p>The Act covers businesses that perform payment functions for end users as a service or business activity, such as holding accounts or funds for end users, initiating, authorizing or transmitting electronic funds transfers, and providing clearing or settlement services. A PSP with a place of business in Canada is covered. A PSP outside Canada is covered when it directs retail payment activities at people or entities in Canada and performs them for end users in Canada (RPAA s.5). Foreign firms often need FINTRAC registration as well; see our <a href="foreign-msb-registration-canada.html">foreign MSB registration guide</a>.</p>
          <p>Banks and some other institutions are excluded, and some activities fall outside the Act, so we confirm where you stand before preparing anything. Our guide on <a href="who-must-register-psp-rpaa.html">who must register as a PSP</a> works through the test, and our <a href="rpaa-registration-guide.html">step-by-step guide to applying for RPAA registration</a> covers the application itself.</p>"""),
        ("fees", "What it costs", """          <p>Our fee is a fixed US$3,500. The Bank's one-time, non-refundable application fee was CA$2,500 when it was introduced in November 2024 and is indexed to inflation each January, so we confirm the current amount before you apply.</p>
          <p>The Bank also plans to charge registered PSPs annual assessment fees to recover its supervision costs. It isn't charging them yet and will start once the cost-recovery regulations are finalized.</p>"""),
        ("process", "How we handle your application", """          <ol>
            <li><strong>Assessment.</strong> Which of your activities are retail payment activities, and whether you need FINTRAC registration as well.</li>
            <li><strong>Preparation.</strong> Your business, ownership, payment activities, agents, mandataries and third-party providers, gathered and checked.</li>
            <li><strong>Application.</strong> Completed in PSP Connect, the Bank of Canada's online portal, and submitted with the application fee.</li>
            <li><strong>Review.</strong> The Bank shares applications with the Department of Finance and FINTRAC, and the Minister of Finance can order a national security review. We help you answer questions along the way.</li>
            <li><strong>Decision.</strong> Once registered, your business is listed in the Bank's public registry of PSPs.</li>
          </ol>
          <p>In our experience the process often takes 2 to 8 months, though that isn't guaranteed. A new PSP can't start retail payment activities until the Bank registers it, so we plan the timeline with you from the start.</p>"""),
        ("after", "After registration", """          <p>Registered PSPs need a <a href="rpaa-compliance-frameworks.html">risk management and incident response framework</a> and, if they hold end-user funds, a safeguarding framework. They also report incidents, changes and an annual report to the Bank. Our <a href="rpaa-compliance-program.html">RPAA compliance program</a> sets these up for a fixed US$3,500.</p>"""),
        ("fintrac", "RPAA and FINTRAC: do you need both?", """          <p>Often, yes. A payment business that remits or transmits funds usually needs FINTRAC registration as an MSB as well. The Bank's regime deals with operational risk and the safety of users' funds, and FINTRAC's with money laundering, terrorist financing and sanctions evasion. We can prepare both registrations together.</p>"""),
    ],
    sources=[("Bank of Canada, Retail payments", B_RPS), ("Supervisory framework", B_FW), ("Frequently asked questions about retail payments supervision", B_REG),
             ("Registration application fee", B_FEE), ("Criteria for registering PSPs", B_CRIT), ("Registry of payment service providers", B_REGISTRY)],
    for_title="Who it's for",
    for_items=[("Payment processors and wallets", "Businesses that hold, move or process funds for end users."),
               ("Foreign PSPs serving Canada", "Providers abroad with end users in Canada."),
               ("MSBs that also process payments", "Businesses that need both FINTRAC and Bank of Canada registration.")],
    arts=["register", "many", "address"],
    faqs=[("How much does RPAA registration cost?", "Our fee is a fixed US$3,500. The Bank of Canada also charges a one-time, non-refundable application fee, which was CA$2,500 when introduced in November 2024 and is indexed to inflation each January. We confirm the current amount before you apply."),
          ("Is the Bank of Canada fee included in your price?", "No. The application fee is paid directly to the Bank and isn't part of our US$3,500."),
          ("Do foreign payment service providers have to register?", "Yes, if they direct retail payment activities at people or entities in Canada and perform them for end users in Canada."),
          ("Do I also need to register with FINTRAC?", "Often. If you also provide money services, such as remitting or transmitting funds, you need FINTRAC registration as an MSB too."),
          ("How long does RPAA registration take?", "In our experience it often takes 2 to 8 months, including any national security review. That isn't guaranteed, and a new PSP can't start retail payment activities until it's registered."),
          ("What happens after registration?", "You need risk management, incident response and, if you hold end-user funds, safeguarding frameworks, plus incident notices, change notices and annual reports. Our RPAA compliance program covers these."),
          ("Is RPAA registration a licence?", "No. The Bank of Canada registers payment service providers under the RPAA and says it doesn't license or endorse them. There is no PSP licence in Canada."),
          ("Where do I apply for RPAA registration?", "Online, through PSP Connect, the Bank of Canada's portal for payment service providers. The application, the fee and the Bank's questions all go through it."),
          ("Can I operate while my RPAA application is under review?", "Not if you applied on or after 8 September 2025: the Bank says those applicants may not start retail payment activities until they're registered. PSPs that applied during the transition period, before that date, can keep operating until the Bank decides.")],
    related=["rpaa-compliance-program.html", "msb-registration.html", "outsourced-compliance-officer.html"],
)

# ------------------------------------------------------------------ RPAA compliance program
DEEP["rpaa-compliance-program.html"] = dict(
    guides=['rpaa-outsourcing-risk-management-psp.html', 'rpaa-business-continuity-testing.html', 'rpaa-compliance-frameworks.html', 'rpaa-safeguarding-end-user-funds.html', 'rpaa-incident-reporting.html', 'rpaa-annual-report.html'],
    name="RPAA compliance program",
    title="RPAA Compliance Program for PSPs | AML Canada",
    desc="RPAA frameworks for PSPs: governance, risk registers, incident response, third parties, safeguarding, cyber and continuity, annual reports. Fixed fee US$3,500.",
    service_type="RPAA compliance program and frameworks for payment service providers",
    offers=[("3500", "USD", "Compliance program for payment service providers, built to the Bank of Canada's RPAA requirements, fixed fee")],
    kicker="RPAA compliance program for payment service providers",
    h1="RPAA frameworks built around your payment flows.",
    lede="Risk management, incident response and safeguarding frameworks for payment service providers. Fixed fee US$3,500.",
    hero_price="Fixed fee · US$3,500",
    label="RPAA · Framework · 7 of 7",
    need="rpaa",
    intro=("Registration with the Bank of Canada comes first. Since September 8, 2025, payment service providers must also have frameworks for risk management, incident response and safeguarding end-user funds.",
           ["We write a compliance program built to the Bank's requirements around your payment flows, systems, providers and team, so the frameworks describe what you do and your people can follow them.",
            "The program covers seven areas, from senior officer governance to annual reports and change notices, for a fixed fee of US$3,500."]),
    facts=[("Fee", "US$3,500", "fixed, seven frameworks"),
           ("In force", "Sept 8, 2025", "frameworks required"),
           ("Incidents", "48 hours", "at most, once found material"),
           ("Changes", "30 days", "after most registration changes")],
    fee=dict(amount="US$3,500", unit="fixed fee · program documents",
             note="Ongoing support, such as preparing your annual report, can be covered by outsourced compliance officer hours.",
             items=["Senior officer and governance",
                    "Risk framework and registers",
                    "Incident response",
                    "Third parties and agents",
                    "Safeguarding",
                    "Cyber, IT and continuity",
                    "Annual report and change notices"]),
    guide=[
        ("includes", "What an RPAA compliance program includes", """          <p>The <a href="https://laws-lois.justice.gc.ca/eng/acts/R-7.36/FullText.html" rel="noopener">Retail Payment Activities Act</a> (RPAA) and the <a href="https://laws-lois.justice.gc.ca/eng/regulations/SOR-2023-229/FullText.html" rel="noopener">Retail Payment Activities Regulations</a> set out what a registered payment service provider (PSP) must have in place. If you're not sure the RPAA applies to you, start with <a href="who-must-register-psp-rpaa.html">who must register as a PSP</a>.</p>
          <ol>
            <li><strong>A risk management and incident response framework.</strong> Every PSP needs one in writing (RPAA s.17(1); Regulations ss.5 to 9). It's reviewed at least once a year and before any material change, and everyone with a role in it is trained. See our guide to the <a href="rpaa-compliance-frameworks.html">RPAA risk management framework</a>.</li>
            <li><strong>Safeguarding of end-user funds, if you hold them.</strong> A PSP that holds end-user funds also needs a safeguarding-of-funds framework (RPAA s.20(1); Regulations ss.15 to 17). See <a href="rpaa-safeguarding-end-user-funds.html">RPAA safeguarding of end-user funds</a>.</li>
            <li><strong>Incident notices.</strong> When an incident has a material impact, you notify the Bank and each materially affected end user, PSP or designated clearing house without delay (RPAA s.18). The Bank's guideline sets the outer limit at 48 hours after you determine the incident is material. See <a href="rpaa-incident-reporting.html">RPAA incident reporting</a>.</li>
            <li><strong>Significant change notices.</strong> At least five business days before a significant change or new activity (Regulations s.20).</li>
            <li><strong>An annual report.</strong> Due by March 31 for the previous calendar year (RPAA s.21; Regulations s.18). See <a href="rpaa-annual-report.html">the RPAA annual report</a>.</li>
            <li><strong>Records.</strong> Records sufficient to show you comply, kept until five years after the day they stop showing current compliance (Regulations s.40).</li>
            <li><strong>Independent review.</strong> At least every three years for the risk framework if you have an internal or external auditor (Regulations s.10), and for safeguarding if you hold end-user funds (Regulations s.17).</li>
          </ol>
          <p>The schedule to the regulations classifies a breach of section 17(1) of the Act, read with section 5 of the regulations, as a very serious violation, with a penalty of up to $10,000,000 (Regulations s.48(1)(b)). Many payment businesses also need FINTRAC registration and an AML compliance program. See <a href="rpaa-vs-fintrac-msb-registration.html">RPAA vs FINTRAC MSB registration</a>.</p>
          <p>The sections below set out the seven areas our program documents cover.</p>"""),
        ("governance", "Senior officer and governance", """          <p>Clear roles and responsibilities, with a senior officer accountable for the frameworks, and enough resources to run them. We set out who owns each framework, how it's approved and reviewed, and how issues reach senior management.</p>"""),
        ("risk", "Risk framework and registers", """          <p>The Bank expects PSPs to identify their operational risks, protect against them, detect problems, and respond and recover, with periodic review and testing. We build your risk framework and the registers behind it: the risks in your payment activities, the controls that address them and who is responsible. Our guide to the <a href="rpaa-compliance-frameworks.html">RPAA risk management and incident response framework</a> sets out what section 5 of the regulations requires.</p>"""),
        ("incident", "Incident response", """          <p>When something goes wrong, your team needs to know what to do. The framework covers how incidents are identified, escalated, contained and recovered from. When you determine that an incident has a material impact, you notify the Bank and any affected end users, PSPs and clearing houses without delay, and no later than 48 hours after that determination.</p>"""),
        ("third-parties", "Third parties and agents", """          <p>Many PSPs depend on processors, banks, cloud providers and others, and some act through agents or mandataries. The framework covers how you assess and manage the risks they bring. Foreign PSPs also identify the agents or mandataries acting for them in Canada.</p>"""),
        ("safeguarding", "Safeguarding end-user funds", """          <p>If you hold end-user funds, you must safeguard them, either in a trust account, or in a segregated account protected by insurance or a guarantee. Your written safeguarding framework explains how end users get timely access to their funds and how funds would be paid out if your business became insolvent. Our guide to <a href="rpaa-safeguarding-end-user-funds.html">RPAA safeguarding of end-user funds</a> covers the requirements in detail, and our guide to the <a href="rpaa-safeguarding-legal-opinion-trust-account.html">trust account legal opinion</a> covers what the Bank asks for.</p>"""),
        ("cyber", "Cyber, IT and continuity", """          <p>Protecting the integrity, confidentiality and availability of your systems and data, detecting cyber threats, and keeping payments running, or restoring them quickly, when systems or providers fail.</p>"""),
        ("review-records", "Independent review and records", """          <p>If you have an internal or external auditor, section 10 of the regulations requires an independent review of your risk management and incident response framework at least once every three years. It's carried out by a sufficiently skilled individual who has had no role in establishing, implementing or maintaining the framework, and the gaps it finds are reported to the senior officer, if you have one. A PSP that holds end-user funds needs an independent review of its safeguarding at least every three years regardless (section 17).</p>
          <p>Section 40 requires records sufficient to show that you comply with the Act and regulations. You keep them until five years after the day they stop showing current compliance. Section 42 extends the rules to records held by your agents and third-party service providers.</p>"""),
        ("reporting", "Annual report and change notices", """          <p>PSPs file an annual report with the Bank no later than March 31 of the following year. The Bank lists its contents as up-to-date information on risk management and incident response, safeguarding of end-user funds where that applies, and certain financial and activity metrics.</p>
          <p>Changes to registration information are generally notified within 30 days after they happen, and certain changes at least 30 or 60 days before they take effect (Retail Payment Activities Regulations, ss.35 and 36). A significant change or new activity needs notice at least five business days before. An acquisition of control needs a new application, approved by the Bank before the acquisition closes (RPAA s.24). The framework sets out how you track, prepare and approve each of these.</p>"""),
    ],
    sources=[("Bank of Canada, Supervisory framework", B_FW), ("Retail payments", B_RPS), ("Reminder: PSP reporting obligations under the RPAA", B_REPORTING),
             ("Acquisitions of control and prescribed changes", B_ACQ), ("Retail Payment Activities Regulations", L_RPAR),
             ("Retail Payment Activities Act", "https://laws-lois.justice.gc.ca/eng/acts/R-7.36/FullText.html")],
    for_title="Who it's for",
    for_items=[("Newly registered PSPs", "Putting the Bank's frameworks in place for the first time."),
               ("PSPs that hold customer funds", "Safeguarding arrangements that need to be written down and tested."),
               ("Growing payment businesses", "New products, partners or markets that the frameworks didn't cover.")],
    arts=["programme", "scan", "many"],
    faqs=[("What does the RPAA require from payment service providers?", "Risk management and incident response frameworks, safeguarding of end-user funds where you hold them, incident notices within 48 hours of determining an incident is material, change notices, and an annual report by March 31."),
          ("How much does an RPAA compliance program cost?", "A fixed US$3,500 for the program documents covering all seven areas."),
          ("Is an independent review of the RPAA framework always required?", "Only for PSPs that have an internal or external auditor, at least every three years. A PSP that holds end-user funds needs an independent review of safeguarding compliance at least every three years regardless."),
          ("Is this the same as our FINTRAC AML program?", "No. The RPAA program covers operational risk and safeguarding under the Bank of Canada. A FINTRAC compliance program covers money laundering, terrorist financing and sanctions evasion. Many payment businesses need both."),
          ("Do you help us put the frameworks in place?", "Yes. We write them around how you operate and walk your team through them. Ongoing support can be covered by outsourced compliance officer hours.")],
    related=["rpaa-registration.html", "outsourced-compliance-officer.html", "compliance-programs.html"],
)

# ------------------------------------------------------------------ effectiveness reviews (scoped)
F_WHO = "https://fintrac-canafe.canada.ca/reporting-declaration/info/re-ed-eng"
L_R156 = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2002-184/section-156.html"
L_A96 = "https://laws-lois.justice.gc.ca/eng/acts/P-24.501/section-9.6.html"
L_AMPR = "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2007-292/FullText.html"
DEEP["effectiveness-reviews.html"] = dict(
    name="Effectiveness reviews",
    modified="2026-11-23",
    title="FINTRAC Effectiveness Review & AML Audit (Two-Year) | AML Canada",
    desc="The FINTRAC two-year effectiveness review, often called an AML audit: your policies, risk assessment and training tested, with written findings.",
    service_type="Compliance program effectiveness review",
    offers=[],
    kicker="FINTRAC two-year effectiveness review and AML audit",
    h1="Find the gaps before an examiner does.",
    lede="The two-year effectiveness review FINTRAC requires, and preparation for a FINTRAC examination.",
    hero_price="Scoped to your business",
    label="Gap found · Review",
    flag=True,
    need="review",
    intro=("Every business FINTRAC regulates must review the effectiveness of its compliance program at least every two years.",
           ["An effectiveness review, often called an AML audit, tests whether your policies and procedures, risk assessment and training work day to day, and whether what your team does matches what your documents say.",
            "We also help you prepare for a FINTRAC examination: what to expect, what to have ready and what to fix first. The fee depends on the size and complexity of your business, and is agreed in your written scope."]),
    facts=[("How often", "Every 2 years", "at a minimum"),
           ("Covers", "3 parts", "policies, risk assessment, training"),
           ("Tests", "Daily work", "against your documents"),
           ("Fee", "Scoped", "agreed in writing")],
    fee=dict(amount="Scoped", unit="quoted after your consultation",
             note="Depends on your size, products and the number of files to test.",
             items=["A scoped review, agreed in writing",
                    "Testing of what happens against what's written",
                    "Written findings and recommendations, in order of priority",
                    "Help preparing records and your team for an examination"]),
    guide=[
        ("audit", "AML audit in Canada: what it usually means", """          <p>When a business, or its bank, asks for an AML audit in Canada, what it usually needs is the two-year effectiveness review FINTRAC requires. Businesses and banks often call it an AML audit or an independent AML review. FINTRAC's guidance doesn't use the term AML audit. Its term is the <strong>two-year effectiveness review</strong>: an evaluation that tests whether your compliance program works, and whether it has gaps or weaknesses that could stop you detecting and preventing money laundering, terrorist financing and sanctions evasion.</p>"""),
        ("who-needs", "Who needs an effectiveness review", f"""          <p>Every business FINTRAC regulates. <a href="{L_A96}" rel="noopener">Section 9.6(1) of the PCMLTFA</a> requires every person or entity referred to in section 5 of the Act to have a compliance program, and <a href="{L_R156}" rel="noopener">PCMLTFR s. 156(1)(f) and (3)</a> make a documented review plan and a review every two years part of that program. <a href="{F_WHO}" rel="noopener">FINTRAC's list of reporting entities</a> includes:</p>
          <ul>
            <li>money services businesses and foreign money services businesses;</li>
            <li>financial entities, such as banks, credit unions, caisses populaires, trust companies and loan companies;</li>
            <li>securities dealers;</li>
            <li>life insurance companies, brokers and agents;</li>
            <li>real estate brokers, sales representatives and developers (when carrying out certain activities);</li>
            <li>mortgage administrators, brokers and lenders;</li>
            <li>dealers in precious metals and precious stones;</li>
            <li>casinos;</li>
            <li>accountants and accounting firms, and British Columbia notaries public and notary corporations (when carrying out certain activities for clients);</li>
            <li>agents of the Crown that sell money orders, and armoured car businesses;</li>
            <li>cheque cashers, factors, and financing or leasing entities (since July 10, 2025);</li>
            <li>acquirer services in relation to private automated banking machines, and title insurers (since October 1, 2025).</li>
          </ul>
          <p>Size doesn't change this. A sole proprietor with no employees, agents or others authorized to act for them doesn't need a training program, but still needs the review.</p>"""),
        ("how-often", "How often is an effectiveness review required?", """          <p>At least every two years. FINTRAC requires every reporting entity to review the effectiveness of its compliance program, covering its policies and procedures, risk assessment and ongoing training program and plan, at a minimum once every two years. The review looks at how the program runs day to day as well as what the documents say.</p>
          <p>The timing rule is stricter than many people expect. FINTRAC's guidance says you must start each review no later than 24 months from the <em>start</em> of your previous review, and you must have completed the previous review before you start the next one.</p>"""),
        ("plan", "The review plan you need to document", """          <p>FINTRAC requires you to institute and document a plan for the review, not just carry it out. The plan must include every element of your compliance program, and FINTRAC expects it to set out:</p>
          <ul>
            <li>the scope of the review, and the reasons behind the areas you focus on;</li>
            <li>the time period the review covers;</li>
            <li>the evaluation methods you expect to use, such as staff interviews, record sampling and document review;</li>
            <li>the sample sizes.</li>
          </ul>
          <p>How deep the review goes on each element can vary with the complexity of your business, your transaction volumes, the findings of earlier reviews and your current money laundering, terrorist financing and sanctions evasion risks.</p>"""),
        ("who-reviews", "Who can carry out the review", """          <p>FINTRAC's guidance says the review is carried out, and its results documented, by an internal or external auditor or, if the business has no auditor, by the business itself. Whoever does it should know the requirements of the PCMLTFA and its regulations. As a best practice, FINTRAC says the reviewer should not be someone directly involved in your compliance program, so the review stays impartial. An external review gives you that independence. Whoever carries it out, making sure it happens on time remains your responsibility.</p>"""),
        ("tests", "What a review tests", """          <p>A review checks whether what your team does matches what your documents say, and whether you meet the PCMLTFA. The examples in FINTRAC's guidance include:</p>
          <ul>
            <li>interviews with staff who handle transactions, to test their knowledge of your policies on client identification, record keeping and reporting;</li>
            <li>a sample of client records, to see whether identification procedures were followed and the risk assessment was applied;</li>
            <li>whether ongoing monitoring happens as often as each client's risk level requires, and whether high-risk clients received enhanced measures;</li>
            <li>a review of transactions, to see whether suspicious transactions were reported to FINTRAC;</li>
            <li>whether large cash transactions and electronic funds transfers were reported accurately and on time;</li>
            <li>agreements with agents or mandataries, and a sample of the information they used to verify identity;</li>
            <li>whether your risk assessment reflects your current operations, including clients, products, delivery channels, new technology and geography;</li>
            <li>whether your policies and procedures are up to date with current law and your business practices.</li>
          </ul>"""),
        ("report", "Documenting the results and reporting to a senior officer", """          <p>FINTRAC says the review should record the date it was done, the period it covered, who performed it, the results of the tests, and the conclusions, including any deficiencies, recommendations and action plans.</p>
          <p>If you are an entity, you must also report in writing to a senior officer within 30 days of completing the review. The report covers the review's findings, any updates made to your policies and procedures during the period that were not made because of the review, and the status of implementing those updates.</p>"""),
        ("how-we-run-it", "How we run an AML audit (effectiveness review)","""          <ol>
            <li><strong>Scoping call.</strong> We learn your products, clients, volumes and earlier findings, and agree the scope in writing.</li>
            <li><strong>Written review plan.</strong> Scope, rationale, review period, methods and sample sizes, as FINTRAC expects.</li>
            <li><strong>Document review.</strong> Your policies and procedures, risk assessment, and training program and plan.</li>
            <li><strong>Interviews and sampling.</strong> We talk to the people who do the work and test samples of client files, monitoring and reports.</li>
            <li><strong>Findings.</strong> A written report with deficiencies, recommendations and an action plan, in order of priority, ready for the 30-day report to your senior officer.</li>
          </ol>
          <p>Our <a href="fintrac-effectiveness-review-checklist.html">two-year effectiveness review checklist</a> lists what to gather before a review starts.</p>"""),
        ("vs-exam", "Effectiveness review or FINTRAC examination?", """          <p>An effectiveness review is your own check of your program. A FINTRAC examination is FINTRAC's assessment of your compliance. A recent, honest review, with its findings being fixed, is one of the best ways to prepare for an examination.</p>"""),
    ],
    sources=[("FINTRAC, Compliance program requirements", F_G4), ("FINTRAC, Who must report to FINTRAC", F_WHO),
             ("PCMLTFA, section 9.6", L_A96), ("PCMLTFR, section 156", L_R156),
             ("Administrative Monetary Penalties Regulations", L_AMPR)],
    for_title="Who it's for",
    for_items=[("Reporting entities due a review", "Including businesses whose last review is approaching two years."),
               ("Businesses expecting an examination", "Getting ready before FINTRAC arrives."),
               ("New compliance officers", "Taking stock of a program they've inherited.")],
    arts=["review", "scan", "programme"],
    faqs=[("Is an AML audit the same as a FINTRAC effectiveness review?", "Usually, yes. AML audit is the common name; FINTRAC calls it the two-year effectiveness review. It tests your policies and procedures, risk assessment, and training program and plan."),
          ("How often is an AML effectiveness review required in Canada?", "At least every two years. Each review must start no later than 24 months from the start of the previous one, and the previous review must be finished first."),
          ("Who receives the results?", "If you are an entity, you must report the findings in writing to a senior officer within 30 days of completing the review."),
          ("Can we do the review ourselves?", "FINTRAC's guidance allows a self-review if you have no internal or external auditor, provided whoever does it knows the requirements. An external review adds independence."),
          ("When is our first effectiveness review due?", "Neither the Regulations nor FINTRAC's compliance program guidance sets a date for the first review. The Act requires you to establish and implement a compliance program (PCMLTFA s. 9.6(1)), and a documented plan for the review is one of its elements (PCMLTFR s. 156(1)(f)). The review itself is required every two years (s. 156(3)). If you're unsure, FINTRAC answers questions on requirements at guidelines-lignesdirectrices@fintrac-canafe.gc.ca."),
          ("What if we've missed the two-year deadline?", "Neither the Regulations nor FINTRAC's guidance gives a grace period. The penalty regulations class a breach of PCMLTFR s. 156(1)(f) and (3), the review plan and two-year review, as a very serious violation. In our view, start the review as soon as you can and document it. If you're an entity, the findings still go in writing to a senior officer within 30 days of finishing."),
          ("Can the firm that set up our compliance program also review it?", "The Regulations don't rule it out. They say an internal or external auditor carries out the review, or the business itself if it has no auditor (PCMLTFR s. 156(3)). As a best practice, FINTRAC says the review should not be conducted by someone directly involved in your compliance program activities, so it stays impartial. FINTRAC's guidance doesn't say whether having written the documents counts as direct involvement."),
          ("How is an effectiveness review different from a gap assessment?", "A gap assessment isn't a term FINTRAC's compliance program guidance uses. It usually means comparing your documents with the requirements to find what's missing. The two-year effectiveness review is the review the Regulations require: it follows a documented plan that covers every element of your program and tests whether the program works in practice, using methods such as staff interviews, record sampling and document review."),
          ("What do we receive?", "Written findings and recommendations, in order of priority, so you know what to fix first."),
          ("FINTRAC has contacted us about an examination. Where do we start?", "Book a consultation. We review your program and records with you and help you prepare to show how it works.")],
    related=["compliance-programs.html", "outsourced-compliance-officer.html", "training.html"],
)

# ------------------------------------------------------------------ training (scoped)
F_VIDEOS = "https://fintrac-canafe.canada.ca/training-formation/training-formation-eng"
DEEP["training.html"] = dict(
    checked="23 November 2026",
    name="Training",
    modified="2026-11-23",
    title="FINTRAC AML Training in Canada | AML Canada",
    desc="FINTRAC AML training in Canada for MSB front-line staff, compliance teams and senior management, built to meet FINTRAC's training requirement.",
    service_type="Anti-money laundering (AML) training",
    offers=[],
    kicker="FINTRAC AML training for your team",
    h1="AML training that fits your business and your team.",
    lede="Anti-money laundering training for front-line staff, compliance teams and senior management.",
    hero_price="Scoped to your team",
    label="Staff · Trained · Recorded",
    need="training",
    intro=("If you have employees, agents or others authorized to act for you, a written, ongoing compliance training program is a required part of your compliance program.",
           ["Training works when staff recognize the situation in front of them and know what to do next. We build anti-money laundering (AML) and anti-terrorist financing training around your products, customers and risks.",
            "We train front-line staff, compliance teams and senior management, and help you keep the records that show training happened. The fee depends on your team and is agreed in your written scope."]),
    facts=[("Required", "Yes", "if you have employees or agents"),
           ("Program", "Written + ongoing", "with a delivery plan"),
           ("Audiences", "3", "front line, compliance, management"),
           ("Records", "Kept", "who, what and when")],
    fee=dict(amount="Scoped", unit="quoted after your consultation",
             note="Depends on the number of people, roles and sessions.",
             items=["Training built around your business",
                    "Training for each role: front line, compliance and management",
                    "A written training program and plan",
                    "Training records"]),
    guide=[
        ("training-required", "Is AML training required in Canada?", """          <p>Yes, if you have employees, agents or others authorized to act on your behalf. In that case a written, ongoing compliance training program, with a plan for delivering it, is one of the required elements of a <a href="compliance-programs.html">FINTRAC compliance program</a>. Training should fit your business and your risks, and reach the people who deal with clients or transactions. A sole proprietor with no employees, agents or others authorized to act for them doesn't need a training program.</p>"""),
        ("covers", "What the training covers", f"""          <p>FINTRAC's <a href="{F_G4}" rel="noopener">compliance program guidance</a> says a training program should explain five things to the people who act for you. We build the training around them and around your products, customers and risks.</p>
          <ol>
            <li><strong>Your requirements</strong> under the PCMLTFA and its Regulations.</li>
            <li><strong>Background</strong>, such as the definitions and methods of money laundering and terrorist activity financing.</li>
            <li><strong>Vulnerabilities</strong>: how your business could be used, with indicators and examples.</li>
            <li><strong>Your policies and procedures</strong>, including reporting, record keeping and know your client.</li>
            <li><strong>Roles and responsibilities</strong> in detecting and deterring money laundering and terrorist financing, and when dealing with potentially suspicious activities or transactions.</li>
          </ol>
          <p>Depending on your business, your requirements and policies can include:</p>
          <ul>
            <li>knowing your client: verifying identity, beneficial ownership, and politically exposed persons and heads of international organizations;</li>
            <li>third-party determinations and business relationships;</li>
            <li>ongoing monitoring, and the enhanced measures you apply to high-risk clients;</li>
            <li>sanctions and listed person screening;</li>
            <li>reporting to FINTRAC, including suspicious transactions, and the 24-hour rule;</li>
            <li>record keeping;</li>
            <li>ministerial directives, and how you'll apply new ones;</li>
            <li>travel rule information for funds and virtual currency transfers, where it applies.</li>
          </ul>
          <p>The exact list depends on the kind of business you are and the services you offer.</p>"""),
        ("plan", "What a training plan includes", f"""          <p>You must document a plan for your ongoing training program and for delivering it. FINTRAC's guidance says the plan should cover:</p>
          <ul>
            <li><strong>Who is trained.</strong> Anyone who has contact with clients, is involved in client transactions, handles cash, funds or virtual currency for you, or implements or oversees the compliance program.</li>
            <li><strong>Topics and materials</strong>, and where the training materials come from.</li>
            <li><strong>How training is delivered.</strong> FINTRAC's examples include self-directed learning and e-learning, information sessions, face-to-face meetings, classroom, conferences and on-the-job training.</li>
            <li><strong>How often.</strong> At regular intervals, when certain events happen, or both. Our guide explains <a href="fintrac-training-requirements.html#frequency">how often AML training is required</a>.</li>
          </ul>
          <p>The program should also keep a record of the training delivered, such as the date, the attendees and the topics covered. The program and plan should fit your size, structure and complexity, and your exposure to money laundering, terrorist financing and sanctions evasion risk.</p>"""),
        ("roles", "Training for each role", """          <p>Front-line staff learn to recognize unusual activity, identify clients and know when and how to escalate. Compliance teams cover reviews, reporting, the 24-hour rule and deadlines, and how to document decisions. Senior management covers their responsibilities for the program and how to oversee it.</p>"""),
        ("records", "Training records", """          <p>Being able to show who was trained, on what and when is part of showing your program works. We help you keep those records, ready for your effectiveness review or a FINTRAC examination.</p>"""),
    ],
    sources=[("FINTRAC, Compliance program requirements", F_G4), ("FINTRAC, Videos: learning resources", F_VIDEOS)],
    for_title="When teams book training",
    for_items=[("A new program", "Staff learning a compliance program that has just been written."),
               ("Before a review or examination", "Training and records brought up to date ahead of your effectiveness review or a FINTRAC examination."),
               ("New products or rules", "Training updated when you launch something new or the requirements change.")],
    arts=["training", "many", "programme"],
    faqs=[("Is AML training mandatory in Canada?", "Yes, if you have employees, agents or others authorized to act for you. A sole proprietor with no employees, agents or others acting for them doesn't need a training program."),
          ("Who needs AML training?", "Anyone whose work touches your compliance obligations, typically front-line staff, agents, compliance teams and senior management."),
          ("How often is AML training required?", "Neither the Regulations nor FINTRAC fix an interval. The Regulations require an ongoing training program, and FINTRAC's guidance says your training plan should state how often you train: at regular intervals, such as monthly, semi-annually or annually, when certain events happen, such as before a new employee deals with clients, or both."),
          ("What goes in a training plan?", "FINTRAC says the plan should cover who is trained, the topics and materials, how training is delivered and how often. The program should also keep a record of training delivered, such as the date, the attendees and the topics covered."),
          ("Is there free FINTRAC training?", "FINTRAC publishes videos for reporting entities on its website, on its Videos: learning resources page. They include an introduction to FINTRAC for reporting entities, a series on verifying the identity of a client, a series on suspicious transaction reports and a beneficial ownership webinar. FINTRAC describes them as a general overview of its role with practical guidance. Your training program still needs to explain your own policies and procedures."),
          ("Do you provide training records?", "Yes. We help you keep records of who was trained, on what and when.")],
    related=["compliance-programs.html", "effectiveness-reviews.html", "outsourced-compliance-officer.html"],
)


# ================================================================== guides (articles)
# Each guide targets one informational search intent and hands off to one service page.
F_TRAVEL = "https://fintrac-canafe.canada.ca/guidance-directives/transaction-operation/travel-acheminement/1-eng"
F_REC_MSB = "https://fintrac-canafe.canada.ca/guidance-directives/recordkeeping-document/record/msb-eng"
RQ_MSB = "https://www.revenuquebec.ca/en/businesses/sector-specific-measures/money-services-businesses-msbs/money-services-business-licence-application/"


# ------------------------------------------------------------------ company incorporation
CC_FEES = "https://ised-isde.canada.ca/site/corporations-canada/en/services-fees-and-processing-times"
CC_DIR = "https://ised-isde.canada.ca/site/corporations-canada/en/business-corporations/directors-and-officers"
CC_NEXT = "https://ised-isde.canada.ca/site/corporations-canada/en/business-corporations/next-steps-following-incorporation-your-business"
CC_ISC = "https://ised-isde.canada.ca/site/corporations-canada/en/individuals-significant-control/individuals-significant-control-file-your-information"
CC_NAME = "https://ised-isde.canada.ca/site/corporations-canada/en/naming-corporation/naming-corporation-how-get-name"
L_CBCA = "https://laws-lois.justice.gc.ca/eng/acts/C-44/"
ON_INC = "https://www.ontario.ca/page/business/start/register-your-business-online"
ON_FEES = "https://www.ontario.ca/page/cost-time-required-to-register-change-search-for-business-name-corporation-not-for-profit"
# CRA pages for the "After incorporation" block, checked 23 November 2026.
IN_CRA_BN = ("https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/"
             "business-number-program-account/need-bn.html")
IN_CRA_GST = "https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html"
IN_CRA_T2 = ("https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/"
             "corporation-income-tax-return/when-file-your-corporation-income-tax-return.html")

DEEP["incorporation-canada.html"] = dict(
    name="Company incorporation",
    checked="23 November 2026",
    modified="2026-11-23",
    title="Canadian Company Incorporation, Usually Within 24 Hours | AML Canada",
    desc="Incorporate a Canadian company, federally or in Ontario, usually within 24 hours. Fixed fee US$1,500, ready for FINTRAC or RPAA registration.",
    service_type="Canadian company incorporation",
    offers=[("1500", "USD", "Canadian company incorporation, fixed fee (government filing fees separate)")],
    timing="Usually within 24 hours",
    h1="Incorporate your Canadian company, usually within 24 hours.",
    lede="Federal or Ontario incorporation, usually done within 24 hours. Fixed fee US$1,500.",
    hero_price="Fixed fee · US$1,500",
    label="Company · Incorporated",
    need="incorporate",
    intro=("A Canadian company is usually the first step before registering with FINTRAC as a money services business or with the Bank of Canada as a payment service provider.",
           ["We incorporate your company federally or in a province such as Ontario, choosing with you what fits your plans, and set it up so it's ready for the registrations that come next.",
            "Once we have your details, incorporation usually takes a few hours and is usually done within 24 hours, though that isn't guaranteed. Our fee is a fixed US$1,500; government filing fees are separate and paid to the government."]),
    facts=[("Our fee", "US$1,500", "fixed"),
           ("Typical timing", "Within 24h", "usually, once we have your details"),
           ("Federal filing fee", "CA$200", "online, paid to Corporations Canada"),
           ("Ontario filing fee", "CA$300", "online, paid to Ontario")],
    fee=dict(amount="US$1,500", unit="fixed fee · plus government filing fees",
             note="Government filing fees are separate: currently CA$200 federally online (CA$100 more for 4-hour express service) or CA$300 online in Ontario. A named Ontario company also needs an Ontario-biased Nuans name search report.",
             items=["Advice on federal or provincial incorporation",
                    "Company name or numbered company",
                    "Articles of incorporation filed",
                    "Registered office address and first directors",
                    "Set up ready for FINTRAC or RPAA registration",
                    "Usually complete within 24 hours"]),
    guide=[
        ("federal-or-provincial", "Federal or provincial?", """          <p>You can incorporate federally, under the Canada Business Corporations Act (CBCA) through Corporations Canada, or in a province or territory, such as Ontario under its Business Corporations Act. A federal company can use its name across Canada, though it still registers in the provinces where it does business. A provincial company is often simpler if you'll operate mainly in one province. We help you choose before anything is filed.</p>"""),
        ("directors", "Directors and residency", """          <p>Federal corporations must have at least 25% resident Canadian directors; if the company has fewer than four directors, at least one must be a resident Canadian. Under CBCA s.2, a resident Canadian includes a Canadian citizen ordinarily resident in Canada and a permanent resident ordinarily resident in Canada, with limited exceptions. Ontario doesn't require resident Canadian directors, which can matter for founders based outside Canada. Some regulated sectors have stricter rules.</p>"""),
        ("timing", "How long it takes", """          <p>Once we have your details and documents, incorporation usually takes a few hours and is usually done within 24 hours; it isn't guaranteed. Corporations Canada processes online incorporations in about a day, with a 4-hour express option for an extra government fee, and Ontario incorporates immediately online.</p>"""),
        ("fees", "What it costs", f"""          <p>Our fee is a fixed US$1,500. Government fees are paid separately to the government: currently CA$200 for federal online incorporation (CA$100 more for 4-hour express) or CA$300 for Ontario online incorporation.</p>
          <p>For a federal online incorporation, the name search is built into the application, so a word name doesn't need a separate Nuans report. <a href="{CC_NAME}" rel="noopener">Corporations Canada</a> says the name search for incorporation is integrated into the application process, and you don't need to order a separate report first. It still asks for a Nuans report for some other filings, such as revivals and amalgamations. A named Ontario company needs an Ontario-biased Nuans name search report, and <a href="{ON_INC}" rel="noopener">Ontario</a> won't accept a federal-biased one; a numbered company doesn't need one.</p>"""),
        ("after", "After incorporation: tax accounts and filings", f"""          <ul>
            <li><strong>Business number.</strong> The <a href="{IN_CRA_BN}" rel="noopener">CRA</a> says a federal incorporation gives you a business number (BN) and a corporation income tax (RC) program account, so you don't register separately for that account. Incorporating in Ontario does too. GST/HST and payroll accounts are registered with the CRA separately, once you have your BN.</li>
            <li><strong>GST/HST.</strong> Most businesses are small suppliers and don't have to register while their taxable supplies stay at or below CA$30,000 over four consecutive calendar quarters. Once you go over CA$30,000, in a single quarter or over four consecutive quarters, you must register, according to the <a href="{IN_CRA_GST}" rel="noopener">CRA</a>.</li>
            <li><strong>Corporation income tax return.</strong> A corporation files its T2 return within six months of the end of each tax year (<a href="{IN_CRA_T2}" rel="noopener">CRA</a>).</li>
            <li><strong>Annual return.</strong> A federal corporation files an annual return with Corporations Canada within 60 days of its anniversary date each year, but not for the year it was incorporated (federal online annual return: CA$12). Ontario lists its annual return for an Ontario corporation at no fee.</li>
            <li><strong>Individuals with significant control.</strong> Keep corporate records, including a register of individuals with significant control. For a federal corporation, file ISC information with Corporations Canada at incorporation, every year with the annual return, and within 15 days of a change to the register. This has applied since January 22, 2024.</li>
            <li><strong>Provinces.</strong> Register in each province where you carry on business.</li>
            <li><strong>Regulated services.</strong> Register with <a href="msb-registration.html">FINTRAC as an MSB</a> or with the <a href="rpaa-registration.html">Bank of Canada under the RPAA</a> before you start offering those services.</li>
          </ul>
          <p>If you're incorporating from outside Canada, our guide on <a href="incorporate-in-canada-non-resident.html">how to incorporate in Canada as a non-resident</a> covers director residency and tax residency in more detail.</p>"""),
    ],
    sources=[("Corporations Canada, Services, fees and processing times", CC_FEES), ("Directors and officers", CC_DIR),
             ("Next steps after incorporating", CC_NEXT), ("Individuals with significant control: file your information", CC_ISC),
             ("Naming a corporation", CC_NAME), ("Canada Business Corporations Act", L_CBCA),
             ("Ontario, Register your business online", ON_INC), ("Ontario fees and timing", ON_FEES),
             ("CRA, When you need a BN", IN_CRA_BN), ("CRA, When to register for and start charging the GST/HST", IN_CRA_GST),
             ("CRA, When to file your corporation income tax return", IN_CRA_T2)],
    for_title="Who it's for",
    for_items=[("Foreign businesses entering Canada", "A Canadian company to hold your registration and contracts."),
               ("New MSBs and payment companies", "The company that will register with FINTRAC or the Bank of Canada."),
               ("Founders on a deadline", "Usually incorporated within 24 hours, so the next steps can start.")],
    arts=["one", "address", "register"],
    faqs=[("How much does it cost to incorporate a company in Canada?", "Our fee is a fixed US$1,500. Government filing fees are separate: currently CA$200 federally online or CA$300 in Ontario online."),
          ("How long does incorporation take?", "Usually within 24 hours once we have your details and documents, often a few hours. It isn't guaranteed."),
          ("Can a non-resident incorporate in Canada?", "Yes. Federal companies need at least 25% resident Canadian directors (at least one if there are fewer than four). Ontario doesn't require resident Canadian directors."),
          ("Should we incorporate before registering as an MSB?", "Usually, yes. The company is what registers with FINTRAC, so incorporating first means the registration can start straight away."),
          ("Do I need a Nuans report to incorporate federally?", "Not for a federal incorporation. Corporations Canada says the name search is integrated into the online application, so you don't order a separate report. A named Ontario company does need an Ontario-biased Nuans report. A numbered company needs none."),
          ("When does a new company have to register for GST/HST?", "The CRA says most businesses must register once their taxable supplies go over CA$30,000 in a single calendar quarter or over four consecutive calendar quarters. Below that, registration is voluntary.")],
    related=["msb-registration.html", "canadian-address.html", "rpaa-registration.html"],
)


# ------------------------------------------------------------------ apostille & notarization (added 21 October 2026)

# ------------------------------------------------------------------ apostille and notarization (scoped)
# Owner-confirmed 21 October 2026: corporate documents only; AML Canada coordinates, a licensed
# Ontario partner notary (unnamed) notarizes; fee quoted per document set; government fees separate;
# no turnaround promise, no remote notarization, no personal documents, no legal advice.
# Facts checked 21 October 2026 against the official pages below.
AP_GAC = "https://international.canada.ca/en/global-affairs/services/document-authentication"
AP_GAC_REQ = "https://international.canada.ca/en/global-affairs/services/document-authentication/requirements"
AP_GAC_FAQ = "https://international.canada.ca/en/global-affairs/services/document-authentication/faq"
AP_GAC_GLOSS = "https://international.canada.ca/en/global-affairs/services/document-authentication/glossary"
AP_GAC_PORTAL = "https://apostille-gac.powerappsportals.com/en/search-document/"
AP_GAC_NEWS = "https://www.canada.ca/en/global-affairs/news/2023/12/improving-authentication-services-in-canada.html"
AP_HCCH = "https://www.hcch.net/en/instruments/conventions/status-table/?cid=41"
AP_ON = "https://www.ontario.ca/page/authenticate-document-use-outside-canada"
AP_ON_NOTARY = "https://www.ontario.ca/page/information-notaries-public-ontario"
AP_BC_FEES = "https://www2.gov.bc.ca/gov/content/governments/government-id/guide-to-the-authentication-of-documents/fees"
AP_AB = "https://www.alberta.ca/document-authentication-other-jurisdictions-countries"
AP_SK = "https://www.saskatchewan.ca/government/notarized-documents-legislation-maps/authenticating-notarized-documents"
AP_QC_ABOUT = "https://www.quebec.ca/en/justice-and-civil-status/services/apostille/about"
AP_QC_APPLY = "https://www.quebec.ca/en/justice-and-civil-status/services/apostille/applying"

DEEP["apostille-notarization-canada.html"] = dict(
    checked="21 October 2026",
    name="Apostille & notarization",
    modified="2026-11-23",
    title="Apostille Services Canada for Corporate Documents | AML Canada",
    desc="Apostille and notarization of Canadian corporate documents for foreign banks, payment partners and regulators, with a licensed Ontario partner notary.",
    service_type="Apostille and notarization of corporate documents",
    offers=[],
    kicker="Apostille and notarization services in Canada for corporate documents",
    h1="Get your Canadian corporate documents accepted abroad.",
    lede="We coordinate notarization by a licensed Ontario partner notary and the apostille, for corporate documents going to foreign banks, payment partners and regulators.",
    hero_price="Quote · per document set",
    label="Apostille · Corporate documents",
    need="apostille",
    intro=("Foreign banks, payment partners and regulators often ask for Canadian corporate documents that carry an apostille.",
           ["We coordinate the process for corporate documents: certificates of incorporation and status, articles, register and minute book extracts, director and shareholder resolutions, corporate powers of attorney, and evidence of FINTRAC MSB or Bank of Canada RPAA registration. We check what the receiving party has asked for, prepare the document set and send each document to the right authority.",
            "Notarization is done by a licensed notary public in Ontario who we work with. AML Canada is not a notary, and our staff don't notarize documents. We don't handle personal documents or give legal advice. Our fee is quoted per document set once we know what you need, and government fees are paid separately."]),
    facts=[("In force", "Jan 11, 2024", "Apostille Convention in Canada"),
           ("Ontario fee", "CA$16 to CA$32", "per document, paid to Ontario"),
           ("Federal fee", "Free", "Global Affairs Canada"),
           ("Our fee", "Quote", "per document set")],
    fee=dict(amount="Quote", unit="per document set · plus government fees",
             note="Depends on how many documents you need, whether each needs notarization and which authority issues the apostille. Government fees are separate: in Ontario, CA$16 per notarized document and CA$32 per Ontario government document. Global Affairs Canada charges no fee.",
             items=["A check of what the receiving bank, partner or regulator has asked for",
                    "Review of each document and how it must be prepared",
                    "Notarization by our licensed Ontario partner notary, where needed",
                    "Submission to the correct competent authority",
                    "Apostilled documents couriered back to you",
                    "Updates until your documents are back"]),
    guide=[
        ("what", "What an apostille is", f"""          <p>Authentication confirms that the signature and seal of a public official on a document are genuine, so the document can be recognized in another country. An apostille is a type of authentication certificate accepted by every country that is a member of the Apostille Convention, according to the <a href="{AP_GAC_GLOSS}" rel="noopener">Global Affairs Canada glossary</a>. Global Affairs Canada issues it as a separate page that it securely attaches to your document.</p>
          <p>An apostille confirms where a document came from. It doesn't confirm what the document says. Ontario's <a href="{AP_ON}" rel="noopener">Official Documents Services</a> checks signatures and seals against its records and doesn't validate the contents.</p>"""),
        ("convention", "Canada and the Apostille Convention", f"""          <p>Canada acceded to the Hague Apostille Convention on May 12, 2023, and the Convention entered into force for Canada on <strong>January 11, 2024</strong>, according to the <a href="{AP_HCCH}" rel="noopener">Hague Conference status table</a>. The table listed 130 contracting parties when we checked it. For documents going to a member country, the apostille replaces legalization at that country's embassy or consulate.</p>
          <p>Whether a document needs authentication at all is set by the law of the destination country. Canadian law doesn't require it, so start with the receiving bank, partner or regulator.</p>"""),
        ("who-issues", "Who issues the apostille", f"""          <p>Canada has six authorities that issue apostilles: Global Affairs Canada and five provinces. The <a href="{AP_GAC_REQ}" rel="noopener">Global Affairs Canada requirements</a> set out who handles what:</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Where the document comes from</th><th scope="col">Who issues the apostille</th></tr></thead>
            <tbody>
              <tr><th scope="row">Government of Canada, such as Corporations Canada documents</th><td>Global Affairs Canada</td></tr>
              <tr><th scope="row">Manitoba, New Brunswick, Newfoundland and Labrador, Northwest Territories, Nova Scotia, Nunavut, Prince Edward Island, Yukon</th><td>Global Affairs Canada, for documents issued or notarized there</td></tr>
              <tr><th scope="row">Alberta, Ontario, Saskatchewan</th><td>The province, for documents issued there and for any document notarized there</td></tr>
              <tr><th scope="row">British Columbia, Quebec</th><td>The province, for documents issued there; a notarized document qualifies only if the original was issued in the province</td></tr>
            </tbody>
          </table></div>
          <p>A document notarized in Alberta, Ontario or Saskatchewan goes to that province, wherever it was originally issued. British Columbia and Quebec authenticate a notarized document only if the original was issued in their province. In practice, a copy of a federal certificate notarized by an Ontario notary goes to Ontario's Official Documents Services, not to Global Affairs Canada.</p>"""),
        ("notarize", "Public or private document: when to notarize first", f"""          <p>Some government documents can be apostilled directly. Most private and corporate records can't. The Global Affairs Canada <a href="{AP_GAC_PORTAL}" rel="noopener">document eligibility tool</a> says:</p>
          <ul>
            <li>a Corporations Canada certificate of incorporation with an original signature or seal doesn't need notarizing, but one without an original signature or seal does;</li>
            <li>certificates of compliance and existence, articles of incorporation, business registration documents, corporate bylaws and other business or corporate records must be notarized;</li>
            <li>powers of attorney, as private legal documents, must be notarized.</li>
          </ul>
          <p>Ontario's <a href="{AP_ON}" rel="noopener">Official Documents Services</a> accepts business registry documents issued since 1991 by the Business and Personal Property Branch or the Ontario Business Registry without notarization. It won't accept documents commissioned by a commissioner for taking affidavits, or electronic copies.</p>
          <p>In Ontario, a notary must be physically present with the person when notarizing. The <a href="{AP_ON_NOTARY}" rel="noopener">Ministry of the Attorney General</a> says remote notarization isn't permitted under the Notaries Act, and Official Documents Services won't authenticate or apostille documents notarized remotely. Our partner notary works in person.</p>"""),
        ("documents", "Corporate documents we handle, by type", f"""          <p>A public document is one issued by a government registry. A private document is one your company makes itself, and it must be notarized before it can be apostilled. Some public documents also need notarizing first, depending on the version you hold. This table uses the <a href="{AP_GAC_PORTAL}" rel="noopener">Global Affairs Canada eligibility tool</a> and Ontario's <a href="{AP_ON}" rel="noopener">Official Documents Services</a> guidance.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Document</th><th scope="col">Public or private</th><th scope="col">Notarize first?</th></tr></thead>
            <tbody>
              <tr><th scope="rowgroup" colspan="3">Core corporate documents</th></tr>
              <tr><th scope="row">Corporations Canada certificate of incorporation with an original signature or seal</th><td>Public</td><td>No</td></tr>
              <tr><th scope="row">Corporations Canada certificate of incorporation without an original signature or seal</th><td>Public</td><td>Yes</td></tr>
              <tr><th scope="row">Corporations Canada certificates of compliance, existence or amendment, and articles of incorporation</th><td>Public</td><td>Yes, Global Affairs Canada says business or corporate records must be notarized</td></tr>
              <tr><th scope="row">Ontario Business Registry documents issued since 1991, such as a certificate of status</th><td>Public</td><td>No, in Ontario</td></tr>
              <tr><th scope="rowgroup" colspan="3">Registers and minute book</th></tr>
              <tr><th scope="row">Register extracts, minute book pages and by-laws</th><td>Private</td><td>Yes</td></tr>
              <tr><th scope="rowgroup" colspan="3">Resolutions and powers of attorney</th></tr>
              <tr><th scope="row">Director and shareholder resolutions</th><td>Private</td><td>Yes</td></tr>
              <tr><th scope="row">Corporate power of attorney</th><td>Private</td><td>Yes, as a private legal document</td></tr>
              <tr><th scope="rowgroup" colspan="3">Registration evidence</th></tr>
              <tr><th scope="row">Evidence of FINTRAC MSB or Bank of Canada RPAA registration</th><td>Public registry record</td><td>Usually. Global Affairs Canada's tool says documents from a Government of Canada department or agency that aren't on its list must be notarized. FINTRAC says it doesn't issue certificates of registration, so ask the receiving party what evidence it accepts.</td></tr>
            </tbody>
          </table></div>
          <p>The version you hold matters, so we check each document before anything is submitted. Our guide to <a href="apostille-corporate-documents-canada.html">how to apostille Canadian corporate documents</a> covers each type in more detail.</p>"""),
        ("non-convention", "Countries that are not part of the Convention", f"""          <p>For a country outside the Convention, the document may need to be legalized at that country's embassy, high commission or consulate after it has been authenticated in Canada, according to <a href="{AP_GAC_REQ}" rel="noopener">Global Affairs Canada</a>. Ontario issues a certificate of authentication instead of an apostille for those countries. Global Affairs Canada also notes that some countries accept only its own authentication, so check with the destination country's mission before choosing a route.</p>"""),
        ("fees-times", "Government fees and processing times", f"""          <p>These are the fees and times each authority published when we checked on October 21, 2026. They change, so we confirm them again before we submit.</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Authority</th><th scope="col">Government fee</th><th scope="col">Published processing time</th></tr></thead>
            <tbody>
              <tr><th scope="row"><a href="{AP_GAC}" rel="noopener">Global Affairs Canada</a></th><td>Free</td><td>Processing requests received 25 business days earlier, plus mailing time. No expedited service.</td></tr>
              <tr><th scope="row"><a href="{AP_ON}" rel="noopener">Ontario</a></th><td>CA$16 per notarized document; CA$32 per Ontario government document</td><td>Mail-in within 15 business days; about 30 minutes in person if the documents are complete</td></tr>
              <tr><th scope="row"><a href="{AP_BC_FEES}" rel="noopener">British Columbia</a></th><td>CA$20 per document</td><td>2 to 4 weeks, not including mail time</td></tr>
              <tr><th scope="row"><a href="{AP_AB}" rel="noopener">Alberta</a></th><td>CA$25 per document</td><td>At least 7 to 10 business days</td></tr>
              <tr><th scope="row"><a href="{AP_SK}" rel="noopener">Saskatchewan</a></th><td>CA$50 per certificate, signatory or package</td><td>Typically 4 to 7 business days, not including mail time</td></tr>
              <tr><th scope="row"><a href="{AP_QC_APPLY}" rel="noopener">Quebec</a></th><td>CA$66.50 per document</td><td>Varies with volume; Quebec posts the date of the requests it is processing</td></tr>
            </tbody>
          </table></div>
          <p>Government fees are paid on top of our quote. We don't promise a turnaround, because each authority sets its own processing times.</p>"""),
        ("how", "How we handle your documents", """          <ol>
            <li><strong>Consultation.</strong> Which documents you need, which country they're going to and what the receiving party has asked for.</li>
            <li><strong>Document check.</strong> We confirm whether each document can be apostilled directly or needs notarization first, and which authority issues it. If you need a fresh certificate of status or certified copies, we tell you what to order.</li>
            <li><strong>Notarization.</strong> Our licensed Ontario partner notary notarizes the documents that need it, in person.</li>
            <li><strong>Apostille submission.</strong> We submit each document to the correct competent authority with the government fee.</li>
            <li><strong>Return.</strong> Once the apostilles are issued, we courier the documents back to you.</li>
          </ol>
          <p>Our guides explain <a href="apostille-canada-guide.html">how to get an apostille in Canada</a> and <a href="apostille-corporate-documents-canada.html">which corporate documents foreign banks and regulators ask for</a>.</p>"""),
    ],
    sources=[("Global Affairs Canada, Authentication of documents", AP_GAC), ("Requirements", AP_GAC_REQ),
             ("Frequently asked questions", AP_GAC_FAQ), ("Glossary", AP_GAC_GLOSS),
             ("Global Affairs Canada, document eligibility tool", AP_GAC_PORTAL),
             ("HCCH, Apostille Convention status table", AP_HCCH),
             ("Ontario, Authenticate a document for use outside Canada", AP_ON),
             ("Ontario, Information for notaries public", AP_ON_NOTARY),
             ("British Columbia, Document authentication fee", AP_BC_FEES), ("Alberta, Documents for other jurisdictions or countries", AP_AB),
             ("Saskatchewan, Authenticating notarized documents", AP_SK), ("Quebec, About apostille", AP_QC_ABOUT),
             ("Quebec, Applying for an apostille", AP_QC_APPLY)],
    for_title="Who it's for",
    for_items=[("Canadian companies opening accounts abroad", "Corporate documents a foreign bank needs to see before it onboards you."),
               ("MSBs and payment companies", "Registration evidence and corporate records for foreign payment partners."),
               ("Companies answering a foreign regulator", "Certified, notarized and apostilled records for a licence or filing abroad.")],
    arts=["one", "register", "review"],
    faqs=[("What is an apostille?", "A certificate that confirms the signature and seal of the official on a Canadian public document are genuine, so the document is accepted in other countries that belong to the Apostille Convention. It doesn't confirm the document's contents."),
          ("When did Canada join the Apostille Convention?", "Canada acceded on May 12, 2023, and the Convention entered into force for Canada on January 11, 2024."),
          ("Can a Corporations Canada certificate be apostilled without notarization?", "A certificate of incorporation with an original signature or seal can go to Global Affairs Canada directly. Global Affairs Canada says other business and corporate records, including certificates of compliance and existence and articles, must be notarized."),
          ("Is AML Canada a notary?", "No. We coordinate the process. Notarization is done by a licensed notary public in Ontario who we work with."),
          ("Can documents be notarized remotely?", "No. Ontario's Notaries Act doesn't permit remote notarization, and Ontario won't apostille a document notarized remotely."),
          ("How much does an apostille cost?", "Our fee is quoted per document set. Government fees are separate: Global Affairs Canada charges nothing, and Ontario charges CA$16 per notarized document and CA$32 per Ontario government document.")],
    related=["incorporation-canada.html", "msb-registration.html", "canadian-address.html"],
)


# ------------------------------------------------------------------ FINTRAC reporting software (quote)
F_METHODS = "https://fintrac-canafe.canada.ca/reporting-declaration/electron-eng"
F_API = "https://fintrac-canafe.canada.ca/reporting-declaration/info/api/api-eng"
F_FWR = "https://fintrac-canafe.canada.ca/reporting-declaration/info/f2r-eng"

RS_TABLE = """<div class="table-wrap"><table>
            <thead><tr><th scope="col">Report</th><th scope="col">When it applies</th><th scope="col">Deadline</th></tr></thead>
            <tbody>
              <tr><th scope="row">Suspicious transaction report (STR)</th><td>Reasonable grounds to suspect a transaction is related to money laundering, terrorist financing or sanctions evasion. No minimum amount.</td><td>As soon as practicable</td></tr>
              <tr><th scope="row">Large cash transaction report (LCTR)</th><td>You receive cash of $10,000 or more, in one transaction or in two or more that the 24-hour rule requires you to add together.</td><td>15 calendar days</td></tr>
              <tr><th scope="row">Electronic funds transfer report (EFTR)</th><td>You initiate, or finally receive, an international electronic funds transfer of $10,000 or more, in one transfer or in two or more that the 24-hour rule requires you to add together.</td><td>5 working days</td></tr>
              <tr><th scope="row">Large virtual currency transaction report (LVCTR)</th><td>You receive virtual currency worth $10,000 or more, in one transaction or in two or more that the 24-hour rule requires you to add together.</td><td>5 working days</td></tr>
            </tbody>
          </table></div>"""

DEEP["fintrac-reporting-software.html"] = dict(
    checked="23 November 2026",
    name="FINTRAC reporting software",
    modified="2026-11-23",
    title="FINTRAC Reporting Software for MSBs | AML Canada",
    desc="FINTRAC reporting software for STRs, LCTRs, EFTRs, LVCTRs and CDRs: data import, 24-hour rule checks, validation, maker-checker approval and API submission.",
    service_type="FINTRAC reporting software",
    offers=[],
    kicker="FINTRAC reporting software and API report submission",
    h1="Your FINTRAC reports checked, approved and tracked in one place.",
    lede="Our reporting platform takes your transaction data through 24-hour rule checks, validation and approval, then submits through FINTRAC API report submission where you're enrolled, and keeps the record.",
    hero_price="Quote · after a scoping call",
    label="Report validated · Approved",
    need="reporting",
    intro=("Most of the work in FINTRAC reporting happens before you press submit.",
           ["Transactions sit in more than one system. Smaller transactions may have to be added together under the 24-hour rule. Conductor and beneficiary details go missing, each report needs checking before it goes, and a rejected report has to be fixed and resubmitted. Spreadsheets and email make all of that slow and hard to evidence.",
            "Our platform covers the five reports filed electronically: suspicious transaction reports, large cash transaction reports, electronic funds transfer reports, large virtual currency transaction reports and casino disbursement reports. Your compliance team still decides what gets reported. The platform does the checking, routing and record keeping around that decision. Pricing is confirmed after a scoping call."]),
    facts=[("Reports", "5 workflows", "STR, LCTR, EFTR, LVCTR, CDR"),
           ("Checks", "24-hour rule", "report-specific aggregation"),
           ("Approval", "Maker-checker", "with time-stamped sign-off"),
           ("Fee", "Quote", "after a scoping call")],
    fee=dict(amount="Quote", unit="after a scoping call",
             note="Pricing is confirmed after a scoping call.",
             items=["Set-up of your report types, thresholds, aggregation rules and field mappings by a compliance specialist",
                    "Import of transaction files such as CSV, with reusable mappings",
                    "Pre-submission validation, with warnings shown apart from blocking errors",
                    "Maker-checker review and recorded sign-off",
                    "Submission through FINTRAC API report submission where you are enrolled",
                    "A report archive you can download as PDF or CSV"]),
    guide=[
        ("channels", "How reports reach FINTRAC", f"""          <p>A business with an internet connection must send FINTRAC its suspicious transaction reports, large cash transaction reports, large virtual currency transaction reports, electronic funds transfer reports and casino disbursement reports electronically. Listed person or entity property reports still go on a paper form. FINTRAC's <a href="{F_METHODS}" rel="noopener">reporting methods page</a> lists two electronic reporting systems, plus a shared process for sending EFTRs to FINTRAC and the Canada Revenue Agency at the same time:</p>
          <ul>
            <li><strong>FINTRAC Web Reporting System.</strong> You enter and submit reports one at a time in a browser. FINTRAC says it is geared to businesses with lower reporting volumes.</li>
            <li><strong>FINTRAC API report submission.</strong> A system-to-system connection that sends report data straight to FINTRAC, geared to businesses with higher volumes.</li>
          </ul>
          <p>The older batch systems are being retired. FINTRAC's transition periods for moving higher-volume reporting to the API ended on November 6, 2023 for LCTRs and LVCTRs, July 3, 2024 for STRs, and August 22, 2024 for EFTRs and casino disbursement reports (<a href="{F_API}" rel="noopener">FINTRAC, API report submission</a>, checked November 15, 2026).</p>"""),
        ("three-ways", "Three ways to file with FINTRAC", f"""          <p>For the five electronic reports, the choice is between using one of FINTRAC's two systems directly and using a reporting platform that prepares reports and submits them through one of them. A business without the technical capability to report electronically must use FINTRAC's paper forms (<a href="{F_METHODS}" rel="noopener">FINTRAC, Methods to report</a>).</p>
          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Option</th><th scope="col">How it works</th><th scope="col">Geared to</th><th scope="col">What you set up</th><th scope="col">Checks before submission</th></tr></thead>
            <tbody>
              <tr><th scope="row">FINTRAC Web Reporting System</th><td>You fill in and submit each report in a browser.</td><td>Lower reporting volumes, according to FINTRAC</td><td>Access, by first emailing FINTRAC at F2R@fintrac-canafe.gc.ca, and users with roles: data entry officers can only create reports, and verification and submission officers submit them.</td><td>FINTRAC's validation: a rejected message for missing mandatory information, and a warning for missing information marked "mandatory if applicable".</td></tr>
              <tr><th scope="row">Your own connection to FINTRAC's API</th><td>Your systems send report data straight to FINTRAC.</td><td>Higher reporting volumes, according to FINTRAC</td><td>An application and secret keys through FINTRAC's API portal, and your own build against FINTRAC's JSON schemas and validation rules, kept up to date as FINTRAC updates them.</td><td>Whatever checks you build, then FINTRAC's validation messages.</td></tr>
              <tr><th scope="row">A reporting platform, such as ours</th><td>Transaction data is imported, checked and approved, then submitted through FINTRAC API report submission where you're enrolled.</td><td>Submits through FINTRAC's API, or prepares report data for your existing FINTRAC channel until you're enrolled</td><td>Report types, thresholds, aggregation rules, field mappings and approval paths, set by a compliance specialist. API enrolment still applies.</td><td>24-hour rule checks, pre-submission validation with warnings shown apart from blocking errors, and maker-checker sign-off.</td></tr>
            </tbody>
          </table></div>
          <p>Whichever you use, your business stays responsible for its reports. FINTRAC's <a href="{F_FWR}" rel="noopener">Web Reporting System guide</a> and <a href="{F_API}" rel="noopener">API report submission page</a> explain each system.</p>"""),
        ("api", "What FINTRAC API report submission involves", f"""          <p>To use the API you need an application and secret keys, which your technical administrator sets up through FINTRAC's API portal. A business that files larger volumes and doesn't have API access yet contacts FINTRAC at F2R@fintrac-canafe.gc.ca.</p>
          <p>FINTRAC offers two groups of endpoints, one for single reports and one for bulk submission, and each lets you create, change or delete a report submission. A single report can hold up to 500 transactions (25 MB). A bulk file can hold up to 5,000 reports and up to 5,000 transactions per report, within 300 MB. FINTRAC publishes JSON schemas and validation rules for each report type.</p>
          <p>Our platform builds report data in the format FINTRAC's API expects, submits approved reports individually or in aggregate, and records FINTRAC's response against each report. If your business isn't enrolled for the API yet, we help with enrolment. Until then the platform produces validated, approved report data for submission through your existing FINTRAC channel, and records the status against the report.</p>"""),
        ("reports", "The reports the platform covers", f"""          <p>These are the thresholds and deadlines from FINTRAC's guidance, as we summarize them in our <a href="fintrac-reporting-requirements.html">FINTRAC reporting guide</a>. Which reports you must file depends on your business and your activities.</p>
{RS_TABLE}
          <p>Listed person or entity property reports are filed on paper, so the platform doesn't handle them. Casino disbursement reports, which apply to casinos, have their own workflow.</p>"""),
        ("aggregation", "24-hour rule checks", f"""          <p>For large cash and large virtual currency transactions, FINTRAC's <a href="{F_24}" rel="noopener">24-hour rule</a> means two or more transactions of any amount that total $10,000 or more within a 24-hour window are reported together when you know they were conducted by or on behalf of the same person or entity, or are for the same beneficiary. Electronic funds transfers and casino disbursements have their own aggregation rules. FINTRAC expects the rule to be applied across all your locations, which is hard to do by hand across branches, agents and payment channels.</p>
          <p>The rule doesn't work the same way for every report. Which transactions are added together depends on the report type, timing, who conducted them, third parties and beneficiaries. The platform applies configurable checks for each report type and shows the transactions it has grouped. Your team confirms whether a report is required.</p>"""),
        ("validation", "Validation before a report is submitted", f"""          <p>FINTRAC's Web Reporting System shows two kinds of validation message, according to its <a href="{F_FWR}" rel="noopener">guide</a>. A <strong>rejected</strong> message means mandatory information is missing, and the report can't be submitted until it's added. A <strong>warning</strong> means information marked "mandatory if applicable" is missing or incomplete. A warning doesn't stop submission, but if the information is in your records you are required to include it.</p>
          <p>The platform runs its checks before a report reaches approval. It checks:</p>
          <ul>
            <li>mandatory and mandatory-if-applicable fields;</li>
            <li>formats, codes and conditional fields;</li>
            <li>missing conductor or beneficiary information, and third-party fields on casino disbursement reports;</li>
            <li>duplicate report references and missing links between transactions;</li>
            <li>dates and amounts that don't agree.</li>
          </ul>
          <p>Blocking errors are shown apart from warnings, so your team deals with what would stop a filing first. Validation can't guarantee FINTRAC will accept a report.</p>"""),
        ("approval", "Review and approval", """          <p>Maker-checker review is configurable. A preparer drafts and validates the report, and a reviewer signs it off. Reviewers can comment on the report itself and return it for correction, and every action is time-stamped, so you can show who prepared, reviewed, approved and submitted each report, and when. Reminders flag reports that are getting close to their deadline.</p>
          <p>Suspicious transaction reports need judgement that software can't supply. The platform provides structured fields for the narrative and routes the report for approval, but establishing reasonable grounds to suspect, writing the narrative and deciding to file stay with your compliance officer. Using the platform doesn't transfer your legal responsibility for reporting.</p>"""),
        ("after", "After submission", """          <p>A submitted report can come back with warnings or be rejected. The platform records FINTRAC's acknowledgement and confirmation number, keeps the JSON data that was sent, assigns corrections to a team member and links each corrected version to the original, so the history of a report reads as one record. You can change or delete submitted reports through the same workflow.</p>
          <p>Submitted reports are kept in an archive you can download as PDF or CSV. Retention controls are confirmed in writing during scoping. That gives your effectiveness reviewer, and FINTRAC's examiners, a time-stamped record of each report's review and sign-off, the JSON data sent and FINTRAC's response.</p>"""),
        ("look-for", "What to look for in FINTRAC reporting software", """          <p>Whichever product you consider, these are the questions that matter for FINTRAC reporting:</p>
          <ul>
            <li><strong>Report coverage.</strong> Does it cover the reports you file: STRs, LCTRs, EFTRs, LVCTRs and, for casinos, casino disbursement reports? Listed person or entity property reports go on paper.</li>
            <li><strong>24-hour rule.</strong> Does it apply the rule for each report type, and show which transactions it grouped so your team can confirm?</li>
            <li><strong>Validation.</strong> Does it check mandatory and mandatory-if-applicable fields before submission, and separate warnings from blocking errors, as FINTRAC's own validation does?</li>
            <li><strong>Approval trail.</strong> Can you show who prepared, reviewed, approved and submitted each report, and when?</li>
            <li><strong>FINTRAC's response.</strong> Does it record the acknowledgement, warnings or rejection for each report, and let you change or delete a submitted report? FINTRAC's API supports create, change and delete actions.</li>
            <li><strong>Schema updates.</strong> FINTRAC publishes JSON schemas and validation rules for each report type and updates them. Who keeps the software in step?</li>
            <li><strong>Records.</strong> Can you export a record of each report for your effectiveness review or a FINTRAC examination?</li>
            <li><strong>Judgement.</strong> Does the decision to file an STR stay with your compliance officer?</li>
          </ul>
          <p>The sections above describe how our platform handles validation, approval, FINTRAC responses and records.</p>"""),
        ("setup", "How we set it up", """          <ol>
            <li><strong>Scoping call.</strong> Your report types, data sources and how you file today.</li>
            <li><strong>Data review.</strong> We check which fields your systems hold and where reporting data is missing.</li>
            <li><strong>Configuration.</strong> A compliance specialist sets your report types, thresholds, aggregation rules, field mappings, user roles and approval paths.</li>
            <li><strong>Testing.</strong> We test with sample and past transactions in a sandbox environment, apart from live FINTRAC submissions.</li>
            <li><strong>API enrolment.</strong> Where it applies, we help you complete FINTRAC API enrolment.</li>
            <li><strong>Go live.</strong> Approved workflows move to production.</li>
          </ol>
          <p>There's no standard implementation timeline. Security controls, hosting location and data residency are confirmed in writing for each client during scoping. If you'd rather not run reporting yourselves, our <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> service includes FINTRAC reporting.</p>"""),
    ],
    sources=[("FINTRAC, Methods to report to FINTRAC", F_METHODS), ("FINTRAC API report submission", F_API),
             ("Using the FINTRAC Web Reporting System", F_FWR), ("Reporting suspicious transactions", F_STR),
             ("Reporting large cash transactions", F_LCTR), ("Reporting electronic funds transfers", F_EFT),
             ("Reporting large virtual currency transactions", F_LVCTR), ("The 24-hour rule", F_24)],
    for_title="Who it's for",
    for_items=[("Money transfer and foreign exchange MSBs", "EFTRs and LCTRs, with 24-hour rule checks before approval."),
               ("Virtual currency dealers", "LVCTRs, validated before approval."),
               ("Payment businesses with FINTRAC obligations", "Where your service model makes you an MSB or another reporting entity."),
               ("Casinos", "Casino disbursement reports, with 24-hour rule checks and approval.")],
    arts=["scan", "programme", "review", "one"],
    faqs=[("What is FINTRAC reporting software?", "Software that helps a reporting entity prepare, check, approve, submit and track the reports it must send FINTRAC, such as STRs, LCTRs, EFTRs and LVCTRs. Ours also applies 24-hour rule checks and keeps the full history of each report."),
          ("Which FINTRAC reports does the platform support?", "Suspicious transaction reports, large cash transaction reports, electronic funds transfer reports, large virtual currency transaction reports and casino disbursement reports. Listed person or entity property reports are filed on paper, so they aren't included."),
          ("Does it submit reports to FINTRAC directly?", "Yes, through FINTRAC API report submission once your business is enrolled. Until then it produces validated, approved report data for your existing FINTRAC channel."),
          ("Does the software decide whether to file an STR?", "No. It structures preparation and approval, but reasonable grounds to suspect, the narrative and the decision to file stay with your compliance team."),
          ("Can we import our transaction files?", "Yes. Structured files such as CSV exports are the main import route, and reusable mappings match your fields to FINTRAC's report fields. Other sources are confirmed during scoping."),
          ("Is FINTRAC API report submission mandatory?", "FINTRAC's reporting pages don't set a volume figure. They describe the Web Reporting System as geared to lower reporting volumes and API report submission as geared to higher volumes. Businesses that sent higher volumes through the older systems being retired had transition periods to move to the API, which ended between November 6, 2023 and August 22, 2024. A business with an internet connection must report electronically, and one without the technical capability to do so must use paper forms."),
          ("How much does it cost?", "Pricing is confirmed after a scoping call."),
          ("Where is our data hosted?", "Hosting location, data residency and security controls are confirmed in writing for each client during scoping.")],
    related=["outsourced-compliance-officer.html", "compliance-programs.html", "effectiveness-reviews.html"],
)


# ------------------------------------------------------------------ sell your MSB
DEEP["sell-your-msb.html"] = dict(
    name="Sell your MSB",
    modified="2026-10-25",
    checked="25 October 2026",
    title="Sell Your Registered MSB Company to a Buyer | AML Canada",
    desc="Sell a Canadian company registered with FINTRAC as an MSB. We check it, match it with a buyer, and handle the share sale and the FINTRAC updates.",
    service_type="Sale of a FINTRAC-registered money services business",
    offers=[],
    kicker="Sell your registered MSB company",
    h1="Sell a registered Canadian MSB.",
    lede="We review your company, present it to buyers without naming it, and take both sides through the share sale and the FINTRAC updates afterwards.",
    hero_price="Quote after review",
    label="MSB · Registered · Sell",
    need="sell",
    intro=("A Canadian company registered with FINTRAC as a money services business can be sold by selling its shares. The registration stays with the company.",
           ["Buyers want a registration that is active, covers the services they need and comes with clean records. We check that first, so there are no surprises in the buyer's due diligence.",
            "Your company is presented without its name or registration number. Those are shared only with a buyer who has signed an NDA.",
            "After the sale, the changes to the registration information, such as new owners and directors, are reported to FINTRAC within 30 days."]),
    facts=[("Registration", "Stays", "with the company"),
           ("FINTRAC updates", "30 days", "after the change"),
           ("Your name", "Withheld", "until NDA"),
           ("Review", "First", "before we list it")],
    fee=dict(amount="Quote", unit="after we review the company",
             note="We tell you what the company is likely to sell for, and our fee, before anything is listed.",
             items=["Registry, corporate records and compliance history reviewed",
                    "A listing without your company's name or registration number",
                    "Buyers screened, including the eligibility of new owners and directors",
                    "Share purchase documents coordinated with both sides",
                    "FINTRAC change filings within 30 days of closing",
                    "Bank of Canada re-registration managed if the company is a registered PSP"]),
    guide=[
        ("who", "Which companies we can sell", """          <ul>
            <li>Canadian corporations registered with FINTRAC as money services businesses, with the status Registered on FINTRAC's registry;</li>
            <li>companies with or without trading history;</li>
            <li>companies that are also registered with the Bank of Canada as payment service providers, with extra time allowed for re-registration before closing.</li>
          </ul>"""),
        ("check", "What we check before listing", f"""          <ul>
            <li>the status, registered services and expiry date on <a href="{F_REGISTRY}" rel="noopener">FINTRAC's MSB registry</a>;</li>
            <li>corporate records, share register and good standing;</li>
            <li>FINTRAC correspondence, any examinations and any unpaid penalties;</li>
            <li>the compliance program and records, if the company has traded;</li>
            <li>bank accounts and payment partners, and whether they would continue after a change of control.</li>
          </ul>"""),
        ("price", "What affects the price", """          <p>The registered services, how long is left before the registration expires, whether the company has traded and how clean its records are, and whether it's also registered with the Bank of Canada. A company that has had compliance problems is harder to sell, and some can't be sold until those problems are fixed.</p>"""),
        ("how", "How the sale works", f"""          <ol>
            <li><strong>Review.</strong> You send us the corporate documents and FINTRAC approval. We check them and agree a price range and our fee with you.</li>
            <li><strong>Listing.</strong> The company appears on <a href="msb-for-sale.html#available">MSB for sale</a> without its name or registration number.</li>
            <li><strong>Buyer.</strong> Interested buyers sign an NDA. We check that the new owners and directors aren't ineligible under PCMLTFA s.11.11.</li>
            <li><strong>Sale.</strong> A share purchase agreement, payment and the share transfer.</li>
            <li><strong>Bank of Canada.</strong> If the company is a registered PSP, it is re-registered before closing (RPAA s.24).</li>
            <li><strong>FINTRAC.</strong> Changes such as new owners, directors and compliance officer reported within 30 days. <a href="{F_UPD}" rel="noopener">FINTRAC</a></li>
          </ol>"""),
    ],
    sources=[("FINTRAC MSB registry", F_REGISTRY), ("Update, renew or cancel your registration", F_UPD), ("Who is not eligible to register", F_NOT_ELIGIBLE),
             ("PCMLTFA", L_PCMLTFA), ("Bank of Canada, Acquisitions of control and prescribed changes", B_ACQ)],
    for_title="Who sells",
    for_items=[("Founders changing plans", "A registered company that won't be used as planned."),
               ("Groups restructuring", "A Canadian entity that is no longer needed."),
               ("Owners of new registrations", "A company registered but not yet trading.")],
    arts=["one", "register", "many"],
    faqs=[("Can I sell a FINTRAC-registered MSB?", "Yes. You sell the company's shares and the registration stays with the company. The changes, such as new owners and directors, are reported to FINTRAC within 30 days."),
          ("Will my company's name be published?", "No. It is listed without its name or registration number. Those are shared only with a buyer who has signed an NDA."),
          ("What if the company is registered with the Bank of Canada too?", "Buying control of a registered PSP is an acquisition of control under the RPAA, so the company must be re-registered by the Bank before the sale closes. We plan the timeline around it."),
          ("How long does a sale take?", "It depends on finding the right buyer, their due diligence and any Bank of Canada re-registration. We give you a timeline after the review.")],
    related=["msb-for-sale.html", "buy-or-register-msb-canada.html", "outsourced-compliance-officer.html"],
)
