"""Builds site-v3 from one set of shared blocks.

The homepage (site-v3/index.html) is hand-authored, but its nav, fonts, form and
footer sit between <!-- shared:NAME --> markers and are rewritten from here, so
every page carries the same mega-menu, footer and consultation form.
Every other page is generated in full.
Run: python build_v3.py
"""
import json
import re
from html import escape

from content_v3 import CHECKED, DEEP
from guides_v3 import GUIDES, PUBLISHED
from pathlib import Path

OUT = Path(__file__).parent / "site-v3"

OPERATOR = "ComplyFactor Limited"
EMAIL = "info@amlcanada.ca"
PRIVACY_EMAIL = EMAIL  # one public address for everything
UPDATED = "11 October 2026"
LASTMOD = "2026-10-11"
PHONE_DISPLAY = "+1 807-806-0444"
PHONE_TEL = "+18078060444"
ADDRESS_LINES = ["Suite 211, 320 Matheson Blvd West", "Mississauga, ON L5R 3R1", "Canada"]
POSTAL = {"@type": "PostalAddress", "streetAddress": "320 Matheson Blvd West, Suite 211", "addressLocality": "Mississauga",
          "addressRegion": "ON", "postalCode": "L5R 3R1", "addressCountry": "CA"}

# (file, name, art, short description, price label)
SERVICES = [
    ("outsourced-compliance-officer.html", "Outsourced compliance officer", "scan", "A Canadian AML compliance officer (MLRO): onboarding reviews, FINTRAC reporting, policies and risk assessments.", "US$1,500 / 10 hours"),
    ("msb-registration.html", "MSB registration", "register", "FINTRAC registration for money services businesses, foreign MSBs and virtual currency dealers.", "US$3,500"),
    ("compliance-programs.html", "Compliance programs", "programme", "14 PCMLTFA compliance program documents, based on your business.", "US$3,500"),
    ("rpaa-registration.html", "RPAA registration", "register", "Payment service provider registration with the Bank of Canada under the RPAA.", "US$3,500 + Bank fee"),
    ("rpaa-compliance-program.html", "RPAA compliance program", "programme", "Governance, risk, incident response, safeguarding and continuity frameworks for PSPs.", "US$3,500"),
    ("msb-for-sale.html", "MSB for sale", "one", "A Canadian company already registered with FINTRAC as a money services business.", "From €28,000"),
    ("incorporation-canada.html", "Company incorporation", "one", "A Canadian company, federal or Ontario, usually incorporated within a few hours to 24 hours.", "US$1,500"),
    ("apostille-notarization-canada.html", "Apostille & notarization", "review", "Notarization and apostilles for Canadian corporate documents used abroad, through a licensed Ontario notary partner.", "Quote"),
    ("canadian-address.html", "Canadian address", "address", "A Canadian business address for foreign MSBs and companies entering Canada.", "US$200 / month"),
    ("effectiveness-reviews.html", "Effectiveness reviews", "review", "The two-year review FINTRAC requires, and preparation for an examination.", "Scoped"),
    ("training.html", "Training", "training", "AML training for front-line staff, compliance teams and management.", "Scoped"),
]
SERVICE = {s[0]: s for s in SERVICES}
PICK = {f: DEEP[f]["need"] for f, *_ in SERVICES}

AUD = [
    ("msb", "Money services businesses", "Foreign exchange dealers, money transfer businesses and others that need to register with FINTRAC, stay compliant and report on time.",
     ["msb-registration.html", "compliance-programs.html", "outsourced-compliance-officer.html", "effectiveness-reviews.html"]),
    ("vc", "Virtual currency dealers", "Crypto exchanges and dealers in virtual currency, which register with FINTRAC as money services businesses and report large virtual currency transactions.",
     ["msb-registration.html", "compliance-programs.html", "outsourced-compliance-officer.html"]),
    ("psp", "Payment service providers", "Payment processors, wallets and other PSPs that register with the Bank of Canada under the RPAA, and often with FINTRAC too.",
     ["rpaa-registration.html", "rpaa-compliance-program.html", "msb-registration.html"]),
    ("foreign", "Foreign businesses entering Canada", "Companies outside Canada that serve customers in Canada and need a Canadian company, registration, a Canadian address, a compliance officer, or a registered company to acquire.",
     ["incorporation-canada.html", "canadian-address.html", "msb-registration.html", "msb-for-sale.html", "outsourced-compliance-officer.html", "apostille-notarization-canada.html"]),
    ("fintech", "Payment and fintech companies", "Start-ups and growing companies that need to understand their obligations and meet them as they scale.",
     ["compliance-programs.html", "rpaa-registration.html", "training.html"]),
    ("officers", "Compliance officers", "Compliance officers at reporting entities who need a second pair of hands, a review, or training for their teams.",
     ["outsourced-compliance-officer.html", "effectiveness-reviews.html", "training.html"]),
]

ICONS = """  <svg class="sprite" aria-hidden="true" focusable="false">
    <symbol id="i-mark" viewBox="0 0 24 24"><path d="M2 8V2h6M16 2h6v6M22 16v6h-6M8 22H2v-6" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="3.2" fill="var(--amber)"/></symbol>
    <symbol id="i-arrow" viewBox="0 0 16 16"><path d="M2.5 8h10M8.5 3.5 13 8l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol>
    <symbol id="i-down" viewBox="0 0 16 16"><path d="M8 2.5v10M3.5 8.5 8 13l4.5-4.5" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol>
    <symbol id="i-check" viewBox="0 0 16 16"><path d="m3 8.5 3.2 3L13 4.5" fill="none" stroke="currentColor" stroke-width="1.6"/></symbol>
    <symbol id="i-gap" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 5v3.6" stroke="currentColor" stroke-width="1.5"/><circle cx="8" cy="11" r=".9" fill="currentColor"/></symbol>
    <symbol id="i-plus" viewBox="0 0 16 16"><path d="M8 2.5v11M2.5 8h11" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol>
    <symbol id="i-menu" viewBox="0 0 20 20"><path d="M2 7h16M2 13h16" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol>
    <symbol id="i-close" viewBox="0 0 20 20"><path d="m4 4 12 12M16 4 4 16" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol>
    <symbol id="i-chev" viewBox="0 0 16 16"><path d="m4 6 4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6"/></symbol>
    <symbol id="i-chev-r" viewBox="0 0 16 16"><path d="m6 4 4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.5"/></symbol>
    <symbol id="i-out" viewBox="0 0 16 16"><path d="M5 11 11 5M6 5h5v5" fill="none" stroke="currentColor" stroke-width="1.6"/></symbol>
  </svg>"""


def arrow():
    return '<svg aria-hidden="true"><use href="#i-arrow"/></svg>'


FONTS = """  <link rel="preload" href="fonts/geist-latin-wght.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/geist-mono-latin-wght.woff2" as="font" type="font/woff2" crossorigin>"""


SITE = "https://amlcanada.ca/"
ORG_ID = SITE + "#organization"

# JSON-LD. Organization and WebSite live on the homepage only; every other page
# points at the organization by @id. Breadcrumb names match the visible crumbs.
SCHEMA_SERVICES = {f: (d["name"], d["service_type"], d["desc"], d["offers"]) for f, d in DEEP.items()}
SCHEMA_CRUMBS = {
    "services.html": "Services", "pricing.html": "Pricing", "guides.html": "Guides", "who-we-help.html": "Who we help", "how-we-work.html": "How we work",
    "about.html": "About", "contact.html": "Book a consultation",
    "privacy.html": "Privacy policy", "terms.html": "Terms of use",
}


