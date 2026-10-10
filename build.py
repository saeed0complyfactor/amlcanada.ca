"""Builds AML Canada's supporting pages and keeps the shared header, menu and
footer identical on every page, including the hand-written homepage.

Run:  python build.py
"""
from pathlib import Path
import html
import re
import json
import legal

ROOT = Path(__file__).parent
SITE = ROOT / "site"
YEAR = 2026
DOMAIN = "https://amlcanada.ca"
ORG_ID = f"{DOMAIN}/#org"
DESCRIPTOR = "AML & Regulatory Compliance Services in Canada"
PHONE_DISPLAY = "+1 807-806-0444"

# ---- Switches. Each feature turns on when its value is filled in, then run: python build.py
WEB3FORMS_KEY = "cbe536ca-6b46-40cb-b5d6-71ec02ef63d2"  # web3forms.com public access key: the consultation form sends to your inbox
CF_BEACON_TOKEN = ""      # Cloudflare Web Analytics site token (cookieless visitor stats)
GA4_ID = ""               # Google Analytics 4 measurement ID, e.g. G-XXXXXXXXXX (loads only after cookie consent)
GSC_VERIFICATION = ""     # optional: Google Search Console meta-tag code (DNS TXT verification needs nothing here)
PHONE_TEL = "+18078060444"
ADDRESS_LINES = ["Suite 211, 320 Matheson Blvd West", "Mississauga, ON L5R 3R1", "Canada"]
POSTAL = {"@type": "PostalAddress", "streetAddress": "320 Matheson Blvd West, Suite 211", "addressLocality": "Mississauga", "addressRegion": "ON", "postalCode": "L5R 3R1", "addressCountry": "CA"}

SEO = {
    "index.html": ("AML & Regulatory Compliance in Canada | AML Canada",
                   "FINTRAC MSB registration, AML compliance programs, effectiveness reviews and AML training for MSBs, crypto and fintech companies in Canada."),
    "services.html": ("AML Compliance Services in Canada | AML Canada",
                      "AML compliance services in Canada: MSB registration, Canadian business address, compliance programs, effectiveness reviews and training."),
    "canadian-address.html": ("Canadian Business Address for Foreign MSBs | AML Canada",
                              "A Canadian business address for foreign money services businesses and companies entering Canada, coordinated with your FINTRAC MSB registration."),
    "msb-registration.html": ("MSB Registration with FINTRAC in Canada | AML Canada",
                              "Register your money services business with FINTRAC. Help with Canadian and foreign MSB registration, virtual currency dealers and your compliance program."),
    "compliance-programs.html": ("AML Compliance Programs for FINTRAC | AML Canada",
                                 "AML compliance programs built for your business: policies and procedures, risk assessment, compliance officer support and an ongoing training program."),
    "effectiveness-reviews.html": ("FINTRAC Two-Year Effectiveness Reviews | AML Canada",
                                   "Two-year AML effectiveness reviews that test whether your compliance program works in practice, plus FINTRAC examination preparation."),
    "training.html": ("AML Training for Staff in Canada | AML Canada",
                      "Scenario-based AML and anti-terrorist financing training for front-line staff, compliance teams and senior management, with training records."),
    "who-we-help.html": ("AML Compliance for MSBs, Crypto and Fintech | AML Canada",
                         "AML compliance support for MSBs, virtual currency dealers, payment and fintech companies, foreign businesses entering Canada and compliance officers."),
    "how-we-work.html": ("How We Work | AML Canada",
                         "How an AML compliance engagement with AML Canada runs: consultation, written scope, delivery and ongoing support."),
    "about.html": ("About AML Canada | AML Compliance Consulting",
                   "AML Canada provides AML and anti-terrorist financing compliance consulting for businesses regulated by FINTRAC in Canada."),
    "contact.html": ("Book an AML Compliance Consultation | AML Canada",
                     "Book a consultation with AML Canada about FINTRAC MSB registration, compliance programs, effectiveness reviews or AML training."),
    "credits.html": ("Photo Credits | AML Canada", "Photo credits for the AML Canada website."),
    "privacy.html": ("Privacy Policy | AML Canada", "How AML Canada (ComplyFactor Limited) collects, uses and protects personal information under PIPEDA, Quebec Law 25 and CASL."),
    "terms.html": ("Terms of Service | AML Canada", "The terms that govern your use of amlcanada.ca, operated by ComplyFactor Limited as AML Canada."),
    "404.html": ("Page not found | AML Canada", "This page doesn’t exist. Find AML Canada’s services or book a consultation."),
}


def url_for(filename):
    return f"{DOMAIN}/" if filename == "index.html" else f"{DOMAIN}/{filename}"


def jsonld(obj):
    import json
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


