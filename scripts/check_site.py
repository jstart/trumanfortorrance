#!/usr/bin/env python3
"""Check local site links, routed anchors and Git-tracked evidence without dependencies.

External URLs are intentionally not fetched. Run sync_hillside.py --check separately
for generated-content drift and imported evidence hashes.
"""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.duplicates = []
        self.references = []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.duplicates.append(attrs['id'])
            self.ids.add(attrs['id'])
        for name in ['href', 'src']:
            if attrs.get(name):
                self.references.append(attrs[name])
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            match = re.search(r'url=(.*)', attrs.get('content', ''), re.I)
            if match:
                self.references.append(match.group(1).strip())


def main():
    tracked = set(subprocess.check_output(
        ['git', '-C', str(ROOT), 'ls-files', '-z']).decode().split('\0')) - {''}
    pages = {ROOT / name: Page(ROOT / name) for name in tracked
             if name.endswith('.html') and (ROOT / name).is_file()}
    references = []
    errors = []
    for file, page in pages.items():
        errors.extend(f'{file.relative_to(ROOT)}: duplicate ID {id}' for id in page.duplicates)
        references.extend((file, url) for url in page.references)
    for name in tracked:
        file = ROOT / name
        if file.suffix == '.md' and file.is_file():
            references.extend((file, url) for url in
                              re.findall(r'\]\(([^)]+)\)', file.read_text(encoding='utf-8')))
    guide = ROOT / 'hillside-overlay'
    for row in json.loads((guide / 'sources.json').read_text(encoding='utf-8')):
        if row.get('local'):
            references.append((guide / 'sources.json', row['local']))
    for row in json.loads((guide / 'asset-provenance.json').read_text(encoding='utf-8'))['assets']:
        references.append((guide / 'asset-provenance.json', row['file']))
    targets = set()
    count = 0
    for file, raw in references:
        url = urlsplit(raw)
        if url.scheme or url.netloc:
            continue
        target = (ROOT / unquote(url.path).lstrip('/') if url.path.startswith('/')
                  else file.parent / unquote(url.path)) if url.path else file
        target = target.resolve()
        if target.is_dir():
            target = target / 'index.html'
        if not target.is_relative_to(ROOT):
            errors.append(f'{file.relative_to(ROOT)}: link outside repository: {raw}')
            continue
        name = str(target.relative_to(ROOT))
        count += 1
        targets.add(name)
        if not target.is_file() or name not in tracked:
            errors.append(f'{file.relative_to(ROOT)}: missing or untracked: {raw}')
            continue
        if url.fragment and target in pages:
            fragment = unquote(url.fragment)
            ids = pages[target].ids
            # Senior guide hashes select language sections or cards through main.js.
            if not any(id in ids for id in [fragment, 'lang-' + fragment, 'en-' + fragment]):
                errors.append(f'{file.relative_to(ROOT)}: missing anchor: {raw}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Checked {count} local references to {len(targets)} tracked files; no missing links or duplicate IDs.')


if __name__ == '__main__':
    main()
