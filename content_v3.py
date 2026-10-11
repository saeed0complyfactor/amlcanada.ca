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
              <tr><th scope="row">Large cash transaction report (LCTR)</th><td>Cash of $10,000 or more, in one transaction or in two or more that the 24-hour rule requires you to add together.</td><td>15 calendar days</td></tr>
              <tr><th scope="row">Electronic funds transfer report (EFTR)</th><td>International electronic funds transfers of $10,000 or more, in one transfer or in two or more that the 24-hour rule requires you to add together.</td><td>5 working days</td></tr>
              <tr><th scope="row">Large virtual currency transaction report (LVCTR)</th><td>Virtual currency worth $10,000 or more, in one transaction or in two or more that the 24-hour rule requires you to add together.</td><td>5 working days</td></tr>
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
    name="Outsourced compliance officer",
    title="Outsourced AML Compliance Officer (MLRO) Canada | AML Canada",
    desc="An outsourced Canadian AML compliance officer (MLRO): onboarding reviews, FINTRAC reporting, policies and risk assessments. US$1,500 per 10 hours.",
    service_type="Outsourced AML compliance officer (MLRO)",
    offers=[("1500", "USD", "Block of 10 hours of outsourced compliance officer time")],
    h1="A Canadian compliance officer, without the full-time hire.",
    lede="An outsourced AML compliance officer, or MLRO, for businesses FINTRAC regulates. US$1,500 per 10 hours, scaled as you grow.",
    hero_price="US$1,500 · 10 hours",
    label="Compliance officer · On duty",
    need="officer",
    intro=("Every business FINTRAC regulates has to appoint a compliance officer. For many growing businesses, the right person is experienced, part-time and already working in Canada.",
           ["AML Canada provides an outsourced compliance officer, also known as an MLRO (money laundering reporting officer). We carry the day-to-day anti-money laundering and anti-terrorist financing work for you: second-line review of customer onboarding, advice on difficult cases, regulatory reporting to FINTRAC, and keeping your policies and risk assessments current.",
            "You buy time in blocks of 10 hours for US$1,500. Start with the hours you need now and add blocks as your customers, products and markets grow.",
            "Your business stays responsible for its obligations under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA). We do the work behind them on time and keep a record of what was done."]),
    facts=[("Fee", "US$1,500", "per block of 10 hours"),
           ("Hours", "Scalable", "add blocks as you grow"),
           ("Reports", "STR · EFTR · LVCTR", "LCTR and the others that apply to you"),
           ("Based", "In Canada", "working alongside your team")],
    fee=dict(amount="US$1,500", unit="per 10 hours · scalable",
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
          <p>Amounts are in Canadian dollars. Under FINTRAC's 24-hour rule, two or more transactions that total $10,000 or more within a static 24-hour window are reported together when you know they were conducted by or on behalf of the same person or entity, or are for the same beneficiary.</p>
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
          <p>We estimate a starting number of hours with you in the consultation, then adjust once your volumes are clear. Hours are bought in blocks of 10, so the cost follows your workload.</p>"""),
        ("responsibility", "Your responsibilities, and ours", """          <p>Your business remains the reporting entity even when we do the work, and your senior management stays accountable for the program. We document decisions, send escalations to the right people and keep you informed of what was done in your name.</p>
          <ul>
            <li>You provide access, information and timely decisions.</li>
            <li>We carry out the agreed work, flag risks early and keep records you can show an examiner.</li>
            <li>We agree in writing who signs off on what, including reports and policy changes.</li>
          </ul>"""),
        ("mlro", "MLRO, compliance officer or CCO?", """          <p>The titles differ by country. In the UK and Europe the role is usually called the MLRO, or money laundering reporting officer. Canada's PCMLTFA framework uses "compliance officer", and many firms use "chief compliance officer" too. If you're entering Canada from abroad and looking for an MLRO, the Canadian compliance officer is the equivalent role, with Canada's own reports, thresholds and deadlines.</p>"""),
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
          ("What does an outsourced compliance officer cost?", "US$1,500 for each block of 10 hours. You choose how many blocks you need, and you can add more as your business grows."),
          ("What is an MLRO in Canada?", "MLRO means money laundering reporting officer, a title used mainly in the UK and Europe. The Canadian equivalent under the PCMLTFA is the compliance officer."),
          ("Which FINTRAC reports do you handle?", "Suspicious transaction reports, electronic funds transfer reports, large virtual currency transaction reports, large cash transaction reports, and listed person or entity property reports, whichever apply to your business."),
          ("Do you work with foreign money services businesses?", "Yes. We work with businesses based outside Canada that serve people in Canada."),
          ("Can we start small?", "Yes. Start with the hours you need now, and add blocks of 10 hours when your volumes grow.")],
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
        ("who-must-register", "Who has to register", """          <p>A business with a place of business in Canada must register with FINTRAC before it operates as a money services business, for example by dealing in foreign exchange, remitting or transmitting funds, or dealing in virtual currency. Registering or being licensed with a province doesn't replace FINTRAC registration. Whether your own activities are covered depends on how your business works, which is the first thing we confirm with you.</p>
          <p>An MSB that holds funds for its users or transfers funds at their request may also need to register with the Bank of Canada under the Retail Payment Activities Act. We cover that in <a href="rpaa-registration.html">RPAA registration</a>.</p>
          <p>Our guide on <a href="how-to-register-msb-canada.html">how to register an MSB in Canada</a> lists every money service and walks through each step of the application.</p>"""),
        ("foreign-msb", "Foreign MSB registration", """          <p>A foreign MSB has no place of business in Canada but directs and provides money services to people or entities in Canada. It registers with FINTRAC before it starts and names a representative for service who resides in Canada; our <a href="foreign-msb-registration-canada.html">foreign MSB guide</a> covers the details.</p>"""),
        ("application", "What the application involves", """          <p>FINTRAC asks for details of the business, its owners, senior management and compliance officer, its bank accounts, locations and agents, and its expected transaction volumes, with documents showing who owns and controls it. Criminal record checks are needed for the chief executive officer, the president, the directors and anyone who owns or controls 20% or more. A document that isn't in English or French needs a translation attested by a certified translator (PCMLTFA s.11.12(1.1)).</p>
          <p>If FINTRAC asks for clarification, the answer is due within 30 days of the request, or FINTRAC can deny the application (PCMLTFA s.11.14). Registered businesses face the same 30-day limit, with revocation as the consequence (s.11.17).</p>"""),
        ("how", "How registration works with us", """          <ol>
            <li><strong>Assessment.</strong> Which of your services are money services, whether you're an MSB or a foreign MSB, and what follows from that.</li>
            <li><strong>Preparation.</strong> A checklist of everything FINTRAC needs, and help gathering and checking it. Criminal record checks from several countries often take longest, so we start them first.</li>
            <li><strong>Submission.</strong> Your registration, submitted to FINTRAC with your approval.</li>
            <li><strong>Follow-up.</strong> Answers to FINTRAC's questions, within its deadlines, until your registration is decided.</li>
            <li><strong>Compliance program.</strong> Prepared at the same time as your registration, so you can operate once you're registered.</li>
          </ol>"""),
        ("how-long", "How long registration takes", """          <p>FINTRAC says most complete applications are processed within three months. In our experience it has ranged from about 1 week to 7 months. The main factors are how complete and consistent the application is, how quickly criminal record checks arrive, and FINTRAC's workload at the time.</p>"""),
        ("after", "After you register", """          <p>Registration is valid for two years and has to be renewed before it expires. Changes to your registration information must be reported to FINTRAC within 30 days.</p>
          <p>After registration, an MSB also needs a compliance program, client identification, record keeping and reporting to FINTRAC. Since October 1, 2025, an MSB must also check that its agents and mandataries are eligible, including by reviewing criminal record checks, before engaging them.</p>"""),
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
          ("Do crypto businesses register with FINTRAC?", "Yes. Dealing in virtual currency is a money service, so crypto dealers and exchanges register as MSBs.")],
    related=["compliance-programs.html", "outsourced-compliance-officer.html", "rpaa-registration.html"],
)