ORG = {
    "@type": "Organization",
    "@id": ORG_ID,
    "name": "AML Canada",
    "url": f"{DOMAIN}/",
    "description": "AML and anti-terrorist financing compliance consulting for businesses regulated by FINTRAC in Canada.",
    "slogan": DESCRIPTOR,
    "areaServed": {"@type": "Country", "name": "Canada"},
    "telephone": PHONE_TEL,
    "address": POSTAL,
    "contactPoint": {"@type": "ContactPoint", "telephone": PHONE_TEL, "contactType": "customer service", "areaServed": "CA", "availableLanguage": ["en"]},
    "knowsAbout": ["Anti-money laundering", "Anti-terrorist financing", "FINTRAC", "PCMLTFA", "Money services business registration", "AML compliance programs", "Effectiveness reviews", "AML training"],
}


def seo_head(filename, crumbs=None, service=None):
    title, desc = SEO[filename]
    url = url_for(filename)
    graph = [ORG]
    if filename == "index.html":
        graph.append({"@type": "WebSite", "@id": f"{DOMAIN}/#website", "url": f"{DOMAIN}/", "name": "AML Canada", "publisher": {"@id": ORG_ID}, "inLanguage": "en-CA"})
    graph.append({"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "isPartOf": {"@id": f"{DOMAIN}/#website"}, "inLanguage": "en-CA"})
    if crumbs:
        items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": url_for(h)} for i, (n, h) in enumerate(crumbs)]
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    if service:
        graph.append({"@type": "Service", "name": service, "serviceType": service, "description": desc, "provider": {"@id": ORG_ID}, "areaServed": {"@type": "Country", "name": "Canada"}, "url": url})
    e = html.escape
    config = {"web3formsKey": WEB3FORMS_KEY, "ga4": GA4_ID}
    tracking = f'<script>window.AMLC = {json.dumps(config)};</script>'
    if CF_BEACON_TOKEN:
        beacon = json.dumps({"token": CF_BEACON_TOKEN})
        tracking += f"\n<script defer src=\"https://static.cloudflareinsights.com/beacon.min.js\" data-cf-beacon='{beacon}'></script>"
    if GSC_VERIFICATION and filename == "index.html":
        tracking += f'\n<meta name="google-site-verification" content="{e(GSC_VERIFICATION)}">'
    if filename == "404.html":
        return f"""<title>{e(title)}</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{tracking}"""
    return f"""<title>{e(title)}</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AML Canada">
<meta property="og:locale" content="en_CA">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Aerial view of downtown Toronto at sunset">
<meta name="twitter:card" content="summary_large_image">
{tracking}
{jsonld({"@context": "https://schema.org", "@graph": graph})}"""

NAV = [
    ("Services", "services.html"),
    ("Who we help", "who-we-help.html"),
    ("How we work", "how-we-work.html"),
    ("About", "about.html"),
    ("Book a consultation", "contact.html"),
]

SERVICES = [
    ("canadian-address", "Canadian address"),
    ("msb-registration", "MSB registration"),
    ("compliance-programs", "Compliance programs"),
    ("effectiveness-reviews", "Effectiveness reviews"),
    ("training", "Training"),
]

PHOTOS = {
    "hero-toronto": ("mwangi gatheca", "qlKaN7eqay8"),
    "hero-vancouver": ("Adrian Yu", "Wc45W-dQFlA"),
    "hero-montreal": ("Olivier Devillers", "AzHrzWtmp1A"),
    "card-currency": ("Jason Leung", "SAYzxuS1O3M"),
    "card-passport": ("Kylie Anderson", "aGDILBE1Kus"),
    "card-signing": ("Gabrielle Henderson", "HJckKnwCXxQ"),
    "card-training": ("Sable Flow", "KHpjeuaWOec"),
    "tower": ("Harry Shelton", "pPxhM0CRzl4"),
    "meeting": ("Dylan Gillis", "KdeqA3aTnBY"),
    "payments": ("Vitaly Gariev", "VmyqDMyRVq0"),
    "peace-tower": ("Caio Fernandes", "9ax9_oAO0FQ"),
    "page-towers": ("Diego Bernal", "m0CDmLSwJsY"),
    "page-street": ("Zarif Ali", "MM92ZvKB8L0"),
    "page-parliament": ("Philip Yu", "rNIB2hWr6kU"),
    "page-calgary": ("Mahesh Gupta", "Q3hxoJk4Sgw"),
    "page-glassroof": ("Frederic Bourbeau", "8a1B2dH9WNM"),
    "page-meeting": ("Dylan Gillis", "KdeqA3aTnBY"),
    "page-peacetower": ("Caio Fernandes", "9ax9_oAO0FQ"),
    "page-calgarytower": ("Kyler Nixon", "_ZBekGTBh-c"),
}

CHEV = '<svg><use href="#chev"/></svg>'

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <symbol id="chev" viewBox="0 0 16 16"><path d="M6 3.5 10.5 8 6 12.5"/></symbol>
    <symbol id="menu" viewBox="0 0 24 24"><path d="M4 7.5h16M4 12h16M4 16.5h16"/></symbol>
    <symbol id="close" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></symbol>
    <symbol id="pause" viewBox="0 0 16 16"><path d="M5.5 4v8M10.5 4v8"/></symbol>
    <symbol id="play" viewBox="0 0 16 16"><path d="M5.5 3.8v8.4L12 8z"/></symbol>
  </defs>
</svg>"""


def header(current=""):
    links = "\n      ".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>' for label, href in NAV
    )
    return f"""<a class="skip" href="#main">Skip to content</a>

<header class="site-header">
  <a class="wordmark" href="index.html" aria-label="AML Canada, home">AML Canada</a>
  <div class="utility">
    <a class="utility-cta" href="contact.html">Book a consultation</a>
    <button class="utility-btn" type="button" aria-expanded="false" aria-controls="menu" aria-label="Open menu"><svg><use href="#menu"/></svg></button>
  </div>
</header>

<div class="menu" id="menu" hidden>
  <div class="menu-inner">
    <button class="menu-close" type="button" aria-label="Close menu"><svg><use href="#close"/></svg></button>
    <nav aria-label="Main">
      {links}
    </nav>
    <div class="menu-side">
      <p class="menu-note">AML and anti-terrorist financing compliance for businesses regulated by FINTRAC.</p>
      <ul class="menu-services">{"".join(f'<li><a href="{slug}.html">{name}</a></li>' for slug, name in SERVICES)}</ul>
    </div>
  </div>
</div>"""


def footer():
    index = "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in [("Home", "index.html")] + NAV)
    services = "".join(f'<li><a href="{slug}.html">{name}</a></li>' for slug, name in SERVICES)
    return f"""<footer class="site-footer">
  <div class="wrap foot-grid">
    <div class="foot-col">
      <h2>Index</h2>
      <ul>{index}</ul>
    </div>
    <div class="foot-col">
      <h2>Services</h2>
      <ul>{services}</ul>
    </div>
    <div class="foot-col">
      <h2>Contact</h2>
      <address class="foot-address">{"<br>".join(ADDRESS_LINES)}</address>
      <ul><li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li><li><a href="contact.html">Book a consultation</a></li></ul>
    </div>
    <div class="foot-col">
      <h2>Information</h2>
      <p>The information on this site is general and is not legal advice.</p>
      <ul><li><a href="privacy.html">Privacy policy</a></li><li><a href="terms.html">Terms of service</a></li><li><button type="button" class="cookie-settings" hidden>Cookie settings</button></li><li><a href="credits.html">Photo credits</a></li></ul>
    </div>
  </div>
  <div class="wrap foot-base"><span class="wordmark wordmark-foot">AML Canada</span><p>© {YEAR} AML Canada</p></div>
</footer>"""


def page(filename, title, description, body, current="", crumbs=None, service=None):
    return f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- chrome:seo -->
{seo_head(filename, crumbs, service)}
<!-- /chrome:seo -->
<meta name="theme-color" content="#062433">
<link rel="preload" href="fonts/source-serif-4-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/public-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css">
</head>
<body class="inner">
{SPRITE}

<!-- chrome:header -->
{header(current)}
<!-- /chrome:header -->

<main id="main">
{body}
</main>

<!-- chrome:footer -->
{footer()}
<!-- /chrome:footer -->

<script src="main.js"></script>
</body>
</html>
"""


def page_hero(title, intro, image, alt, crumbs):
    trail = " ".join(f'<a href="{h}">{t}</a><span aria-hidden="true">/</span>' for t, h in crumbs)
    return f"""  <section class="page-hero">
    <div class="page-hero-media"><img src="img/{image}.jpg" alt="{html.escape(alt)}" width="2400" height="1100"></div>
    <div class="page-hero-panel">
      <nav class="crumbs" aria-label="Breadcrumb">{trail}</nav>
      <h1>{title}</h1>
      <p>{intro}</p>
    </div>
  </section>"""


def lead_block(lead, paragraphs):
    ps = "".join(f"<p>{p}</p>" for p in paragraphs)
    return f"""  <section class="lead-block">
    <div class="wrap lead-grid">
      <p class="lead">{lead}</p>
      <div class="lead-body">{ps}</div>
    </div>
  </section>"""


def rule_list(heading, items, dark=False, intro=""):
    rows = "".join(
        f'<li><h3>{t}</h3>{f"<p>{d}</p>" if d else ""}</li>' for t, d in items
    )
    cls = "rule-section dark" if dark else "rule-section"
    intro_html = f'<p class="rule-intro">{intro}</p>' if intro else ""
    return f"""  <section class="{cls}">
    <div class="wrap rule-grid">
      <div><h2>{heading}</h2>{intro_html}</div>
      <ul class="rule-list">{rows}</ul>
    </div>
  </section>"""


def link_cards(heading, cards):
    items = "".join(
        f'<a class="link-card" href="{href}"><span class="link-card-title">{t}</span><span class="link-card-text">{d}</span><span class="link-card-more">Read more{CHEV}</span></a>'
        for t, d, href in cards
    )
    return f"""  <section class="link-cards">
    <div class="wrap">
      <h2 class="eyeline">{heading}</h2>
      <div class="link-card-grid">{items}</div>
    </div>
  </section>"""


def cta(text="Tell us about your business and what you need, and we’ll find a time to talk.", need=""):
    q = f"?need={html.escape(need)}" if need else ""
    return f"""  <section class="cta-band">
    <div class="wrap cta-grid">
      <h2>Book a consultation</h2>
      <p>{text}</p>
      <a class="btn" href="contact.html{q}">Book a consultation{CHEV}</a>
    </div>
  </section>"""


STEPS = [
    ("Consultation", "A conversation about your business, your timeline and what is required of you."),
    ("Scope", "A written scope of the work, so you know what you are getting before anything starts."),
    ("Delivery", "We do the work with you and explain the decisions along the way."),
    ("Ongoing support", "Help as your business, your products or your obligations change."),
]


def steps_strip():
    items = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in STEPS)
    return f"""  <section class="steps">
    <div class="wrap">
      <div class="steps-head"><h2>How the work runs</h2><a class="text-link" href="how-we-work.html">How we work{CHEV}</a></div>
      <ol class="steps-list">{items}</ol>
    </div>
  </section>"""


# ---------------------------------------------------------------- service pages
SERVICE_PAGES = {
    "canadian-address": dict(
        intro="A Canadian business address for companies setting up in Canada.",
        image="page-street", alt="A downtown Toronto street with office towers", card="card-passport", card_alt="A traveller holding a Canadian passport in an airport",
        lead="Setting up in Canada from abroad is easier with a Canadian base for your business.",
        body=[
            "We provide a Canadian business address for companies entering the Canadian market, including foreign money services businesses.",
            "What the address includes depends on your situation. We confirm it with you, in writing, before anything starts.",
        ],
        who=[
            ("Foreign money services businesses", "Companies outside Canada that serve customers in Canada."),
            ("Companies opening Canadian operations", "Businesses establishing a presence before hiring locally."),
            ("Start-ups preparing to launch", "Founders who need their Canadian setup in order early."),
        ],
        what=[
            ("A Canadian business address", "A Canadian base for your business setup."),
            ("A scope confirmed in writing", "What is included, and for how long, agreed before anything starts."),
            ("Coordination with your registration", "If you are also registering with FINTRAC, we keep the two aligned."),
        ],
        related=["msb-registration", "compliance-programs"],
    ),
    "msb-registration": dict(
        intro="Registration with FINTRAC as a money services business, prepared properly.",
        image="page-calgary", alt="The Calgary skyline above the Bow River", card="card-currency", card_alt="International banknotes spread across a table",
        lead="Businesses that provide money services in Canada, such as foreign exchange dealing, money transferring or dealing in virtual currency, must register with FINTRAC.",
        body=[
            "Foreign money services businesses that direct and provide these services to people in Canada must register too.",
            "We help you work out whether and how registration applies to you, prepare the information FINTRAC asks for, and put the compliance program you will need in place alongside it.",
        ],
        who=[
            ("New money services businesses", "Foreign exchange dealers, money transfer businesses and others getting started."),
            ("Virtual currency dealers", "Exchanges and dealers in virtual currency."),
            ("Foreign money services businesses", "Businesses outside Canada serving people in Canada."),
        ],
        what=[
            ("An assessment of your activities", "Which of your services are money services, and what follows from that."),
            ("Preparation of your registration", "The information FINTRAC asks for, gathered and checked with you."),
            ("Support through submission", "Including follow-up questions after you apply."),
            ("Your compliance program", "Built alongside your registration, not after it."),
        ],
        related=["compliance-programs", "canadian-address"],
    ),
    "compliance-programs": dict(
        intro="Policies, procedures and risk assessments written for the way your business actually operates.",
        image="page-glassroof", alt="A glass and steel roof seen from below", card="tower", card_alt="Looking up at a glass office tower",
        lead="Businesses regulated by FINTRAC must have a compliance program. It has to work in practice, not only on paper.",
        body=[
            "A compliance program generally brings together a compliance officer, written policies and procedures, a risk assessment, an ongoing training program, and a regular review of how well it works.",
            "We build or rebuild the parts you need, around your products, your customers and the way your team works.",
        ],
        who=[
            ("Newly registered businesses", "Putting a program in place for the first time."),
            ("Growing businesses", "New products, new markets or more volume than the program was written for."),
            ("Businesses after a review or examination", "Closing the gaps that were found."),
        ],
        what=[
            ("Policies and procedures", "Written for your business, in language your team can follow."),
            ("Risk assessment", "Your products, customers, channels and geography, assessed and documented."),
            ("Compliance officer support", "A second pair of hands for the person responsible."),
            ("Training program", "A plan for ongoing training that fits your staff and your risks."),
        ],
        related=["effectiveness-reviews", "training"],
    ),
    "effectiveness-reviews": dict(
        intro="Find the gaps in your compliance program before an examiner does.",
        image="hero-montreal", alt="The Old Port of Montreal on a clear day", card="card-signing", card_alt="Two people reviewing and signing documents at a table",
        lead="Reporting entities must review the effectiveness of their compliance program every two years.",
        body=[
            "An effectiveness review looks at whether your policies, risk assessment and training work in practice, and whether what your team does matches what your documents say.",
            "We also help you prepare for a FINTRAC examination: what to expect, what to have ready, and what to fix first.",
        ],
        who=[
            ("Reporting entities due a review", "Including businesses whose last review is approaching two years."),
            ("Businesses expecting an examination", "Getting ready before FINTRAC arrives."),
            ("New compliance officers", "Taking stock of a program they have inherited."),
        ],
        what=[
            ("A scoped review", "Agreed in writing before the work starts."),
            ("Testing in practice", "Checking that what happens matches what is written."),
            ("Written findings", "Clear findings and recommendations, in order of priority."),
            ("Examination preparation", "Help getting your records and your team ready."),
        ],
        related=["compliance-programs", "training"],
    ),
    "training": dict(
        intro="AML training for front-line staff and compliance teams, built around situations they will recognize.",
        image="page-meeting", alt="People around a meeting table taking notes", card="card-training", card_alt="A small team working through ideas at a whiteboard",
        lead="An ongoing compliance training program is one of the required parts of a compliance program.",
        body=[
            "Training works when staff recognize the situation in front of them and know what to do next. We build training around real scenarios for your business.",
            "We train front-line staff and compliance teams, and help you keep the records that show training happened.",
        ],
        who=[
            ("Front-line staff", "The people who meet customers and process transactions."),
            ("Compliance teams", "Analysts and compliance officers who need depth."),
            ("Senior management", "Leaders responsible for the program’s oversight."),
        ],
        what=[
            ("Scenario-based training", "Built around situations your staff will recognize."),
            ("Training for each role", "Front line, compliance and management."),
            ("Training records", "Evidence of who was trained, on what, and when."),
        ],
        related=["compliance-programs", "effectiveness-reviews"],
    ),
}

SERVICE_SUMMARY = {
    "canadian-address": "A Canadian business address for companies setting up in Canada.",
    "msb-registration": "Registration with FINTRAC as a money services business, including foreign MSBs and virtual currency dealers.",
    "compliance-programs": "Policies and procedures, risk assessment and compliance officer support.",
    "effectiveness-reviews": "A structured review of your program, and preparation for a FINTRAC examination.",
    "training": "Scenario-based AML training for front-line staff and compliance teams.",
}


def photo_band(heading, items, image, alt, flip=False):
    rows = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in items)
    return f"""  <section class="photo-feature">
    <div class="wrap">
      <article class="group{' flip' if flip else ''}">
        <figure class="group-photo"><img src="img/{image}.jpg" alt="{html.escape(alt)}" width="1200" height="900"></figure>
        <div class="group-copy"><h2>{heading}</h2><ul class="who-list">{rows}</ul></div>
      </article>
    </div>
  </section>"""