def jsonld(path):
    if path in ("", "index.html"):
        graph = [{
            "@type": "Organization", "@id": ORG_ID, "name": "AML Canada", "legalName": OPERATOR,
            "url": SITE,
            "logo": {"@type": "ImageObject", "@id": SITE + "#logo", "url": SITE + "icon-512.png", "contentUrl": SITE + "icon-512.png", "width": 512, "height": 512},
            "image": SITE + "og-default.png",
            "description": "AML and regulatory compliance services in Canada: FINTRAC registration, compliance programs, effectiveness reviews and training.",
            "email": EMAIL, "telephone": PHONE_TEL, "address": POSTAL,
            "areaServed": {"@type": "Country", "name": "Canada"},
            "contactPoint": {"@type": "ContactPoint", "contactType": "customer service", "email": EMAIL, "telephone": PHONE_TEL, "areaServed": "CA"},
        }, {
            "@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "AML Canada",
            "inLanguage": "en-CA", "publisher": {"@id": ORG_ID},
        }]
    else:
        url = SITE + path
        trail = [("Home", SITE)]
        graph = []
        if path in SCHEMA_SERVICES:
            name, stype, desc, offers = SCHEMA_SERVICES[path]
            trail += [("Services", SITE + "services.html"), (name, url)]
            svc = {"@type": "Service", "@id": url + "#service", "name": name, "serviceType": stype,
                   "description": desc, "url": url, "provider": {"@id": ORG_ID},
                   "areaServed": {"@type": "Country", "name": "Canada"}}
            if offers:
                svc["offers"] = [{"@type": "Offer", "price": pr, "priceCurrency": cur, "description": od, "url": url}
                                 for pr, cur, od in offers]
            graph.append(svc)
        elif path in GUIDES:
            g = GUIDES[path]
            trail += [("Guides", SITE + "guides.html"), (g["crumb"], url)]
            graph.append({"@type": "Article", "@id": url + "#article", "headline": g["h1"], "description": g["desc"],
                          "url": url, "mainEntityOfPage": url, "image": SITE + "og-default.png", "inLanguage": "en-CA",
                          "datePublished": g.get("date", PUBLISHED), "dateModified": max(g.get("modified", g.get("date", PUBLISHED)), LASTMOD),
                          "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID},
                          "about": {"@id": SITE + g["service"] + "#service"} if g["service"] in SCHEMA_SERVICES else None})
            if graph[-1]["about"] is None:
                del graph[-1]["about"]
        elif path in SCHEMA_CRUMBS:
            trail.append((SCHEMA_CRUMBS[path], url))
        else:
            return ""
        graph.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i, "name": n, "item": u} for i, (n, u) in enumerate(trail, 1)]})
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    data = data.replace("</", "<\\/")
    return f'\n  <script type="application/ld+json">{data}</script>'


SOCIAL = """  <meta property="og:image" content="https://amlcanada.ca/og-default.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="AML Canada: AML compliance for businesses FINTRAC regulates">
  <meta name="twitter:card" content="summary_large_image">"""
ICON_LINKS = """  <link rel="icon" href="favicon.ico" sizes="48x48">
  <link rel="icon" href="icon-96.png" type="image/png" sizes="96x96">
  <link rel="icon" href="icon-192.png" type="image/png" sizes="192x192">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">"""


def og_article(path):
    """article:modified_time for a guide: its own date when that is newer than the site-wide LASTMOD."""
    modified = max(GUIDES[path].get("modified", GUIDES[path].get("date", PUBLISHED)), LASTMOD)
    return f'\n  <meta property="article:modified_time" content="{modified}">'


def head(title, desc, path, robots=""):
    return f"""<!doctype html>
<html lang="en-CA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(desc)}">
  <link rel="canonical" href="https://amlcanada.ca/{path}">{robots}
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(desc)}">
  <meta property="og:type" content="{'article' if path in GUIDES else 'website'}">{og_article(path) if path in GUIDES else ''}
  <meta property="og:url" content="https://amlcanada.ca/{path}">
  <meta property="og:site_name" content="AML Canada">
  <meta property="og:locale" content="en_CA">
{SOCIAL}
  <meta name="theme-color" content="#06080C">
{FONTS}
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="pages.css">
{ICON_LINKS}
  <script>document.documentElement.classList.add("js");</script>{jsonld(path)}
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

{ICONS}
"""


# ---------------------------------------------------------------- mega-menu
def mega_group(key, label, items, current_set):
    """items: (href, title, desc). The preview shows the hovered item."""
    first = items[0]
    links = "\n".join(
        f'              <li><a class="mega-link" href="{h}" data-title="{escape(t)}" data-desc="{escape(d)}">{t}<svg aria-hidden="true"><use href="#i-chev-r"/></svg></a></li>'
        for h, t, d in items
    )
    cur = ' data-current' if current_set else ""
    return f"""        <li class="mega-item"{cur}>
          <button class="mega-trigger" type="button" aria-expanded="false" aria-controls="mega-{key}" data-mega-trigger>{label}<svg aria-hidden="true"><use href="#i-chev"/></svg></button>
          <div class="mega-panel" id="mega-{key}" hidden data-mega-panel>
            <ul class="mega-list">
{links}
            </ul>
            <div class="mega-preview" aria-hidden="true">
              <p class="mega-title" data-mega-title>{escape(first[1])}</p>
              <p class="mega-desc" data-mega-desc>{escape(first[2])}</p>
              <a class="mega-more" href="{first[0]}" tabindex="-1" data-mega-more>Read more<svg><use href="#i-out"/></svg></a>
            </div>
          </div>
        </li>"""


# ---------------------------------------------------------------- clients (shown with their consent)
CLIENTS = [("relm", "Relm", 147, 60, 40), ("radom", "Radom", 120, 32, 30), ("mosta", "Mosta", 125, 30, 28), ("hercle", "Hercle", 92, 21, 30)]


def clients_block():
    logos = "\n".join(f'          <li><img src="clients/{f}.svg" alt="{n}" width="{round(w * h2 / h)}" height="{h2}" loading="lazy" decoding="async"></li>'
                      for f, n, w, h, h2 in CLIENTS)
    return f"""    <section class="clients" data-theme="light" aria-labelledby="clients-title">
      <div class="wrap clients-inner">
        <h2 class="clients-h" id="clients-title">Clients served by our team</h2>
        <ul class="clients-row">
{logos}
        </ul>
      </div>
    </section>
"""


def nav(current):
    svc_items = [("services.html", "All services", "FINTRAC and Bank of Canada registration, compliance programs, outsourced compliance officers, reviews and training.")] + \
                [(h, t, d) for h, t, _, d, _ in SERVICES]
    aud_items = [(f"who-we-help.html#{k}", t, d) for k, t, d, _ in AUD]
    in_svc = current in ("services.html", *SERVICE)
    plain = lambda h, t: f'        <li><a class="mega-plain" href="{h}"{" aria-current=\"page\"" if current == h else ""}>{t}</a></li>'
    menu_links = [("./", "Home"), ("services.html", "Services"), ("who-we-help.html", "Who we help"),
                  ("how-we-work.html", "How we work"), ("pricing.html", "Pricing"), ("guides.html", "Guides"), ("about.html", "About"), ("contact.html", "Book a consultation")]
    mlinks = "\n".join(f'      <a href="{h}" data-menu-link{" aria-current=\"page\"" if h == current or (h == "./" and current == "index.html") else ""}>{t}</a>' for h, t in menu_links)
    return f"""  <header class="nav" data-nav>
    <div class="nav-pill">
      <a class="brand" href="./" aria-label="AML Canada home">
        <svg class="brand-mark" aria-hidden="true"><use href="#i-mark"/></svg>
        <span>AML Canada</span>
      </a>
      <nav class="mega" aria-label="Main" data-mega>
        <ul class="mega-bar">
{mega_group("services", "Services", svc_items, in_svc)}
{mega_group("who", "Who we help", aud_items, current == "who-we-help.html")}
{plain("how-we-work.html", "How we work")}
{plain("pricing.html", "Pricing")}
{plain("guides.html", "Guides")}
{plain("about.html", "About")}
        </ul>
      </nav>
      <div class="nav-end">
        <a class="nbtn nbtn-amber" href="contact.html"><span>Book a</span><span>consultation</span></a>
        <a class="nbtn nbtn-white" href="./#checker"><span>Gap</span><span>check</span></a>
        <a class="nbtn nbtn-grey" href="mailto:{EMAIL}"><span>Contact</span><span>us</span></a>
        <button class="nav-menu" type="button" aria-expanded="false" aria-controls="menu" data-menu-open>
          <svg aria-hidden="true"><use href="#i-menu"/></svg>
          <span class="sr">Menu</span>
        </button>
      </div>
    </div>
  </header>

  <div class="menu" id="menu" role="dialog" aria-modal="true" aria-label="Menu" hidden data-menu>
    <div class="menu-top">
      <a class="brand" href="./">
        <svg class="brand-mark" aria-hidden="true"><use href="#i-mark"/></svg>
        <span>AML Canada</span>
      </a>
      <button class="nav-menu" type="button" data-menu-close>
        <svg aria-hidden="true"><use href="#i-close"/></svg>
        <span class="sr">Close menu</span>
      </button>
    </div>
    <nav class="menu-links" aria-label="Menu">
{mlinks}
    </nav>
    <div class="menu-sub">
      {"".join(f'<a href="{h}" data-menu-link>{t}</a>' for h, t, *_ in SERVICES)}
    </div>
    <p class="menu-note"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
"""