# ------------------------------------------------------------------ compliance program
DEEP["compliance-programs.html"] = dict(
    name="Compliance programs",
    title="FINTRAC AML Compliance Program (PCMLTFA) | AML Canada",
    desc="PCMLTFA compliance program documents for FINTRAC-regulated businesses: policies and procedures, risk assessment, training and review plans. Fixed fee US$3,500.",
    service_type="PCMLTFA AML compliance program documents",
    offers=[("3500", "USD", "FINTRAC PCMLTFA compliance program documents, fixed fee")],
    h1="An AML compliance program built around your products, customers and team.",
    lede="FINTRAC and PCMLTFA compliance program documents for the businesses FINTRAC regulates. Fixed fee US$3,500.",
    hero_price="Fixed fee · US$3,500",
    label="Program · 5 of 5 parts",
    need="programme",
    intro=("Every business FINTRAC regulates must have a compliance program. Since March 2026 the PCMLTFA requires programs to be reasonably designed, risk-based and effective.",
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
        ("program-elements", "The five parts of a compliance program", """          <p>FINTRAC's guidance sets out five required elements:</p>
          <ol>
            <li><strong>A compliance officer</strong>, appointed to be responsible for implementing the program.</li>
            <li><strong>Written policies and procedures</strong>, kept up to date and, for an entity, approved by a senior officer.</li>
            <li><strong>A risk assessment</strong> of the business's money laundering, terrorist financing and sanctions evasion risks, documented.</li>
            <li><strong>A written, ongoing compliance training program</strong>, with a plan for delivering it, if you have employees, agents or others authorized to act for you.</li>
            <li><strong>A review of effectiveness</strong> of the policies and procedures, risk assessment and training program, at least every two years.</li>
          </ol>"""),
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
          ("How much does a compliance program cost?", "A fixed US$3,500 for 14 PCMLTFA compliance program documents, from the AML/ATF Compliance Policy to the Fraud Risk Management Policy."),
          ("Do you use templates?", "We use a consistent structure, and the content is written for your products, customers and team. A program that doesn't describe how your business works won't hold up in an examination."),
          ("Does the fee include the effectiveness review?", "No. The program includes a plan for your review. The review itself is a separate, scoped piece of work."),
          ("Can you keep the program up to date afterwards?", "Yes, through outsourced compliance officer hours at US$1,500 per 10 hours."),
          ("Our bank has asked for our AML program. What now?", "Book a consultation. We'll look at what you have, tell you what's missing and agree a written scope to close the gaps.")],
    related=["outsourced-compliance-officer.html", "effectiveness-reviews.html", "msb-registration.html"],
)

