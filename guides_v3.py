"""Guides (articles) for site-v3, rendered by build_v3.guide_page.

Each guide answers one question people search for and points to one service.
Regulatory statements were checked on 11 October 2026 against the sources listed
with each guide. Re-check before updating, and change "updated" when you do.
"""
from content_v3 import (B_FEE, B_FW, B_REG, B_RPS, F_24, F_EFT, F_G4, F_LCTR, F_LVCTR, F_MSB, F_REG, F_REC_MSB,
                        F_STR, F_TRAVEL, F_UPD, MSB_ACTIVITIES, REPORTS_TABLE, RQ_MSB)

PUBLISHED = "2026-10-11"
GUIDES = {}

# ------------------------------------------------------------------ 1. how to register an MSB
GUIDES["how-to-register-msb-canada.html"] = dict(
    title="How to Register an MSB in Canada: FINTRAC Guide | AML Canada",
    desc="How to register a money services business (MSB) with FINTRAC, step by step: who must register, what FINTRAC asks for, criminal record checks, renewal and what comes after.",
    crumb="How to register an MSB",
    h1="How to register an MSB in Canada",
    lede="A step-by-step guide to registering a money services business with FINTRAC, from checking whether you need to, to staying registered.",
    label="Guide · MSB registration",
    service="msb-registration.html",
    takeaways=["Register with FINTRAC before you start operating. FINTRAC doesn't charge a fee.",
               "Criminal record checks are needed for the CEO, president, directors and 20%+ owners.",
               "Registration lasts two years. Report changes within 30 days.",
               "You also need a compliance program, reporting and record keeping from day one."],
    sections=[
        ("need-to-register", "Step 1: Check whether you need to register", f"""          <p>In Canada, a money services business (MSB) is a business that provides certain money services. If you have a place of business in Canada and you provide any of these, you must register with FINTRAC, the Financial Transactions and Reports Analysis Centre of Canada, before you start:</p>
          {MSB_ACTIVITIES}
          <p>If you have no place of business in Canada but you direct and provide these services to people or entities in Canada, you're a foreign MSB, and you must register too. Our <a href="foreign-msb-registration-canada.html">foreign MSB guide</a> covers that case.</p>
          <p>Registering or being licensed with a province doesn't replace FINTRAC registration. Quebec, for example, has its own licence for money-services businesses, issued by Revenu Québec, which sits on top of FINTRAC registration.</p>"""),
        ("licence", "Is there an \"MSB licence\" in Canada?", """          <p>People often search for an "MSB licence". At the federal level, what Canada requires is <strong>registration with FINTRAC</strong> under the Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA). Quebec is the main exception: it licenses money-services businesses separately. Elsewhere, when someone says "MSB licence Canada", they almost always mean FINTRAC registration.</p>"""),
        ("gather", "Step 2: Gather what FINTRAC asks for", """          <p>FINTRAC's registration asks for:</p>
          <ul>
            <li>details of the business, including incorporation, ownership and senior management;</li>
            <li>bank account information;</li>
            <li>your compliance officer;</li>
            <li>how many employees you have, and every location you operate from;</li>
            <li>estimated annual transaction totals for each money service you offer;</li>
            <li>any agents or mandataries that provide services on your behalf;</li>
            <li>for a foreign MSB, a representative for service who lives in Canada;</li>
            <li>documents confirming the business exists and how it's owned and controlled;</li>
            <li>criminal record checks.</li>
          </ul>"""),
        ("criminal-record-checks", "Step 3: Order criminal record checks early", """          <p>FINTRAC needs criminal record checks for the chief executive officer, the president, the directors, and anyone who owns or controls 20% or more of the business, directly or indirectly. A sole proprietor provides one for themselves.</p>
          <p>Each check must come from a competent authority in the person's country of residence, be dated no more than six months before you submit it, and be translated if it isn't in English or French. When owners and directors live in different countries, this is often the step that takes longest, so start it first.</p>"""),
        ("submit", "Step 4: Submit and answer FINTRAC's questions", """          <p>Once everything is gathered and checked, you submit your registration to FINTRAC. FINTRAC may come back with questions or ask for more information before it decides. Complete, consistent information is the best way to avoid back-and-forth: the transaction estimates, locations, ownership and documents should all tell the same story.</p>"""),
        ("program", "Step 5: Have your compliance program ready", """          <p>Registration lets you operate; it doesn't make you compliant. From the day you start, you need a compliance program with five parts: a compliance officer, written policies and procedures, a risk assessment, an ongoing training program, and an effectiveness review at least every two years. You also need to identify clients, keep records, generally for at least five years, and report to FINTRAC.</p>
          <p>Building the program alongside the registration, rather than after it, means you're ready to operate as soon as you're registered.</p>"""),
        ("stay-registered", "Step 6: Stay registered", """          <p>MSB registration is valid for two years and must be renewed before it expires. Between renewals, tell FINTRAC within 30 days when your registration information changes: a new address, new owners or directors, a new compliance officer, or a change in the services you offer.</p>"""),
    ],
    faqs=[("Does FINTRAC charge to register an MSB?", "No. FINTRAC doesn't charge a registration fee. Your costs are your own time, criminal record checks, any translations, and professional help if you use it."),
          ("Can I register an MSB without a Canadian office?", "Yes, as a foreign MSB, if you direct and provide money services to people in Canada. You'll need a representative for service who lives in Canada."),
          ("Do I need a compliance program before registering?", "You need it in place to operate, and FINTRAC asks for your compliance officer when you register. It makes sense to build both together."),
          ("How long is MSB registration valid?", "Two years. Changes to your registration information must be reported within 30 days.")],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("Money services businesses", F_MSB), ("Update, renew or cancel your registration", F_UPD),
             ("Compliance program requirements", F_G4), ("Revenu Québec, Money-services business licence", RQ_MSB)],
    related=["msb-registration-cost-canada.html", "foreign-msb-registration-canada.html", "fintrac-reporting-requirements.html"],
)