def service_page(slug, name):
    d = SERVICE_PAGES[slug]
    related = [(dict(SERVICES)[r], SERVICE_SUMMARY[r], f"{r}.html") for r in d["related"]]
    body = "\n".join([
        page_hero(name, d["intro"], d["image"], d["alt"], [("Home", "index.html"), ("Services", "services.html")]),
        lead_block(d["lead"], d["body"]),
        photo_band("Who it’s for", d["who"], d["card"], d["card_alt"], flip=SERVICES.index((slug, name)) % 2 == 1),
        rule_list("What we do", d["what"], dark=True),
        link_cards("Related services", related),
        cta(need=name),
    ])
    return page(f"{slug}.html", name, d["intro"], body, crumbs=[("Home", "index.html"), ("Services", "services.html"), (name, f"{slug}.html")], service=name)


def services_index():
    cards = "".join(
        f'<a class="svc-row" href="{slug}.html"><span class="svc-name">{name}</span><span class="svc-text">{SERVICE_SUMMARY[slug]}</span>{CHEV}</a>'
        for slug, name in SERVICES
    )
    body = "\n".join([
        page_hero("Services", "Registration, compliance programs, reviews and training for businesses regulated by FINTRAC.", "page-towers", "Looking up at dark office towers against a pale sky", [("Home", "index.html")]),
        f"""  <section class="svc-index">
    <div class="wrap svc-grid">
      <p class="lead">From your first registration to your next examination, we help you meet your obligations and show that you have.</p>
      <div class="svc-list">{cards}</div>
    </div>
  </section>""",
        steps_strip(),
        cta(),
    ])
    return page("services.html", "Services", "AML Canada’s services: Canadian address, MSB registration, compliance programs, effectiveness reviews and training.", body, "services.html", crumbs=[("Home", "index.html"), ("Services", "services.html")])