# ---------------------------------------------------------------- form
FORM = f"""        <form class="form" novalidate data-consult>
          <input type="hidden" name="subject" value="New consultation request from amlcanada.ca">
          <input type="hidden" name="from_name" value="AML Canada website">
          <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
          <fieldset class="field">
            <legend class="field-label">I need help with</legend>
            <div class="chips" data-need>
              <label class="chip"><input type="radio" name="need" value="officer"><span>A compliance officer</span></label>
              <label class="chip"><input type="radio" name="need" value="incorporate"><span>Incorporating a company</span></label>
              <label class="chip"><input type="radio" name="need" value="register"><span>Registering an MSB</span></label>
              <label class="chip"><input type="radio" name="need" value="address"><span>Setting up from abroad</span></label>
              <label class="chip"><input type="radio" name="need" value="programme"><span>A compliance program</span></label>
              <label class="chip"><input type="radio" name="need" value="rpaa"><span>Bank of Canada RPAA</span></label>
              <label class="chip"><input type="radio" name="need" value="acquire"><span>Buying an MSB</span></label>
              <label class="chip"><input type="radio" name="need" value="review"><span>A review or examination</span></label>
              <label class="chip"><input type="radio" name="need" value="training"><span>Staff training</span></label>
              <label class="chip"><input type="radio" name="need" value="apostille"><span>Apostille or notarization</span></label>
              <label class="chip"><input type="radio" name="need" value="unsure" checked><span>Not sure yet</span></label>
            </div>
          </fieldset>
          <div class="form-row">
            <div class="field">
              <label class="field-label" for="f-name">Name</label>
              <input class="input" id="f-name" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label class="field-label" for="f-email">Work email</label>
              <input class="input" id="f-email" name="email" type="email" autocomplete="email" required>
            </div>
          </div>
          <div class="field">
            <label class="field-label" for="f-company">Company</label>
            <input class="input" id="f-company" name="company" autocomplete="organization" required>
          </div>
          <div class="field">
            <label class="field-label" for="f-notes">Anything we should know? <span class="opt">Optional</span></label>
            <textarea class="input" id="f-notes" name="notes" rows="4" data-notes></textarea>
          </div>
          <button class="btn btn-ink btn-block" type="submit">Book a consultation {arrow()}</button>
          <p class="form-legal">We use your details only to reply to this request. See our <a href="privacy.html">privacy policy</a>.</p>
          <p class="form-msg" role="status" data-msg></p>
        </form>
"""


# ---------------------------------------------------------------- footer
def footer():
    svc = "\n".join(f'        <a href="{h}">{t}</a>' for h, t, *_ in SERVICES)
    return f"""  <footer class="footer" data-theme="dark">
    <div class="wrap footer-grid">
      <div class="footer-brand">
        <a class="brand" href="./">
          <svg class="brand-mark" aria-hidden="true"><use href="#i-mark"/></svg>
          <span>AML Canada</span>
        </a>
        <p>AML &amp; Regulatory Compliance Services in Canada. A private consultancy, not affiliated with FINTRAC or the Bank of Canada.</p>
      </div>
      <nav class="footer-col" aria-label="Services">
        <p class="footer-h">Services</p>
{svc}
      </nav>
      <nav class="footer-col" aria-label="Company">
        <p class="footer-h">Company</p>
        <a href="who-we-help.html">Who we help</a>
        <a href="how-we-work.html">How we work</a>
        <a href="pricing.html">Pricing</a>
        <a href="guides.html">Guides</a>
        <a href="about.html">About</a>
        <a href="contact.html">Book a consultation</a>
      </nav>
      <div class="footer-col">
        <p class="footer-h">Reach us</p>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <address>{"<br>".join(ADDRESS_LINES[:2])}</address>
      </div>
    </div>
    <div class="wrap footer-base">
      <p>© <span data-year>2026</span> {OPERATOR}. AML Canada is operated by {OPERATOR}.</p>
      <p class="footer-legal"><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><button type="button" class="footer-cookie" data-consent-open hidden>Cookie choices</button></p>
    </div>
    <div class="wrap footer-note"><p>The information on this site is general and is not legal advice.</p></div>
  </footer>

  <div class="consent" role="region" aria-label="Cookie choices" hidden data-consent>
    <p>We'd like to use Google Analytics cookies to understand how this site is used. They load only if you accept. <a href="privacy.html#cookies">How we use data</a></p>
    <div class="consent-actions">
      <button class="nbtn nbtn-grey" type="button" data-consent-no><span>Decline</span></button>
      <button class="nbtn nbtn-amber" type="button" data-consent-yes><span>Accept</span></button>
    </div>
  </div>

  <script src="site-config.js" defer></script>
  <script src="main.js" defer></script>
"""


def page_hero(crumbs, title, lede, label, flag=False, actions=True, need="", price="", kicker=""):
    crumb_html = "".join(f'<a href="{h}">{t}</a><span aria-hidden="true">/</span>' for h, t in crumbs)
    act = f"""
          <div class="hero-actions">
            <a class="btn btn-amber" href="contact.html{'?need=' + need if need else ''}">Book a consultation {arrow()}</a>
            <a class="link-dark" href="#start">Read on</a>{f'{chr(10)}            <span class="hero-price">{price}</span>' if price else ""}
          </div>""" if actions else ""
    # With a kicker, the keyword phrase is the H1 and the display tagline becomes a styled paragraph.
    head_html = (f'<h1 id="page-title" class="hero-kicker">{kicker}</h1>\n        <p class="page-headline">{lede[0]}</p>'
                 if kicker else f'<h1 id="page-title">{lede[0]}</h1>')
    return f"""    <section class="page-hero" data-theme="dark" aria-labelledby="page-title">
      <canvas class="page-canvas" aria-hidden="true" data-page-canvas data-label="{escape(label)}"{' data-flag' if flag else ''}></canvas>
      <div class="page-boxes" aria-hidden="true" data-page-boxes></div>
      <div class="page-shade" aria-hidden="true"></div>
      <div class="wrap page-hero-inner">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="./">Home</a><span aria-hidden="true">/</span>{crumb_html}<span aria-current="page">{escape(title)}</span></nav>
        {head_html}
        <p class="page-lede">{lede[1]}</p>{act}
      </div>
    </section>
"""


def close_and_footer(close_title="Tell us what you need help&nbsp;with.", need=""):
    return f"""    <section class="close" data-theme="dark" aria-labelledby="close-title">
      <canvas class="close-canvas" aria-hidden="true" data-close-canvas></canvas>
      <div class="wrap close-inner">
        <h2 id="close-title">{close_title}</h2>
        <a class="btn btn-amber" href="contact.html{'?need=' + need if need else ''}">Book a consultation {arrow()}</a>
      </div>
    </section>
  </main>

{footer()}</body>
</html>
"""


def intro(lead, body):
    paras = "\n".join(f"          <p>{p}</p>" for p in body)
    return f"""    <section class="intro" id="start" data-theme="light">
      <div class="wrap intro-grid">
        <p class="intro-lead" data-reveal>{lead}</p>
        <div class="intro-body" data-reveal>
{paras}
        </div>
      </div>
    </section>
"""


def who_for(title, items, arts):
    cards = "\n".join(
        f"""          <article class="card card-plain" data-reveal>
            <div class="card-art" aria-hidden="true" data-art="{a}"></div>
            <h3>{t}</h3>
            <p>{d}</p>
          </article>""" for (t, d), a in zip(items, arts)
    )
    return f"""    <section class="for" data-theme="light" aria-labelledby="for-title">
      <div class="wrap">
        <h2 id="for-title">{title}</h2>
        <div class="cards">
{cards}
        </div>
      </div>
    </section>
"""


def what_we_do(items, title="What we do"):
    rows = "\n".join(
        f"""          <li class="work-row" data-reveal>
            <span class="work-idx">{i:02d}</span>
            <h3>{t}</h3>
            <p>{d}</p>
          </li>""" for i, (t, d) in enumerate(items, 1)
    )
    return f"""    <section class="work" data-theme="light" aria-labelledby="work-title">
      <div class="wrap">
        <div class="work-head">
          <h2 id="work-title">{title}</h2>
          <p>Set out in a written scope that you agree first.</p>
        </div>
        <ol class="work-list">
{rows}
        </ol>
      </div>
    </section>
"""


def related(keys):
    cards = "\n".join(
        f"""          <a class="rel" href="{h}" data-reveal>
            <div class="rel-art" aria-hidden="true" data-art="{a}"></div>
            <div class="rel-body">
              <h3>{t}</h3>
              <p>{d}</p>
              <span class="link-ink">Read more {arrow()}</span>
            </div>
          </a>""" for h, t, a, d, _ in (SERVICE[k] for k in keys)
    )
    return f"""    <section class="related" data-theme="light" aria-labelledby="related-title">
      <div class="wrap">
        <h2 id="related-title">Often paired with</h2>
        <div class="rel-grid">
{cards}
        </div>
      </div>
    </section>
"""


