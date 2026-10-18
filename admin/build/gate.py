"""gate.py: the release gate for ux.sgit.ai. Must print GATE PASS before anything is published.

    python3 admin/build/gate.py

Stdlib only. Each check prints one line; any failure exits 1.
"""

import json
import re
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build                                                                    # noqa: E402

ROOT     = build.ROOT
FAILURES = []
FIELDS   = ['id', 'title', 'product', 'where', 'area', 'problems', 'visibility', 'recommendation', 'kind', 'severity', 'status', 'principle',
            'observed', 'checked', 'evidence', 'impact', 'fix', 'prototype', 'source']
SKIP     = {'.git', 'content', 'admin/build', '.github', 'node_modules'}


def check(name, problems):
    problems = list(problems)
    print(('ok    ' if not problems else 'FAIL  ') + name + ('' if not problems else f' ({len(problems)})'))
    for p in problems[:12]:
        print('        ' + p)
    if problems:
        FAILURES.append(name)


def tracked_files():
    for path in ROOT.rglob('*'):
        rel = path.relative_to(ROOT).as_posix()
        if path.is_file() and not any(rel == s or rel.startswith(s + '/') for s in SKIP):
            yield rel, path


# ------------------------------------------------------------------ checks

def check_fresh(site, files):
    stale = [rel for rel, text in files.items()
             if not (ROOT / rel).exists() or (ROOT / rel).read_text(encoding='utf-8') != text]
    check('generated files are fresh (run admin/build/build.py)', stale)
    orphans = [rel for rel, _ in tracked_files() if rel.endswith('.html') and rel not in files]
    check('every .html is generated', orphans)


def check_findings(site):
    problems = []
    ids      = set()
    products = set(site.products)
    tax      = {k: {t['id'] for t in v} for k, v in site.taxonomy.items() if isinstance(v, list)}
    vaults   = set(site.vault)
    for n, f in enumerate(site.findings):
        tag = f.get('id', f'#{n}')
        for key in FIELDS:
            if key not in f:
                problems.append(f'{tag}: missing {key}')
        if not re.fullmatch(r'UX-\d{3,}', f.get('id', '')):
            problems.append(f'{tag}: id must look like UX-001')
        if f.get('id') in ids:
            problems.append(f'{tag}: duplicate id')
        ids.add(f.get('id'))
        if not f.get('problems') or not set(f.get('problems', [])) <= tax['problems']:
            problems.append(f'{tag}: problems {f.get("problems")!r} must be a non-empty list from data/taxonomy.json')
        for img in f.get('images', []):
            if not (ROOT / img.get('src', '').lstrip('/')).is_file() or not img.get('alt') or not img.get('caption'):
                problems.append(f'{tag}: image {img.get("src")!r} is missing, or has no alt text or caption')
        checks = [('product', products), ('visibility', tax['visibility']), ('recommendation', tax['recommendations']), ('area', set(build.AREAS)), ('kind', set(build.KINDS)),
                  ('severity', set(build.SEVERITY)), ('status', set(build.STATUS)), ('principle', set(site.principle))]
        for key, allowed in checks:
            if f.get(key) not in allowed:
                problems.append(f'{tag}: {key} {f.get(key)!r} is not one of {sorted(allowed)}')
        for key in ('observed', 'checked'):
            stamp = f.get(key) or {}
            try:
                date.fromisoformat(stamp.get('date', ''))
            except ValueError:
                problems.append(f'{tag}: {key}.date {stamp.get("date")!r} is not YYYY-MM-DD')
            if not stamp.get('version'):
                problems.append(f'{tag}: {key}.version is empty')
        if (f.get('checked') or {}).get('date', '') < (f.get('observed') or {}).get('date', ''):
            problems.append(f'{tag}: checked before it was observed')
        proto = f.get('prototype')
        if proto and proto.get('vault') not in vaults:
            problems.append(f'{tag}: prototype vault {proto.get("vault")!r} is not in data/lab.json')
        for key in ('title', 'evidence', 'impact', 'fix'):
            if len(str(f.get(key, '')).strip()) < 10:
                problems.append(f'{tag}: {key} is too short to be evidence')
    check(f'findings.json: {len(site.findings)} findings well formed', problems)

    numbers = [int(f['id'][3:]) for f in site.findings if re.fullmatch(r'UX-\d+', f.get('id', ''))]
    check('finding ids run 1..n with no gaps', [] if sorted(numbers) == list(range(1, len(numbers) + 1)) else ['ids are not 1..n'])


def check_taxonomy(site):
    used = {
        'problems'        : {p for f in site.findings for p in f['problems']},
        'visibility'      : {f['visibility'] for f in site.findings},
        'recommendations' : {f['recommendation'] for f in site.findings},
    }
    check('every taxonomy value and product is used by at least one finding',
          [f'{k}: {t["id"]}' for k in used for t in site.taxonomy[k] if t['id'] not in used[k]]
          + [f'products: {k}' for k in site.products if k != 'sgit.ai' and k not in {f['product'] for f in site.findings}])


def check_principles(site):
    used = {f['principle'] for f in site.findings}
    check('every principle is broken by at least one finding',
          [p['id'] for p in site.principles if p['id'] not in used])
    missing = [f'{p["id"]}: {k}' for p in site.principles for k in ('id', 'title', 'rule', 'why', 'test') if not p.get(k)]
    check('every principle has a rule, a reason and a test', missing)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if a.get(key):
                self.links.append(a[key])


