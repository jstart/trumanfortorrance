# Maintain the Hillside Overlay research

This is a dated public-record snapshot from October 26, 2026, not a live permit feed.
The site uses the senior guide's shared layout and reader controls. Narrative background
and limits are edited directly; repeated structured evidence is maintained once in JSON.

## Sources of truth

| Edit this | Generates |
| --- | --- |
| `hillside-overlay/comparison.json` | Five case cards in `index.html` and `comparison.csv` |
| `hillside-overlay/sources.json` | Source cards in `index.html` |
| `hillside-overlay/source_reviews.json` | Rows in `review.html` and `source_reviews.csv` |

Run after editing those JSON files:

```sh
python3 scripts/sync_hillside.py
python3 scripts/sync_hillside.py --check
python3 scripts/check_site.py
```

Commit the JSON and generated outputs together. Do not edit between `BEGIN GENERATED`
and `END GENERATED` comments: the sync command replaces only those blocks and the CSVs.
It does not regenerate the surrounding narrative, homepage descriptions, source counts
or research dates; update those when scope changes. The Python standard library is the
only requirement, and generated HTML is committed so deployment needs no build step.

Case IDs determine permanent `#case-…` anchors. Each case references source IDs, which
must exist in `sources.json`; their anchors are `#source-…`. `notes` preserves a case's
vote-tally caveat. The source-review ledger distinguishes recommendations, adopted
motions, appellant arguments and unresolved evidence; one project appearing in several
sources is not several projects.

## Original sources and archives

Prefer an original City/agency URL for primary citations. A source's optional `local`
path is relative to `hillside-overlay/`; it is a secondary archived copy or locally
prepared evidence. The sync command renders original links first, then archived links.
Local snapshots with no equivalent original download remain labeled as archives.

Commit every referenced PDF, image, CSV and JSON. `asset-provenance.json` records hashes
of deployed files; `original_sha256` retains the imported bytes' hash when an artifact
is adapted. Excerpts also retain the full original packet hash and original page ranges.
Never label an excerpt as a complete packet or renumber its cited original pages.

The sync command refreshes hashes only for maintained JSON and generated CSV files.
An imported evidence hash mismatch fails the command. Restore accidental changes;
for an intentional new snapshot, review its provenance, record a new source/version
and update the manifest deliberately. Do not silently replace dated original evidence.

The dependency-free link check scans HTML, redirects, Markdown, registry paths and
provenance for missing/untracked local targets and duplicate HTML IDs. It understands
the senior guide's language/card hash routing. External availability and factual accuracy
are separate checks; original websites can change or block automated access.

## Research boundaries to preserve

- Susana documents adopted main-house HAA reasoning; Doris supplies minutes-level
  reasoning, with its signed resolution still unrecovered.
- Revised September minutes record Via Linda Vista's garage denial Resolution 2026-77.
  This resolves that entitlement action, not the separate October ADU clearance.
- Via El Chico concerns a neighboring ADU/SB 9 development. Do not attribute those units
  or their construction status to the applicant's main-house additions.
- Calle Mayor is a conventional hillside comparison; its final motion controls over the
  inconsistent hearing-closure tally. Keep its MOD number separate from the stray MOD
  reference in Via El Chico's minutes.
- The archived Resolution 2026-46 May approval certification conflicts with October
  staff history describing May denial and September direction toward approval. Retain
  both accounts. October final action and operative signed resolutions remain unresolved;
  an HCD referral is not an enforcement finding. This mixed-use project is separate from
  the five residential comparisons.
- The announced August 30 deadline differs from the later statement reporting acceptance
  through August 31. Staff's year-end expectation is not a scheduled hearing.
- Susana's numerical Council tally is inconsistent. Automatic captions are not audio-verified.
  Approval, permit issuance, final inspection and occupancy are distinct stages.

No prevalence rate, completed-unit count, causal design effect or neighborhood-wide
harm estimate is established. Agenda-title screening through October 20 is bounded;
project decisions do not establish adoption of new overlay standards. Keep these limits
with any later revision or derivative export.

## Evidence package history

The supplied research packages were `Hillside Overlay Research.html`,
`Susana Avenue — source summary.pdf`, `susana_project_visuals_2026-10-26`,
`susana_hearing_sources_2026-10-26`, `hillside_overlay_followthrough_2026-10-26`,
`hillside_adu_review/expanded_review_2026-10-26/decision_explainer`, and
`recent_council_2026-10-26`. They were selectively integrated, not copied wholesale.
Private inputs, unsent outreach drafts and unrelated working archives are excluded.
The older dashboard publishing scripts do not rebuild this integrated site.
