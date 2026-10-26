# Truman for Torrance

Static site. The home page (`/`) is a generic placeholder to fill in later. The Senior Resources Guide
lives at `/senior-resources/`: discounts and benefits for Torrance seniors and people with disabilities,
in English, Spanish, Korean, Japanese, and Chinese (Traditional).

**Live site (once DNS is set):** https://trumanfortorrance.com/

No build step. Edit files and push to `main`. Layout follows the `wfplasouthbay` repo:
plain HTML, CSS, and vanilla JS, with a `CNAME` for the custom domain.

## Senior Resources Guide: link to a language or a card (`/senior-resources/`)

| Link | Shows |
|------|-------|
| `/senior-resources/#en`, `#es`, `#ko`, `#ja`, `#zh` | The guide in that language |
| `/senior-resources/#es-tax` | Spanish, scrolled to the property tax card |
| `/senior-en`, `/senior-es`, `/senior-ko`, `/senior-ja`, `/senior-zh` | Short paths that redirect to the matching `/senior-resources/#xx` |
| `/senior-trash`, `/senior-tax`, `/senior-hip`, `/senior-focal` | Short paths to that card, in the visitor's language |

Short links exist only for this site's own pages, never for outside resources. Outside programs
are linked directly from each card.

Card ids: `trash`, `tax`, `care`, `medicare`, `food`, `hip`, `focal`.
With no hash, the page opens in the visitor's last language or browser language.

## Quick edits

| To change | Edit |
|-----------|------|
| Home page | `index.html` |
| Guide text or translations | `senior-resources/index.html` (one `<div class="lang">` per language) |
| Colors, fonts, layout | `css/styles.css` (tokens at the top) |
| Language switching | `js/main.js`, `js/config.js` |
| Short-link targets | the `senior-*/index.html` files |

## Custom domain (GitHub Pages)

1. Repo Settings > Pages: deploy from branch `main`, folder `/ (root)`.
2. At the registrar, add four apex A records: `185.199.108.153`, `185.199.109.153`,
   `185.199.110.153`, `185.199.111.153`, and a `www` CNAME to `jstart.github.io`.
3. Once the certificate is issued, turn on "Enforce HTTPS".

## Before publishing

- Translations (Spanish, Korean, Japanese, Chinese) are drafts and should be reviewed by fluent speakers.
- Income limits and rates change each year; recheck each program page.
- If this site is tied to a campaign, add any required "paid for by" disclosure to the footer.

Prepared by Christopher Truman, a Torrance resident, as an individual. Not an official City,
County, State, or Commission on Aging document.

## Reader tools

- Jump links: a sticky row of chips under the intro scrolls to each program. Card ids: `trash`, `tax`, `care`, `medicare`, `food`, `hip`, `focal`.
- "Larger text" button (header): scales the page to 125% and remembers the choice in the browser.
- "Print" button (header): prints the guide in the visitor's language with links written out. Print styles are at the bottom of `css/styles.css`.
- Each language footer asks readers to email info@trumanfortorrance.com about mistakes. Make sure that address forwards (Porkbun email forwarding).

## Yearly checklist

Recheck these each fall (the property tax window opens October 1) and whenever a program announces changes,
then update `senior-resources/index.html` (all five languages) and the "Last updated" line in each footer.

- Trash and utility tax: monthly trash rates (City rate table, changes every July 1) and the income limit on the City's UUT exemption application (indexed each year, $39,900 for the 2025 calendar year).
- Property Tax Postponement: filing window, household income limit, interest rate, and mailing address (State Controller's application package).
- CARE and FERA: income limits and discount percentages (SCE flyer, effective June 1).
- Medicare costs: Part B premium.
- CalFresh: links and any age or income changes.
- Home Improvement Program: HUD income limits (published each April) and services list.
- Focal Point on Aging: phone number and hours.
- Translations: have fluent speakers review, then remove the draft-translation banner.

## Hillside Overlay research

The homepage Resources section links to `/hillside-overlay/`, an English research snapshot
from October 26, 2026. Plain HTML and a page-scoped stylesheet use the existing site theme;
no build step or runtime dependency was added.

- `hillside-overlay/index.html`: three-case decision explainer, selected overlay background,
  reform timeline, Susana visuals, source citations and research limits.
- `hillside-overlay/review.html`: decision-source ledger with optional client-side filtering.
- `hillside-overlay/expanded-search.html`: rendered expanded follow-through findings.
- `hillside-overlay/sources/`, `visuals/`, `downloads/`: selected evidence and the supplied
  two-page Susana PDF. `asset-provenance.json` records SHA-256 hashes for copied assets.
- CSV/JSON companions preserve the supplied comparison, source ledger and permit-stage snapshot.

The newer three-case decision package replaces the older briefing's unresolved Doris Way
status and Via Linda Vista agenda lead. The Susana Council tally remains unresolved.
The timeline distinguishes the announced August 30 deadline from the later statement
reporting acceptance through August 31; a year-end expectation is not a scheduled hearing.
Permit stages are dated observations, not a live feed. No completed-unit or prevalence
conclusion is established. The broader briefing was selectively adapted; its stale case
sections and social-post drafts are not published.

Source packages supplied for this draft: `Hillside Overlay Research.html`,
`Susana Avenue — source summary.pdf`, `susana_project_visuals_2026-10-26`,
`susana_hearing_sources_2026-10-26`, `hillside_overlay_followthrough_2026-10-26`,
and `hillside_adu_review/expanded_review_2026-10-26/decision_explainer`.
The full research working folders, unsent outreach drafts and unrelated archives are excluded.

Preview with `python3 -m http.server 8765`, then visit `/hillside-overlay/`.
Before publishing updates, reconcile newer decisions, permit revisions, source currency and
research dates, and check local links, mobile/keyboard behavior and print output again.
