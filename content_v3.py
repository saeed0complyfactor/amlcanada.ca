"""Long-form service content for site-v3 (rendered by build_v3.deep_page).

Fees come from the owner (11 October 2026). Regulatory statements were checked on
11 October 2026 against the FINTRAC and Bank of Canada pages listed in each page's
sources; re-check them before each update.
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
B_RPS = "https://www.bankofcanada.ca/core-functions/retail-payments-supervision/"
B_FW = "https://www.bankofcanada.ca/core-functions/retail-payments-supervision/supervisory-framework/"
B_REG = "https://www.bankofcanada.ca/core-functions/retail-payments-supervision/registration/"
B_FEE = "https://www.bankofcanada.ca/2024/10/registration-application-fee/"

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
              <tr><th scope="row">Suspicious transaction report (STR)</th><td>Reasonable grounds to suspect a transaction is related to money laundering or terrorist financing. No minimum amount.</td><td>As soon as practicable</td></tr>
              <tr><th scope="row">Large cash transaction report (LCTR)</th><td>Cash of $10,000 or more, in one transaction or several within 24 hours.</td><td>15 calendar days</td></tr>
              <tr><th scope="row">Electronic funds transfer report (EFTR)</th><td>International electronic funds transfers of $10,000 or more, in one transfer or several within 24 hours.</td><td>5 working days</td></tr>
              <tr><th scope="row">Large virtual currency transaction report (LVCTR)</th><td>Virtual currency worth $10,000 or more, in one transaction or several within 24 hours.</td><td>5 working days</td></tr>
              <tr><th scope="row">Terrorist property and listed person reports</th><td>Property you know or believe is owned or controlled by a terrorist, terrorist group or listed person.</td><td>Immediately</td></tr>
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
            "Your business stays responsible for its obligations under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA). Our job is to make sure the work behind them is done properly, on time and on record."]),
    facts=[("Fee", "US$1,500", "per block of 10 hours"),
           ("Hours", "Scalable", "add blocks as you grow"),
           ("Reports", "STR · EFTR · LVCTR", "LCTR and the others that apply to you"),
           ("Based", "In Canada", "working alongside your team")],
    fee=dict(amount="US$1,500", unit="per 10 hours · scalable",
             note="How your hours are used each month is set out in your written scope before work starts.",
             items=["All AML and compliance obligations under your program",
                    "Second-line review of customer onboarding",
                    "Advice on cases, products and regulatory questions",
                    "Regulatory reporting: STR, EFTR, LVCTR, LCTR and others",
                    "Policy and procedure maintenance",
                    "Business risk assessment",
                    "Client risk assessments",
                    "Hours that scale as your business grows"]),
    guide=[
        ("role", "What an outsourced compliance officer does", f"""          <p>Under the PCMLTFA, a business that FINTRAC regulates must appoint a compliance officer who is responsible for implementing its compliance program. FINTRAC's guidance expects that person to have the authority, and the access to resources and senior management, needed to do the job.</p>
          <p>An outsourced compliance officer fills that role, or supports the person who holds it, from outside the business. It's common for money services businesses, virtual currency dealers, payment companies and foreign businesses entering Canada, which need experienced compliance judgment but not a full-time senior hire.</p>
          <p>The work is practical and ongoing. Customers are onboarded every day, transactions need watching, reports have deadlines measured in days, and the rules and your business both change. We do that work with your team, inside your systems, so your program works in practice and not only on paper.</p>"""),
        ("scope", "What's included", f"""          <p>The scope covers your AML and compliance obligations as a whole. These are the parts most clients use their hours on.</p>
          <h3>Second-line customer onboarding review</h3>
          <p>Your front line collects customer information. As the second line, we review it: how identity was verified, beneficial ownership, politically exposed person and head of international organization determinations, third-party determinations, sanctions and listed person screening results, and the customer's risk rating. We approve or escalate files, apply enhanced measures where the risk is high, and sample completed files to check that the process holds up.</p>
          <h3>Advisory</h3>
          <p>Questions don't wait for a review cycle. A new product, a new market, a new agent, a payment partner's due diligence questionnaire, a bank asking about your program, or a letter from FINTRAC. We give you a clear answer, explain the reasoning, and record the decision so you can show it later.</p>
          <h3>Regulatory reporting</h3>
          <p>We prepare and file the reports your business has to make to FINTRAC, including suspicious transaction reports, electronic funds transfer reports, large virtual currency transaction reports and large cash transaction reports. Each one has its own threshold and deadline:</p>
          {REPORTS_TABLE}
          <p>Amounts are in Canadian dollars. Under FINTRAC's 24-hour rule, several smaller transactions can together reach the $10,000 threshold and become reportable.</p>
          <h3>Policy maintenance</h3>
          <p>Your compliance policies and procedures have to be kept up to date. We update them when the regulations change, when FINTRAC publishes new guidance, and when your business launches something new, and we keep a record of what changed and why.</p>
          <h3>Business risk assessment</h3>
          <p>Your program rests on a documented assessment of your money laundering and terrorist financing risks: your clients and business relationships, your products, services and delivery channels, where you operate, and new technologies. We write it, keep it current and make sure your controls follow from it.</p>
          <h3>Client risk assessments</h3>
          <p>Every client gets a risk rating that drives how closely you monitor them. We set the methodology, review ratings and make sure high-risk clients get the enhanced measures they need.</p>"""),
        ("how", "How the engagement runs", """          <ol>
            <li><strong>Consultation.</strong> Your business, your customers, your volumes and what you already have in place.</li>
            <li><strong>Written scope.</strong> What we'll do, how many hours to start with, and how we'll report the time to you.</li>
            <li><strong>Set-up.</strong> Access to the systems we need, such as your onboarding and screening tools and your FINTRAC reporting account, and a handover of open items.</li>
            <li><strong>Ongoing work.</strong> Onboarding reviews, reporting, advice and maintenance, with regular check-ins with your management.</li>
            <li><strong>Scaling.</strong> As volumes grow, add blocks of hours, or hand the work to an in-house compliance officer we help you hire and train.</li>
          </ol>"""),
        ("hours", "How many hours you might need", """          <p>It depends on how many customers you onboard, how many alerts and reports you generate, how many products and markets you serve, and whether you deal in cash or virtual currency. A business preparing to launch needs far fewer hours than one onboarding hundreds of customers a month.</p>
          <p>We estimate a starting number of hours with you in the consultation, then adjust once real volumes are clear. Hours are bought in blocks of 10, so the cost follows your workload rather than a fixed salary.</p>"""),
        ("responsibility", "Your responsibilities, and ours", """          <p>Outsourcing the work doesn't outsource the obligation. Your business remains the reporting entity, and your senior management stays accountable for the program. We make that workable: decisions are documented, escalations reach the right people, and you always know what was done in your name.</p>
          <ul>
            <li>You provide access, information and timely decisions.</li>
            <li>We carry out the agreed work, flag risks early and keep records you can show an examiner.</li>
            <li>We agree in writing who signs off on what, including reports and policy changes.</li>
          </ul>"""),
        ("mlro", "MLRO, compliance officer or CCO?", """          <p>The titles differ by country. In the UK and Europe the role is usually called the MLRO, or money laundering reporting officer. Canada's PCMLTFA framework uses "compliance officer", and many firms use "chief compliance officer" too. If you're entering Canada from abroad and looking for an MLRO, the Canadian compliance officer is the equivalent role, with Canada's own reports, thresholds and deadlines.</p>"""),
    ],
    sources=[("FINTRAC, Compliance program requirements", F_G4), ("Reporting suspicious transactions", F_STR),
             ("Reporting electronic funds transfers", F_EFT), ("Reporting large virtual currency transactions", F_LVCTR),
             ("Reporting large cash transactions", F_LCTR), ("The 24-hour rule", F_24)],
    for_title="Who it's for",
    for_items=[("New MSBs and fintechs", "Registered, or about to be, and needing a compliance officer from day one."),
               ("Foreign businesses serving Canada", "Teams abroad that need someone who works with Canadian requirements every day."),
               ("Growing compliance teams", "Extra capacity for onboarding reviews, reporting and maintenance.")],
    arts=["scan", "address", "many"],
    faqs=[("Can a business outsource its compliance officer in Canada?", "Many businesses use an outside compliance officer, or outside support for the person they appoint. However it's arranged, your business stays responsible for its obligations, and the compliance officer needs the authority and access to senior management to do the job. We set the arrangement out in writing so it's clear who does what."),
          ("What does an outsourced compliance officer cost?", "US$1,500 for each block of 10 hours. You choose how many blocks you need, and you can add more as your business grows."),
          ("What is an MLRO in Canada?", "MLRO means money laundering reporting officer, a title used mainly in the UK and Europe. The Canadian equivalent under the PCMLTFA is the compliance officer."),
          ("Which FINTRAC reports do you handle?", "Suspicious transaction reports, electronic funds transfer reports, large virtual currency transaction reports, large cash transaction reports, and terrorist property and listed person reports, whichever apply to your business."),
          ("Do you work with foreign money services businesses?", "Yes. Many of our clients are based outside Canada and serve people in Canada."),
          ("Can we start small?", "Yes. Start with the hours you need now, and add blocks of 10 hours when your volumes grow.")],
    related=["compliance-programs.html", "msb-registration.html", "effectiveness-reviews.html"],
)