# ------------------------------------------------------------------ 2. cost
GUIDES["msb-registration-cost-canada.html"] = dict(
    title="How Much Does MSB Registration Cost in Canada? | AML Canada",
    desc="What it costs to register a money services business in Canada: FINTRAC's fee (none), the real costs behind registration, and what professional help costs.",
    crumb="MSB registration cost",
    h1="How much does MSB registration cost in Canada?",
    lede="FINTRAC charges nothing to register. The real costs are elsewhere. Here's what to budget for, and what our fixed fees cover.",
    label="Guide · Costs",
    service="pricing.html",
    takeaways=["FINTRAC registration itself is free.",
               "Budget for criminal record checks, translations and documents.",
               "A compliance program is needed to operate, not just to register.",
               "Our fixed fees: US$3,500 registration; US$3,500 program documents."],
    sections=[
        ("fintrac-fee", "FINTRAC's fee: none", """          <p>FINTRAC doesn't charge a fee to register a money services business, or to renew. If anyone tells you there's a government fee for FINTRAC MSB registration, ask what it's for.</p>"""),
        ("real-costs", "The real costs of registering", """          <ul>
            <li><strong>Criminal record checks</strong> for the CEO, president, directors and anyone owning or controlling 20% or more. Costs vary by country, and checks must be dated within six months of submission.</li>
            <li><strong>Translations</strong> of any checks or documents that aren't in English or French.</li>
            <li><strong>Corporate documents</strong> showing the business exists and how it's owned and controlled.</li>
            <li><strong>Time</strong>: gathering, checking and answering FINTRAC's questions.</li>
            <li><strong>Provincial licensing</strong> where it applies. Quebec licenses money-services businesses separately through Revenu Québec, with its own fees.</li>
          </ul>"""),
        ("operating-costs", "What it costs to operate once registered", """          <p>Registration is the entry ticket. To operate, an MSB needs a compliance program (compliance officer, policies and procedures, risk assessment, training and a two-year effectiveness review), and it has to report to FINTRAC and keep records. Those are ongoing costs, whether you staff them in-house or outsource them.</p>"""),
        ("our-fees", "What professional help costs with us", """          <div class="table-wrap"><table>
            <thead><tr><th scope="col">Service</th><th scope="col">Fee</th></tr></thead>
            <tbody>
              <tr><th scope="row"><a href="msb-registration.html">FINTRAC MSB registration</a></th><td>US$3,500, fixed</td></tr>
              <tr><th scope="row"><a href="compliance-programs.html">PCMLTFA compliance program (14 documents)</a></th><td>US$3,500, fixed</td></tr>
              <tr><th scope="row"><a href="outsourced-compliance-officer.html">Outsourced compliance officer</a></th><td>US$1,500 per 10 hours</td></tr>
              <tr><th scope="row"><a href="canadian-address.html">Canadian business address</a></th><td>US$200 per month</td></tr>
              <tr><th scope="row"><a href="msb-for-sale.html">Registered MSB to acquire</a></th><td>From €28,000</td></tr>
            </tbody>
          </table></div>
          <p>All fees are on our <a href="pricing.html">pricing page</a>. Every engagement starts with a consultation and a written scope, so you know the fee before any work begins.</p>"""),
        ("buy-or-register", "Registering vs buying a registered MSB", """          <p>Some businesses buy a company that's already registered instead of registering a new one. It costs more up front, and it still needs due diligence, updates to FINTRAC within 30 days of changes like new owners and directors, and a compliance program that fits the new owners. See <a href="msb-for-sale.html">MSB for sale</a>.</p>"""),
    ],
    faqs=[("Is FINTRAC MSB registration free?", "Yes. FINTRAC doesn't charge to register or renew."),
          ("How much does it cost to set up an MSB in Canada?", "Registration is free, but budget for criminal record checks, translations, documents and a compliance program. Our fixed fees are US$3,500 for registration and US$3,500 for compliance program documents."),
          ("Does Quebec charge for an MSB licence?", "Yes. Quebec licenses money-services businesses separately through Revenu Québec, which sets its own fees.")],
    sources=[("FINTRAC, Register your MSB or FMSB", F_REG), ("Update, renew or cancel your registration", F_UPD), ("Compliance program requirements", F_G4),
             ("Revenu Québec, Money-services business licence", RQ_MSB)],
    related=["how-to-register-msb-canada.html", "foreign-msb-registration-canada.html", "rpaa-registration-guide.html"],
)