def who_we_help():
    groups = [
        ("Money services businesses", "Foreign exchange dealers, money transfer businesses and others that need to register with FINTRAC and stay compliant.", ["msb-registration", "compliance-programs", "effectiveness-reviews"], "card-currency", "International banknotes spread across a table"),
        ("Virtual currency dealers", "Exchanges and dealers in virtual currency, which register with FINTRAC as money services businesses.", ["msb-registration", "compliance-programs", "training"], "payments", "A customer paying with a card at a café table"),
        ("Foreign businesses entering Canada", "Companies outside Canada that serve customers in Canada and need registration support and a Canadian business address.", ["canadian-address", "msb-registration"], "card-passport", "A traveller holding a Canadian passport in an airport"),
        ("Payment and fintech companies", "Start-ups and growing companies that need to understand their obligations and meet them as they scale.", ["compliance-programs", "training"], "meeting", "People around a meeting table with notebooks"),
        ("Compliance officers", "Compliance officers at reporting entities who need a second pair of hands, a review, or training for their teams.", ["effectiveness-reviews", "training", "compliance-programs"], "card-training", "A small team working through ideas at a whiteboard"),
    ]
    rows = []
    for i, (t, d, svcs, img, alt) in enumerate(groups):
        links = "".join(f'<li><a href="{s}.html">{dict(SERVICES)[s]}{CHEV}</a></li>' for s in svcs)
        rows.append(f"""      <article class="group{' flip' if i % 2 else ''}">
        <figure class="group-photo"><img src="img/{img}.jpg" alt="{alt}" width="1200" height="900"></figure>
        <div class="group-copy"><h2>{t}</h2><p>{d}</p><h3>Services that usually help</h3><ul class="group-links">{links}</ul></div>
      </article>""")
    body = "\n".join([
        page_hero("Who we help", "Businesses regulated by FINTRAC, from first registration to their next examination.", "hero-vancouver", "Aerial view of the Vancouver waterfront and mountains", [("Home", "index.html")]),
        f"""  <section class="groups">
    <div class="wrap">
{chr(10).join(rows)}
    </div>
  </section>""",
        cta(),
    ])
    return page("who-we-help.html", "Who we help", "AML Canada works with money services businesses, virtual currency dealers, payment and fintech companies, foreign businesses entering Canada, and compliance officers.", body, "who-we-help.html", crumbs=[("Home", "index.html"), ("Who we help", "who-we-help.html")])