# ------------------------------------------------------------------ MSB registration
DEEP["msb-registration.html"] = dict(
    name="MSB registration",
    title="FINTRAC MSB Registration in Canada | AML Canada",
    desc="FINTRAC registration for money services businesses, foreign MSBs and virtual currency (crypto) dealers. Fixed fee US$3,500, prepared and submitted with you.",
    service_type="FINTRAC money services business registration",
    timing="About 1 week to 7 months",
    offers=[("3500", "USD", "FINTRAC MSB registration, fixed fee")],
    h1="MSB registration with FINTRAC, prepared properly.",
    lede="For money services businesses, foreign MSBs and virtual currency dealers. Fixed fee US$3,500.",
    hero_price="Fixed fee · US$3,500",
    label="MSB · Registration prepared",
    need="register",
    intro=("Money services businesses (MSBs) must register with FINTRAC before they start operating, and so must foreign businesses that serve people in Canada.",
           ["FINTRAC, the Financial Transactions and Reports Analysis Centre of Canada, registers money services businesses under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA). It's how foreign exchange dealers, money transfer businesses, virtual currency dealers and others become allowed to operate in Canada.",
            "We work out whether and how registration applies to you, gather and check everything FINTRAC asks for, support you through submission and FINTRAC's questions, and put your compliance program in place alongside it.",
            "Our fee is a fixed US$3,500. FINTRAC itself doesn't charge to register."]),
    facts=[("FINTRAC fee", "None", "FINTRAC doesn't charge to register"),
           ("When", "Before you operate", "registration comes first"),
           ("Typical approval", "1 week–7 months", "depending on completeness and FINTRAC's workload"),
           ("Valid for", "2 years", "then renewed")],
    fee=dict(amount="US$3,500", unit="fixed fee · one time",
             note="Covers your registration. Compliance program documents are a separate fixed fee of US$3,500.",
             items=["Assessment of which of your activities are money services",
                    "Registration information gathered and checked with you",
                    "Ownership, corporate and criminal record check requirements coordinated",
                    "Submission, and FINTRAC's follow-up questions",
                    "Foreign MSB requirements, including your representative in Canada",
                    "Coordination with your compliance program"]),
    guide=[
        ("who-must-register", "Who has to register as an MSB", f"""          <p>A business with a place of business in Canada must register with FINTRAC before it operates as a money services business. FINTRAC's guidance lists these activities:</p>
          {MSB_ACTIVITIES}
          <p>Registering or being licensed with a province or territory doesn't replace FINTRAC registration. Whether your own activities are covered depends on how your business works, which is the first thing we confirm with you.</p>"""),
        ("foreign-msb", "Foreign MSB registration", """          <p>A foreign money services business (FMSB) has no place of business in Canada but directs and provides money services to people or entities in Canada. It must register with FINTRAC before it starts. FINTRAC treats a business as directing services at Canada if, for example, its marketing targets people in Canada, it uses a .ca domain, or it's listed in a Canadian business directory.</p>
          <p>A foreign MSB must name a representative for service who lives in Canada. The foreign business itself, not the representative, stays responsible for meeting its obligations.</p>"""),
        ("what-fintrac-asks", "What FINTRAC asks for", """          <ul>
            <li>details of your business, including incorporation, ownership and senior management;</li>
            <li>your bank account information;</li>
            <li>your compliance officer;</li>
            <li>how many employees you have, and every location you operate from;</li>
            <li>estimated annual transaction totals for each money service you offer;</li>
            <li>any agents or mandataries that provide services on your behalf;</li>
            <li>for a foreign MSB, your representative for service in Canada;</li>
            <li>documents confirming the business exists and how it's owned and controlled, such as a certificate of incorporation;</li>
            <li>criminal record checks.</li>
          </ul>
          <p>Criminal record checks are needed for the chief executive officer, the president, directors, and anyone who owns or controls 20% or more of the business, directly or indirectly. They must come from a competent authority in the person's country of residence, be dated no more than six months before you submit them, and be translated if they aren't in English or French. Gathering these from several countries is often what takes longest, so we start early.</p>"""),
        ("how", "How registration works with us", """          <ol>
            <li><strong>Assessment.</strong> Which of your services are money services, whether you're an MSB or a foreign MSB, and what follows from that.</li>
            <li><strong>Preparation.</strong> A checklist of everything FINTRAC needs, and help gathering and checking it.</li>
            <li><strong>Submission.</strong> Your registration, submitted to FINTRAC with your approval.</li>
            <li><strong>Follow-up.</strong> Answers to FINTRAC's questions until your registration is decided.</li>
            <li><strong>Compliance program.</strong> Built alongside your registration, not after it, so you're ready to operate.</li>
          </ol>"""),
        ("how-long", "How long registration takes", """          <p>In our experience, FINTRAC approval takes anywhere from about 1 week to 7 months. Some of our clients have been registered in about a week. The biggest factors are how complete and consistent the application is, how quickly criminal record checks arrive, and FINTRAC's workload at the time. A thorough application avoids the follow-up questions that slow things down.</p>"""),
        ("after", "After you register", """          <p>Registration is valid for two years and has to be renewed before it expires. Between renewals, you must tell FINTRAC within 30 days when your registration information changes, such as a new address, new owners or directors, or a change to the services you offer.</p>
          <p>Registration is the start, not the finish. A registered MSB also needs a working compliance program, client identification, record keeping, and reporting to FINTRAC. Records generally have to be kept for at least five years.</p>"""),
        ("crypto", "Virtual currency dealers", """          <p>Dealing in virtual currency is a money service, so crypto exchanges and dealers register with FINTRAC as MSBs, including foreign ones that serve people in Canada. Once registered, they have additional obligations, such as reporting virtual currency transactions of $10,000 or more within five working days. Provincial securities rules can also apply to some crypto trading platforms; we'll tell you if that's something you need separate advice on.</p>"""),
    ],
    sources=[("FINTRAC, Money services businesses", F_MSB), ("Register your MSB or FMSB", F_REG),
             ("Update, renew or cancel your registration", F_UPD), ("Reporting large virtual currency transactions", F_LVCTR)],
    for_title="Who it's for",
    for_items=[("New money services businesses", "Foreign exchange dealers, money transfer businesses and others getting started."),
               ("Virtual currency dealers", "Crypto exchanges and dealers in virtual currency."),
               ("Foreign money services businesses", "Businesses outside Canada serving people in Canada.")],
    arts=["one", "many", "address"],
    faqs=[("How much does MSB registration cost?", "FINTRAC doesn't charge a registration fee. Our fee to prepare and support your registration is a fixed US$3,500."),
          ("How long does FINTRAC registration take?", "In our experience, FINTRAC approval takes anywhere from about 1 week to 7 months. Some of our clients have been registered in about a week. It depends mostly on how complete the application is, how quickly criminal record checks arrive, and FINTRAC's workload."),
          ("Can a company outside Canada register as an MSB?", "Yes. A foreign business that directs and provides money services to people in Canada registers as a foreign MSB and must name a representative for service who lives in Canada."),
          ("Do I need a compliance program before I register?", "You need one to operate. FINTRAC asks for your compliance officer when you register, and your obligations start as soon as you begin. We build your program alongside your registration. Program documents are a separate fixed fee of US$3,500."),
          ("How often do I renew?", "Every two years. Changes to your registration information have to be reported within 30 days."),
          ("Do crypto businesses register with FINTRAC?", "Yes. Dealing in virtual currency is a money service, so crypto dealers and exchanges register as MSBs.")],
    related=["compliance-programs.html", "outsourced-compliance-officer.html", "canadian-address.html"],
)

