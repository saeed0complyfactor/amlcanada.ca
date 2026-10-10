"""Privacy Policy and Terms of Service for AML Canada.

Adapted from ComplyFactor's policies (v1.0, 1 January 2026) for AML Canada, a
brand of ComplyFactor Limited. Website-only scope: no live chat, newsletter or
software platforms. Have a lawyer review before relying on them.
"""

EFFECTIVE = "11 October 2026"
VERSION = "1.0"

ENTITY = ("ComplyFactor Limited, an Ontario corporation (Ontario Corporation No. 1001501600), operating as AML Canada. "
          "Registered office: 1025 King Street East, Suite 107 #1596, Cambridge, Ontario N3H 3P5. "
          "Principal office: 320 Matheson Boulevard West, Suite 211, Mississauga, Ontario L5R 3R1, Canada.")

PRIVACY_EMAIL = "privacy@amlcanada.ca"
LEGAL_EMAIL = "legal@amlcanada.ca"
INFO_EMAIL = "info@amlcanada.ca"

PRIVACY = {
    "title": "Privacy Policy",
    "intro": [
        f"This Privacy Policy explains how AML Canada collects, uses, discloses and protects personal information through amlcanada.ca (the “Website”), our consultation requests, and our enquiry and scoping process. It is written to meet Canada’s Personal Information Protection and Electronic Documents Act (PIPEDA), Quebec’s Law 25, and Canada’s Anti-Spam Legislation (CASL).",
    ],
    "sections": [
        ("1. Who is responsible", [
            ("p", f"1.1 The organization accountable for your personal information is {ENTITY}"),
            ("p", f"1.2 Our Privacy Officer is responsible for this policy and for our compliance with privacy law. Contact: Privacy Officer, <a href=\"mailto:{PRIVACY_EMAIL}\">{PRIVACY_EMAIL}</a>."),
        ]),
        ("2. What we collect and why", [
            ("table", ["Source", "Personal information", "Why we use it"], [
                ["Consultation and contact form", "Name, work email, company, the service you need, and your message", "To respond to your request, arrange a consultation and follow up"],
                ["Scoping information you share", "Business model, registrations, ownership and director details, transaction volumes, compliance documents, regulator correspondence", "To assess, scope and price an engagement, and to run conflict checks"],
                ["Phone calls and emails", "Your contact details and what you tell us", "To answer your questions and keep a record of our conversations"],
                ["Visitor analytics (Cloudflare Web Analytics)", "Pages viewed, referral source, approximate country, browser and device type. No cookies and no personal identifiers", "To understand how the Website is used and improve it"],
                ["Analytics cookies (Google Analytics), only with your consent", "Cookie and device identifiers, IP address, pages viewed, referral source, approximate location", "To measure Website performance and which services interest visitors"],
                ["Clients and contracting", "Signatory and contact details, billing details, and know-your-client information about the client and its owners and directors", "To deliver services, invoice, and verify who we work with"],
            ]),
            ("p", "2.1 Information about other people. If you give us information about another person (for example a director or beneficial owner), you must make sure you are entitled to share it and that they know about this policy."),
            ("p", "2.2 Information we don’t want. Please do not send us sensitive personal information (such as health information) or suspicious transaction report content through the Website or our enquiry forms."),
            ("p", "2.3 Public sources. We may obtain information from public registers (such as FINTRAC’s MSB registry and corporate registries), professional networking sites and adverse-media sources. We use it to verify prospective clients and to meet our own due diligence obligations."),
            ("p", "2.4 Automated decisions. We do not make decisions that produce legal or similarly significant effects about you based solely on automated processing."),
        ]),
        ("3. Who we share it with", [
            ("p", "3.1 We do not sell personal information, and we do not share it for third parties’ own marketing."),
            ("p", "3.2 We share personal information only with:"),
            ("ul", [
                "Our team and affiliates: ComplyFactor Limited, its affiliates, and our employees and contractors, on a need-to-know basis and under confidentiality obligations.",
                "Service providers acting for us: website hosting (GitHub Pages), form delivery (Web3Forms), analytics (Cloudflare and, with your consent, Google), and email and productivity tools. Each is bound to use the information only to provide its service to us.",
                "Professional advisers: lawyers, accountants, auditors and insurers, under duties of confidentiality.",
                "Authorities: regulators, law enforcement, courts and government bodies, where the law requires or permits it.",
                "Corporate transactions: a buyer, investor or successor in a merger, sale or reorganization, under confidentiality and only as needed.",
                "Others with your consent or at your direction.",
            ]),
        ]),
        ("4. Where your information is processed", [
            ("p", "4.1 We operate from Canada. Our service providers store and process information mainly in Canada, the United States and the European Union, so your information may be processed outside your province or country and may be accessible to courts and authorities there under local law."),
            ("p", f"4.2 Before transferring information outside Quebec, we assess whether it will be adequately protected, as Law 25 requires. You can ask for more detail by contacting our Privacy Officer."),
        ]),
        ("5. How long we keep it", [
            ("table", ["Information", "Retention"], [
                ["Enquiries and scoping information that don’t lead to an engagement", "2 years after last contact"],
                ["Analytics data", "14 months"],
                ["Client, contracting, billing and know-your-client records", "7 years after the engagement ends"],
            ]),
            ("p", "5.1 We may keep information longer where needed to meet a legal obligation or to establish or defend a legal claim. At the end of the retention period, we securely delete or anonymize it."),
        ]),
        ("6. Security", [
            ("p", "6.1 We protect personal information with safeguards suited to its sensitivity, including encryption in transit, access controls with multi-factor authentication, least-privilege access, confidentiality agreements and staff training. No system is completely secure, and you share information at your own risk."),
            ("p", "6.2 If a breach of security safeguards creates a real risk of significant harm (Canada) or a risk of serious injury (Quebec), we will notify you and the relevant authority as the law requires."),
        ]),
        ("<span id=\"cookies\"></span>7. Cookies and similar technologies", [
            ("p", "7.1 The Website does not need cookies to work. Our visitor analytics (Cloudflare Web Analytics) does not use cookies. We use Google Analytics cookies only if you accept them in our cookie banner. You can change your choice at any time with the “Cookie settings” link in the footer, or by blocking cookies in your browser."),
        ]),
        ("8. Your rights", [
            ("p", "8.1 Depending on where you live, you may have the right to:"),
            ("ul", [
                "access the personal information we hold about you and get a copy;",
                "correct inaccurate or incomplete information;",
                "withdraw consent at any time, without affecting earlier processing;",
                "ask us to delete it, or (in Quebec) to de-index it or stop disseminating it;",
                "object to processing for direct marketing;",
                "be informed about automated decisions and have a person review them.",
            ]),
            ("p", f"8.2 To make a request, email <a href=\"mailto:{PRIVACY_EMAIL}\">{PRIVACY_EMAIL}</a>. We may need to verify your identity. We respond within 30 days and tell you if we need longer, as the law allows. We may decline a request where the law permits, for example where disclosure would reveal another person’s information, confidential commercial information, or information relating to a legal or regulatory matter."),
            ("p", "8.3 If you’re not satisfied with our response, you can complain to the Office of the Privacy Commissioner of Canada or the Commission d’accès à l’information du Québec. We’d appreciate the chance to resolve your concern first."),
        ]),
        ("9. Commercial electronic messages", [
            ("p", "9.1 We send commercial electronic messages only with your consent: express consent, or implied consent where CASL allows it (within 6 months of an enquiry you made, or 2 years of a purchase or engagement). Every message identifies us and includes a working unsubscribe link, and we action unsubscribes within 10 business days."),
        ]),
        ("10. Children", [
            ("p", "10.1 Our services are for businesses and professionals. They are not directed at anyone under 18, and we do not knowingly collect their personal information."),
        ]),
        ("11. Changes to this policy", [
            ("p", "11.1 We may update this policy. We will post the new version with its effective date and, where a change is material, tell you by email if we hold your address."),
        ]),
        ("12. Contact", [
            ("p", f"Privacy Officer, <a href=\"mailto:{PRIVACY_EMAIL}\">{PRIVACY_EMAIL}</a>"),
            ("p", "AML Canada (ComplyFactor Limited), 320 Matheson Boulevard West, Suite 211, Mississauga, Ontario L5R 3R1, Canada"),
        ]),
    ],
}