# ------------------------------------------------------------------ 3. foreign MSB
GUIDES["foreign-msb-registration-canada.html"] = dict(
    title="Foreign MSB Registration in Canada (FMSB) | AML Canada",
    desc="When a business outside Canada must register with FINTRAC as a foreign money services business, what 'directing and providing' means, and what FMSBs need in Canada.",
    crumb="Foreign MSB registration",
    h1="Foreign MSB registration in Canada",
    lede="No office in Canada doesn't mean no obligations. When a foreign business must register with FINTRAC, and what it needs once it does.",
    label="Guide · Foreign MSB",
    service="msb-registration.html",
    takeaways=["Foreign MSBs that direct and provide services to Canada must register first.",
               "Marketing to Canadians, a .ca domain or Canadian listings can count.",
               "You need a representative for service who lives in Canada.",
               "The foreign business stays responsible for its obligations."],
    sections=[
        ("what-is", "What is a foreign MSB?", f"""          <p>A foreign money services business (FMSB) has no place of business in Canada but directs and provides money services to people or entities in Canada. The money services are the same ones that apply to Canadian MSBs:</p>
          {MSB_ACTIVITIES}
          <p>A foreign MSB must register with FINTRAC before it starts providing these services to Canada.</p>"""),
        ("directing", "What counts as directing services at Canada", """          <p>FINTRAC looks at whether your business targets people in Canada. Examples it gives include marketing aimed at people in Canada, operating a .ca domain name, and being listed in a Canadian business directory. If your website, ads or partnerships are built to attract Canadian customers, assume you're in scope and get it confirmed.</p>"""),
        ("representative", "Your representative for service in Canada", """          <p>A foreign MSB must name a representative for service who lives in Canada and can accept notices on its behalf. The representative doesn't take over your obligations: the foreign business itself stays responsible for complying with Canada's anti-money laundering law.</p>
          <p>A representative for service is a person, and it's a separate requirement from having a Canadian business address. Many foreign MSBs want both. We offer a <a href="canadian-address.html">FINTRAC-compliant Canadian address</a>; ask us about the representative requirement in your consultation.</p>"""),
        ("obligations", "Obligations once registered", """          <p>Foreign MSBs carry substantially the same obligations as Canadian ones: a compliance program, client identification, record keeping, reporting to FINTRAC, the travel rule for funds and virtual currency transfers, and renewing their registration every two years, with changes reported within 30 days.</p>
          <p>Many foreign MSBs don't have an experienced compliance person in Canada. An <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> who works with FINTRAC's requirements every day can fill that gap.</p>"""),
        ("checks", "Criminal record checks from abroad", """          <p>FINTRAC needs criminal record checks for the CEO, president, directors and anyone owning or controlling 20% or more, issued in each person's country of residence, dated within six months, and translated if needed. For international ownership, this is usually the longest step.</p>"""),
    ],
    faqs=[("Do foreign companies need to register with FINTRAC?", "Yes, if they direct and provide money services to people or entities in Canada. They register as foreign MSBs before they start."),
          ("Does a foreign MSB need a Canadian address?", "FINTRAC requires a representative for service who lives in Canada. A Canadian business address is a separate thing that many foreign MSBs also want for banking, partners and customers."),
          ("Can a foreign MSB outsource its compliance officer?", "Many do. The foreign business stays responsible for its obligations, but an experienced compliance officer in Canada can carry the day-to-day work.")],
    sources=[("FINTRAC, Money services businesses", F_MSB), ("Register your MSB or FMSB", F_REG), ("Travel rule", F_TRAVEL), ("Update, renew or cancel your registration", F_UPD)],
    related=["how-to-register-msb-canada.html", "crypto-registration-canada.html", "msb-registration-cost-canada.html"],
)