def fee_band(fee, need):
    items = "\n".join(f'            <li>{i}</li>' for i in fee["items"])
    return f"""    <section class="fee" data-theme="light" aria-labelledby="fee-title">
      <div class="wrap">
        <div class="fee-card" data-theme="dark" data-reveal>
          <div class="fee-main">
            <h2 class="fee-label" id="fee-title">Fee</h2>
            <p class="fee-amount">{fee["amount"]}</p>
            <p class="fee-unit">{fee["unit"]}</p>
            <p class="fee-note">{fee["note"]}</p>
            <a class="btn btn-amber" href="contact.html?need={need}">Book a consultation {arrow()}</a>
          </div>
          <div class="fee-incl">
            <p class="fee-label">Included</p>
            <ul class="fee-list">
{items}
            </ul>
          </div>
        </div>
      </div>
    </section>
"""


def facts_strip(facts):
    cells = "\n".join(f"""          <div class="fact" data-reveal>
            <dt>{k}</dt>
            <dd><span class="fact-v">{v}</span><span class="fact-n">{n}</span></dd>
          </div>""" for k, v, n in facts)
    return f"""    <section class="facts" data-theme="light" aria-label="Key facts">
      <div class="wrap">
        <dl class="facts-grid">
{cells}
        </dl>
      </div>
    </section>
"""


def guide(sections, sources, checked=CHECKED):
    toc = "\n".join(f'            <li><a href="#{sid}">{h}</a></li>' for sid, h, _ in sections)
    body = "\n".join(f"""          <section id="{sid}" class="legal-sec guide-sec">
            <h2>{h}</h2>
{html}
          </section>""" for sid, h, html in sections)
    src = "; ".join(f'<a href="{u}" rel="noopener">{t}</a>' for t, u in sources)
    return f"""    <section class="guide" data-theme="light" aria-label="Guide">
      <div class="wrap legal-grid">
        <nav class="legal-toc" aria-label="On this page">
          <p class="legal-toc-h">On this page</p>
          <ol>
{toc}
          </ol>
        </nav>
        <article class="legal-body guide-body">
{body}
          <p class="sources">Sources: {src}. Checked {checked}. General information, not legal advice.</p>
        </article>
      </div>
    </section>
"""


def faq_schema(faqs):
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": re.sub(r"<[^>]+>", "", q),
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in faqs]}
    out = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'\n    <script type="application/ld+json">{out}</script>'


def faq_block(faqs, title="Questions"):
    items = "\n".join(f'            <details><summary>{q}<svg aria-hidden="true"><use href="#i-plus"/></svg></summary><p>{a}</p></details>'
                      for q, a in faqs)
    return f"""    <section class="faq faq-inner" data-theme="light" aria-labelledby="faq-title">
      <div class="wrap faq-grid">
        <div class="faq-head">
          <h2 id="faq-title">{title}</h2>
          <p>Still not sure? <a href="contact.html">Book a consultation</a> or write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        </div>
        <div class="faq-panel">
{items}
        </div>
      </div>
    </section>{faq_schema(faqs)}
"""


def deep_page(file):
    d = DEEP[file]
    return (head(d["title"], d["desc"], file) + nav(file) + '  <main id="main">\n'
            + page_hero([("services.html", "Services")], d["name"], (d["h1"], d["lede"]), d["label"], d.get("flag", False),
                        need=d["need"], price=d["hero_price"], kicker=d.get("kicker", ""))
            + intro(*d["intro"])
            + fee_band(d["fee"], d["need"])
            + facts_strip(d["facts"])
            + guide(d["guide"], d["sources"], d.get("checked", CHECKED))
            + who_for(d["for_title"], d["for_items"], d["arts"])
            + faq_block(d["faqs"], f'{d["name"]}: questions')
            + (guide_cards(gs, "Guides on this") if (gs := [f for f, g in GUIDES.items() if file in (g["service"], *g.get("also", ()))][:3]) else "")
            + related(d["related"])
            + close_and_footer(need=d["need"]))


PAGES = {}


# Services index
svc_cards = "\n".join(
    f"""          <a class="svc" href="{h}" data-reveal>
            <div class="svc-art" aria-hidden="true" data-art="{a}"></div>
            <div class="svc-body">
              <h3>{t}</h3>
              <p>{d}</p>
              <span class="svc-price">{pr}</span>
            </div>
            <span class="svc-go" aria-hidden="true">{arrow()}</span>
          </a>""" for h, t, a, d, pr in SERVICES
)
PAGES["services.html"] = (
    head("AML & FINTRAC Compliance Services in Canada | AML Canada",
         "FINTRAC MSB registration, PCMLTFA compliance programs, outsourced compliance officers, Bank of Canada RPAA registration and MSBs for sale, with clear fees.",
         "services.html")
    + nav("services.html") + '  <main id="main">\n'
    + page_hero([], "Services", ("FINTRAC and Bank of Canada compliance, from registration to review.",
                f"{len(SERVICES)} services for money services businesses, payment service providers and fintechs, most at a fixed fee."), f"Services · {len(SERVICES)}")
    + intro("From your first registration to your next examination, we help you meet your obligations and show that you have.",
            ["Most services have a fixed fee, shown below and on our <a href=\"pricing.html\">pricing page</a>. Effectiveness reviews and training are scoped to your business.",
             "Most clients start with the one they need most and add others later."])
    + f"""    <section class="svc-list" data-theme="light" aria-labelledby="svc-title">
      <div class="wrap">
        <h2 id="svc-title" class="sr">All services</h2>
        <div class="svc-grid">
{svc_cards}
        </div>
      </div>
    </section>
"""
    + clients_block()
    + what_we_do([("Consultation", "A conversation about your business, your timeline and what's required of you."),
                  ("Written scope", "What you're getting and what it costs, in writing."),
                  ("Delivery", "We do the work with you and explain the decisions along the way."),
                  ("Ongoing support", "Updates to your program when you launch a product, enter a market or change how you operate.")], "How the work runs")
    + close_and_footer()
)

# Pricing
price_rows = "\n".join(
    f"""            <tr>
              <th scope="row"><a href="{h}">{t}</a></th>
              <td class="pr-amount">{DEEP[h]["fee"]["amount"]}</td>
              <td>{DEEP[h]["fee"]["unit"]}</td>
              <td>{d}</td>
              <td>{DEEP[h].get("timing", "Scoped to your business")}</td>
            </tr>""" for h, t, a, d, pr in SERVICES
)
PAGES["pricing.html"] = (
    head("AML Compliance Pricing: FINTRAC & RPAA Fees | AML Canada",
         "Fixed fees: incorporation US$1,500, FINTRAC MSB registration US$3,500, PCMLTFA program US$3,500, RPAA registration US$3,500, compliance officer US$1,500/10h.",
         "pricing.html")
    + nav("pricing.html") + '  <main id="main">\n'
    + page_hero([], "Pricing", ("Clear fees, agreed in writing.",
                "Most of our services have a fixed fee. Here's what each one costs and what it covers."), "Fees · Fixed")
    + f"""    <section class="pricing" id="start" data-theme="light" aria-labelledby="pricing-title">
      <div class="wrap">
        <div class="work-head">
          <h2 id="pricing-title">What each service costs</h2>
          <p>Fees are in US dollars unless shown otherwise. Government fees are separate and paid directly to the regulator.</p>
        </div>
        <div class="table-wrap">
          <table class="price-table">
            <thead><tr><th scope="col">Service</th><th scope="col">Fee</th><th scope="col">Basis</th><th scope="col">What it covers</th><th scope="col">Typical timing</th></tr></thead>
            <tbody>
{price_rows}
            </tbody>
          </table>
        </div>
        <p class="price-timing-note">Timings are general guides from our experience, not guarantees. Registration decisions are made by FINTRAC and the Bank of Canada and depend on how complete an application is and on their workload.</p>
        <ul class="price-notes">
          <li><strong>FINTRAC</strong> doesn't charge a fee to register a money services business.</li>
          <li><strong>Incorporation</strong> government fees are separate: currently CA$200 federally online, or CA$300 in Ontario online.</li>
          <li><strong>The Bank of Canada</strong> charges RPAA applicants a one-time, non-refundable application fee, paid directly to the Bank. It was CA$2,500 when introduced in November 2024 and is indexed to inflation each January, so we confirm the current amount before you apply. The Bank will also charge registered PSPs annual assessment fees once its cost-recovery regulations are final.</li>
          <li><strong>Every engagement</strong> starts with a consultation and a written scope, so you know the fee before any work begins.</li>
        </ul>
      </div>
    </section>
"""
    + faq_block([
        ("How much does FINTRAC MSB registration cost?", "FINTRAC charges no registration fee. Our fee to prepare and support your registration is a fixed US$3,500."),
        ("How much does an AML compliance program cost?", "A fixed US$3,500 for 14 PCMLTFA compliance program documents."),
        ("How much does an outsourced compliance officer cost?", "US$1,500 per block of 10 hours, with hours that scale as your business grows."),
        ("How much does RPAA registration cost?", "Our fee is a fixed US$3,500, plus the Bank of Canada's one-time application fee (CA$2,500 when introduced, indexed to inflation each year), paid to the Bank. The RPAA compliance program is a further US$3,500."),
        ("How much does a registered MSB cost to buy?", "Acquisitions start from €28,000, depending on the company."),
        ("How much does it cost to incorporate a company in Canada?", "Our fee is a fixed US$1,500, usually done within a few hours to 24 hours. Government filing fees are separate."),
        ("How long do registrations take?", "FINTRAC says most complete MSB applications are processed within three months. In our experience, it has taken about 1 week to 7 months, and Bank of Canada RPAA registration about 2 to 8 months. Incorporation usually takes a few hours to 24 hours."),
        ("Why are fees in US dollars?", "Our fees are quoted in US dollars, except MSB acquisitions, which are in euros. The Bank of Canada's own fee is in Canadian dollars."),
    ], "Pricing questions")
    + close_and_footer()
)