# ------------------------------------------------------------------ Canadian address
DEEP["canadian-address.html"] = dict(
    name="Canadian business address",
    title="Canadian Business Address for Foreign Companies | AML Canada",
    desc="A Canadian business address for foreign MSBs and companies entering Canada, for your setup, banking and partners. US$200 per month.",
    service_type="Canadian business address",
    offers=[("200", "USD", "Canadian business address, per month")],
    h1="A Canadian business address for your setup in Canada.",
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
        ("how", "How it works", """          <ol>
            <li><strong>Consultation.</strong> Your plans for Canada and how you'll use the address.</li>
            <li><strong>Written scope.</strong> What's included, including mail handling.</li>
            <li><strong>Registration check.</strong> How the address fits your FINTRAC registration, if you have one or are applying.</li>
            <li><strong>Start.</strong> Your address is ready to use with your banks and partners.</li>
            <li><strong>Monthly.</strong> US$200 per month while you use it.</li>
          </ol>"""),
    ],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("Money services businesses", F_MSB)],
    for_title="Who uses it",
    for_items=[("Foreign money services businesses", "Companies outside Canada that serve customers in Canada."),
               ("Companies opening Canadian operations", "Businesses establishing a presence before hiring locally."),
               ("Start-ups preparing to launch", "Founders who need their Canadian setup in order early.")],
    arts=["address", "one", "register"],
    faqs=[("How much is a Canadian business address?", "US$200 per month."),
          ("Can I use the address on my FINTRAC registration?", "It depends on how you're registered. A foreign MSB registers with a representative for service who resides in Canada, and a physical location in Canada can change a foreign MSB into a domestic MSB. We confirm how the address fits your registration before you use it."),
          ("Is the address my representative for service?", "No. A foreign MSB's representative for service is a person who resides in Canada, which is a separate requirement. Ask us about it in your consultation."),
          ("What happens to mail sent to the address?", "How mail is handled is set out in your written scope.")],
    related=["msb-registration.html", "msb-for-sale.html", "outsourced-compliance-officer.html"],
)