# ------------------------------------------------------------------ 4. reporting
GUIDES["fintrac-reporting-requirements.html"] = dict(
    title="FINTRAC Reporting for MSBs: STR, LCTR, EFTR, LVCTR | AML Canada",
    desc="Which reports a money services business must file with FINTRAC, when each applies, the $10,000 threshold, the 24-hour rule and the deadline for each report.",
    crumb="FINTRAC reporting",
    h1="FINTRAC reporting for MSBs: which report, and when",
    lede="Suspicious transactions, large cash, international transfers and virtual currency: what each FINTRAC report covers and how long you have.",
    label="Guide · Reporting",
    service="outsourced-compliance-officer.html",
    takeaways=["STRs have no minimum amount and are due as soon as practicable.",
               "LCTR, EFTR and LVCTR apply at $10,000 or more.",
               "The 24-hour rule adds up smaller transactions.",
               "Deadlines run from 5 working days to 15 calendar days."],
    sections=[
        ("overview", "The reports at a glance", f"""          {REPORTS_TABLE}
          <p>Amounts are in Canadian dollars, or the equivalent in another currency or in virtual currency.</p>"""),
        ("str", "Suspicious transaction reports (STR)", """          <p>You must report a transaction, or an attempted one, when you have reasonable grounds to suspect it's related to money laundering or terrorist financing. There's no minimum amount. FINTRAC expects the report "as soon as practicable": somewhere between immediately and as soon as possible, with completing the STR taking priority over other tasks.</p>
          <p>Good STRs explain why: what you saw, the indicators, and how the facts fit together. A transaction can need both an STR and another report, for example a suspicious large cash deposit.</p>"""),
        ("lctr", "Large cash transaction reports (LCTR)", """          <p>When you receive $10,000 or more in cash, in one transaction or several within 24 hours, you report it within 15 calendar days.</p>"""),
        ("eftr", "Electronic funds transfer reports (EFTR)", """          <p>International electronic funds transfers of $10,000 or more, sent or finally received, in one transfer or several within 24 hours, are reported within 5 working days.</p>"""),
        ("lvctr", "Large virtual currency transaction reports (LVCTR)", """          <p>When you receive virtual currency worth $10,000 or more, in one transaction or several within 24 hours, you report it within 5 working days after the day you receive it. A working day is Monday to Friday, excluding public holidays.</p>"""),
        ("24-hour-rule", "The 24-hour rule", """          <p>The 24-hour rule stops threshold reporting being avoided by splitting transactions. When several transactions of the same type, each below $10,000, total $10,000 or more within 24 hours and are conducted by or on behalf of the same person or entity, or for the same beneficiary, they're treated as one and reported. Your systems need to add them up.</p>"""),
        ("terrorist-property", "Terrorist property and listed person reports", """          <p>If you know or believe property in your possession or control is owned or controlled by a terrorist, a terrorist group or a listed person, you must report it to FINTRAC immediately, and you can't deal with that property.</p>"""),
        ("travel-rule", "The travel rule", """          <p>When MSBs send electronic funds or virtual currency transfers, the information about who requested the transfer and the beneficiary must travel with it: names, addresses and account or reference numbers. Received travel-rule information can't be stripped out. It's not a separate report, but it supports your record keeping and reporting.</p>"""),
        ("getting-it-right", "Getting reporting right", """          <ul>
            <li>Know which reports apply to your services, and test that your systems flag them.</li>
            <li>Track deadlines from the right day, in working days or calendar days as the report requires.</li>
            <li>Document why you did or didn't file an STR.</li>
            <li>Keep the records behind every report, generally for at least five years.</li>
          </ul>
          <p>Reporting is one of the main things an <a href="outsourced-compliance-officer.html">outsourced compliance officer</a> takes off your plate.</p>"""),
    ],
    faqs=[("What is the FINTRAC reporting threshold?", "$10,000 for large cash, international electronic funds transfer and large virtual currency transaction reports, including smaller transactions that add up to $10,000 within 24 hours. Suspicious transaction reports have no threshold."),
          ("How long do I have to file an EFTR?", "5 working days."),
          ("How long do I have to file an LCTR?", "15 calendar days after the day you receive the cash."),
          ("When is an STR due?", "As soon as practicable, which FINTRAC describes as between immediately and as soon as possible.")],
    sources=[("FINTRAC, Reporting suspicious transactions", F_STR), ("Reporting large cash transactions", F_LCTR), ("Reporting electronic funds transfers", F_EFT),
             ("Reporting large virtual currency transactions", F_LVCTR), ("The 24-hour rule", F_24), ("Travel rule", F_TRAVEL), ("Record keeping for MSBs", F_REC_MSB)],
    related=["crypto-registration-canada.html", "how-to-register-msb-canada.html", "foreign-msb-registration-canada.html"],
)