# Who we help
aud_rows = "\n".join(
    f"""          <li class="aud" id="{k}" data-reveal>
            <h3>{t}</h3>
            <p>{d}</p>
            <div class="aud-svc">
              <span class="aud-label">Services that usually help</span>
              <div class="aud-chips">{"".join(f'<a class="aud-chip" href="{k}">{SERVICE[k][1]}</a>' for k in ks)}</div>
            </div>
          </li>""" for k, t, d, ks in AUD
)
PAGES["who-we-help.html"] = (
    head("AML Compliance for MSBs, Crypto, PSPs and Fintech | AML Canada", "AML compliance help for money services businesses, crypto dealers, payment service providers, foreign businesses entering Canada and compliance officers.", "who-we-help.html")
    + nav("who-we-help.html") + '  <main id="main">\n'
    + page_hero([], "Who we help", ("Businesses FINTRAC and the Bank of Canada regulate, at every stage.",
                "From first registration to the next examination."), "Client · ID verified")
    + f"""    <section class="audiences" id="start" data-theme="light" aria-labelledby="aud-title">
      <div class="wrap">
        <div class="work-head">
          <h2 id="aud-title">Find yourself here.</h2>
          <p>Six kinds of business we work with, and the services that usually help them first.</p>
        </div>
        <ol class="aud-list">
{aud_rows}
        </ol>
      </div>
    </section>
"""
    + close_and_footer()
)

# How we work: reuses the pinned checkpoint corridor
STEPS = [
    ("Consultation", "We start with a conversation.", "About your business, your timeline and what's required of you. You leave it with a clear next step.",
     ["Your business model and the services you offer", "Your deadlines, such as a launch or an examination", "What you already have in place"]),
    ("Scope", "We write down what we'll do.", "What we'll do, what we need from you, and when. Nothing starts until you've agreed it.",
     ["The work, in plain language", "What we need from you, and when", "Timeline and milestones"]),
    ("Delivery", "We do the work with you.", "We explain each decision as we go, so your team can stand behind it.",
     ["Regular check-ins", "Drafts you can comment on", "The reasons behind each decision, in writing"]),
    ("Ongoing support", "We stay for what comes next.", "Your obligations change as your business does: the next product, the next market or the next review.",
     ["Updates when your business changes", "Help with questions from FINTRAC", "Your next effectiveness review"]),
]
tabs = "\n".join(
    f'            <button role="tab" id="gt-{i}" aria-controls="gp-{i}" aria-selected="{"true" if i == 0 else "false"}"{"" if i == 0 else " tabindex=\"-1\""} type="button">{n}</button>'
    for i, (n, *_ ) in enumerate(STEPS)
)
panels = "\n".join(
    f"""            <div class="gate-panel" role="tabpanel" id="gp-{i}" aria-labelledby="gt-{i}"{"" if i == 0 else " hidden"}>
              <h3>{h}</h3>
              <div>
                <p>{d}</p>
                <ul class="gate-list">{"".join(f"<li>{x}</li>" for x in items)}</ul>
              </div>
            </div>""" for i, (n, h, d, items) in enumerate(STEPS)
)
PAGES["how-we-work.html"] = (
    head("How Our AML Compliance Engagements Work | AML Canada", "Every AML Canada engagement starts with a consultation and a written scope, with the fee agreed before any work begins, then delivery and ongoing support.", "how-we-work.html")
    + nav("how-we-work.html") + '  <main id="main">\n'
    + page_hero([], "How we work", ("Every engagement starts with a conversation and a written scope.",
                "Compliance work goes better when you know what's happening and why."), "Scope · Agreed")
    + intro("We keep engagements simple: a conversation, a written scope, the work itself, and support afterwards.",
            ["You agree the scope and the fee before any work begins."])
    + f"""    <section class="gates gates-steps" id="steps" data-theme="dark" data-gates aria-labelledby="gates-title">
      <div class="gates-pin">
        <div class="wrap gates-inner">
          <div class="gates-head">
            <h2 id="gates-title">Four steps, in the same order every time.</h2>
            <p>You always know which step you're in and what comes next.</p>
          </div>
          <div class="gates-tabs" role="tablist" aria-label="The four steps" data-gate-tabs>
{tabs}
          </div>
          <div class="corridor" aria-hidden="true" data-corridor></div>
          <div class="gates-panels">
{panels}
          </div>
        </div>
      </div>
    </section>
"""
    + close_and_footer()
)

# About
BELIEFS = [
    ("Clear answers", "People come to us under pressure. We tell you plainly what applies to you and what happens next."),
    ("Specific to you", "We write each program around how your business works."),
    ("Accuracy first", "We check every regulatory statement before we rely on it."),
    ("One next step", "Every conversation ends with a clear next step."),
]
beliefs = "\n".join(
    f"""          <li class="belief" data-reveal>
            <span class="work-idx">{i:02d}</span>
            <h3>{t}</h3>
            <p>{d}</p>
          </li>""" for i, (t, d) in enumerate(BELIEFS, 1)
)
PAGES["about.html"] = (
    head("About AML Canada | Operated by ComplyFactor Limited", "AML Canada is an AML and FINTRAC compliance consultancy operated by ComplyFactor Limited, for MSBs, crypto dealers, payment service providers and fintechs.", "about.html")
    + nav("about.html") + '  <main id="main">\n'
    + page_hero([], "About", ("Making FINTRAC obligations clear and manageable.",
                "AML and anti-terrorist financing compliance for businesses regulated by FINTRAC."), "AML Canada")
    + intro("AML Canada helps businesses register with FINTRAC, build compliance programs that work, prepare for examinations and train their people.",
            ["AML Canada is operated by ComplyFactor Limited. We provide anti-money laundering (AML) and anti-terrorist financing compliance services to businesses regulated by FINTRAC, Canada's financial intelligence unit, and to payment service providers supervised by the Bank of Canada under the RPAA. We're a private consultancy, not part of or affiliated with FINTRAC, the Bank of Canada or the Government of Canada.",
             "Most of our clients are busy running their business. We explain what they have to do and help them do it, from the first registration to the next review."])
    + f"""    <section class="beliefs" data-theme="dark" aria-labelledby="beliefs-title">
      <div class="wrap">
        <h2 id="beliefs-title">What we believe</h2>
        <ol class="belief-grid">
{beliefs}
        </ol>
      </div>
    </section>
"""
    + close_and_footer()
)