def how_we_work():
    detail = [
        ("Consultation", "We start with a conversation about your business, your timeline and what is required of you. You leave it with a clear next step.", ["Your business model and the services you offer", "Your deadlines, such as a launch or an examination", "What you already have in place"]),
        ("Scope", "We write down what we will do, what we need from you, and when. Nothing starts until you have agreed it.", ["The work, in plain language", "What we need from you, and when", "Timeline and milestones"]),
        ("Delivery", "We do the work with you, not around you, and explain the decisions along the way so your team can stand behind them.", ["Regular check-ins", "Drafts you can comment on", "Decisions explained, not just made"]),
        ("Ongoing support", "Your obligations change as your business does. We are there for the next product, the next market or the next review.", ["Updates when your business changes", "Help with questions from FINTRAC", "Your next effectiveness review"]),
    ]
    items = "".join(
        f'<li><div class="hw-head"><span class="hw-n">{i + 1}</span><h2>{t}</h2></div><p>{d}</p><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></li>'
        for i, (t, d, xs) in enumerate(detail)
    )
    body = "\n".join([
        page_hero("How we work", "Every engagement starts with a conversation and a written scope.", "page-parliament", "Parliament Hill in Ottawa from across the river", [("Home", "index.html")]),
        lead_block("Compliance work goes better when you know what is happening and why.", ["We keep engagements simple: a conversation, a written scope, the work itself, and support afterwards. Each step is set out below."]),
        f"""  <section class="hw">
    <div class="wrap"><ol class="hw-list">{items}</ol></div>
  </section>""",
        cta(),
    ])
    return page("how-we-work.html", "How we work", "How an engagement with AML Canada runs: consultation, scope, delivery and ongoing support.", body, "how-we-work.html", crumbs=[("Home", "index.html"), ("How we work", "how-we-work.html")])