# ------------------------------------------------------------------ compliance program
DEEP["compliance-programs.html"] = dict(
    name="Compliance programs",
    title="FINTRAC AML Compliance Program (PCMLTFA) | AML Canada",
    desc="PCMLTFA compliance program documents for FINTRAC-regulated businesses: policies and procedures, risk assessment, training and review plans. Fixed fee US$3,500.",
    service_type="PCMLTFA AML compliance program documents",
    offers=[("3500", "USD", "FINTRAC PCMLTFA compliance program documents, fixed fee")],
    h1="An AML compliance program written for how you actually operate.",
    lede="FINTRAC and PCMLTFA compliance program documents for the businesses FINTRAC regulates. Fixed fee US$3,500.",
    hero_price="Fixed fee · US$3,500",
    label="Program · 5 of 5 parts",
    need="programme",
    intro=("Every business FINTRAC regulates must have a compliance program. It has to work in practice, not only on paper.",
           ["Under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA), a compliance program brings together a compliance officer, written policies and procedures, a risk assessment, an ongoing training program and a regular review of how well it all works.",
            "We write your program documents around your products, your customers and the way your team works, in language your staff can follow. No template with your name pasted on.",
            "You receive 14 documents, from the AML/ATF Compliance Policy to the Fraud Risk Management Policy, for a fixed fee of US$3,500."]),
    facts=[("Documents", "14", "in one fixed fee"),
           ("Required parts", "5", "in every program"),
           ("Review", "Every 2 years", "at a minimum"),
           ("Policies", "Kept current", "and approved by a senior officer")],
    fee=dict(amount="US$3,500", unit="fixed fee · program documents",
             note="Keeping the program current afterwards can be covered by outsourced compliance officer hours.",
             items=PCMLTFA_DOCS),
    guide=[
        ("documents", "The 14 documents you receive", """          <p>Your fixed fee covers a complete set of PCMLTFA compliance program documents, written for your business:</p>
          <ol class="doc-list">
""" + "\n".join(f"            <li>{d}</li>" for d in PCMLTFA_DOCS) + """
          </ol>
          <p>Together they cover the policies, procedures, risk assessment, training and review planning behind the five required parts of a FINTRAC compliance program, plus your risk appetite and fraud risk management.</p>"""),
        ("program-elements", "The five parts of a compliance program", """          <p>FINTRAC's guidance sets out five required elements:</p>
          <ol>
            <li><strong>A compliance officer</strong>, appointed to be responsible for implementing the program.</li>
            <li><strong>Written policies and procedures</strong>, kept up to date and, for an entity, approved by a senior officer.</li>
            <li><strong>A risk assessment</strong> of the business's money laundering and terrorist financing risks, documented.</li>
            <li><strong>A written, ongoing compliance training program</strong>, with a plan for delivering it.</li>
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
        ("risk-assessment", "Your risk assessment", """          <p>The risk assessment is the foundation of everything else. It looks at your clients and business relationships, your products, services and delivery channels, the places you operate in and deal with, new developments and technologies, and anything else relevant to your business. Your controls should follow from it: higher risk, closer attention.</p>"""),
        ("bank", "If your bank or payment partner has asked for your program", """          <p>Banks and payment partners usually want to see that your program exists, fits your business, has a named compliance officer, and is actually followed. If you've been asked and don't have one, or aren't sure yours will stand up, book a consultation. We'll tell you what's missing and how quickly it can be put right.</p>"""),
        ("keeping-current", "Keeping it current", """          <p>A program written once and left on a shelf goes out of date as your business and the rules change. We can keep it current through outsourced compliance officer hours, and test it in your two-year effectiveness review.</p>"""),
    ],
    sources=[("FINTRAC, Compliance program requirements", F_G4), ("Money services businesses", F_MSB), ("The 24-hour rule", F_24)],
    for_title="Who it's for",
    for_items=[("Newly registered businesses", "Putting a program in place for the first time."),
               ("Growing businesses", "New products, new markets or more volume than the program was written for."),
               ("Businesses after a review or examination", "Closing the gaps that were found.")],
    arts=["one", "programme", "scan"],
    faqs=[("What does an AML compliance program include in Canada?", "Five parts: a compliance officer, written policies and procedures, a risk assessment, an ongoing training program and plan, and an effectiveness review at least every two years."),
          ("How much does a compliance program cost?", "A fixed US$3,500 for 14 PCMLTFA compliance program documents, from the AML/ATF Compliance Policy to the Fraud Risk Management Policy."),
          ("Do you use templates?", "We use a proven structure, but the content is written for your products, customers and team. A program that doesn't describe how you actually work won't hold up in an examination."),
          ("Does the fee include the effectiveness review?", "No. The program includes a plan for your review. The review itself is a separate, scoped piece of work."),
          ("Can you keep the program up to date afterwards?", "Yes, through outsourced compliance officer hours at US$1,500 per 10 hours."),
          ("Our bank has asked for our AML program. What now?", "Book a consultation. We'll look at what you have, tell you what's missing and agree a written scope to close the gaps.")],
    related=["outsourced-compliance-officer.html", "effectiveness-reviews.html", "msb-registration.html"],
)

# ------------------------------------------------------------------ Canadian address
DEEP["canadian-address.html"] = dict(
    name="Canadian address",
    title="FINTRAC-Compliant Canadian Business Address | AML Canada",
    desc="A FINTRAC-compliant Canadian business address for foreign MSBs and companies entering Canada, for your registration and setup. US$200 per month.",
    service_type="Canadian business address",
    offers=[("200", "USD", "Canadian business address, per month")],
    h1="A Canadian business address you can register with.",
    lede="A FINTRAC-compliant Canadian address for foreign MSBs and companies entering Canada. US$200 per month.",
    hero_price="US$200 · per month",
    label="Business address · Canada",
    need="address",
    intro=("Setting up in Canada from abroad is easier with a Canadian base for your business.",
           ["We provide a FINTRAC-compliant Canadian business address for companies entering the Canadian market, including foreign money services businesses, for your registration, your partners and your customers.",
            "It costs US$200 per month. What's included, such as how mail is handled, is confirmed with you in writing before anything starts."]),
    facts=[("Fee", "US$200", "per month"),
           ("For", "Foreign MSBs", "and companies entering Canada"),
           ("Use", "FINTRAC-compliant", "for your registration"),
           ("Scope", "In writing", "before anything starts")],
    fee=dict(amount="US$200", unit="per month",
             note="Often combined with MSB registration and an outsourced compliance officer.",
             items=["A Canadian business address",
                    "FINTRAC-compliant, for your registration",
                    "Scope, including mail handling, confirmed in writing",
                    "Coordinated with your MSB registration"]),
    guide=[
        ("why", "Why a Canadian address helps", """          <p>FINTRAC's registration asks for the locations you operate from, and Canadian banks, payment partners and customers look for a Canadian presence. A Canadian business address gives your setup a stable Canadian base from the start.</p>"""),
        ("representative", "An address isn't the same as a representative for service", """          <p>A foreign MSB registering with FINTRAC must also name a representative for service: a person who lives in Canada and can accept notices on its behalf. That's a separate requirement from your address. If you need help with it, raise it in your consultation and we'll explain the options.</p>"""),
        ("how", "How it works", """          <ol>
            <li><strong>Consultation.</strong> Your plans for Canada and how you'll use the address.</li>
            <li><strong>Written scope.</strong> What's included, confirmed before anything starts.</li>
            <li><strong>Start.</strong> Your address is ready to use on your registration and with your partners.</li>
            <li><strong>Monthly.</strong> US$200 per month while you use it.</li>
          </ol>"""),
    ],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("Money services businesses", F_MSB)],
    for_title="Who it's for",
    for_items=[("Foreign money services businesses", "Companies outside Canada that serve customers in Canada."),
               ("Companies opening Canadian operations", "Businesses establishing a presence before hiring locally."),
               ("Start-ups preparing to launch", "Founders who need their Canadian setup in order early.")],
    arts=["address", "one", "register"],
    faqs=[("How much is a Canadian business address?", "US$200 per month."),
          ("Can I use the address on my FINTRAC registration?", "Yes. The address is FINTRAC-compliant, and we coordinate it with your MSB registration."),
          ("Is the address my representative for service?", "No. A foreign MSB's representative for service is a person living in Canada, which is a separate requirement. Ask us about it in your consultation."),
          ("What happens to mail sent to the address?", "How mail is handled is confirmed in your written scope before anything starts.")],
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
    intro=("Buying a company that's already registered can be a faster route into Canada than starting from nothing, if the company is clean and the handover is done properly.",
           ["We offer Canadian companies already registered with FINTRAC as money services businesses for acquisition, starting from €28,000. The price depends on the company, the services it's registered for and its history.",
            "We take you through choosing the right company, checking it before you commit, the change of ownership, and the updates FINTRAC has to receive afterwards."]),
    facts=[("Price", "From €28,000", "depending on the company"),
           ("FINTRAC updates", "30 days", "to report changes"),
           ("Registration", "2 years", "then renewed"),
           ("Due diligence", "First", "before you commit")],
    fee=dict(amount="€28,000", unit="starting price · acquisition",
             note="Compliance program, compliance officer and Canadian address are available alongside, at their own fees.",
             items=["A Canadian company registered with FINTRAC as an MSB",
                    "Company records and registration history reviewed with you",
                    "Support through the change of ownership",
                    "Updates to FINTRAC within 30 days, including new owners and directors",
                    "Guidance on what the new owners need to provide"]),
    guide=[
        ("how", "How buying a registered MSB works", """          <ol>
            <li><strong>Consultation.</strong> Your plans: the services you'll offer, your customers and your timeline.</li>
            <li><strong>Matching.</strong> A company registered for the money services you need.</li>
            <li><strong>Due diligence.</strong> Corporate records, registration status and history, reviewed before you commit.</li>
            <li><strong>Change of ownership.</strong> The transfer of the company to you.</li>
            <li><strong>FINTRAC updates.</strong> Changes to the registration information, such as owners, directors and compliance officer, reported within 30 days.</li>
          </ol>"""),
        ("check", "What to check before you buy", """          <ul>
            <li>that the registration is active and covers the services you plan to offer;</li>
            <li>when the registration is next due for renewal;</li>
            <li>the company's corporate records, ownership history and any past compliance issues;</li>
            <li>that the new owners and directors can provide what FINTRAC asks for, including criminal record checks for directors and anyone owning or controlling 20% or more;</li>
            <li>whether provincial requirements apply where you'll operate. Quebec, for example, licenses money services businesses separately.</li>
          </ul>"""),
        ("after", "After the purchase", """          <p>The obligations come with the company. The business needs a compliance officer and a compliance program that reflect its new owners and services, and it must report to FINTRAC, keep records and renew its registration every two years. FINTRAC registration doesn't guarantee a bank account or payment partners, which make their own decisions.</p>"""),
        ("compare", "Buying an MSB or registering a new one", """          <div class="table-wrap"><table>
            <thead><tr><th scope="col"></th><th scope="col">Register a new MSB</th><th scope="col">Buy a registered MSB</th></tr></thead>
            <tbody>
              <tr><th scope="row">Our fee</th><td>US$3,500, fixed</td><td>From €28,000</td></tr>
              <tr><th scope="row">Starting point</th><td>A new or existing company of yours</td><td>A company already registered</td></tr>
              <tr><th scope="row">Main wait</th><td>Preparing the application and FINTRAC's review</td><td>Due diligence and the change of ownership</td></tr>
              <tr><th scope="row">Afterwards</th><td colspan="2">The same obligations: compliance program, reporting, record keeping and renewal</td></tr>
            </tbody>
          </table></div>"""),
    ],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("Update, renew or cancel your registration", F_UPD), ("Money services businesses", F_MSB)],
    for_title="Who it's for",
    for_items=[("Foreign payment businesses", "Entering Canada through an established registered company."),
               ("Founders on a timeline", "Launching sooner than a new registration might allow."),
               ("Groups adding a Canadian entity", "A registered company to sit alongside existing operations.")],
    arts=["one", "register", "many"],
    faqs=[("How much does a registered MSB cost?", "Acquisitions start from €28,000. The price depends on the company, the services it's registered for and its history."),
          ("Does the FINTRAC registration stay with the company?", "The registration belongs to the registered business. When you buy the company, FINTRAC must be told about changes to its registration information, such as new owners and directors, within 30 days."),
          ("Do the new owners need criminal record checks?", "FINTRAC asks for criminal record checks for directors and anyone owning or controlling 20% or more of the business, so plan for them as part of the purchase."),
          ("Does it come with a bank account?", "FINTRAC registration doesn't guarantee banking or payment partners. We discuss what each company has in place before you commit."),
          ("Can a buyer outside Canada acquire an MSB?", "Yes. Foreign buyers can acquire a registered Canadian company, subject to the same FINTRAC requirements.")],
    related=["msb-registration.html", "outsourced-compliance-officer.html", "canadian-address.html"],
)