def resolve(url):
    path = url.split('#')[0].split('?')[0]
    if path.endswith('/'):
        path += 'index.html'
    return path.lstrip('/')


def check_links(site, files):
    pages    = {rel: text for rel, text in files.items() if rel.endswith('.html')}
    parsed   = {}
    for rel, text in pages.items():
        p = Links()
        p.feed(text)
        parsed[rel] = p
    on_disk  = {rel for rel, _ in tracked_files()} | set(files)
    problems = []
    for rel, p in parsed.items():
        for url in p.links:
            if url.startswith(('http://', 'https://', 'mailto:', 'data:')):
                continue
            if url.startswith('#'):
                if url[1:] and url[1:] not in p.ids:
                    problems.append(f'{rel}: {url} has no target')
                continue
            if not url.startswith('/'):
                problems.append(f'{rel}: relative link {url} (use root-relative)')
                continue
            target = resolve(url)
            if target not in on_disk:
                problems.append(f'{rel}: {url} goes nowhere')
                continue
            frag = url.partition('#')[2]
            if frag and target in parsed and frag not in parsed[target].ids:
                problems.append(f'{rel}: {url} anchor missing')
    check(f'internal links and anchors resolve ({sum(len(p.links) for p in parsed.values())} links)', problems)

    for f in site.findings:
        target = resolve(f['source']['href'])
        frag   = f['source']['href'].partition('#')[2]
        if target not in parsed or (frag and frag not in parsed[target].ids):
            problems.append(f'{f["id"]}: source {f["source"]["href"]} goes nowhere')
    check('every finding source resolves', [p for p in problems if ': source ' in p])

    twins = [rel for rel in pages if rel != '404.html' and rel[:-5] + '.md' not in files]
    check('every page has a markdown twin', twins)


def check_colour():
    css      = (ROOT / 'assets/site.css').read_text(encoding='utf-8')
    head, _, rest = css.partition('/* tokens:end */')
    if '/* tokens:start */' not in head:
        check('colour only in the token block', ['assets/site.css has no tokens:start/tokens:end block'])
        return
    literal  = re.compile(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|oklch)\(')
    problems = [f'assets/site.css: {m.group(0)}' for m in literal.finditer(rest)]
    for rel, path in tracked_files():
        if rel.endswith(('.html', '.js')) and rel not in ('assets/favicon.svg',):
            text = path.read_text(encoding='utf-8')
            problems += [f'{rel}: {m.group(0)}' for m in re.finditer(r'style="[^"]*(?:#[0-9a-fA-F]{3,8}|rgb\()', text)]
    check('colour only in the token block of assets/site.css', problems)


def check_version(site, files):
    v        = site.version
    problems = []
    for rel in ('llms.txt', 'index.md'):
        if v not in files.get(rel, '') and rel == 'llms.txt':
            problems.append(f'{rel} does not state {v}')
    for rel, text in files.items():
        if rel.endswith('.html'):
            found = set(re.findall(r'>(v\d+\.\d+\.\d+)</a>', text))
            if found and found != {v}:
                problems.append(f'{rel} shows {sorted(found)}')
    versions = [x['version'] for x in site.versions]
    if len(set(versions)) != len(versions):
        problems.append('duplicate versions in data/versions.json')
    check(f'version {v} agrees everywhere', problems)


def check_lab(site):
    problems = []
    for c in site.lab['compare']:
        for d in site.lab['directions']:
            shot = ROOT / 'lab/shots' / f'{c["id"]}__{d["id"]}__390.webp'
            if not shot.exists():
                problems.append(f'missing {shot.relative_to(ROOT)}')
    for v in site.lab['vaults']:
        if not re.fullmatch(r'sgit_public_read_[0-9a-f]{64}:' + re.escape(v['id']), v['read_key']):
            problems.append(f'{v["slug"]}: read key is not a published read key for {v["id"]}')
    check('lab screenshots exist and every vault key is a published read key', problems)


def check_credentials():
    """Only published read keys may appear in tracked files: no private read keys, no vault keys, no tokens."""
    bad      = re.compile(r'sgit_private_read_[0-9a-f]|sgit_(?:vault|write|admin)_[0-9a-z]|\bsk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}')
    problems = []
    for rel, path in tracked_files():
        if path.suffix in ('.webp', '.png', '.jpg', '.svg', '.ico'):
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        problems += [f'{rel}: {m.group(0)[:24]}…' for m in bad.finditer(text)]
    check('no write credentials or private keys in tracked files', problems)


def main():
    site  = build.Site()
    check_findings(site)
    check_principles(site)
    check_taxonomy(site)
    if FAILURES:
        print('\nGATE FAIL: the data is malformed, so nothing else was checked')
        sys.exit(1)
    files = site.build()
    check_fresh(site, files)
    check_links(site, files)
    check_colour()
    check_version(site, files)
    check_lab(site)
    check_credentials()
    if FAILURES:
        print(f'\nGATE FAIL: {len(FAILURES)} check(s) failed')
        sys.exit(1)
    print('\nGATE PASS')


if __name__ == '__main__':
    main()