TERMS = {
    "title": "Terms of Service",
    "intro": [],
    "sections": [
        ("1. Who we are and who these Terms bind", [
            ("p", "1.1 These Terms of Service (“Terms”) govern your access to and use of amlcanada.ca (the “Website”) and any enquiry you make through it."),
            ("p", f"1.2 The Website is operated by {ENTITY} In these Terms, “AML Canada”, “we”, “us” and “our” mean ComplyFactor Limited operating as AML Canada. “You” means the individual using the Website and, where you use it for an organization, that organization. You confirm you have authority to bind it."),
            ("p", "1.3 By using the Website you agree to these Terms and to our <a href=\"privacy.html\">Privacy Policy</a>. If you do not agree, do not use the Website."),
            ("p", "1.4 The Website is intended for businesses and professionals. You must be at least 18 years old to use it."),
        ]),
        ("2. No advice and no client relationship", [
            ("p", "2.1 Content on the Website is general information only. It is not legal, regulatory, tax, accounting or compliance advice. It is not tailored to your circumstances and may not reflect the most recent changes to legislation, regulatory guidance or regulator practice."),
            ("p", "2.2 No advisory, client, fiduciary or professional relationship arises between you and AML Canada from your use of the Website, from submitting an enquiry, or from sharing information with us to scope an engagement. Such a relationship arises only when both parties sign an engagement letter or services agreement (an “Engagement Agreement”)."),
            ("p", "2.3 You must not rely on the Website as a substitute for advice from a qualified professional, or for your own judgment as a reporting entity, compliance officer or senior officer. Decisions you make, and filings you submit to FINTRAC or any other authority, remain your responsibility."),
        ]),
        ("3. Relationship to other agreements", [
            ("p", "3.1 If you have signed an Engagement Agreement with us, that agreement governs the services it covers and prevails over these Terms where they conflict. These Terms continue to govern your use of the Website."),
        ]),
        ("4. Acceptable use", [
            ("p", "4.1 You must not, and must not permit anyone else to:"),
            ("ul", [
                "use the Website in breach of any law, including anti-money laundering, sanctions, privacy or anti-spam law;",
                "use the Website to facilitate money laundering, terrorist financing, sanctions evasion or fraud, or to test how to avoid detection by compliance controls;",
                "scrape, crawl, harvest or bulk-extract content from the Website, except as search engines ordinarily do;",
                "copy, resell, republish or commercially exploit our content;",
                "use the Website or its content to build or train a competing product, service or AI model;",
                "probe, scan or test the vulnerability of the Website, or bypass any security control;",
                "submit malware, or content that is unlawful, infringing or defamatory;",
                "impersonate any person, misrepresent your affiliation, or submit false information in an enquiry; or",
                "use our name or logo, or the fact of any dealings with us, in marketing, banking-partner submissions or regulatory filings without our prior written consent.",
            ]),
        ]),
        ("5. Intellectual property", [
            ("p", "5.1 We and our licensors own all intellectual property rights in the Website and its content, including text, designs and the AML Canada name. Photographs are used under the licences listed on our <a href=\"credits.html\">photo credits</a> page."),
            ("p", "5.2 Subject to these Terms, we grant you a limited, revocable, non-exclusive, non-transferable licence to access the Website and view its content for your internal business purposes."),
            ("p", "5.3 If you send us feedback or suggestions, we may use them without restriction or compensation."),
        ]),
        ("6. Enquiries and information you share with us", [
            ("p", "6.1 When you submit an enquiry or share information to scope an engagement, you confirm you are entitled to share it. Where it includes personal information about others (for example directors, shareholders or employees), you confirm you have given any notice and obtained any consent the law requires."),
            ("p", "6.2 We treat scoping information as confidential and use it to assess, scope and price an engagement, to run conflict checks, and as our Privacy Policy describes. Until an Engagement Agreement is signed, we owe no duty to act on that information, and we may decline an engagement for any reason."),
            ("p", "6.3 Do not send us copies of suspicious transaction reports, or information whose disclosure is restricted by law, unless and until an Engagement Agreement is in place that covers it."),
        ]),
        ("7. Third-party links", [
            ("p", "7.1 The Website may link to third-party sites, including regulator websites. We do not control them and are not responsible for them. Your use of them is governed by their own terms."),
        ]),
        ("8. Disclaimers", [
            ("p", "8.1 To the fullest extent permitted by law, the Website is provided “as is” and “as available”. We disclaim all warranties and conditions, express or implied, including merchantability, fitness for a particular purpose, accuracy, non-infringement, and that the Website will be uninterrupted, error-free or secure."),
            ("p", "8.2 We do not warrant that use of the Website will result in your registration, banking relationship or regulatory approval, or will prevent an administrative monetary penalty, enforcement action or examination finding."),
        ]),
        ("9. Limitation of liability", [
            ("p", "9.1 Nothing in these Terms limits or excludes liability for death or personal injury caused by negligence, for fraud or fraudulent misrepresentation, or for any other liability that cannot be limited or excluded by law."),
            ("p", "9.2 Subject to section 9.1, we are not liable, whether in contract, tort (including negligence), breach of statutory duty or otherwise, for any:"),
            ("ul", [
                "loss of profits, revenue, business, contracts, goodwill or anticipated savings;",
                "administrative monetary penalties, fines, regulatory sanctions, or costs of regulatory examinations or remediation;",
                "loss of a registration, licence or banking relationship; or",
                "indirect, special, consequential, incidental or punitive loss.",
            ]),
            ("p", "9.3 Subject to section 9.1, our total aggregate liability arising out of or in connection with the Website and these Terms is limited to CAD 100."),
            ("p", "9.4 Any claim must be brought within one year after the cause of action arises, where the law permits."),
        ]),
        ("10. Indemnity", [
            ("p", "10.1 You will defend, indemnify and hold harmless ComplyFactor Limited, its affiliates, directors, officers, employees and contractors against any claims, losses, penalties, damages and costs (including reasonable legal fees) arising from your breach of these Terms or applicable law, or from content you submit."),
        ]),
        ("11. Changes to these Terms", [
            ("p", "11.1 We may update these Terms. We will post the updated version with a new effective date. Continued use of the Website after the effective date means you accept the changes."),
        ]),
        ("12. Governing law and disputes", [
            ("p", "12.1 These Terms are governed by the laws of the Province of Ontario and the federal laws of Canada applicable in it. The courts of Ontario sitting in Toronto have exclusive jurisdiction."),
            ("p", "12.2 If you use the Website as a consumer, nothing in these Terms affects rights you have under the mandatory consumer protection laws of your place of residence."),
        ]),
        ("13. General", [
            ("p", "13.1 These Terms, our Privacy Policy and any applicable agreement under section 3 form the entire agreement on their subject. If a provision is found unenforceable, it is limited to the minimum extent necessary and the rest continues. Our failure to enforce a right is not a waiver."),
            ("p", f"13.2 Contact: <a href=\"mailto:{LEGAL_EMAIL}\">{LEGAL_EMAIL}</a>, or by post to 320 Matheson Boulevard West, Suite 211, Mississauga, Ontario L5R 3R1, Canada."),
        ]),
    ],
}


def render(doc):
    out = []
    for heading, blocks in doc["sections"]:
        out.append(f"<h2>{heading}</h2>")
        for kind, val, *rest in blocks:
            if kind == "p":
                out.append(f"<p>{val}</p>")
            elif kind == "ul":
                out.append("<ul>" + "".join(f"<li>{x}</li>" for x in val) + "</ul>")
            elif kind == "table":
                rows = rest[0]
                head = "".join(f'<th scope="col">{h}</th>' for h in val)
                body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
                out.append(f'<div class="legal-table"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
    return "\n        ".join(out)
