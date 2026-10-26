#!/usr/bin/env python3
"""Generate committed hillside cards, source ledger and CSVs from canonical JSON.

Run from any directory. --check reports drift without changing files. Uses only
Python's standard library; GitHub Pages serves the committed HTML directly.
"""
import argparse
import csv
import hashlib
import html
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / 'hillside-overlay'
CASE_FIELDS = [
    ('Case', 'id'), ('Review scope', 'tier'), ('Protection', 'protected_scope'),
    ('Review retained', 'retained_review'), ('Design changes', 'design_change'),
    ('Decision', 'decision'), ('Permit stage', 'construction'),
    ('Still unknown', 'unknown'),
]


def escape(value):
    return html.escape(str(value), quote=True)


def read_json(name):
    return json.loads((GUIDE / name).read_text(encoding='utf-8'))


def render_cases(cases):
    cards = []
    for case in cases:
        lines = [f'<section class="card" id="case-{escape(case["id"])}">',
                 f'  <h3>{escape(case["address"])}</h3>', '  <dl>']
        for label, key in CASE_FIELDS:
            lines.append(f'    <dt>{label}</dt><dd>{escape(case[key])}</dd>')
        if case.get('notes'):
            lines.append(f'    <dt>Vote-tally limit</dt><dd>{escape(case["notes"])}</dd>')
        lines.extend(['  </dl>', '  <span class="citations">'])
        for source_id in case['sources']:
            lines.append(f'    <a href="#source-{escape(source_id)}">{escape(source_id)}</a>')
        lines.extend(['  </span>', '</section>'])
        cards.append('\n'.join(lines))
    return '\n'.join(cards)


def render_sources(sources):
    cards = []
    for source in sources:
        lines = [f'<section class="card" id="source-{escape(source["id"])}">',
                 f'  <h3>{escape(source["id"])}: {escape(source["title"])}</h3>',
                 f'  <p>{escape(source["locator"])}</p>', '  <p class="card__links">']
        for key, label in [('url', 'Official source'), ('local', 'Archived evidence')]:
            if source.get(key):
                lines.append(f'    <a class="btn" href="{escape(source[key])}">{label}</a>')
        lines.extend(['  </p>', '</section>'])
        cards.append('\n'.join(lines))
    return '\n'.join(cards)


def render_reviews(reviews):
    rows = []
    for review in reviews:
        source = (f'<a href="{escape(review["url"])}">{escape(review["id"])}: '
                  f'{escape(review["source_name"])}</a><br>'
                  f'<small>{escape(review["project"])}</small>')
        values = [escape(review['meeting_date']), source,
                  *[escape(review[key]) for key in
                    ['classification', 'authority', 'pages', 'finding', 'review_scope']]]
        rows.append('<tr>\n' + '\n'.join(f'  <td>{value}</td>' for value in values) + '\n</tr>')
    return '\n'.join(rows)


def render_csv(rows):
    fields = list(dict.fromkeys(key for row in rows for key in row))
    output = io.StringIO(newline='')
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    for row in rows:
        writer.writerow({key: '; '.join(value) if isinstance(value, list) else value
                         for key, value in row.items()})
    return output.getvalue()


def replace_block(text, name, content):
    begin = f'<!-- BEGIN GENERATED {name} -->'
    end = f'<!-- END GENERATED {name} -->'
    if text.count(begin) != 1 or text.count(end) != 1:
        raise ValueError(f'Expected one generated block: {name}')
    prefix, tail = text.split(begin)
    _, suffix = tail.split(end)
    return prefix + begin + '\n' + content + '\n' + end + suffix


def validate(cases, sources, reviews):
    for label, records in [('cases', cases), ('sources', sources), ('reviews', reviews)]:
        ids = [str(row['id']) for row in records]
        if len(ids) != len(set(ids)):
            raise ValueError(f'Duplicate IDs in {label}')
    source_ids = {source['id'] for source in sources}
    for case in cases:
        missing = set(case['sources']) - source_ids
        if missing:
            raise ValueError(f'{case["id"]}: unknown sources {sorted(missing)}')
    for source in sources:
        if source.get('local') and not (GUIDE / source['local']).is_file():
            raise ValueError(f'Missing local evidence: {source["local"]}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='fail on drift; do not write')
    args = parser.parse_args()
    cases, sources, reviews = [read_json(name) for name in
                               ['comparison.json', 'sources.json', 'source_reviews.json']]
    validate(cases, sources, reviews)
    index = (GUIDE / 'index.html').read_text(encoding='utf-8')
    index = replace_block(index, 'cases', render_cases(cases))
    index = replace_block(index, 'sources', render_sources(sources))
    review = replace_block((GUIDE / 'review.html').read_text(encoding='utf-8'),
                           'reviews', render_reviews(reviews))
    outputs = {'index.html': index, 'review.html': review,
               'comparison.csv': render_csv(cases), 'source_reviews.csv': render_csv(reviews)}
    # Original hashes retain the import provenance; sha256 describes deployed bytes.
    provenance = read_json('asset-provenance.json')
    for item in provenance['assets']:
        file = item['file']
        data = outputs[file].encode('utf-8') if file in outputs else (GUIDE / file).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest != item['sha256']:
            maintained = {'comparison.json', 'sources.json', 'source_reviews.json',
                          'comparison.csv', 'source_reviews.csv'}
            if file not in maintained:
                raise ValueError(f'Imported evidence hash mismatch: {file}')
            item.setdefault('original_sha256', item['sha256'])
            item['sha256'] = digest
            item['adaptation'] = 'Maintained JSON or generated CSV; original supplied hash retained.'
    outputs['asset-provenance.json'] = json.dumps(provenance, indent=2) + '\n'
    stale = []
    for name, text in outputs.items():
        file = GUIDE / name
        if file.read_text(encoding='utf-8') != text:
            stale.append(name)
            if not args.check:
                file.write_text(text, encoding='utf-8')
    if args.check and stale:
        parser.exit(1, 'Out of date: ' + ', '.join(stale) + '\nRun python3 scripts/sync_hillside.py\n')
    print(('Checked' if args.check else 'Synchronized') +
          f' {len(cases)} cases, {len(sources)} sources and {len(reviews)} ledger entries.')


if __name__ == '__main__':
    main()
