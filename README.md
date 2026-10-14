# Truman for Torrance: Senior Benefits Guide

One-page static site that lists discounts and benefits for Torrance seniors and people with
disabilities, in English, Spanish, Korean, Japanese, and Chinese (Traditional).

**Live site (once DNS is set):** https://trumanfortorrance.com/

No build step. Edit files and push to `main`. Layout follows the `wfplasouthbay` repo:
plain HTML, CSS, and vanilla JS, with a `CNAME` for the custom domain.

## Link directly to a language or a card

| Link | Shows |
|------|-------|
| `/#en`, `/#es`, `/#ko`, `/#ja`, `/#zh` | The guide in that language |
| `/#es-tax` | Spanish, scrolled to the property tax card |
| `/es/`, `/ko/`, `/ja/`, `/zh/`, `/en/` | Short paths that redirect to the matching `/#xx` |
| `/trash/`, `/tax/`, `/care/`, `/food/`, `/hip/`, `/focal/` | Short paths that redirect to the official program page |

Card ids: `trash`, `tax`, `care`, `medicare`, `food`, `hip`, `focal`.
With no hash, the page opens in the visitor's last language or browser language.

## Quick edits

| To change | Edit |
|-----------|------|
| Card text or translations | `index.html` (one `<div class="lang">` per language) |
| Colors, fonts, layout | `css/styles.css` (tokens at the top) |
| Language switching | `js/main.js`, `js/config.js` |
| Short-link targets | `trash/`, `tax/`, `care/`, `food/`, `hip/`, `focal/` `index.html` files |

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