def about():
    principles = [
        ("Clear answers", "People come to us under pressure. We tell you plainly what applies to you and what happens next."),
        ("Specific, not generic", "Programs written for your business, not templates with your name on them."),
        ("Accuracy first", "We check every regulatory statement before we rely on it."),
        ("One next step", "Every conversation ends with a clear next step."),
    ]
    body = "\n".join([
        page_hero("About AML Canada", "AML and anti-terrorist financing compliance for businesses regulated by FINTRAC.", "page-peacetower", "The Peace Tower and neighbouring buildings in Ottawa", [("Home", "index.html")]),
        lead_block("AML Canada helps businesses register with FINTRAC, build compliance programs that work, prepare for examinations and train their people.", [
            "FINTRAC is Canada’s financial intelligence unit. The businesses it regulates carry real obligations, and most of them are busy running everything else.",
            "We exist to make those obligations clear and manageable, from the first registration to the next review.",
        ]),
        rule_list("What we believe", principles, dark=True),
        f"""  <section class="photo-band"><img src="img/peace-tower.jpg" alt="The Peace Tower on Parliament Hill, Ottawa" width="1200" height="1400"></section>""",
        cta(),
    ])
    return page("about.html", "About", "About AML Canada: AML and anti-terrorist financing compliance for businesses regulated by FINTRAC.", body, "about.html", crumbs=[("Home", "index.html"), ("About", "about.html")])


