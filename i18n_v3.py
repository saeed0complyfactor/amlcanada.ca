"""Translated copies of site-v3 (run after build_v3.py; build_v3.main() calls it).

English pages stay the source of truth. Each translatable piece of text (a "unit": the inner HTML
of the outermost element that holds text directly, plus titles, meta text, alt/aria text and
JSON-LD names) is looked up in i18n/<lang>.json. Missing units fall back to English and are
written to i18n/todo-<lang>.json for translation. Output: site-v3/<lang>/<page>, hreflang
links on every page, a language switcher, and a sitemap with xhtml:link alternates.
"""
import json
from collections import Counter
import re
from pathlib import Path

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

ROOT = Path(__file__).parent
OUT = ROOT / "site-v3"
I18N = ROOT / "i18n"
SITE = "https://amlcanada.ca/"

# folder -> (hreflang / html lang, native name, short label)
LANGS = {
    "fr": ("fr-CA", "Français", "FR"),
    "de": ("de", "Deutsch", "DE"),
    "ar": ("ar", "العربية", "AR"),
    "zh-hans": ("zh-Hans", "简体中文", "简"),
    "zh-hant": ("zh-Hant", "繁體中文", "繁"),
}
EN = ("en-CA", "English", "EN")
ENGLISH_ONLY = {"privacy.html", "terms.html", "404.html"}  # legal text stays English (owner's choice)

NOTE = {  # shown at the end of every translated page
    "fr": ("Cette page est une traduction de l'anglais. En cas de divergence, la version anglaise prévaut.", "Lire en anglais"),
    "de": ("Diese Seite wurde aus dem Englischen übersetzt. Bei Abweichungen gilt die englische Fassung.", "Auf Englisch lesen"),
    "ar": ("هذه الصفحة مترجمة من الإنجليزية. في حال وجود أي اختلاف، تسري النسخة الإنجليزية.", "اقرأ بالإنجليزية"),
    "zh-hans": ("本页译自英文。如有出入，以英文版本为准。", "阅读英文版"),
    "zh-hant": ("本頁譯自英文。如有出入，以英文版本為準。", "閱讀英文版"),
}
LANG_LABEL = {"fr": "Langue", "de": "Sprache", "ar": "اللغة", "zh-hans": "语言", "zh-hant": "語言", "en": "Language"}

SKIP_TAGS = {"script", "style", "svg", "noscript", "template", "code", "pre"}
ATTRS = ("alt", "aria-label", "title", "placeholder", "data-title", "data-desc", "data-label")
META = {"description", "og:title", "og:description", "twitter:title", "twitter:description"}
LD_KEYS = {"name", "description", "text", "headline", "serviceType", "alternativeName"}
LD_KEEP = {"AML Canada", "ComplyFactor Limited"}
HAS_TEXT = re.compile(r"[^\W\d_]")  # at least one letter


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def pages():
    return sorted(p.name for p in OUT.glob("*.html") if p.name not in ENGLISH_ONLY)


def url(lang, page):
    path = "" if page == "index.html" else page
    return SITE + (f"{lang}/" if lang != "en" else "") + path


def has_direct_text(el):
    return any(isinstance(c, NavigableString) and not isinstance(c, Comment) and c.strip() for c in el.children)


def units(soup):
    """Elements to translate whole: the outermost elements that hold text directly."""
    found = []

    def walk(el):
        for c in el.children:
            if isinstance(c, Tag) and c.name not in SKIP_TAGS:
                (found.append(c) if has_direct_text(c) else walk(c))
    walk(soup.body)
    return [u for u in found if HAS_TEXT.search(u.get_text())]


def ld_walk(node, fn):
    if isinstance(node, dict):
        return {k: (fn(v) if k in LD_KEYS and isinstance(v, str) and v not in LD_KEEP else ld_walk(v, fn)) for k, v in node.items()}
    if isinstance(node, list):
        return [ld_walk(v, fn) for v in node]
    return node