# ------------------------------------------------------------------ MSB for sale
DEEP["msb-for-sale.html"] = dict(
    name="MSB for sale",
    title="Registered MSB for Sale in Canada | AML Canada",
    desc="Buy a Canadian company already registered with FINTRAC as a money services business. Acquisitions from €28,000, with FINTRAC updates handled with you.",
    service_type="Acquisition of a FINTRAC-registered money services business",
    offers=[("28000", "EUR", "Registered Canadian MSB for acquisition, starting price")],
    h1="A registered Canadian MSB, ready to take over.",
    lede="Acquire a Canadian company already registered with FINTRAC as a money services business. From €28,000.",
    hero_price="From €28,000",
    label="MSB · Registered · For sale",
    need="acquire",
    intro=("Buying a company that's already registered with FINTRAC is one way into Canada, if the company's records are clean and the change of ownership is reported on time.",
           ["We offer Canadian companies already registered with FINTRAC as money services businesses for acquisition, starting from €28,000. The price depends on the company, the services it's registered for and its history.",
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
        ("how", "How buying a registered MSB works", """          <ol>
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
          <p>Our guide to <a href="buying-an-msb-canada.html">buying an MSB in Canada</a> has the full due-diligence checklist.</p>"""),
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
          </table></div>"""),
    ],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("Update, renew or cancel your registration", F_UPD), ("Money services businesses", F_MSB),
             ("PCMLTFA, section 11.11", L_PCMLTFA), ("Bank of Canada, Acquisitions of control and prescribed changes", B_ACQ)],
    for_title="Who buys",
    for_items=[("Foreign payment businesses", "Entering Canada through an existing registered company."),
               ("Groups adding a Canadian entity", "A registered company to sit alongside existing operations."),
               ("Founders who prefer an existing company", "A company with a registration history they can review before committing.")],
    arts=["one", "register", "many"],
    faqs=[("How much does a registered MSB cost?", "Acquisitions start from €28,000. The price depends on the company, the services it's registered for and its history."),
          ("Does the FINTRAC registration stay with the company?", "The registration belongs to the registered business, so the purchase is of the company's shares; a new entity would need its own registration. After the purchase, FINTRAC must be told about changes to the registration information, such as new owners and directors, within 30 days."),
          ("Do the new owners need criminal record checks?", "FINTRAC asks for criminal record checks for the chief executive officer, the president, the directors and anyone owning or controlling 20% or more of the business. Any check that isn't in English or French needs a translation attested by a certified translator."),
          ("What if the company is registered with the Bank of Canada too?", "Then it must apply again and be re-registered by the Bank before the purchase closes. We check this during due diligence."),
          ("Does it come with a bank account?", "FINTRAC registration doesn't guarantee banking or payment partners. We discuss what each company has in place before you commit."),
          ("Can a buyer outside Canada acquire an MSB?", "Yes. Foreign buyers can acquire a registered Canadian company, subject to the same FINTRAC requirements.")],
    related=["msb-registration.html", "outsourced-compliance-officer.html", "canadian-address.html"],
)

# ------------------------------------------------------------------ RPAA registration
DEEP["rpaa-registration.html"] = dict(
    name="RPAA registration",
    title="RPAA PSP Registration with the Bank of Canada | AML Canada",
    desc="Register as a payment service provider (PSP) with the Bank of Canada under the RPAA. Fixed fee US$3,500, plus the Bank's own application fee.",
    service_type="Bank of Canada RPAA payment service provider registration",
    timing="Often 2 to 8 months (not guaranteed)",
    offers=[("3500", "USD", "RPAA PSP registration with the Bank of Canada, fixed fee (excludes the Bank's application fee)")],
    h1="PSP registration with the Bank of Canada.",
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
        ("who", "Does the RPAA apply to you?", """          <p>The Act covers businesses that perform payment functions for end users as a service or business activity, such as holding accounts or funds for end users, initiating, authorizing or transmitting electronic funds transfers, and providing clearing or settlement services. A PSP with a place of business in Canada is covered. A PSP outside Canada is covered when it directs retail payment activities at people or entities in Canada and performs them for end users in Canada (RPAA s.5).</p>
          <p>Banks and some other institutions are excluded, and some activities fall outside the Act, so we confirm where you stand before preparing anything. Our <a href="rpaa-registration-guide.html">RPAA guide</a> explains the Act in more detail.</p>"""),
        ("fees", "What it costs", """          <p>Our fee is a fixed US$3,500. The Bank's one-time, non-refundable application fee was CA$2,500 when it was introduced in November 2024 and is indexed to inflation each January, so we confirm the current amount before you apply.</p>
          <p>The Bank also plans to charge registered PSPs annual assessment fees to recover its supervision costs. It isn't charging them yet and will start once the cost-recovery regulations are finalized.</p>"""),
        ("process", "How we handle your application", """          <ol>
            <li><strong>Assessment.</strong> Which of your activities are retail payment activities, and whether you need FINTRAC registration as well.</li>
            <li><strong>Preparation.</strong> Your business, ownership, payment activities, agents, mandataries and third-party providers, gathered and checked.</li>
            <li><strong>Application.</strong> Submitted to the Bank of Canada, with the application fee.</li>
            <li><strong>Review.</strong> The Bank shares applications with the Department of Finance and FINTRAC, and the Minister of Finance can order a national security review. We help you answer questions along the way.</li>
            <li><strong>Decision.</strong> Once registered, your business is listed in the Bank's public registry of PSPs.</li>
          </ol>
          <p>In our experience the process often takes 2 to 8 months, though that isn't guaranteed. A new PSP can't start retail payment activities until the Bank registers it, so we plan the timeline with you from the start.</p>"""),
        ("after", "After registration", """          <p>Registered PSPs need a risk management and incident response framework and, if they hold end-user funds, a safeguarding framework. They also report incidents, changes and an annual report to the Bank. Our <a href="rpaa-compliance-program.html">RPAA compliance program</a> sets these up for a fixed US$3,500.</p>"""),
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
          ("What happens after registration?", "You need risk management, incident response and, if you hold end-user funds, safeguarding frameworks, plus incident notices, change notices and annual reports. Our RPAA compliance program covers these.")],
    related=["rpaa-compliance-program.html", "msb-registration.html", "outsourced-compliance-officer.html"],
)

# ------------------------------------------------------------------ RPAA compliance program
DEEP["rpaa-compliance-program.html"] = dict(
    name="RPAA compliance program",
    title="RPAA Compliance Program for PSPs | AML Canada",
    desc="RPAA frameworks for PSPs: governance, risk registers, incident response, third parties, safeguarding, cyber and continuity, annual reports. Fixed fee US$3,500.",
    service_type="RPAA compliance program and frameworks for payment service providers",
    offers=[("3500", "USD", "Compliance program for payment service providers, built to the Bank of Canada's RPAA requirements, fixed fee")],
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
        ("governance", "Senior officer and governance", """          <p>Clear roles and responsibilities, with a senior officer accountable for the frameworks, and enough resources to run them. We set out who owns each framework, how it's approved and reviewed, and how issues reach senior management.</p>"""),
        ("risk", "Risk framework and registers", """          <p>The Bank expects PSPs to identify their operational risks, protect against them, detect problems, and respond and recover, with periodic review and testing. We build your risk framework and the registers behind it: the risks in your payment activities, the controls that address them and who is responsible.</p>"""),
        ("incident", "Incident response", """          <p>When something goes wrong, your team needs to know what to do. The framework covers how incidents are identified, escalated, contained and recovered from. When you determine that an incident has a material impact, you notify the Bank and any affected end users, PSPs and clearing houses without delay, and no later than 48 hours after that determination.</p>"""),
        ("third-parties", "Third parties and agents", """          <p>Many PSPs depend on processors, banks, cloud providers and others, and some act through agents or mandataries. The framework covers how you assess and manage the risks they bring. Foreign PSPs also identify the agents or mandataries acting for them in Canada.</p>"""),
        ("safeguarding", "Safeguarding end-user funds", """          <p>If you hold end-user funds, you must safeguard them, either in a trust account, or in a segregated account protected by insurance or a guarantee. Your written safeguarding framework explains how end users get timely access to their funds and how funds would be paid out if your business became insolvent.</p>"""),
        ("cyber", "Cyber, IT and continuity", """          <p>Protecting the integrity, confidentiality and availability of your systems and data, detecting cyber threats, and keeping payments running, or restoring them quickly, when systems or providers fail.</p>"""),
        ("reporting", "Annual report and change notices", """          <p>PSPs file an annual report with the Bank no later than March 31 of the following year. The Bank lists its contents as up-to-date information on risk management and incident response, safeguarding of end-user funds where that applies, and certain financial and activity metrics.</p>
          <p>Changes to registration information are generally notified within 30 days after they happen, and certain changes at least 30 or 60 days before they take effect (Retail Payment Activities Regulations, ss.35 and 36). A significant change or new activity needs notice at least five business days before. An acquisition of control needs a new application, approved by the Bank before the acquisition closes (RPAA s.24). The framework sets out how you track, prepare and approve each of these.</p>"""),
    ],
    sources=[("Bank of Canada, Supervisory framework", B_FW), ("Retail payments", B_RPS), ("Reminder: PSP reporting obligations under the RPAA", B_REPORTING),
             ("Acquisitions of control and prescribed changes", B_ACQ), ("Retail Payment Activities Regulations", L_RPAR)],
    for_title="Who it's for",
    for_items=[("Newly registered PSPs", "Putting the Bank's frameworks in place for the first time."),
               ("PSPs that hold customer funds", "Safeguarding arrangements that need to be written down and tested."),
               ("Growing payment businesses", "New products, partners or markets that the frameworks didn't cover.")],
    arts=["programme", "scan", "many"],
    faqs=[("What does the RPAA require from payment service providers?", "Risk management and incident response frameworks, safeguarding of end-user funds where you hold them, incident notices within 48 hours of determining an incident is material, change notices, and an annual report by March 31."),
          ("How much does an RPAA compliance program cost?", "A fixed US$3,500 for the program documents covering all seven areas."),
          ("Is this the same as our FINTRAC AML program?", "No. The RPAA program covers operational risk and safeguarding under the Bank of Canada. A FINTRAC compliance program covers money laundering, terrorist financing and sanctions evasion. Many payment businesses need both."),
          ("Do you help us put the frameworks in place?", "Yes. We write them around how you operate and walk your team through them. Ongoing support can be covered by outsourced compliance officer hours.")],
    related=["rpaa-registration.html", "outsourced-compliance-officer.html", "compliance-programs.html"],
)