FORM = """<form class="consult-form" id="consult-form" novalidate>
        <label><span>Name</span><input name="name" autocomplete="name" required></label>
        <label><span>Work email</span><input name="email" type="email" autocomplete="email" required></label>
        <label><span>Company</span><input name="company" autocomplete="organization" required></label>
        <label><span>I need help with</span>
          <select name="need" required>
            <option value="">Choose one</option>
            <option>Canadian address</option>
            <option>MSB registration</option>
            <option>Compliance program</option>
            <option>Effectiveness review</option>
            <option>Training</option>
            <option>Not sure yet</option>
          </select>
        </label>
        <label class="full"><span>Anything we should know? <em>(optional)</em></span><textarea name="message" rows="4"></textarea></label>
        <p class="form-consent full">By sending this form you agree to our <a href="privacy.html">Privacy Policy</a>. We use your details only to respond to your request.</p>
        <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="form-foot full">
          <button type="submit" class="btn">Book a consultation<svg><use href="#chev"/></svg></button>
          <p class="form-msg" role="status" aria-live="polite"></p>
        </div>
      </form>"""


def contact():
    nxt = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in [
        ("We read your request", "So the first conversation starts from your situation, not from scratch."),
        ("We find a time", "We come back to you to arrange the consultation."),
        ("You leave with a next step", "Whether that is a scope of work or simply an answer."),
    ])
    body = "\n".join([
        page_hero("Book a consultation", "Tell us about your business and what you need.", "page-calgarytower", "The Calgary skyline at golden hour", [("Home", "index.html")]),
        f"""  <section class="consult consult-page" id="consult">
    <div class="wrap consult-grid">
      <div>
        <h2>What happens next</h2>
        <ol class="next-list">{nxt}</ol>
        <div class="reach">
          <h2 class="reach-title">Call or visit</h2>
          <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
          <address>{"<br>".join(ADDRESS_LINES)}</address>
        </div>
      </div>
      {FORM}
    </div>
  </section>""",
    ])
    return page("contact.html", "Book a consultation", "Book a consultation with AML Canada about FINTRAC registration, compliance programs, effectiveness reviews or training.", body, "contact.html", crumbs=[("Home", "index.html"), ("Book a consultation", "contact.html")])


def credits():
    rows = "".join(
        f'<tr><td><img src="img/{k}.jpg" alt="" width="120" height="80" loading="lazy"></td><td>{html.escape(by)}</td><td><a href="https://unsplash.com/photos/{slug}">unsplash.com/photos/{slug}</a></td></tr>'
        for k, (by, slug) in PHOTOS.items()
    )
    body = "\n".join([
        f"""  <section class="plain-page">
    <div class="wrap">
      <nav class="crumbs dark" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span></nav>
      <h1>Photo credits</h1>
      <p class="plain-intro">Photographs on this site are from Unsplash and used under the Unsplash License. Some are cropped and colour-graded.</p>
      <table class="credits"><thead><tr><th scope="col">Photo</th><th scope="col">Photographer</th><th scope="col">Source</th></tr></thead><tbody>{rows}</tbody></table>
    </div>
  </section>""",
    ])
    return page("credits.html", "Photo credits", "Photo credits for the AML Canada website.", body, crumbs=[("Home", "index.html"), ("Photo credits", "credits.html")])