def strings(soup):
    """Every English string a page needs translated (keys of i18n/<lang>.json)."""
    out = [norm(u.decode_contents()) for u in units(soup)]
    if soup.title:
        out.append(norm(soup.title.string or ""))
    for m in soup.find_all("meta"):
        if (m.get("name") or m.get("property")) in META and m.get("content"):
            out.append(norm(m["content"]))
    for el in soup.body.find_all(True):
        out += [norm(el[a]) for a in ATTRS if el.get(a) and HAS_TEXT.search(el[a])]
    for s in soup.find_all("script", type="application/ld+json"):
        ld_walk(json.loads(s.string), lambda v: out.append(norm(v)) or v)
    return out


def js_strings():
    js = (OUT / "main.js").read_text(encoding="utf-8")
    return [json.loads(f'"{m}"') for m in re.findall(r'\btr\("((?:[^"\\]|\\.)*)"', js)]


def switcher(lang, page):
    cur = EN if lang == "en" else LANGS[lang]
    items = [("en", EN)] + list(LANGS.items())
    links = "".join(
        f'<li><a href="/{"" if k == "en" else k + "/"}{"" if page == "index.html" else page}" hreflang="{v[0]}" lang="{v[0]}"'
        f'{" aria-current=\"true\"" if k == lang else ""}>{v[1]}</a></li>' for k, v in items)
    return (f'<!--i18n:switch--><details class="lang-switch" data-lang-switch><summary aria-label="{LANG_LABEL[lang]}: {cur[1]}">'
            f'<svg aria-hidden="true" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="1.3"/>'
            f'<path d="M1.8 8h12.4M8 1.8c2 2 2 10.4 0 12.4M8 1.8c-2 2-2 10.4 0 12.4" fill="none" stroke="currentColor" stroke-width="1.3"/></svg>'
            f'<span>{cur[2]}</span></summary><ul>{links}</ul></details><!--/i18n:switch-->')


def alternates(page):
    tags = [f'<link rel="alternate" hreflang="{EN[0]}" href="{url("en", page)}">']
    tags += [f'<link rel="alternate" hreflang="{v[0]}" href="{url(k, page)}">' for k, v in LANGS.items()]
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{url("en", page)}">')
    return "<!--i18n:alt-->\n  " + "\n  ".join(tags) + "\n  <!--/i18n:alt-->"


def strip_blocks(html):
    return re.sub(r"\s*<!--i18n:(\w+)-->.*?<!--/i18n:\1-->", "", html, flags=re.S)


def add_chrome(html, lang, page):
    """hreflang links in <head>, switcher in the nav bar and the mobile menu (idempotent)."""
    html = strip_blocks(html)
    html = html.replace("</head>", f"  {alternates(page)}\n</head>", 1)
    sw = switcher(lang, page)
    html = html.replace('<div class="nav-end">', '<div class="nav-end">\n        ' + sw, 1)
    menu = re.sub(r"<details.*?</summary>(.*)</details>", rf'<nav class="lang-menu" aria-label="{LANG_LABEL[lang]}">\1</nav>', sw, flags=re.S)
    html = html.replace('<p class="menu-note">', menu + '\n    <p class="menu-note">', 1)
    return html


def relink(soup, lang, translated):
    """Pages live in site-v3/<lang>/: keep links to translated pages, point everything else at ../"""
    for el in soup.find_all(href=True) + soup.find_all(src=True):
        attr = "href" if el.has_attr("href") else "src"
        v = el[attr]
        if re.match(r"^([a-z]+:|/|#|\.\./)", v) or el.get("rel") == ["alternate"]:
            continue
        path = re.split(r"[?#]", v, maxsplit=1)[0]
        if path in ("", "./") or path in translated:
            continue
        el[attr] = "../" + v
    for el in soup.find_all(srcset=True):
        el["srcset"] = ", ".join(p if p.startswith(("/", "http")) else "../" + p for p in (x.strip() for x in el["srcset"].split(",")))