# ------------------------------------------------------------------ effectiveness reviews (scoped)
DEEP["effectiveness-reviews.html"] = dict(
    name="Effectiveness reviews",
    title="FINTRAC Effectiveness Review (Two-Year) | AML Canada",
    desc="The AML effectiveness review FINTRAC requires every two years: your policies, risk assessment and training tested, with written findings.",
    service_type="Compliance program effectiveness review",
    offers=[],
    h1="Find the gaps before an examiner does.",
    lede="The two-year effectiveness review FINTRAC requires, and preparation for a FINTRAC examination.",
    hero_price="Scoped to your business",
    label="Gap found · Review",
    flag=True,
    need="review",
    intro=("Every business FINTRAC regulates must review the effectiveness of its compliance program at least every two years.",
           ["An effectiveness review tests whether your policies and procedures, risk assessment and training work day to day, and whether what your team does matches what your documents say.",
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
        ("how-often", "How often is an effectiveness review required?", """          <p>At least every two years. FINTRAC requires every reporting entity to review the effectiveness of its compliance program, covering its policies and procedures, risk assessment and training program, at a minimum once every two years. The review looks at how the program runs day to day as well as what the documents say.</p>"""),
        ("who-reviews", "Who can carry out the review", """          <p>FINTRAC's guidance says the review is carried out by an internal or external auditor or, if the business has no auditor, by the business itself. Whoever does it should know the requirements of the PCMLTFA and its regulations. An external review gives you independence and a fresh view.</p>"""),
        ("tests", "What a review tests", """          <ul>
            <li>whether your policies and procedures reflect current requirements and your current business;</li>
            <li>whether your risk assessment covers your clients, products, channels and geography, including sanctions evasion risk, and whether your controls follow from it;</li>
            <li>whether training happened, reached the right people and matches your risks;</li>
            <li>samples of client files, monitoring and reports to FINTRAC, to see how the program runs.</li>
          </ul>"""),
        ("vs-exam", "Effectiveness review or FINTRAC examination?", """          <p>An effectiveness review is your own check of your program. A FINTRAC examination is FINTRAC's assessment of your compliance. A recent, honest review, with its findings being fixed, is one of the best ways to prepare for an examination.</p>"""),
    ],
    sources=[("FINTRAC, Compliance program requirements", F_G4)],
    for_title="Who it's for",
    for_items=[("Reporting entities due a review", "Including businesses whose last review is approaching two years."),
               ("Businesses expecting an examination", "Getting ready before FINTRAC arrives."),
               ("New compliance officers", "Taking stock of a program they've inherited.")],
    arts=["review", "scan", "programme"],
    faqs=[("How often is an AML effectiveness review required in Canada?", "At least every two years, covering your policies and procedures, risk assessment and training program."),
          ("Can we do the review ourselves?", "FINTRAC's guidance allows a self-review if you have no internal or external auditor, provided whoever does it knows the requirements. An external review adds independence."),
          ("What do we receive?", "Written findings and recommendations, in order of priority, so you know what to fix first."),
          ("FINTRAC has contacted us about an examination. Where do we start?", "Book a consultation. We review your program and records with you and help you prepare to show how it works.")],
    related=["compliance-programs.html", "outsourced-compliance-officer.html", "training.html"],
)

# ------------------------------------------------------------------ training (scoped)
DEEP["training.html"] = dict(
    name="Training",
    title="AML Training for FINTRAC Compliance in Canada | AML Canada",
    desc="Anti-money laundering training for MSB front-line staff, compliance teams and senior management, built to meet FINTRAC's training requirement.",
    service_type="Anti-money laundering (AML) training",
    offers=[],
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
        ("training-required", "Is AML training required in Canada?", """          <p>Yes, if you have employees, agents or others authorized to act on your behalf. In that case a written, ongoing compliance training program, with a plan for delivering it, is one of the required elements of a compliance program for businesses regulated by FINTRAC. Training should fit your business and your risks, and reach the people who deal with clients or transactions. A sole proprietor with no employees, agents or others authorized to act for them doesn't need a training program.</p>"""),
        ("roles", "Training for each role", """          <p>Front-line staff learn to recognize unusual activity, identify clients and know when and how to escalate. Compliance teams cover reviews, reporting, the 24-hour rule and deadlines, and how to document decisions. Senior management covers their responsibilities for the program and how to oversee it.</p>"""),
        ("records", "Training records", """          <p>Being able to show who was trained, on what and when is part of showing your program works. We help you keep those records, ready for your effectiveness review or a FINTRAC examination.</p>"""),
    ],
    sources=[("FINTRAC, Compliance program requirements", F_G4)],
    for_title="When teams book training",
    for_items=[("A new program", "Staff learning a compliance program that has just been written."),
               ("Before a review or examination", "Training and records brought up to date ahead of your effectiveness review or a FINTRAC examination."),
               ("New products or rules", "Training updated when you launch something new or the requirements change.")],
    arts=["training", "many", "programme"],
    faqs=[("Is AML training mandatory in Canada?", "Yes, if you have employees, agents or others authorized to act for you. A sole proprietor with no employees, agents or others acting for them doesn't need a training program."),
          ("Who needs AML training?", "Anyone whose work touches your compliance obligations, typically front-line staff, agents, compliance teams and senior management."),
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

DEEP["incorporation-canada.html"] = dict(
    name="Company incorporation",
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
        ("fees", "What it costs", """          <p>Our fee is a fixed US$1,500. Government fees are paid separately to the government: currently CA$200 for federal online incorporation (CA$100 more for 4-hour express) or CA$300 for Ontario online incorporation.</p>
          <p>For a federal online incorporation, the name search is built into the application, so a word name doesn't need a separate Nuans report. A named Ontario company needs an Ontario-biased Nuans name search report; a numbered company doesn't.</p>"""),
        ("after", "After incorporation", """          <ul>
            <li>Keep corporate records, including a register of individuals with significant control.</li>
            <li>For a federal corporation, file information about individuals with significant control with Corporations Canada at incorporation, every year with the annual return, and within 15 days of a change to the register. This has applied since January 22, 2024.</li>
            <li>File an annual return each year (federal online annual return: CA$12).</li>
            <li>Register for tax accounts, and in each province where you carry on business.</li>
            <li>Register with <a href="msb-registration.html">FINTRAC as an MSB</a> or with the <a href="rpaa-registration.html">Bank of Canada under the RPAA</a> before you start offering those services.</li>
          </ul>"""),
    ],
    sources=[("Corporations Canada, Services, fees and processing times", CC_FEES), ("Directors and officers", CC_DIR),
             ("Next steps after incorporating", CC_NEXT), ("Individuals with significant control: file your information", CC_ISC),
             ("Naming a corporation", CC_NAME), ("Canada Business Corporations Act", L_CBCA),
             ("Ontario, Register your business online", ON_INC), ("Ontario fees and timing", ON_FEES)],
    for_title="Who it's for",
    for_items=[("Foreign businesses entering Canada", "A Canadian company to hold your registration and contracts."),
               ("New MSBs and payment companies", "The company that will register with FINTRAC or the Bank of Canada."),
               ("Founders on a deadline", "Usually incorporated within 24 hours, so the next steps can start.")],
    arts=["one", "address", "register"],
    faqs=[("How much does it cost to incorporate a company in Canada?", "Our fee is a fixed US$1,500. Government filing fees are separate: currently CA$200 federally online or CA$300 in Ontario online."),
          ("How long does incorporation take?", "Usually within 24 hours once we have your details and documents, often a few hours. It isn't guaranteed."),
          ("Can a non-resident incorporate in Canada?", "Yes. Federal companies need at least 25% resident Canadian directors (at least one if there are fewer than four). Ontario doesn't require resident Canadian directors."),
          ("Should we incorporate before registering as an MSB?", "Usually, yes. The company is what registers with FINTRAC, so incorporating first means the registration can start straight away.")],
    related=["msb-registration.html", "canadian-address.html", "rpaa-registration.html"],
)