def not_found():
    links = "".join(f'<li><a href="{s}.html">{n}{CHEV}</a></li>' for s, n in SERVICES)
    body = f"""  <section class="plain-page">
    <div class="wrap">
      <h1>Page not found</h1>
      <p class="plain-intro">The page you were looking for doesn’t exist or has moved. These might help:</p>
      <ul class="group-links not-found-links">{links}<li><a href="contact.html">Book a consultation{CHEV}</a></li></ul>
    </div>
  </section>"""
    s = page("404.html", "Page not found", "", body)
    # GitHub Pages serves this file at any missing path, so every local link must be root-relative.
    return re.sub(r'(href|src)="(?!https?:|/|#|mailto:)([^"]+)"', lambda m: f'{m.group(1)}="/{m.group(2)}"', s)


def legal_page(filename, doc):
    intro = "".join(f"<p class=\"plain-intro\">{p}</p>" for p in doc["intro"])
    body = f"""  <section class="plain-page legal">
    <div class="wrap legal-wrap">
      <nav class="crumbs dark" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span></nav>
      <h1>{doc["title"]}</h1>
      <p class="legal-meta">Effective date: {legal.EFFECTIVE} · Version {legal.VERSION}</p>
      {intro}
      <div class="legal-body">
        {legal.render(doc)}
      </div>
    </div>
  </section>"""
    return page(filename, doc["title"], "", body, crumbs=[("Home", "index.html"), (doc["title"], filename)])


def sync_homepage():
    p = SITE / "index.html"
    s = p.read_text(encoding="utf-8")
    s = re.sub(r"<!-- chrome:header -->.*?<!-- /chrome:header -->", lambda m: f"<!-- chrome:header -->\n{header('')}\n<!-- /chrome:header -->", s, flags=re.S)
    s = re.sub(r"<!-- chrome:seo -->.*?<!-- /chrome:seo -->", lambda m: f"<!-- chrome:seo -->\n{seo_head('index.html')}\n<!-- /chrome:seo -->", s, flags=re.S)
    s = re.sub(r"<!-- chrome:footer -->.*?<!-- /chrome:footer -->", lambda m: f"<!-- chrome:footer -->\n{footer()}\n<!-- /chrome:footer -->", s, flags=re.S)
    p.write_text(s, encoding="utf-8")


def write_discovery(pages):
    from datetime import date
    today = date.today().isoformat()
    order = ["index.html", "services.html"] + [f"{s}.html" for s, _ in SERVICES] + ["who-we-help.html", "how-we-work.html", "about.html", "contact.html", "privacy.html", "terms.html", "credits.html"]
    urls = "".join(f"  <url><loc>{url_for(p)}</loc><lastmod>{today}</lastmod></url>\n" for p in order if p in pages)
    (SITE / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n', encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
    lines = ["# AML Canada", "", f"> {DESCRIPTOR}. AML and anti-terrorist financing compliance consulting for businesses regulated by FINTRAC under the PCMLTFA.", "", "## Services", ""]
    lines += [f"- [{n}]({url_for(s + '.html')}): {SERVICE_SUMMARY[s]}" for s, n in SERVICES]
    lines += ["", "## About", "", f"- [Who we help]({url_for('who-we-help.html')})", f"- [How we work]({url_for('how-we-work.html')})", f"- [About AML Canada]({url_for('about.html')})", f"- [Book a consultation]({url_for('contact.html')})", "", "## Contact", "", f"- Phone: {PHONE_DISPLAY}", f"- Address: {', '.join(ADDRESS_LINES)}", "", "The information on this site is general and is not legal advice."]
    (SITE / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_credits_md():
    lines = ["# Photo credits", "", "All photos are from Unsplash under the Unsplash License. Some are cropped and colour-graded. Listed so they can be swapped for the firm's own photography later.", "", "| File | Photographer | Source |", "|---|---|---|"]
    lines += [f"| site/img/{k}.jpg | {by} | https://unsplash.com/photos/{slug} |" for k, (by, slug) in PHOTOS.items()]
    (ROOT / "CREDITS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    out = {
        "services.html": services_index(),
        "who-we-help.html": who_we_help(),
        "how-we-work.html": how_we_work(),
        "about.html": about(),
        "contact.html": contact(),
        "credits.html": credits(),
        "404.html": not_found(),
        "privacy.html": legal_page("privacy.html", legal.PRIVACY),
        "terms.html": legal_page("terms.html", legal.TERMS),
    }
    for slug, name in SERVICES:
        out[f"{slug}.html"] = service_page(slug, name)
    for name, text in out.items():
        (SITE / name).write_text(text, encoding="utf-8")
    sync_homepage()
    write_discovery(set(out) | {"index.html"})
    write_credits_md()
    print("built", len(out), "pages; homepage chrome synced")