def translate_page(page, lang, tm):
    en_html = (OUT / page).read_text(encoding="utf-8")
    soup = BeautifulSoup(en_html, "html.parser")
    t = lambda s: tm.get(norm(s), s)
    for u in units(soup):
        key = norm(u.decode_contents())
        if key in tm:
            u.clear()
            u.append(BeautifulSoup(tm[key], "html.parser"))
    if soup.title and soup.title.string:
        soup.title.string = t(soup.title.string)
    for m in soup.find_all("meta"):
        if (m.get("name") or m.get("property")) in META and m.get("content"):
            m["content"] = t(m["content"])
        if m.get("property") == "og:url":
            m["content"] = url(lang, page)
        if m.get("property") == "og:locale":
            m["content"] = LANGS[lang][0].replace("-", "_")
    for el in soup.body.find_all(True):
        for a in ATTRS:
            if el.get(a):
                el[a] = t(el[a])
    for s in soup.find_all("script", type="application/ld+json"):
        data = ld_walk(json.loads(s.string), t)
        raw = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        for p in pages():  # page URLs (not #organization / #website) point at this language
            raw = re.sub(rf'"{re.escape(url("en", p))}(#(?!organization|website|logo)[^"]*)?"', lambda m: f'"{url(lang, p)}{m.group(1) or ""}"', raw)
        raw = raw.replace('"inLanguage":"en-CA"', f'"inLanguage":"{LANGS[lang][0]}"')
        s.string = raw
    soup.html["lang"] = LANGS[lang][0]
    if lang == "ar":
        soup.html["dir"] = "rtl"
    can = soup.find("link", rel="canonical")
    if can:
        can["href"] = url(lang, page)
    form = soup.find("form", attrs={"data-consult": True})
    if form:
        form.insert(0, BeautifulSoup(f'<input type="hidden" name="language" value="{LANGS[lang][1]}">', "html.parser"))
    relink(soup, lang, set(pages()))
    js = {s: tm[s] for s in js_strings() if s in tm}
    main_js = soup.find("script", src=re.compile(r"main\.js"))
    if main_js and js:
        main_js.insert_before(BeautifulSoup(f"<script>window.I18N={json.dumps(js, ensure_ascii=False)}</script>", "html.parser"))
    main = soup.find("main")
    if main:
        text, link = NOTE[lang]
        main.append(BeautifulSoup(f'<p class="i18n-note wrap">{text} <a href="{url("en", page)}" hreflang="en-CA" lang="en-CA">{link}</a></p>', "html.parser"))
    return add_chrome(str(soup), lang, page)