# ------------------------------------------------------------------ 5. RPAA
GUIDES["rpaa-registration-guide.html"] = dict(
    title="What Is the RPAA? PSP Registration Guide | AML Canada",
    desc="The Retail Payment Activities Act explained: which payment service providers must register with the Bank of Canada, the fee, the review, and the frameworks required after.",
    crumb="RPAA explained",
    h1="What is the RPAA, and do you need to register?",
    lede="The Retail Payment Activities Act brought payment service providers under Bank of Canada supervision. Who's covered, what registration involves and what comes after.",
    label="Guide · RPAA",
    service="rpaa-registration.html",
    takeaways=["PSPs performing payment functions for end users in Canada register with the Bank.",
               "The Bank charges a one-time application fee, currently CA$2,500.",
               "Applications get a national security review by the Department of Finance.",
               "Frameworks for risk, incidents and safeguarding have applied since Sept 8, 2025."],
    sections=[
        ("what-is", "What the RPAA is", """          <p>The Retail Payment Activities Act (RPAA) is the federal law that brought payment service providers (PSPs), such as payment processors, digital wallets and money transfer apps, under supervision by the Bank of Canada. It focuses on operational risk, incident response and safeguarding the funds PSPs hold for their users.</p>"""),
        ("who", "Who has to register", """          <p>A PSP is covered when it performs one or more payment functions for end users, as a service or business activity:</p>
          <ul>
            <li>providing or maintaining an account held for end users;</li>
            <li>holding funds on behalf of end users;</li>
            <li>initiating an electronic funds transfer at an end user's request;</li>
            <li>authorizing an electronic funds transfer, or transmitting, receiving or facilitating an instruction for one;</li>
            <li>providing clearing or settlement services.</li>
          </ul>
          <p>That covers PSPs with a place of business in Canada, and PSPs outside Canada that perform retail payment activities for end users in Canada. Some institutions, such as banks, are excluded, and some activities fall outside the Act.</p>"""),
        ("fee", "What registration costs", """          <p>The Bank of Canada charges every applicant a one-time, non-refundable application fee. It was set at CA$2,500 from November 1, 2024 and is adjusted every calendar year in line with inflation. Registered PSPs also pay the Bank annual assessment fees to cover the cost of supervision. Our fee to prepare and support your registration is a fixed US$3,500.</p>"""),
        ("review", "How the Bank reviews applications", """          <p>The Bank shares applications with the Department of Finance for national security screening, and with FINTRAC. The Bank must refuse or revoke a registration if the Minister of Finance directs it to for national security reasons. Registration decisions are published as screenings are completed.</p>"""),
        ("after", "What's required after registration", """          <p>Since September 8, 2025, PSPs must have:</p>
          <ul>
            <li>a risk management and incident response framework, covering identification, protection, detection, response and recovery, with defined roles, adequate resources, periodic testing, and the risks from third parties, agents and mandataries;</li>
            <li>if they hold end-user funds, safeguarding: a trust account, or a segregated account with insurance or a guarantee, plus a written framework for users' access to funds and for insolvency.</li>
          </ul>
          <p>PSPs must also notify the Bank without delay of incidents with a material impact, give notice at least five business days before a significant change or new activity, and file an annual report no later than March 31 of the following year. Our <a href="rpaa-compliance-program.html">RPAA compliance program</a> covers these.</p>"""),
        ("fintrac", "RPAA and FINTRAC", """          <p>The two regimes sit side by side. The RPAA covers operational risk and safeguarding under the Bank of Canada; FINTRAC covers money laundering and terrorist financing. A payment business that also remits or transmits funds usually needs to <a href="msb-registration.html">register with FINTRAC as an MSB</a> too.</p>"""),
    ],
    faqs=[("What does RPAA stand for?", "The Retail Payment Activities Act, the law under which the Bank of Canada supervises payment service providers."),
          ("How much is the Bank of Canada's RPAA fee?", "A one-time, non-refundable application fee, set at CA$2,500 from November 1, 2024 and adjusted each year for inflation. Annual assessment fees apply once registered."),
          ("Do foreign PSPs have to register under the RPAA?", "Yes, if they perform retail payment activities for end users in Canada."),
          ("When is the RPAA annual report due?", "No later than March 31 of the year after the reporting year.")],
    sources=[("Bank of Canada, Retail payments supervision", B_RPS), ("Supervisory framework", B_FW), ("Registration", B_REG), ("Registration application fee", B_FEE)],
    related=["how-to-register-msb-canada.html", "fintrac-reporting-requirements.html", "msb-registration-cost-canada.html"],
)