# ------------------------------------------------------------------ RPAA registration
DEEP["rpaa-registration.html"] = dict(
    name="RPAA registration",
    title="RPAA PSP Registration with the Bank of Canada | AML Canada",
    desc="Register as a payment service provider (PSP) with the Bank of Canada under the RPAA. Fixed fee US$3,500, plus the Bank's CA$2,500 application fee.",
    service_type="Bank of Canada RPAA payment service provider registration",
    timing="About 2 to 8 months",
    offers=[("3500", "USD", "RPAA PSP registration with the Bank of Canada, fixed fee (excludes the Bank's application fee)")],
    h1="PSP registration with the Bank of Canada.",
    lede="Retail Payment Activities Act (RPAA) registration for payment service providers. Fixed fee US$3,500, plus the Bank's application fee.",
    hero_price="Fixed fee · US$3,500",
    label="PSP · RPAA · Registered",
    need="rpaa",
    intro=("Payment service providers that perform retail payment activities for people and businesses in Canada must register with the Bank of Canada under the Retail Payment Activities Act (RPAA).",
           ["The RPAA brought payment service providers (PSPs), such as payment processors, digital wallets and money transfer apps, under the Bank of Canada's supervision. Registration comes first; the Bank then expects frameworks for operational risk, incident response and safeguarding customer funds.",
            "We assess whether the RPAA applies to you, prepare your registration application, and support you through the Bank's questions and review.",
            "Our fee is a fixed US$3,500. The Bank of Canada also charges a one-time application fee, currently CA$2,500, which you pay to the Bank."]),
    facts=[("Our fee", "US$3,500", "fixed, one time"),
           ("Bank of Canada fee", "CA$2,500", "one time, paid to the Bank"),
           ("Typical timing", "2–8 months", "including national security review"),
           ("Annual report", "By March 31", "for the previous year")],
    fee=dict(amount="US$3,500", unit="fixed fee · plus CA$2,500 Bank of Canada fee",
             note="The Bank's application fee is non-refundable, set by the Bank and adjusted each calendar year. RPAA compliance program documents are a separate fixed fee of US$3,500.",
             items=["Assessment of whether the RPAA applies to your activities",
                    "Registration application prepared with you",
                    "Your payment activities, agents, mandataries and third parties described",
                    "Support through the Bank's questions and national security review",
                    "Coordination with your FINTRAC registration, where you need both"]),
    guide=[
        ("who", "Who has to register under the RPAA", """          <p>The RPAA applies to payment service providers that perform one or more payment functions for end users, as a service or business activity:</p>
          <ul>
            <li>providing or maintaining an account held for end users;</li>
            <li>holding funds on behalf of end users;</li>
            <li>initiating an electronic funds transfer at an end user's request;</li>
            <li>authorizing an electronic funds transfer, or transmitting, receiving or facilitating an instruction for one;</li>
            <li>providing clearing or settlement services.</li>
          </ul>
          <p>It covers PSPs with a place of business in Canada, and PSPs outside Canada that perform retail payment activities for end users in Canada. Some institutions, such as banks, are excluded, and some activities fall outside the Act, so the first step is confirming that it applies to you.</p>"""),
        ("fees", "What it costs", """          <p>Our fee for preparing and supporting your registration is a fixed US$3,500. Separately, the Bank of Canada charges every applicant a one-time, non-refundable registration application fee. It was set at CA$2,500 from November 1, 2024 and is adjusted each calendar year in line with inflation, so we confirm the current amount when you apply. Once registered, PSPs also pay the Bank annual assessment fees to cover the cost of supervision.</p>"""),
        ("process", "How registration works", """          <ol>
            <li><strong>Assessment.</strong> Which of your activities are retail payment activities, and whether you need FINTRAC registration as well.</li>
            <li><strong>Preparation.</strong> Your business, ownership, payment activities, agents, mandataries and third-party providers, gathered and checked.</li>
            <li><strong>Application.</strong> Submitted to the Bank of Canada, with the application fee.</li>
            <li><strong>Review.</strong> The Bank shares applications with the Department of Finance for national security screening and with FINTRAC. We help you answer questions along the way.</li>
            <li><strong>Decision.</strong> The Bank publishes registration decisions as screenings are completed.</li>
          </ol>
          <p>In our experience, the whole process generally takes about 2 to 8 months.</p>"""),
        ("after", "What the Bank expects once you're registered", """          <p>Since September 8, 2025, registered PSPs must have a risk management and incident response framework and, if they hold end-user funds, a safeguarding framework. They must also:</p>
          <ul>
            <li>notify the Bank without delay of incidents with a material impact on end users, other PSPs or certain clearing and settlement systems;</li>
            <li>give the Bank notice at least five business days before a significant change or new activity;</li>
            <li>file an annual report no later than March 31 of the following year.</li>
          </ul>
          <p>Our RPAA compliance program covers these frameworks for a fixed US$3,500.</p>"""),
        ("fintrac", "RPAA and FINTRAC: do you need both?", """          <p>Often, yes. Many payment businesses that register with the Bank of Canada also provide money services, such as remitting or transmitting funds, that require FINTRAC registration as an MSB. The two regimes cover different things: the RPAA deals with operational risk and safeguarding funds, and FINTRAC with money laundering and terrorist financing. We can handle both registrations together.</p>"""),
    ],
    sources=[("Bank of Canada, Retail payments supervision", B_RPS), ("Supervisory framework", B_FW), ("Registration", B_REG), ("Registration application fee", B_FEE)],
    for_title="Who it's for",
    for_items=[("Payment processors and wallets", "Businesses that hold, move or process funds for end users."),
               ("Foreign PSPs serving Canada", "Providers abroad with end users in Canada."),
               ("MSBs that also process payments", "Businesses that need both FINTRAC and Bank of Canada registration.")],
    arts=["register", "many", "address"],
    faqs=[("How much does RPAA registration cost?", "Our fee is a fixed US$3,500. The Bank of Canada also charges a one-time, non-refundable application fee, currently CA$2,500, which you pay to the Bank."),
          ("Is the Bank of Canada fee included in your price?", "No. The application fee is paid directly to the Bank and isn't part of our US$3,500."),
          ("Do foreign payment service providers have to register?", "Yes, if they perform retail payment activities for end users in Canada."),
          ("Do I also need to register with FINTRAC?", "Often. If you also provide money services, such as remitting or transmitting funds, you need FINTRAC registration as an MSB too."),
          ("How long does RPAA registration take?", "In our experience, Bank of Canada registration generally takes about 2 to 8 months, including the national security review."),
          ("What happens after registration?", "You need risk management, incident response and, if you hold end-user funds, safeguarding frameworks, plus annual reports and change notices. Our RPAA compliance program covers these.")],
    related=["rpaa-compliance-program.html", "msb-registration.html", "outsourced-compliance-officer.html"],
)

