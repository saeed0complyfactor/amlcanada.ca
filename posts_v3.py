"""Dated news and analysis posts ("Latest updates") for site-v3.

Posts use the same shape as a guide in guides_v3.py, plus:
  date      ISO date the post was published, e.g. "2026-10-13"
  kind      "update" (always)
The build lists posts newest first under "Latest updates" on guides.html, gives
them Article structured data with that date, and adds them to the sitemap and
llms files. Newest entries go at the TOP of POSTS.

Rules (see AUTOMATION.md): every fact comes from an official source linked in
"sources" (FINTRAC, Bank of Canada, Government of Canada, Revenu Québec, court or
legislation sites). Penalty amounts, names and dates are copied exactly from the
public notice. No speculation about why a business was penalized beyond what the
notice says. No invented statistics, quotes or client stories.
"""

POSTS = {}