# ------------------------------------------------------------------ 6. crypto
GUIDES["crypto-registration-canada.html"] = dict(
    title="Crypto Business Registration in Canada (FINTRAC) | AML Canada",
    desc="How crypto exchanges and virtual currency dealers register with FINTRAC as MSBs, and what follows: LVCTRs, the travel rule, record keeping and provincial rules.",
    crumb="Crypto registration",
    h1="Registering a crypto business with FINTRAC",
    lede="Virtual currency dealers register as money services businesses. What that means for crypto exchanges and dealers, at home and abroad.",
    label="Guide · Virtual currency",
    service="msb-registration.html",
    takeaways=["Dealing in virtual currency is a money service: register with FINTRAC first.",
               "Foreign crypto businesses serving Canada register as foreign MSBs.",
               "Report virtual currency receipts of $10,000+ within 5 working days.",
               "The travel rule applies to virtual currency transfers."],
    sections=[
        ("register", "Crypto businesses register as MSBs", """          <p>Dealing in virtual currency is one of the money services FINTRAC lists, so crypto exchanges and virtual currency dealers register with FINTRAC as money services businesses before they start. A crypto business outside Canada that directs and provides these services to people in Canada registers as a foreign MSB. The <a href="how-to-register-msb-canada.html">registration steps</a> are the same as for any MSB.</p>"""),
        ("lvctr", "Large virtual currency transaction reports", """          <p>When you receive virtual currency worth $10,000 or more, in one transaction or several within 24 hours, you file a large virtual currency transaction report (LVCTR) within 5 working days after the day you receive it. Suspicious transaction reports apply too, with no minimum amount. See our <a href="fintrac-reporting-requirements.html">FINTRAC reporting guide</a>.</p>"""),
        ("travel-rule", "The travel rule for virtual currency", """          <p>When you send a virtual currency transfer, you must include the requester's name, address and account or reference number, and the beneficiary's name, address and account or reference number. When you receive transfers, you must take reasonable measures to make sure that information is included. You can't strip received travel-rule information out of a transfer.</p>"""),
        ("records", "Record keeping", """          <p>For virtual currency transfers of $1,000 or more, MSBs keep detailed records, including the date, the type and amount of virtual currency, client and beneficiary details, transaction hashes, sending and receiving addresses, and the exchange rates used. Records are generally kept for at least five years.</p>"""),
        ("provincial", "Provincial rules", """          <p>FINTRAC registration is federal. Crypto trading platforms can also fall under provincial securities rules, and Quebec licenses money-services businesses, including some crypto activities, through Revenu Québec. We'll tell you when you need separate advice on those.</p>"""),
        ("program", "Your compliance program", """          <p>A crypto MSB needs the same five-part compliance program as any MSB, written for crypto risks: wallet screening, blockchain analytics, travel rule handling and virtual currency reporting. Our <a href="compliance-programs.html">14-document program</a> includes a Travel Rule Policy and Procedure.</p>"""),
    ],
    faqs=[("Do crypto exchanges need to register in Canada?", "Yes. Dealing in virtual currency is a money service, so crypto exchanges and dealers register with FINTRAC as MSBs."),
          ("What is an LVCTR?", "A large virtual currency transaction report, filed when you receive virtual currency worth $10,000 or more, within 5 working days."),
          ("Does the travel rule apply to crypto in Canada?", "Yes. MSBs must include requester and beneficiary information when they send virtual currency transfers, and take reasonable measures to check it's included when they receive them.")],
    sources=[("FINTRAC, Money services businesses", F_MSB), ("Reporting large virtual currency transactions", F_LVCTR), ("Travel rule", F_TRAVEL),
             ("Record keeping for MSBs", F_REC_MSB), ("Revenu Québec, Money-services business licence", RQ_MSB)],
    related=["fintrac-reporting-requirements.html", "foreign-msb-registration-canada.html", "how-to-register-msb-canada.html"],
)
