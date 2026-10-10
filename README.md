# amlcanada.ca

Website for **AML Canada**, AML & Regulatory Compliance Services in Canada (operated by ComplyFactor Limited).

Static HTML/CSS/JS, published to GitHub Pages from the `site/` folder by `.github/workflows/pages.yml` on every push to `main`.

## Editing

- `site/index.html`: homepage. Its header, menu, footer and SEO tags are filled in by the build, between `<!-- chrome:… -->` markers.
- `build.py`: generates every other page (services, who we help, how we work, about, contact, privacy, terms, credits, 404), plus `sitemap.xml`, `robots.txt` and `llms.txt`.
- `legal.py`: Privacy Policy and Terms of Service text.
- `site/styles.css` and `site/main.js`: shared styles and behaviour.

After any change to `build.py` or `legal.py`:

```
python build.py
```

## Settings (top of `build.py`)

| Setting | What it does |
|---|---|
| `WEB3FORMS_KEY` | Public Web3Forms key; consultation requests are emailed to the address registered with it |
| `CF_BEACON_TOKEN` | Cloudflare Web Analytics token (cookieless visitor stats) |
| `GA4_ID` | Google Analytics 4 ID; loads only after the visitor accepts cookies |
| `GSC_VERIFICATION` | Optional Search Console meta tag (DNS verification needs nothing) |

## Custom domain

`site/CNAME` holds `amlcanada.ca`. DNS at the registrar:

- `A` records for `amlcanada.ca`: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- `CNAME` for `www`: `saeed0complyfactor.github.io`

Then enable **Enforce HTTPS** under Settings → Pages.

Photos: see `CREDITS.md` (Unsplash License). Fonts: Source Serif 4 and Public Sans (SIL Open Font License, licences in `site/fonts/`).