# Contact: the consultation form, standalone
PAGES["contact.html"] = (
    head("Book an AML Compliance Consultation | AML Canada", "Tell us about your business and what FINTRAC or the Bank of Canada requires of it. We reply to find a time, then send a written scope before any work starts.", "contact.html")
    + nav("contact.html") + '  <main id="main">\n'
    + page_hero([], "Book a consultation", ("Tell us where you are.",
                "Tell us about your business and what you need, and we'll come back to you to find a time."), "Consultation · Requested", actions=False)
    + """    <section class="consult consult-page" id="consult" data-theme="light" aria-labelledby="consult-title">
      <div class="wrap consult-grid">
        <div class="consult-copy">
          <h2 id="consult-title">What happens next</h2>
          <ol class="steps">
            <li><span class="step-name">Consultation</span><span>How FINTRAC's requirements apply to your business, what your program needs and what you already have.</span></li>
            <li><span class="step-name">Written scope</span><span>The work, who does which part, and a timeline you agree to.</span></li>
            <li><span class="step-name">Delivery</span><span>We do the work with you and explain decisions along the way.</span></li>
            <li><span class="step-name">Ongoing support</span><span>Updates when your business, products or obligations change.</span></li>
          </ol>
          <div class="direct">
            <p class="direct-h">Or reach us directly</p>
            <p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
            <address>{ADDR}</address>
          </div>
        </div>
""".replace("{EMAIL}", EMAIL).replace("{PHONE_TEL}", PHONE_TEL).replace("{PHONE_DISPLAY}", PHONE_DISPLAY).replace("{ADDR}", "<br>".join(ADDRESS_LINES))
    + "{{FORM}}"
    + """      </div>
    </section>
"""
    + clients_block()
    + close_and_footer()
)




# ---------------------------------------------------------------- guides (articles)
def read_minutes(g):
    words = len(re.sub(r"<[^>]+>", " ", " ".join(h for _, _, h in g["sections"])).split())
    return max(1, round(words / 220))


def takeaways_box(items):
    lis = "\n".join(f"            <li>{t}</li>" for t in items)
    return f"""    <section class="takeaways" id="start" data-theme="light" aria-labelledby="tk-title">
      <div class="wrap">
        <div class="tk-card">
          <h2 class="fee-label" id="tk-title">Key points</h2>
          <ul class="tk-list">
{lis}
          </ul>
        </div>
      </div>
    </section>
"""


def service_cta(file):
    if file == "pricing.html":
        name, desc, price = "Pricing", "Fixed fees for registration, compliance programs, RPAA and outsourced compliance officers.", "See all fees"
    else:
        _, name, _, desc, price = SERVICE[file]
    return f"""    <section class="gcta" data-theme="light" aria-label="Related service">
      <div class="wrap">
        <a class="gcta-card" href="{file}" data-theme="dark">
          <span class="fee-label">Need a hand with this?</span>
          <span class="gcta-name">{name}</span>
          <span class="gcta-desc">{desc}</span>
          <span class="gcta-price">{price}</span>
          <span class="gcta-go" aria-hidden="true">{arrow()}</span>
        </a>
      </div>
    </section>
"""


def guide_cards(files, title="More guides"):
    cards = "\n".join(f"""          <a class="gcard" href="{f}" data-reveal>
            <span class="gcard-tag">{GUIDES[f]["label"].split("·")[-1].strip()}</span>
            <h3>{GUIDES[f]["h1"]}</h3>
            <p>{GUIDES[f]["lede"]}</p>
            <span class="link-ink">Read the guide {arrow()}</span>
          </a>""" for f in files)
    return f"""    <section class="guides-more" data-theme="light" aria-labelledby="gm-title">
      <div class="wrap">
        <h2 id="gm-title">{title}</h2>
        <div class="gcard-grid">
{cards}
        </div>
      </div>
    </section>
"""


def nice_date(iso):
    y, m, d = iso.split("-")
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return f"{int(d)} {months[int(m) - 1]} {y}"


def guide_page(file):
    g = GUIDES[file]
    kind = "Update" if g.get("kind") == "update" else "Guide"
    meta = f'{kind} · {"Published " + nice_date(g["date"]) if g.get("date") else "Updated " + (nice_date(g["modified"]) if g.get("modified") else UPDATED)} · {read_minutes(g)} min read · AML Canada'
    hero = page_hero([("guides.html", "Guides")], g["crumb"], (g["h1"], g["lede"]), g["label"], actions=False)
    hero = hero.replace('<p class="page-lede">', f'<p class="guide-meta">{meta}</p>\n        <p class="page-lede">', 1)
    return (head(g["title"], g["desc"], file) + nav(file) + '  <main id="main">\n'
            + hero
            + takeaways_box(g["takeaways"])
            + guide(g["sections"], g["sources"], g.get("checked", CHECKED))
            + service_cta(g["service"])
            + faq_block(g["faqs"], f'{g["crumb"]}: common questions')
            + guide_cards(g["related"])
            + close_and_footer(need=DEEP[g["service"]]["need"] if g["service"] in DEEP else ""))


for _f in GUIDES:
    PAGES[_f] = guide_page(_f)
for _f in DEEP:  # after the guide helpers, so service pages can list their guides
    PAGES[_f] = deep_page(_f)

PAGES["guides.html"] = (
    head("AML Compliance Guides for Canada: FINTRAC & RPAA | AML Canada",
         "Plain-English guides to FINTRAC MSB registration, foreign MSBs, FINTRAC reporting, crypto registration and the Bank of Canada's RPAA, with sources.",
         "guides.html")
    + nav("guides.html") + '  <main id="main">\n'
    + page_hero([], "Guides", ("Guides to FINTRAC and RPAA compliance.",
                "Plain-English answers to the questions we hear most, checked against FINTRAC and the Bank of Canada."), f"Guides · {len(GUIDES)}", actions=False)
    + (guide_cards(sorted((f for f, g in GUIDES.items() if g.get("kind") == "update"), key=lambda f: GUIDES[f]["date"], reverse=True)[:9],
                   "Latest updates").replace('class="guides-more"', 'class="guides-more guides-index" id="start"', 1)
       if any(g.get("kind") == "update" for g in GUIDES.values()) else "")
    + guide_cards([f for f, g in GUIDES.items() if g.get("kind") != "update"], "All guides").replace(
        'class="guides-more"', 'class="guides-more guides-index" id="start"' if not any(g.get("kind") == "update" for g in GUIDES.values()) else 'class="guides-more"', 1)
    + close_and_footer()
)


# ---------------------------------------------------------------- legal pages
def legal_page(file, title, h1, desc, sections):
    toc = "\n".join(f'          <li><a href="#{sid}">{st}</a></li>' for sid, st, _ in sections)
    body = "\n".join(f"""        <section id="{sid}" class="legal-sec">
          <h2>{st}</h2>
{html}
        </section>""" for sid, st, html in sections)
    return (head(f"{title} | AML Canada", desc, file) + nav(file) + f"""  <main id="main">
    <section class="legal-hero" data-theme="dark" aria-labelledby="page-title">
      <div class="wrap">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="./">Home</a><span aria-hidden="true">/</span><span aria-current="page">{title}</span></nav>
        <h1 id="page-title">{h1}</h1>
        <p class="page-lede">Last updated {UPDATED}. AML Canada is operated by {OPERATOR}.</p>
      </div>
    </section>
    <div class="legal" data-theme="light">
      <div class="wrap legal-grid">
        <nav class="legal-toc" aria-label="On this page">
          <p class="legal-toc-h">On this page</p>
          <ol>
{toc}
          </ol>
        </nav>
        <article class="legal-body">
{body}
        </article>
      </div>
    </div>
  </main>

{footer()}</body>
</html>
""")


def P(*paras):
    return "\n".join(f"          <p>{p}</p>" for p in paras)


def UL(*items):
    return "          <ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def _site_switch(name):
    """Read a value from site-v3/site-config.js so the privacy text matches what actually loads."""
    try:
        m = re.search(name + r'\s*:\s*"([^"]*)"', (OUT / "site-config.js").read_text(encoding="utf-8"))
        return bool(m and m.group(1).strip())
    except OSError:
        return False


GA_ON, CF_ON = _site_switch("gaId"), _site_switch("cfBeacon")
POSTAL_LINE = ", ".join(ADDRESS_LINES)

if GA_ON or CF_ON:
    _analytics = []
    if CF_ON:
        _analytics.append("<strong>Cloudflare Web Analytics</strong> counts visits without cookies and without tracking you across sites.")
    if GA_ON:
        _analytics.append("<strong>Google Analytics</strong> (through the Google tag) uses cookies to measure how the site is used. It loads only after you choose \"Accept\" in the cookie banner. If you decline, or don't choose, it stays off. You can change your choice at any time with \"Cookie choices\" in the footer. Your choice is stored in your browser so we don't ask on every page.")
    COOKIES_TEXT = P(*_analytics)
    USAGE_ITEM = "<strong>Usage information.</strong> Pages visited, referring site, approximate location and device type, collected as described under Cookies and analytics."