# ------------------------------------------------------------------ RPAA compliance program
DEEP["rpaa-compliance-program.html"] = dict(
    name="RPAA compliance program",
    title="RPAA Compliance Program for PSPs | AML Canada",
    desc="RPAA frameworks for PSPs: governance, risk registers, incident response, third parties, safeguarding, cyber and continuity, annual reports. Fixed fee US$3,500.",
    service_type="RPAA compliance program and frameworks for payment service providers",
    offers=[("3500", "USD", "RPAA-compliant compliance program for payment service providers, fixed fee")],
    h1="RPAA frameworks written for how your payments actually run.",
    lede="Risk management, incident response and safeguarding frameworks for payment service providers. Fixed fee US$3,500.",
    hero_price="Fixed fee · US$3,500",
    label="RPAA · Framework · 7 of 7",
    need="rpaa",
    intro=("Registration with the Bank of Canada is the start. Since September 8, 2025, payment service providers must also have frameworks for risk management, incident response and safeguarding end-user funds.",
           ["We write an RPAA-compliant compliance program around your actual payment flows, systems, providers and team, so the frameworks describe what you really do and your people can follow them.",
            "The program covers seven areas, from senior officer governance to annual reports and change notices, for a fixed fee of US$3,500."]),
    facts=[("Fee", "US$3,500", "fixed, seven frameworks"),
           ("In force", "Sept 8, 2025", "frameworks required"),
           ("Incidents", "Without delay", "notify the Bank"),
           ("Changes", "5 business days", "notice before")],
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
        ("incident", "Incident response", """          <p>When something goes wrong, your team needs to know what to do. The framework covers how incidents are identified, escalated, contained and recovered from, and how you notify the Bank without delay when an incident has a material impact on end users, other PSPs or certain clearing and settlement systems.</p>"""),
        ("third-parties", "Third parties and agents", """          <p>Many PSPs depend on processors, banks, cloud providers and others, and some act through agents or mandataries. The framework covers how you assess and manage the risks they bring. Foreign PSPs also identify the agents or mandataries acting for them in Canada.</p>"""),
        ("safeguarding", "Safeguarding end-user funds", """          <p>If you hold end-user funds, you must safeguard them, either in a trust account, or in a segregated account protected by insurance or a guarantee. Your written safeguarding framework explains how end users get timely access to their funds and how funds would be paid out if your business became insolvent.</p>"""),
        ("cyber", "Cyber, IT and continuity", """          <p>Protecting the integrity, confidentiality and availability of your systems and data, detecting cyber threats, and keeping payments running, or restoring them quickly, when systems or providers fail.</p>"""),
        ("reporting", "Annual report and change notices", """          <p>PSPs file an annual report with the Bank no later than March 31 of the following year, covering their registration information, operational risk management, incident response and safeguarding. They also give the Bank notice at least five business days before a significant change or new activity. The framework sets out how you track, prepare and approve both.</p>"""),
    ],
    sources=[("Bank of Canada, Supervisory framework", B_FW), ("Retail payments supervision", B_RPS)],
    for_title="Who it's for",
    for_items=[("Newly registered PSPs", "Putting the Bank's frameworks in place for the first time."),
               ("PSPs that hold customer funds", "Safeguarding arrangements that need to be written down and tested."),
               ("Growing payment businesses", "New products, partners or markets that the frameworks didn't cover.")],
    arts=["programme", "scan", "many"],
    faqs=[("What does the RPAA require from payment service providers?", "Risk management and incident response frameworks, safeguarding of end-user funds where you hold them, incident notices to the Bank, notice before significant changes or new activities, and an annual report by March 31."),
          ("How much does an RPAA compliance program cost?", "A fixed US$3,500 for the program documents covering all seven areas."),
          ("Is this the same as our FINTRAC AML program?", "No. The RPAA program covers operational risk and safeguarding under the Bank of Canada. A FINTRAC compliance program covers money laundering and terrorist financing. Many payment businesses need both."),
          ("Do you help us put the frameworks in place?", "Yes. We write them around how you operate and walk your team through them. Ongoing support can be covered by outsourced compliance officer hours.")],
    related=["rpaa-registration.html", "outsourced-compliance-officer.html", "compliance-programs.html"],
)

