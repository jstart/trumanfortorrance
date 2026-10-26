# Truman for Torrance

A static community resource site built with HTML, CSS and vanilla JavaScript.
GitHub Pages serves the committed files; there is no deployment build or runtime dependency.
The canonical domain is [trumanfortorrance.com](https://trumanfortorrance.com/).

| Page | Content |
| --- | --- |
| `/` | Resource directory |
| `/senior-resources/` | 19 benefit/service cards in English, Spanish, Korean, Japanese and Traditional Chinese |
| `/hillside-overlay/` | Five residential case comparisons, overlay background, reform timeline and source evidence |
| `/hillside-overlay/review.html` | Searchable decision-source ledger |
| `/hillside-overlay/expanded-search.html` | Bounded follow-through search and remaining gaps |

## Preview and check

Use Python 3.9 or newer from the repository root:

```sh
python3 -m http.server 8765
```

Visit [the homepage](http://localhost:8765/) or
[the senior guide](http://localhost:8765/senior-resources/#en).
Stop the server with Ctrl-C. No package installation is needed.

Before committing:

```sh
python3 scripts/sync_hillside.py --check
python3 scripts/check_site.py
git diff --check
```

The checks verify generated-content consistency, evidence hashes, local references,
Git-tracked assets and duplicate IDs. They do not verify current external program rules
or replace browser checks. Check language switching, existing short links, keyboard
navigation, Larger text, mobile layout and print output after relevant changes.

## Edit the site

| Change | Source |
| --- | --- |
| Homepage resource cards | `index.html` |
| Senior guide and translations | `senior-resources/index.html` |
| Senior program sources and verification boundaries | [senior-resources/sources.md](senior-resources/sources.md) |
| Shared layout, colors, typography, controls and print styles | `css/styles.css` |
| Language routing and shared reader controls | `js/main.js` |
| Hillside case cards, source cards, ledger and downloads | [Hillside maintenance](docs/hillside-maintenance.md) |
| Research-only image, table and filter styles | `hillside-overlay/hillside.css` |
| Ledger filtering | `js/source-ledger.js` |
| Senior short redirects | `senior-*/index.html` |

Language and card IDs are discovered from the senior guide's HTML; adding a card does
not require updating a JavaScript list. Shared reader controls also work on the English
research pages. The header and cards use the same CSS classes across both guides.
Content is fully present in the HTML; ledger filtering needs no data fetch.

## Senior guide links and updates

- `#en`, `#es`, `#ko`, `#ja`, `#zh` select a language.
- `#es-tax` selects Spanish and scrolls to Property Tax Postponement.
- `#tax` selects that card in the saved/browser language.
- `/senior-en/`, `/senior-es/`, `/senior-ko/`, `/senior-ja/`, `/senior-zh/` are language redirects.
- `/senior-trash/`, `/senior-tax/`, `/senior-hip/`, `/senior-focal/` redirect to existing cards.

Keep published card IDs and short paths stable. Update all five languages and their
check dates together. The source notes distinguish current program rules from older
research, proposed expansions and modeled enrollment gaps.

Recheck program pages when rules change: City utility rates and application, CARE/FERA
income tables, Medicare costs/enrollment, property-tax filing dates, HIP criteria,
transportation and meal contacts. Confirm Tax-Aide's actual 2027 schedule before adding
appointments, Measure W's current-year forms, and PACE's office arrangements. Standard
ESA is separate from the closing Whole Home pilot.

Spanish, Korean, Japanese and Traditional Chinese versions are draft translations until
reviewed by fluent speakers. Keep their notices in place. Larger text uses the existing
`senior-guide-size` browser preference across guides; language uses `senior-guide-lang`.
Each footer directs corrections to `info@trumanfortorrance.com`; maintain that mailbox.

## Hosting

GitHub Pages settings: branch `main`, root folder. Keep `CNAME`, canonical URLs and
`sitemap.xml` consistent with the intended domain. Changes on this PR branch are drafts;
merging to the configured publishing branch can publish them.

For initial DNS setup, point apex A records to `185.199.108.153`, `185.199.109.153`,
`185.199.110.153`, `185.199.111.153` and `www` to `jstart.github.io`. Enable HTTPS after
the certificate is available. Confirm the current GitHub Pages instructions when changing
hosting configuration.

Prepared by Christopher Truman as an individual Torrance resident, not as an official
City, County, State or Commission on Aging publication. If the site becomes tied to a
campaign, review its disclosure requirements before publishing.