else:
    COOKIES_TEXT = P(
        "This site doesn't use analytics tools, advertising cookies or tracking pixels, and it doesn't set cookies.",
        "If we add analytics, we'll update this policy first. Any tool that uses cookies will load only after you accept it in a cookie banner.")
    USAGE_ITEM = "<strong>Technical information.</strong> Like any website, our hosting provider processes your IP address, browser type and the pages you request so it can deliver the site and keep it secure."

PRIVACY = [
    ("who", "Who we are", P(
        f"AML Canada (amlcanada.ca) is operated by {OPERATOR} (\"we\", \"us\"). This policy explains what personal information we collect through this website, why, and the choices you have.",
        "We handle personal information in line with Canada's <em>Personal Information Protection and Electronic Documents Act</em> (PIPEDA) and, for people in Quebec, the <em>Act respecting the protection of personal information in the private sector</em>.")),
    ("officer", "Privacy officer", P(
        f"Our Privacy Officer is responsible for how we handle personal information and for this policy. You can reach them at <a href=\"mailto:{PRIVACY_EMAIL}\">{PRIVACY_EMAIL}</a> or by mail at: Privacy Officer, {OPERATOR}, {POSTAL_LINE}.")),
    ("collect", "What we collect", P("We collect only what this site needs:") + "\n" + UL(
        "<strong>Consultation requests.</strong> Your name, work email, company, the help you're looking for and anything you choose to tell us in the message.",
        "<strong>Gap check answers.</strong> The gap check runs in your browser. Your answers aren't sent to us unless you carry them into a consultation request, where they appear in the message for you to review before sending.",
        USAGE_ITEM,
        "<strong>Emails you send us.</strong> If you write to us, we keep the correspondence.")),
    ("use", "How we use it", UL(
        "To reply to your request and arrange a consultation.",
        "To provide services you engage us for, under a separate written agreement.",
        "To keep the site secure and prevent abuse, such as spam form submissions.",
        *(["To understand how the site is used and improve it."] if (GA_ON or CF_ON) else [])) + "\n" + P(
        "We don't sell personal information, and we don't use your consultation details for marketing without your consent.")),
    ("cookies", "Cookies and analytics", COOKIES_TEXT),
    ("share", "Who we share it with", P("We share personal information only with service providers that help us run this site and respond to you, and only as much as they need:") + "\n" + UL(
        "<strong>GitHub</strong> (GitHub Pages), which hosts this website.",
        "<strong>Web3Forms</strong>, which delivers consultation form submissions to our inbox.",
        *(["<strong>Cloudflare</strong>, for cookieless visit counts."] if CF_ON else []),
        *(["<strong>Google</strong>, for analytics, only if you accept analytics cookies."] if GA_ON else []),
        "Our email provider, for correspondence.") + "\n" + P(
        "Some of these providers process information outside Canada, including in the United States, where it may be accessible to authorities under local law. We may also disclose information where the law requires it.")),
    ("keep", "How long we keep it", P(
        "We keep consultation requests and correspondence for as long as we need them to respond and, if you become a client, for the period our engagement and legal obligations require. When we no longer need personal information, we delete it or make it anonymous.")),
    ("safe", "How we protect it", P(
        "We use reasonable physical, organizational and technical safeguards, and limit access to people who need it. No method of transmission over the internet is completely secure, so please don't send sensitive personal information, such as identity documents, through the website form.",
        "If a breach of security safeguards involving your personal information creates a real risk of significant harm, we'll notify you and the regulators as the law requires.")),
    ("rights", "Your choices and rights", P(
        f"You can ask to see the personal information we hold about you, ask us to correct it, or withdraw your consent to our use of it (subject to legal or contractual limits). If you're in Quebec, you can also ask for your information in a structured, commonly used technological format. Write to <a href=\"mailto:{PRIVACY_EMAIL}\">{PRIVACY_EMAIL}</a>. We'll respond within 30 days.",
        "If you're not satisfied with our response, you can contact the <a href=\"https://www.priv.gc.ca/\" rel=\"noopener\">Office of the Privacy Commissioner of Canada</a> or, in Quebec, the <a href=\"https://www.cai.gouv.qc.ca/\" rel=\"noopener\">Commission d'accès à l'information</a>.")),
    ("changes", "Changes to this policy", P(
        "We'll update this page when our practices change and show the date of the latest update at the top.")),
]

TERMS = [
    ("about", "About these terms", P(
        f"These terms apply to your use of amlcanada.ca. The site is operated by {OPERATOR} under the name AML Canada. By using the site you agree to these terms. If you don't agree, please don't use it.")),
    ("advice", "General information, not advice", P(
        "Everything on this site, including the gap check, regulatory summaries and figures, is general information. It isn't legal, regulatory or compliance advice, and it may not reflect the latest requirements that apply to your business.",
        "Your obligations depend on your activities and circumstances. Don't act, or decide not to act, on the basis of this site without advice on your specific situation. The gap check is a self-assessment aid, not a compliance assessment.")),
    ("engagement", "No client relationship", P(
        "Using this site, sending a consultation request or emailing us doesn't create a client relationship. A client relationship begins only when we both sign a written engagement setting out the scope of work.")),
    ("use", "Using the site", P("You agree not to:") + "\n" + UL(
        "use the site for anything unlawful or fraudulent;",
        "send spam, malware or anything that interferes with the site;",
        "try to gain unauthorized access to the site or the systems behind it;",
        "copy or reuse the site's content for commercial purposes without our written permission.")),
    ("ip", "Our content", P(
        f"The text, design, graphics and code on this site belong to {OPERATOR} or its licensors and are protected by copyright and other laws. You may view and print pages for your own reference.")),
    ("links", "Links to other sites", P(
        "We link to other websites, such as FINTRAC and the Office of the Privacy Commissioner, for convenience. We don't control them and aren't responsible for their content.")),
    ("liability", "Limitation of liability", P(
        f"We work to keep the site accurate and available, but we provide it \"as is\" without warranties of any kind. To the extent the law allows, {OPERATOR} isn't liable for any loss arising from your use of the site or reliance on its content. Nothing in these terms limits liability that can't be limited by law.")),
    ("law", "Governing law", P(
        "These terms are governed by the laws of the Province of Ontario and the federal laws of Canada that apply there. The courts of Ontario have exclusive jurisdiction over any dispute about them.")),
    ("changes", "Changes and contact", P(
        f"We may update these terms; the date at the top shows the latest version. Questions? Write to <a href=\"mailto:{EMAIL}\">{EMAIL}</a>.")),
]

PAGES["privacy.html"] = legal_page("privacy.html", "Privacy policy", "Privacy policy",
    f"How {OPERATOR}, operator of AML Canada, collects, uses and protects personal information.", PRIVACY)
PAGES["terms.html"] = legal_page("terms.html", "Terms of use", "Terms of use",
    f"The terms that apply to your use of amlcanada.ca, operated by {OPERATOR}.", TERMS)

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="24" height="24" rx="5" fill="#06080C"/><path d="M5 9V5h4M15 5h4v4M19 15v4h-4M9 19H5v-4" fill="none" stroke="#fff" stroke-width="1.8"/><circle cx="12" cy="12" r="2.6" fill="#FFB23F"/></svg>
"""

SITE_CONFIG = """/* Site settings. Fill these in to switch features on; empty values leave them off.

   web3formsKey  Access key from web3forms.com (it's designed to be public).
                 Submissions are emailed to the address you registered there.
   gaId          Google tag / GA4 measurement ID, e.g. "G-XXXXXXXXXX".
                 Loads only after a visitor accepts the cookie banner.
   cfBeacon      Cloudflare Web Analytics token (Cloudflare dashboard > Web Analytics).
                 Cookieless, so it loads without the banner. Leave empty if the site
                 is proxied through Cloudflare with automatic Web Analytics turned on. */
window.SITE_CONFIG = {
  web3formsKey: "",
  gaId: "",
  cfBeacon: "",
};
"""


def replace_block(html, name, block):
    a, b = f"  <!-- shared:{name} -->\n", f"  <!-- /shared:{name} -->"
    i, j = html.index(a) + len(a), html.index(b)
    return html[:i] + block.rstrip("\n") + "\n" + html[j:]


# ---------------------------------------------------------------- 404 + crawler files
def page_404():
    html = (head("Page not found | AML Canada", "This page doesn't exist. Find AML Canada's compliance services or book a consultation.",
                 "404.html", '\n  <meta name="robots" content="noindex">')
            + nav("") + """  <main id="main">
    <section class="legal-hero" data-theme="dark" aria-labelledby="page-title">
      <div class="wrap">
        <p class="page-lede">Error 404</p>
        <h1 id="page-title">This page isn't here.</h1>
        <p class="page-lede">It may have moved, or the link may be wrong. These will get you where you need to go.</p>
        <div class="hero-actions">
          <a class="btn btn-amber" href="services.html">See our services</a>
          <a class="link-dark" href="contact.html">Book a consultation</a>
        </div>
      </div>
    </section>
  </main>