# ------------------------------------------------------------------ effectiveness reviews (scoped)
DEEP["effectiveness-reviews.html"] = dict(
    name="Effectiveness reviews",
    title="FINTRAC Effectiveness Review (Two-Year) | AML Canada",
    desc="The two-year AML effectiveness review FINTRAC requires: your policies, risk assessment and training tested in practice, with written findings and exam preparation.",
    service_type="Compliance program effectiveness review",
    offers=[],
    h1="Find the gaps before an examiner does.",
    lede="The two-year effectiveness review FINTRAC requires, and preparation for a FINTRAC examination.",
    hero_price="Scoped to your business",
    label="Gap found · Review",
    flag=True,
    need="review",
    intro=("Every business FINTRAC regulates must review the effectiveness of its compliance program at least every two years.",
           ["An effectiveness review tests whether your policies and procedures, risk assessment and training work in practice, and whether what your team does matches what your documents say.",
            "We also help you prepare for a FINTRAC examination: what to expect, what to have ready and what to fix first. The fee depends on the size and complexity of your business, and is agreed in your written scope."]),
    facts=[("How often", "Every 2 years", "at a minimum"),
           ("Covers", "3 parts", "policies, risk assessment, training"),
           ("Tests", "In practice", "not only on paper"),
           ("Fee", "Scoped", "agreed in writing")],
    fee=dict(amount="Scoped", unit="quoted after your consultation",
             note="Depends on your size, products and the number of files to test.",
             items=["A scoped review, agreed in writing",
                    "Testing of what happens against what's written",
                    "Written findings and recommendations, in order of priority",
                    "Help preparing records and your team for an examination"]),
    guide=[
        ("how-often", "How often is an effectiveness review required?", """          <p>At least every two years. FINTRAC requires every reporting entity to review the effectiveness of its compliance program, covering its policies and procedures, risk assessment and training program, at a minimum once every two years. The review tests whether the program works, not only whether the documents exist.</p>"""),
        ("who-reviews", "Who can carry out the review", """          <p>FINTRAC's guidance says the review is carried out by an internal or external auditor or, if the business has no auditor, by the business itself. Whoever does it should know the requirements of the PCMLTFA and its regulations. An external review gives you independence and a fresh view.</p>"""),
        ("tests", "What a review tests", """          <ul>
            <li>whether your policies and procedures reflect current requirements and your current business;</li>
            <li>whether your risk assessment covers your clients, products, channels and geography, and whether your controls follow from it;</li>
            <li>whether training happened, reached the right people and matches your risks;</li>
            <li>samples of client files, monitoring and reports to FINTRAC, to see the program working in practice.</li>
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
    desc="Scenario-based anti-money laundering training for MSB front-line staff, compliance teams and senior management, built to meet FINTRAC's training requirement.",
    service_type="Anti-money laundering (AML) training",
    offers=[],
    h1="Training built around situations your staff will recognize.",
    lede="Anti-money laundering training for front-line staff, compliance teams and senior management.",
    hero_price="Scoped to your team",
    label="Staff · Trained · Recorded",
    need="training",
    intro=("A written, ongoing compliance training program is one of the five required parts of a compliance program.",
           ["Training works when staff recognize the situation in front of them and know what to do next. We build anti-money laundering (AML) and anti-terrorist financing training around real scenarios from your business.",
            "We train front-line staff, compliance teams and senior management, and help you keep the records that show training happened. The fee depends on your team and is agreed in your written scope."]),
    facts=[("Required", "Yes", "part of every program"),
           ("Program", "Written + ongoing", "with a delivery plan"),
           ("Audiences", "3", "front line, compliance, management"),
           ("Records", "Kept", "who, what and when")],
    fee=dict(amount="Scoped", unit="quoted after your consultation",
             note="Depends on the number of people, roles and sessions.",
             items=["Scenario-based training for your business",
                    "Training for each role: front line, compliance and management",
                    "A written training program and plan",
                    "Training records"]),
    guide=[
        ("training-required", "Is AML training required in Canada?", """          <p>Yes. A written, ongoing compliance training program, with a plan for delivering it, is one of the five required elements of a compliance program for businesses regulated by FINTRAC. Training should fit your business and your risks, and reach the people who need it, including employees and agents who deal with clients or transactions.</p>"""),
        ("roles", "Training for each role", """          <ul>
            <li><strong>Front-line staff:</strong> recognizing unusual activity, identifying clients properly and knowing when and how to escalate.</li>
            <li><strong>Compliance teams:</strong> reviews, reporting, the 24-hour rule and deadlines, and documenting decisions.</li>
            <li><strong>Senior management:</strong> their responsibilities for the program and how to oversee it.</li>
          </ul>"""),
        ("records", "Training records", """          <p>Being able to show who was trained, on what and when is part of showing your program works. We help you keep those records, ready for your effectiveness review or a FINTRAC examination.</p>"""),
    ],
    sources=[("FINTRAC, Compliance program requirements", F_G4)],
    for_title="Who it's for",
    for_items=[("Front-line staff", "The people who meet customers and process transactions."),
               ("Compliance teams", "Analysts and compliance officers who need depth."),
               ("Senior management", "Leaders responsible for the program's oversight.")],
    arts=["training", "many", "programme"],
    faqs=[("Is AML training mandatory in Canada?", "Yes. An ongoing compliance training program is a required part of a compliance program for businesses FINTRAC regulates."),
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
ON_INC = "https://www.ontario.ca/page/incorporating-business-corporation"
ON_FEES = "https://www.ontario.ca/page/cost-time-required-to-register-change-search-for-business-name-corporation-not-for-profit"

DEEP["incorporation-canada.html"] = dict(
    name="Company incorporation",
    title="Incorporate a Company in Canada in 24 Hours | AML Canada",
    desc="Incorporate a Canadian company, federally or in Ontario, usually within a few hours to 24 hours. Fixed fee US$1,500, ready for FINTRAC or RPAA registration.",
    service_type="Canadian company incorporation",
    offers=[("1500", "USD", "Canadian company incorporation, fixed fee (government filing fees separate)")],
    timing="A few hours to 24 hours",
    h1="Incorporate your Canadian company, fast.",
    lede="Federal or Ontario incorporation, usually done within a few hours to 24 hours. Fixed fee US$1,500.",
    hero_price="Fixed fee · US$1,500",
    label="Company · Incorporated",
    need="incorporate",
    intro=("A Canadian company is usually the first step before registering with FINTRAC as a money services business or with the Bank of Canada as a payment service provider.",
           ["We incorporate your company federally or in a province such as Ontario, choosing with you what fits your plans, and set it up so it's ready for the registrations that come next.",
            "Once we have your details, incorporation usually takes a few hours to 24 hours. Our fee is a fixed US$1,500; government filing fees are separate and paid to the government."]),
    facts=[("Our fee", "US$1,500", "fixed"),
           ("Typical timing", "Hours to 24h", "once we have your details"),
           ("Federal filing fee", "CA$200", "online, paid to Corporations Canada"),
           ("Ontario filing fee", "CA$300", "online, paid to Ontario")],
    fee=dict(amount="US$1,500", unit="fixed fee · plus government filing fees",
             note="Government filing fees are separate: currently CA$200 federally online (CA$100 more for 4-hour express service) or CA$300 online in Ontario. A name search report may also apply if you choose a named rather than a numbered company.",
             items=["Advice on federal or provincial incorporation",
                    "Company name or numbered company",
                    "Articles of incorporation filed",
                    "Registered office address and first directors",
                    "Set up ready for FINTRAC or RPAA registration",
                    "Usually complete within a few hours to 24 hours"]),
    guide=[
        ("federal-or-provincial", "Federal or provincial?", """          <p>You can incorporate federally, under the Canada Business Corporations Act (CBCA) through Corporations Canada, or in a province or territory, such as Ontario under its Business Corporations Act. A federal company can use its name across Canada, though it still registers in the provinces where it does business. A provincial company is often simpler if you'll operate mainly in one province. We help you choose before anything is filed.</p>"""),
        ("directors", "Directors and residency", """          <p>Federal corporations must have at least 25% resident Canadian directors; if the company has fewer than four directors, at least one must be a resident Canadian. A resident Canadian includes a Canadian citizen ordinarily resident in Canada and a permanent resident. Ontario doesn't require resident Canadian directors, which can matter for founders based outside Canada. Some regulated sectors have stricter rules.</p>"""),
        ("timing", "How long it takes", """          <p>Once we have your details and documents, incorporation usually takes a few hours to 24 hours. Corporations Canada processes online incorporations in about a day, with a 4-hour express option for an extra government fee, and Ontario incorporates immediately online.</p>"""),
        ("fees", "What it costs", """          <p>Our fee is a fixed US$1,500. Government fees are paid separately to the government: currently CA$200 for federal online incorporation (CA$100 more for 4-hour express) or CA$300 for Ontario online incorporation. If you choose a named company rather than a numbered one, a name search report is usually needed too.</p>"""),
        ("after", "After incorporation", """          <ul>
            <li>Keep corporate records, including a register of individuals with significant control.</li>
            <li>File an annual return each year (federal online annual return: CA$12).</li>
            <li>Register for tax accounts, and in each province where you carry on business.</li>
            <li>Register with <a href="msb-registration.html">FINTRAC as an MSB</a> or with the <a href="rpaa-registration.html">Bank of Canada under the RPAA</a> before you start offering those services.</li>
          </ul>"""),
    ],
    sources=[("Corporations Canada, Services, fees and processing times", CC_FEES), ("Directors and officers", CC_DIR),
             ("Next steps after incorporating", CC_NEXT), ("Ontario, Incorporating a business corporation", ON_INC), ("Ontario fees and timing", ON_FEES)],
    for_title="Who it's for",
    for_items=[("Foreign businesses entering Canada", "A Canadian company to hold your registration and contracts."),
               ("New MSBs and payment companies", "The company that will register with FINTRAC or the Bank of Canada."),
               ("Founders on a deadline", "Incorporated within a day, so the next steps can start.")],
    arts=["one", "address", "register"],
    faqs=[("How much does it cost to incorporate a company in Canada?", "Our fee is a fixed US$1,500. Government filing fees are separate: currently CA$200 federally online or CA$300 in Ontario online."),
          ("How long does incorporation take?", "Usually a few hours to 24 hours once we have your details and documents."),
          ("Can a non-resident incorporate in Canada?", "Yes. Federal companies need at least 25% resident Canadian directors (at least one if there are fewer than four). Ontario doesn't require resident Canadian directors."),
          ("Should we incorporate before registering as an MSB?", "Usually, yes. The company is what registers with FINTRAC, so incorporating first means the registration can start straight away.")],
    related=["msb-registration.html", "canadian-address.html", "rpaa-registration.html"],
)