def sitemap():
    sm = (OUT / "sitemap.xml").read_text(encoding="utf-8")
    entries = re.findall(r"<url><loc>(.*?)</loc><lastmod>(.*?)</lastmod></url>", sm)
    out = []
    for loc, mod in entries:
        page = loc[len(SITE):] or "index.html"
        if page not in set(pages()):
            out.append(f"  <url><loc>{loc}</loc><lastmod>{mod}</lastmod></url>")
            continue
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{u}"/>' for h, u in
                       [(EN[0], url("en", page))] + [(v[0], url(k, page)) for k, v in LANGS.items()] + [("x-default", url("en", page))])
        for lang in ["en", *LANGS]:
            out.append(f"  <url><loc>{url(lang, page)}</loc><lastmod>{mod}</lastmod>{alts}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(out) + "\n</urlset>\n")


def run():
    I18N.mkdir(exist_ok=True)
    needed = []
    for page in pages():
        html = strip_blocks((OUT / page).read_text(encoding="utf-8"))
        needed += strings(BeautifulSoup(html, "html.parser"))
        (OUT / page).write_text(add_chrome(html, "en", page), encoding="utf-8")
    needed = list(dict.fromkeys(needed + js_strings()))
    for lang in LANGS:
        f = I18N / f"{lang}.json"
        tm = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
        todo = [s for s in needed if s not in tm]
        (I18N / f"todo-{lang}.json").write_text(json.dumps(todo, ensure_ascii=False, indent=0), encoding="utf-8")
        (OUT / lang).mkdir(exist_ok=True)
        for page in pages():
            (OUT / lang / page).write_text(translate_page(page, lang, tm), encoding="utf-8")
        print(f"i18n {lang}: {len(pages())} pages, {len(needed) - len(todo)}/{len(needed)} strings translated")
    (OUT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")


# 3,500 / 3 500 / 3.500 / 66.50 / 66,50 compare as digits; "January 11, 2024" stays two numbers
NUM = re.compile(r"\d+(?:[,.   ]\d{3}(?!\d))*(?:[.,]\d+)?")


def signature(html):
    """What a translation must keep: tags with their link/id/class attributes, and the numbers."""
    soup = BeautifulSoup(html, "html.parser")
    tags = sorted((t.name, t.get("href", ""), t.get("src", ""), t.get("id", ""), " ".join(t.get("class", []))) for t in soup.find_all(True))
    nums = sorted(re.sub(r"\D", "", n) for n in NUM.findall(soup.get_text()))
    return tags, nums


def check(part, src):
    """python i18n_v3.py check i18n/parts/fr-1.json i18n/parts/src-1.json -> problems, one per line."""
    tr, en = json.loads(Path(part).read_text(encoding="utf-8")), json.loads(Path(src).read_text(encoding="utf-8"))
    bad = [f"MISSING: {k[:90]}" for k in en if not tr.get(k, "").strip()]
    bad += [f"EXTRA KEY: {k[:90]}" for k in tr if k not in set(en)]
    for k, v in tr.items():
        if k in set(en) and v.strip():
            (te, ne), (tt, nt) = signature(k), signature(v)
            if te != tt:
                bad.append(f"TAGS DIFFER: {k[:90]}")
            lost, added = Counter(ne) - Counter(nt), Counter(nt) - Counter(ne)
            if lost or any(int(n or 0) > 12 for n in added):  # month names may become digits (10月)
                bad.append(f"NUMBERS DIFFER {ne} vs {nt}: {k[:70]}")
    print("\n".join(bad) or "OK", f"\n{len(bad)} problems, {len(tr)}/{len(en)} translated")


def split(n=2):
    """Write i18n/parts/src-<i>.json: the English strings still missing in any language, in n chunks."""
    parts = I18N / "parts"
    parts.mkdir(exist_ok=True)
    todo = list(dict.fromkeys(s for lang in LANGS for s in json.loads((I18N / f"todo-{lang}.json").read_text(encoding="utf-8"))))
    size = -(-len(todo) // n)
    for i in range(n):
        (parts / f"src-{i + 1}.json").write_text(json.dumps(todo[i * size:(i + 1) * size], ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"{len(todo)} strings in {n} chunks of up to {size}")


def zip_part(lang, chunk):
    """Pair translators' value lists (i18n/parts/work/<lang>-<chunk>-<start>.json, a JSON list for src lines
    start, start+1, ...) with the English keys of src-<chunk>.json -> i18n/parts/<lang>-<chunk>.json, then check it."""
    parts = I18N / "parts"
    src = json.loads((parts / f"src-{chunk}.json").read_text(encoding="utf-8"))
    out = {}
    for f in sorted((parts / "work").glob(f"{lang}-{chunk}-*.json")):
        start = int(f.stem.rsplit("-", 1)[1])
        for i, v in enumerate(json.loads(f.read_text(encoding="utf-8"))):
            if start + i < len(src):
                out[src[start + i]] = v
    target = parts / f"{lang}-{chunk}.json"
    target.write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding="utf-8")
    check(target, parts / f"src-{chunk}.json")


def merge():
    """Fold i18n/parts/<lang>-<i>.json into i18n/<lang>.json."""
    for lang in LANGS:
        f = I18N / f"{lang}.json"
        tm = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
        for p in sorted((I18N / "parts").glob(f"{lang}-[0-9]*.json")):
            tm.update({k: v for k, v in json.loads(p.read_text(encoding="utf-8")).items() if v.strip()})
        f.write_text(json.dumps(tm, ensure_ascii=False, indent=0, sort_keys=True), encoding="utf-8")
        print(f"{lang}: {len(tm)} strings")


if __name__ == "__main__":
    import sys
    {"check": lambda: check(*sys.argv[2:4]), "split": lambda: split(int(sys.argv[2]) if len(sys.argv) > 2 else 2),
     "zip": lambda: zip_part(*sys.argv[2:4]),
     "merge": merge}.get(sys.argv[1] if len(sys.argv) > 1 else "", run)()