""" + footer() + "</body>\n</html>\n")
    # served at any missing path, so every relative URL is anchored to the site root
    html = re.sub(r'(href|src)="(?![#/]|https?:|mailto:|tel:)\.?/?([^"]*)"', r'\1="/\2"', html)
    return html.replace('canonical" href="https://amlcanada.ca/404.html"', 'canonical" href="https://amlcanada.ca/"')


INDEXED = ["", "services.html", *[f for f, *_ in SERVICES], "pricing.html", "guides.html", *GUIDES, "who-we-help.html", "how-we-work.html",
           "about.html", "contact.html", "privacy.html", "terms.html"]

ROBOTS = """# robots.txt for https://amlcanada.ca
# Open to search engines and AI assistants. A crawler that matches a named group
# ignores the * group, so any future Disallow must be repeated in every group.

User-agent: *
Allow: /

# Search engines (Google AI Overviews use Googlebot; Copilot uses Bing)
User-agent: Googlebot
User-agent: Bingbot
User-agent: Applebot
Allow: /

# AI search and user-initiated fetches
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
Allow: /

# AI training and grounding (none of these affect Google Search)
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: Google-Extended
User-agent: Applebot-Extended
User-agent: CCBot
Allow: /

Sitemap: https://amlcanada.ca/sitemap.xml
"""


def sitemap():
    urls = "\n".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{max(GUIDES[u].get('modified', GUIDES[u].get('date', PUBLISHED)), LASTMOD) if u in GUIDES else max(DEEP[u].get('modified', LASTMOD), LASTMOD) if u in DEEP else LASTMOD}</lastmod></url>" for u in INDEXED)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
'''


def llms():
    svc = "\n".join(f"- [{n}]({SITE}{f}): {d}" for f, (n, _, d, _) in SCHEMA_SERVICES.items())
    return f"""# AML Canada

> AML and regulatory compliance services in Canada. AML Canada helps money services businesses, virtual currency dealers, payment service providers and fintechs register with FINTRAC and the Bank of Canada (RPAA), build compliance programs under the PCMLTFA, run their compliance function with an outsourced compliance officer, prepare for examinations and train their staff. Operated by {OPERATOR}, a private consultancy not affiliated with FINTRAC or the Bank of Canada.

## Services

{svc}

## Guides

{chr(10).join(f"- [{g['h1']}]({SITE}{f}): {g['lede']}" for f, g in GUIDES.items())}

## About

- [All services]({SITE}services.html)
- [Pricing]({SITE}pricing.html): Canadian company incorporation US$1,500 (usually a few hours to 24 hours); FINTRAC MSB registration US$3,500 (approval typically 1 week to 7 months); PCMLTFA compliance program (14 documents) US$3,500; outsourced compliance officer US$1,500 per 10 hours; RPAA registration US$3,500 plus the Bank of Canada's CA$2,500 application fee (typically 2 to 8 months); RPAA compliance program US$3,500; Canadian address US$200 per month; registered MSBs for sale from EUR 28,000.
- [Who we help]({SITE}who-we-help.html): money services businesses, virtual currency dealers, foreign MSBs, fintechs and compliance officers.
- [How we work]({SITE}how-we-work.html)
- [About AML Canada]({SITE}about.html)
- [Book a consultation]({SITE}contact.html)

## Contact

- Email: {EMAIL}
- Phone: {PHONE_DISPLAY}
- Address: {", ".join(ADDRESS_LINES)}

## Full content

- [All service pages and guides as plain text]({SITE}llms-full.txt)

The information on this site is general and is not legal advice.
"""



# ---------------------------------------------------------------- llms-full.txt (plain text for AI assistants)
INDEXNOW_KEY = "5f3c9a1e7b2d4c8a9e6f0b1d2c3a4e5f"


def md(html):
    """Very small HTML-to-Markdown pass for the long-form content."""
    t = html
    t = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", t, flags=re.S)
    t = re.sub(r"<tr[^>]*>(.*?)</tr>", lambda m: "| " + " | ".join(
        re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", m.group(1), re.S)) + " |\n", t, flags=re.S)
    t = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", t, flags=re.S)
    t = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>',
               lambda m: f"[{m.group(2)}]({m.group(1) if m.group(1).startswith('http') else SITE + m.group(1)})", t, flags=re.S)
    t = re.sub(r"</p>", "\n\n", t)
    t = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", t, flags=re.S)
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n[ \t]+", "\n", t)
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def llms_full():
    out = [f"# AML Canada: full content\n\n> {SITE} AML and regulatory compliance services in Canada, operated by {OPERATOR}, "
           "a private consultancy not affiliated with FINTRAC or the Bank of Canada. General information, not legal advice. "
           f"Contact: {EMAIL}, {PHONE_DISPLAY}. Fees in USD unless stated.\n"]
    for f, d in DEEP.items():
        fee = d["fee"]
        out.append(f"\n---\n\n## {d['name']}\n\nURL: {SITE}{f}\n\n{d['lede']}\n\n**Fee:** {fee['amount']} ({fee['unit']}). {fee['note']}\n\n**Included:**\n"
                   + "\n".join(f"- {i}" for i in fee["items"]) + "\n\n"
                   + "\n\n".join(f"### {h}\n\n{md(x)}" for _, h, x in d["guide"])
                   + "\n\n### Questions\n\n" + "\n\n".join(f"**{q}** {a}" for q, a in d["faqs"])
                   + "\n\nSources: " + "; ".join(f"[{t}]({u})" for t, u in d["sources"]) + f". Checked {CHECKED}.\n")
    for f, g in GUIDES.items():
        out.append(f"\n---\n\n## Guide: {g['h1']}\n\nURL: {SITE}{f}\n\n{g['lede']}\n\n**Key points:**\n"
                   + "\n".join(f"- {t}" for t in g["takeaways"]) + "\n\n"
                   + "\n\n".join(f"### {h}\n\n{md(x)}" for _, h, x in g["sections"])
                   + "\n\n### Questions\n\n" + "\n\n".join(f"**{q}** {a}" for q, a in g["faqs"])
                   + "\n\nSources: " + "; ".join(f"[{t}]({u})" for t, u in g["sources"]) + f". Checked {g.get('checked', CHECKED)}.\n")
    return "".join(out)


def main():
    for name, html in PAGES.items():
        html = html.replace("{{FORM}}", FORM)
        (OUT / name).write_text(html, encoding="utf-8")
        print("wrote", name)
    home = (OUT / "index.html").read_text(encoding="utf-8")
    home = replace_block(home, "fonts", FONTS)
    home = replace_block(home, "icons", ICON_LINKS)
    home = replace_block(home, "social", SOCIAL)
    home_faqs = re.findall(r"<details><summary>(.*?)<svg.*?</summary><p>(.*?)</p></details>", home, re.S)
    home = replace_block(home, "schema", jsonld("index.html").lstrip("\n") + (faq_schema(home_faqs) if home_faqs else ""))
    home = replace_block(home, "nav", nav("index.html"))
    home = replace_block(home, "form", FORM)
    home = replace_block(home, "footer", footer())
    home = replace_block(home, "clients", clients_block())
    (OUT / "index.html").write_text(home, encoding="utf-8")
    print("synced index.html")
    (OUT / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    (OUT / "404.html").write_text(page_404(), encoding="utf-8")
    (OUT / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    (OUT / "CNAME").write_text("amlcanada.ca\n", encoding="utf-8")
    (OUT / "site.webmanifest").write_text(json.dumps({
        "name": "AML Canada", "short_name": "AML Canada", "start_url": "/", "display": "standalone",
        "background_color": "#06080C", "theme_color": "#06080C",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2) + "\n", encoding="utf-8")
    (OUT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    (OUT / "llms.txt").write_text(llms(), encoding="utf-8")
    (OUT / "llms-full.txt").write_text(llms_full(), encoding="utf-8")
    (OUT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY, encoding="utf-8")
    print("wrote 404.html, robots.txt, sitemap.xml, llms.txt")
    cfg = OUT / "site-config.js"
    if not cfg.exists():
        cfg.write_text(SITE_CONFIG, encoding="utf-8")
        print("wrote site-config.js")


if __name__ == "__main__":
    main()
