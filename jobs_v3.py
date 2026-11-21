"""Open roles for amlcanada.ca/careers.html. Each entry builds one job page with JobPosting schema.

To close a role, set "closed": True (the page stays up without JobPosting schema, Google drops the listing)
or move its validThrough date into the past. Duties and requirements are the owner's call; nothing here
is a claim about AML Canada beyond PRODUCT.md.
"""

APPLY_TO = "info@amlcanada.ca"  # FormSubmit delivers applications and CVs here

JOBS = {
    "careers-aml-compliance-officer.html": dict(
        title="AML Compliance Officer",
        crumb="AML Compliance Officer",
        seo_title="AML Compliance Officer Job, Mississauga (Hybrid) | AML Canada",
        desc="Full-time AML compliance officer role in Mississauga (hybrid): KYC file reviews, transaction monitoring and FINTRAC reporting for MSBs and fintechs.",
        posted="2026-11-22",
        valid_through="2027-01-31",
        employment="FULL_TIME",
        summary=("We're hiring an AML compliance officer to work on FINTRAC compliance for our clients: money services businesses, "
                 "virtual currency dealers, payment service providers and fintechs. You'll review client files, monitor transactions, "
                 "prepare FINTRAC reports and keep compliance programs up to date, working with the rest of our compliance team."),
        duties=[
            "Review client onboarding files as the second line: identity verification, beneficial ownership, politically exposed person and sanctions screening results.",
            "Review transaction monitoring alerts and document the outcome of each review.",
            "Prepare suspicious transaction reports, large cash transaction reports, electronic funds transfer reports and large virtual currency transaction reports for FINTRAC.",
            "Keep clients' AML policies, procedures and record-keeping up to date when their business or the rules change.",
            "Help prepare business-wide and client risk assessments.",
            "Support two-year effectiveness reviews and FINTRAC examinations.",
            "Keep training records and help deliver AML training to client staff.",
        ],
        requirements=[
            "At least 2 years of AML/ATF compliance work at a Canadian reporting entity, such as an MSB, bank, credit union, virtual currency dealer or payments company.",
            "Working knowledge of the PCMLTFA, its regulations and FINTRAC guidance.",
            "Experience preparing at least one type of FINTRAC report.",
            "Clear, careful written English.",
            "Eligible to work in Canada.",
            "Able to work from our Mississauga office on agreed days each week.",
        ],
        assets=[
            "CAMS, CAFC or a similar AML certification.",
            "Experience with virtual currency or payment service providers.",
            "French.",
        ],
    ),
    "careers-mlro.html": dict(
        title="Money Laundering Reporting Officer (MLRO)",
        crumb="MLRO",
        seo_title="MLRO / Chief AML Compliance Officer Job, Mississauga | AML Canada",
        desc="Full-time MLRO (chief AML compliance officer) role in Mississauga (hybrid): lead FINTRAC compliance programs, reporting decisions and examinations for clients.",
        posted="2026-11-22",
        valid_through="2027-01-31",
        employment="FULL_TIME",
        summary=("We're hiring a money laundering reporting officer (MLRO) to act as the appointed compliance officer for client reporting entities "
                 "under the PCMLTFA. You'll own their compliance programs, make reporting decisions, lead FINTRAC examinations and report to "
                 "their senior management, with the support of our compliance team."),
        duties=[
            "Act as the appointed compliance officer for client MSBs, virtual currency dealers and payment businesses.",
            "Own each client's compliance program: policies and procedures, risk assessment, training and the two-year effectiveness review.",
            "Decide on suspicious transaction reports and review the other FINTRAC reports before they're submitted.",
            "Lead clients through FINTRAC examinations and follow-up action plans.",
            "Report to client senior management and boards on compliance risks and gaps.",
            "Review and approve high-risk client onboarding decisions.",
            "Guide and check the work of compliance officers on our team.",
        ],
        requirements=[
            "At least 5 years of AML/ATF compliance work, including at least 2 years as a compliance officer, CAMLO, MLRO or deputy at a FINTRAC reporting entity.",
            "Thorough knowledge of the PCMLTFA, its regulations and FINTRAC guidance, including the 2026 penalty changes.",
            "Experience deciding on suspicious transaction reports.",
            "Experience with a FINTRAC examination or an effectiveness review.",
            "CAMS, CAFC or a similar AML certification.",
            "Eligible to work in Canada.",
            "Able to work from our Mississauga office on agreed days each week.",
        ],
        assets=[
            "Experience with Bank of Canada RPAA requirements for payment service providers.",
            "Experience with virtual currency dealers.",
            "French.",
        ],
    ),
}
