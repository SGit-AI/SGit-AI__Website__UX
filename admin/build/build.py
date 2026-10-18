"""build.py: builds ux.sgit.ai from content/ and data/ into the repository root.

    python3 admin/build/build.py           # write every generated file
    python3 admin/build/build.py --check   # write nothing; exit 1 if any generated file is stale

Every page has a markdown twin beside it (x.html and x.md), generated from the same source, so the
two cannot drift. Every count, list and table about findings is generated from data/findings.json.
Stdlib only.
"""

import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import md                                                                       # noqa: E402

ROOT      = Path(__file__).resolve().parents[2]
CONTENT   = ROOT / 'content'
DATA      = ROOT / 'data'

SEVERITY  = ['high', 'medium', 'low']
STATUS    = ['open', 'partly-fixed', 'fixed']
KINDS     = ['failure', 'gap']
AREAS     = {
    'first-visit' : 'First visit',
    'navigation'  : 'Navigation',
    'findability' : 'Findability',
    'article'     : 'Article page',
    'feedback'    : 'Feedback',
    'money'       : 'Money',
    'personas'    : 'Personas',
    'trust'       : 'Trust',
    'consistency' : 'Consistency',
    'platform'    : 'Platform',
}
STATUS_LABEL = {'open': 'Open', 'partly-fixed': 'Partly fixed', 'fixed': 'Fixed'}
DIRECTIVE    = re.compile(r'^\{\{([a-z-]+)(?::(.*))?\}\}\s*$')


def esc(text):
    return html.escape(str(text), quote=True)


def load(name):
    return json.loads((DATA / name).read_text(encoding='utf-8'))


class Site:
    def __init__(self):
        self.site       = load('site.json')
        self.versions   = load('versions.json')['versions']
        self.findings   = load('findings.json')['findings']
        self.principles = load('principles.json')['principles']
        self.lab        = load('lab.json')
        self.version    = self.versions[0]['version']
        self.date       = self.versions[0]['date']
        self.by_id      = {f['id']: f for f in self.findings}
        self.principle  = {p['id']: p for p in self.principles}
        self.vault      = {v['slug']: v for v in self.lab['vaults']}
        self.pages      = []                                                    # dicts: path, title, description, md, html
        self.files      = {}                                                    # relative path -> text

    # ---------------------------------------------------------------- helpers

    def sorted_findings(self, items=None):
        items = self.findings if items is None else items
        return sorted(items, key=lambda f: (STATUS.index(f['status']), SEVERITY.index(f['severity']), f['id']))

    def select(self, spec):
        """'status=open;severity=high' -> matching findings, sorted."""
        items = self.findings
        for part in filter(None, (spec or '').split(';')):
            key, _, value = part.partition('=')
            allowed       = set(value.split(','))
            items         = [f for f in items if str(f.get(key.strip())) in allowed]
        return self.sorted_findings(items)

    def finding_href(self, f):
        return f'/findings/{f["id"]}.html'

    def vault_open_url(self, slug):
        return self.lab['open_url'] + self.vault[slug]['read_key'].replace(':', '%3A')

    def badge(self, kind, value, label=None):
        return f'<span class="badge badge--{kind}-{esc(value)}">{esc(label or value)}</span>'

    def badges(self, f):
        return ''.join([
            self.badge('status',   f['status'],   STATUS_LABEL[f['status']]),
            self.badge('severity', f['severity'], f['severity'].capitalize()),
            self.badge('kind',     f['kind'],     f['kind'].capitalize()),
        ])

    def counts(self, items=None):
        items = self.findings if items is None else items
        return {
            'total'     : len(items),
            'open'      : sum(f['status'] != 'fixed' for f in items),
            'fixed'     : sum(f['status'] == 'fixed' for f in items),
            'high_open' : sum(f['status'] != 'fixed' and f['severity'] == 'high' for f in items),
            'failures'  : sum(f['kind'] == 'failure' for f in items),
            'gaps'      : sum(f['kind'] == 'gap' for f in items),
            'sites'     : len({f['site'] for f in items}),
        }

    # ------------------------------------------------------------ directives

    def d_stats(self, arg):
        c     = self.counts()
        tiles = [
            (c['total'],     'findings in the register',            '/findings/'),
            (c['open'],      'still open',                          '/findings/?status=open,partly-fixed'),
            (c['high_open'], 'open and high severity',              '/findings/?status=open,partly-fixed&severity=high'),
            (c['fixed'],     'fixed, with the version that fixed it', '/findings/?status=fixed'),
        ]
        md_out   = '\n'.join(f'- **{n}** {label}' for n, label, _ in tiles)
        html_out = '<div class="stats">' + ''.join(
            f'<a class="stat" href="{esc(href)}"><span class="stat__n">{n}</span><span class="stat__label">{esc(label)}</span></a>'
            for n, label, href in tiles) + '</div>'
        return md_out, html_out

    def finding_row(self, f, compact=False):
        meta  = f'<span class="finding__site">{esc(f["site"])}</span> · {esc(AREAS[f["area"]])}'
        body  = '' if compact else f'<p class="finding__impact">{esc(f["impact"])}</p>'
        return (f'<li class="finding" data-site="{esc(f["site"])}" data-area="{esc(f["area"])}" '
                f'data-severity="{esc(f["severity"])}" data-status="{esc(f["status"])}" data-kind="{esc(f["kind"])}" '
                f'data-principle="{esc(f["principle"])}">'
                f'<div class="finding__top"><a class="finding__id" href="{self.finding_href(f)}">{esc(f["id"])}</a>{self.badges(f)}</div>'
                f'<a class="finding__title" href="{self.finding_href(f)}">{esc(f["title"])}</a>'
                f'<p class="finding__meta">{meta}</p>{body}</li>')

    def d_findings_list(self, arg):
        items    = self.select(arg)
        md_out   = '\n'.join(f'- [{f["id"]}]({self.finding_href(f)}) · {f["severity"]} · {STATUS_LABEL[f["status"]].lower()} · {f["title"]} ({f["site"]})' for f in items)
        html_out = '<ul class="findings findings--compact">' + ''.join(self.finding_row(f, compact=True) for f in items) + '</ul>'
        return md_out or '_None._', html_out or '<p><em>None.</em></p>'

    def d_findings_register(self, arg):
        items = self.sorted_findings()
        opts  = {
            'site'      : sorted({f['site'] for f in items}),
            'area'      : [a for a in AREAS if any(f['area'] == a for f in items)],
            'severity'  : SEVERITY,
            'status'    : STATUS,
            'kind'      : KINDS,
            'principle' : [p['id'] for p in self.principles],
        }
        labels = {
            'area'      : AREAS,
            'status'    : STATUS_LABEL,
            'principle' : {p['id']: p['title'] for p in self.principles},
        }
        selects = []
        for key, values in opts.items():
            options = ''.join(f'<option value="{esc(v)}">{esc(labels.get(key, {}).get(v, v))}</option>' for v in values)
            selects.append(f'<label class="filter"><span>{key.capitalize()}</span>'
                           f'<select name="{key}" data-filter="{key}"><option value="">Any</option>{options}</select></label>')
        form = (f'<details class="filters-box" data-open-wide><summary>Filter the register</summary>'
                f'<form class="filters" data-findings-filters action="/findings/" method="get" role="search" aria-label="Filter findings">'
                f'{"".join(selects)}'
                f'<label class="filter filter--q"><span>Words</span><input type="search" name="q" data-filter="q" placeholder="e.g. chip, tag, 404"></label>'
                f'<p class="filters__status" aria-live="polite"><span data-findings-count>{len(items)} of {len(items)}</span> findings · '
                f'<a href="/findings/" data-findings-reset>Clear</a> · the address is the filter: copy it to share this view</p></form></details>')
        md_rows  = ['| ID | Status | Severity | Kind | Site | Area | Finding |', '| --- | --- | --- | --- | --- | --- | --- |']
        md_rows += [f'| [{f["id"]}]({self.finding_href(f)}) | {STATUS_LABEL[f["status"]]} | {f["severity"]} | {f["kind"]} | {f["site"]} | {AREAS[f["area"]]} | {f["title"]} |' for f in items]
        html_out = form + '<ul class="findings" data-findings>' + ''.join(self.finding_row(f) for f in items) + '</ul>'
        html_out += '<p class="findings__empty" data-findings-empty hidden>No finding matches this filter. <a href="/findings/">Show all</a>.</p>'
        return '\n'.join(md_rows), html_out

    def d_by_site(self, arg):
        rows_md   = ['| Site | Findings | Open | Open, high | What it is |', '| --- | --- | --- | --- | --- |']
        rows_html = []
        for name, info in self.site['sites'].items():
            items = [f for f in self.findings if f['site'] == name]
            if not items:
                continue
            c    = self.counts(items)
            link = f'/findings/?site={name}'
            rows_md.append(f'| [{name}]({info["url"]}) | [{c["total"]}]({link}) | {c["open"]} | {c["high_open"]} | {info["what"]} |')
            rows_html.append(f'<tr><th scope="row"><a href="{esc(info["url"])}">{esc(name)}</a></th>'
                             f'<td><a href="{esc(link)}">{c["total"]}</a></td><td>{c["open"]}</td><td>{c["high_open"]}</td><td>{esc(info["what"])}</td></tr>')
        html_out = ('<div class="table-wrap"><table class="table--wide"><thead><tr><th scope="col">Site</th><th scope="col">Findings</th><th scope="col">Open</th>'
                    '<th scope="col">Open, high</th><th scope="col">What it is</th></tr></thead><tbody>' + ''.join(rows_html) + '</tbody></table></div>')
        return '\n'.join(rows_md), html_out

    def d_by_area(self, arg):
        rows_md   = ['| Area | Findings | Open |', '| --- | --- | --- |']
        rows_html = []
        for key, label in AREAS.items():
            items = [f for f in self.findings if f['area'] == key]
            if not items:
                continue
            c    = self.counts(items)
            link = f'/findings/?area={key}'
            rows_md.append(f'| {label} | [{c["total"]}]({link}) | {c["open"]} |')
            rows_html.append(f'<tr><th scope="row">{esc(label)}</th><td><a href="{esc(link)}">{c["total"]}</a></td><td>{c["open"]}</td></tr>')
        html_out = ('<div class="table-wrap"><table class="table--narrow"><thead><tr><th scope="col">Area</th><th scope="col">Findings</th>'
                    '<th scope="col">Open</th></tr></thead><tbody>' + ''.join(rows_html) + '</tbody></table></div>')
        return '\n'.join(rows_md), html_out

    def d_principles(self, arg):
        md_parts, html_parts = [], []
        for n, p in enumerate(self.principles, 1):
            items   = self.sorted_findings([f for f in self.findings if f['principle'] == p['id']])
            c       = self.counts(items)
            link    = f'/findings/?principle={p["id"]}'
            md_list = '\n'.join(f'- [{f["id"]}]({self.finding_href(f)}) · {STATUS_LABEL[f["status"]].lower()} · {f["title"]}' for f in items)
            md_parts.append(f'## {n}. {p["title"]}\n\n**The rule.** {p["rule"]}\n\n**Why.** {p["why"]}\n\n**The test.** {p["test"]}\n\n'
                            f'Broken by {c["total"]} findings, {c["open"]} open:\n\n{md_list}')
            html_parts.append(
                f'<section class="principle" id="{esc(p["id"])}"><h2><span class="principle__n">{n}</span> {esc(p["title"])}</h2>'
                f'<p class="principle__rule">{esc(p["rule"])}</p>'
                f'<dl class="principle__dl"><dt>Why</dt><dd>{esc(p["why"])}</dd><dt>The test</dt><dd>{esc(p["test"])}</dd></dl>'
                f'<p class="principle__count">Broken by <a href="{esc(link)}">{c["total"]} findings</a>, {c["open"]} open.</p>'
                f'<ul class="findings findings--compact">{"".join(self.finding_row(f, compact=True) for f in items)}</ul></section>')
        return '\n\n'.join(md_parts), ''.join(html_parts)

    def d_principles_index(self, arg):
        md_out = '\n'.join(f'{n}. [{p["title"]}](/principles/#{p["id"]})' for n, p in enumerate(self.principles, 1))
        lis    = ''.join(f'<li><a href="/principles/#{esc(p["id"])}">{esc(p["title"])}</a> '
                         f'<span class="muted">({self.counts([f for f in self.findings if f["principle"] == p["id"]])["open"]} open)</span></li>'
                         for p in self.principles)
        return md_out, f'<ol class="principles-index">{lis}</ol>'

    def d_lab_directions(self, arg):
        rows_md   = ['| Direction | The idea | Looks like |', '| --- | --- | --- |']
        rows_md  += [f'| **{d["label"]}** | {d["idea"]} | {d["looks"]} |' for d in self.lab['directions']]
        cards     = ''.join(f'<div class="direction direction--{esc(d["id"])}"><h3>{esc(d["label"])}</h3><p>{esc(d["idea"])}</p>'
                            f'<p class="muted">{esc(d["looks"])}</p></div>' for d in self.lab['directions'])
        return '\n'.join(rows_md), f'<div class="directions">{cards}</div>'

    def d_lab_vaults(self, arg):
        md_parts, html_parts = [], []
        for v in self.lab['vaults']:
            open_url = self.vault_open_url(v['slug'])
            routes   = ', '.join(f'`{r}`' for r in v.get('routes', []))
            md_parts.append(f'### {v["title"]} · `{v["id"]}`\n\n{v["answers"]}\n\n'
                            + (f'Routes: {routes}\n\n' if routes else '')
                            + f'- Open: [{v["slug"]} in the vault host]({open_url})\n- Read key: `{v["read_key"]}`\n- Clone: `sgit clone {v["read_key"]}`')
            route_html = ''.join(f'<code>{esc(r)}</code> ' for r in v.get('routes', []))
            html_parts.append(
                f'<section class="vault" id="{esc(v["slug"])}"><h3>{esc(v["title"])} <code class="vault__id">{esc(v["id"])}</code></h3>'
                f'<p>{esc(v["answers"])}</p>'
                + (f'<p class="vault__routes">{route_html}</p>' if route_html else '')
                + f'<p><a class="button" href="{esc(open_url)}" rel="noopener">Open in the vault host</a></p>'
                f'<details class="vault__key"><summary>Read key and clone command</summary>'
                f'<p class="muted">Read only. Derived one way from a vault key the publisher holds; it cannot become write access.</p>'
                f'<pre><code>sgit clone {esc(v["read_key"])}</code></pre></details></section>')
        return '\n\n'.join(md_parts), '<div class="vaults">' + ''.join(html_parts) + '</div>'

    def d_lab_compare(self, arg):
        md_parts, html_parts = [], []
        dirs = self.lab['directions']
        for c in self.lab['compare']:
            v = self.vault[c['vault']]
            md_parts.append(f'### {c["title"]}\n\n{c["tests"]}. Route `{c["route"]}` in [{v["title"]}](#{c["vault"]}).\n\n'
                            + '\n'.join(f'- [{d["label"]}](/lab/shots/{c["id"]}__{d["id"]}__390.webp)' for d in dirs))
            figs = ''.join(
                f'<figure class="shot"><a href="/lab/shots/{esc(c["id"])}__{esc(d["id"])}__390.webp">'
                f'<img src="/lab/shots/{esc(c["id"])}__{esc(d["id"])}__390.webp" alt="{esc(c["title"])}, {esc(d["label"])}, at phone width" loading="lazy" width="390"></a>'
                f'<figcaption>{esc(d["label"])}</figcaption></figure>' for d in dirs)
            html_parts.append(f'<section class="compare" id="compare-{esc(c["id"])}"><h3>{esc(c["title"])}</h3>'
                              f'<p class="muted">{esc(c["tests"])}. Route <code>{esc(c["route"])}</code> in <a href="#{esc(c["vault"])}">{esc(v["title"])}</a>.</p>'
                              f'<div class="shots">{figs}</div></section>')
        return '\n\n'.join(md_parts), ''.join(html_parts)

    def d_lab_decisions(self, arg):
        md_parts, html_parts = [], []
        for n, d in enumerate(self.lab['decisions'], 1):
            opts = [o['label'] for o in d['options']]
            md_parts.append(f'{n}. **{d["question"]}** {d["why"]} Options: ' + '; '.join(opts) + '.')
            html_parts.append(f'<li><strong>{esc(d["question"])}</strong> <span class="muted">{esc(d["why"])}</span>'
                              f'<ul class="options">{"".join(f"<li>{esc(o)}</li>" for o in opts)}</ul></li>')
        return '\n'.join(md_parts), f'<ol class="decisions">{"".join(html_parts)}</ol>'

    def d_lab_map(self, arg):
        rows      = [f for f in self.sorted_findings() if f.get('prototype')]
        rows_md   = ['| Finding | Status | Prototype |', '| --- | --- | --- |']
        rows_html = []
        for f in rows:
            p     = f['prototype']
            title = self.vault[p['vault']]['title']
            rows_md.append(f'| [{f["id"]}]({self.finding_href(f)}) {f["title"]} | {STATUS_LABEL[f["status"]]} | {title}: `{p["route"]}` |')
            rows_html.append(f'<tr><td><a href="{self.finding_href(f)}">{esc(f["id"])}</a> {esc(f["title"])}</td>'
                             f'<td>{self.badge("status", f["status"], STATUS_LABEL[f["status"]])}</td>'
                             f'<td><a href="#{esc(p["vault"])}">{esc(title)}</a> <code>{esc(p["route"])}</code></td></tr>')
        html_out = ('<div class="table-wrap"><table><thead><tr><th scope="col">Finding</th><th scope="col">Status on the live site</th>'
                    '<th scope="col">Prototype</th></tr></thead><tbody>' + ''.join(rows_html) + '</tbody></table></div>')
        return '\n'.join(rows_md), html_out

    def d_versions(self, arg):
        md_parts, html_parts = [], []
        for v in self.versions:
            changes = '\n'.join(f'- `{c.split(":")[0]}`:{":".join(c.split(":")[1:])}' if ':' in c else f'- {c}' for c in v['changes'])
            md_parts.append(f'## {v["version"]} · {v["date"]}\n\n{v["title"]}.\n\n{changes}')
        for v in self.versions:
            lis = ''.join(f'<li>{md.inline(("`" + c.split(":")[0] + "`:" + ":".join(c.split(":")[1:])) if ":" in c else c)}</li>' for c in v['changes'])
            html_parts.append(f'<section class="release" id="{esc(v["version"])}"><h2>{esc(v["version"])} <span class="muted">· {esc(v["date"])}</span></h2>'
                              f'<p>{esc(v["title"])}.</p><ul>{lis}</ul></section>')
        return '\n\n'.join(md_parts), ''.join(html_parts)

    def d_count(self, arg):
        n = str(self.counts()[arg])
        return n, n

    def d_version(self, arg):
        return self.version, f'<a href="/admin/versions.html">{esc(self.version)}</a>'

    def expand(self, source):
        """Expand {{directive}} lines. Returns (markdown for the twin, markdown with placeholders, {placeholder: html})."""
        twin, staged, blocks = [], [], {}
        for line in source.split('\n'):
            m = DIRECTIVE.match(line.strip())
            if not m:
                line = re.sub(r'\{\{(count|version):?([a-z_]*)\}\}', lambda x: getattr(self, 'd_' + x.group(1))(x.group(2))[0], line)
                twin.append(line)
                staged.append(line)
                continue
            fn = getattr(self, 'd_' + m.group(1).replace('-', '_'), None)
            if fn is None:
                raise SystemExit(f'unknown directive {{{{{m.group(1)}}}}}')
            md_out, html_out = fn(m.group(2))
            key              = f'@@BLOCK{len(blocks)}@@'
            blocks[key]      = html_out
            twin.append(md_out)
            staged.append(f'<div>{key}</div>')
        return '\n'.join(twin), '\n'.join(staged), blocks

    # ----------------------------------------------------------------- pages

    def twin_link(self, url, known):
        """In a markdown twin, point internal page links at the twin."""
        if url.startswith(('http://', 'https://', 'mailto:', '#')):
            return url
        if '?' in url:
            return url
        path, _, frag = url.partition('#')
        target        = path + 'index.md' if path.endswith('/') else re.sub(r'\.html$', '.md', path)
        return (target + ('#' + frag if frag else '')) if target.lstrip('/') in known else url

    def add_page(self, path, meta, body_md):
        twin_md, staged, blocks = self.expand(body_md)
        body_html, headings     = md.render(staged)
        for key, value in blocks.items():
            body_html = body_html.replace(f'<div>{key}</div>', value)
        self.pages.append({
            'path'        : path,
            'title'       : meta.get('title', ''),
            'description' : meta.get('description', ''),
            'layout'      : meta.get('layout', 'page'),
            'twin'        : meta.get('twin', 'yes') == 'yes',
            'sitemap'     : meta.get('sitemap', 'yes') == 'yes',
            'md'          : twin_md.strip() + '\n',
            'html'        : body_html,
            'toc'         : [h for h in headings if h[0] == 2] if meta.get('toc') == 'yes' else [],
        })

    def read_content(self):
        for src in sorted(CONTENT.rglob('*.md')):
            text = src.read_text(encoding='utf-8')
            meta = {}
            if text.startswith('---\n'):
                head, _, text = text[4:].partition('\n---\n')
                for line in head.split('\n'):
                    key, _, value = line.partition(':')
                    if key.strip():
                        meta[key.strip()] = value.strip()
            rel = src.relative_to(CONTENT).with_suffix('.html').as_posix()
            self.add_page(rel, meta, text.lstrip('\n'))

    def finding_pages(self):
        order = self.findings
        for i, f in enumerate(order):
            p     = self.principle[f['principle']]
            prev  = order[i - 1] if i > 0 else None
            nxt   = order[i + 1] if i + 1 < len(order) else None
            where = f['where'] if not f['where'].startswith('http') else f'<{f["where"]}>'
            site  = self.site['sites'].get(f['site'], {})
            rows  = [
                ('Status',       STATUS_LABEL[f['status']] + (f'. {f["status_note"]}' if f.get('status_note') else '')),
                ('Severity',     f['severity'].capitalize()),
                ('Kind',         'Failure: works against the reader' if f['kind'] == 'failure' else 'Gap: something the reader needs is not there'),
                ('Site',         f'[{f["site"]}]({site.get("url", "")})' if site else f['site']),
                ('Where',        where),
                ('Area',         f'[{AREAS[f["area"]]}](/findings/?area={f["area"]})'),
                ('Breaks',       f'[{p["title"]}](/principles/#{p["id"]})'),
                ('Observed',     f'{f["observed"]["date"]}, {f["observed"]["version"]}'),
                ('Last checked', f'{f["checked"]["date"]}, {f["checked"]["version"]}'),
                ('Source',       f'[{f["source"]["label"]}]({f["source"]["href"]})'),
            ]
            if f.get('prototype'):
                pr = f['prototype']
                rows.append(('Prototype', f'[{self.vault[pr["vault"]]["title"]}](/lab/#{pr["vault"]}), route `{pr["route"]}`, in three directions'))
            table = '| | |\n| --- | --- |\n' + '\n'.join(f'| **{k}** | {v.replace("|", chr(92) + "|")} |' for k, v in rows)
            nav   = []
            if prev:
                nav.append(f'Previous: [{prev["id"]} {prev["title"]}]({self.finding_href(prev)})')
            if nxt:
                nav.append(f'Next: [{nxt["id"]} {nxt["title"]}]({self.finding_href(nxt)})')
            body = (f'[Findings](/findings/) / {f["id"]}\n\n# {f["title"]}\n\n{{{{finding-badges:{f["id"]}}}}}\n\n'
                    f'## What we saw\n\n{f["evidence"]}\n\n## Why it matters\n\n{f["impact"]}\n\n## The fix\n\n{f["fix"]}\n\n'
                    f'## The record\n\n{table}\n\n' + '\n\n'.join(nav) + '\n')
            self.add_page(f'findings/{f["id"]}.html',
                          {'title': f'{f["id"]}: {f["title"]}', 'description': f['impact'], 'layout': 'finding'}, body)

    def d_finding_badges(self, arg):
        f = self.by_id[arg]
        return (f'{STATUS_LABEL[f["status"]]} · {f["severity"]} severity · {f["kind"]} · {f["site"]}',
                f'<p class="finding-head">{self.badges(f)}<span class="finding__site">{esc(f["site"])}</span></p>')

    # ---------------------------------------------------------------- layout

    def url_of(self, path):
        if path == 'index.html':
            return '/'
        return '/' + (path[:-len('index.html')] if path.endswith('/index.html') else path)

    def layout(self, page):
        s       = self.site
        url     = self.url_of(page['path'])
        section = '/' + url.strip('/').split('/')[0] + '/' if url != '/' else '/'
        nav     = ''.join(f'<li><a href="{esc(n["href"])}"' + (' aria-current="page"' if n['href'] == section else '') + f'>{esc(n["label"])}</a></li>'
                          for n in s['nav'])
        twin    = '/' + page['path'][:-5] + '.md'
        title   = f'{page["title"]} · {s["name"]}' if page['path'] != 'index.html' else f'{s["name"]} · {s["title"]}'
        toc     = ''
        if page['toc']:
            toc = ('<nav class="toc" aria-label="On this page"><details data-open-wide><summary class="toc__title">On this page</summary><ol>'
                   + ''.join(f'<li><a href="#{hid}">{md.inline(text)}</a></li>' for _, text, hid in page['toc']) + '</ol></details></nav>')
        twin_link = f'<a href="{esc(twin)}">This page as markdown</a> · ' if page['twin'] else ''
        network   = ' · '.join(f'<a href="{esc(n["url"])}" rel="noopener">{esc(n["label"])}</a>' for n in s['network'])
        scripts   = '<script src="/assets/findings.js" defer></script>' if 'data-findings' in page['html'] else ''
        canonical = s['origin'] + url
        return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(page['description'])}">
<link rel="canonical" href="{esc(canonical)}">
{f'<link rel="alternate" type="text/markdown" href="{esc(twin)}">' if page['twin'] else ''}
<link rel="alternate" type="text/plain" title="Site index for agents" href="/llms.txt">
<meta property="og:title" content="{esc(page['title'])}">
<meta property="og:description" content="{esc(page['description'])}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:site_name" content="{esc(s['name'])}">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css">
{scripts}
</head>
<body class="layout-{esc(page['layout'])}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap site-head__row">
    <a class="brand" href="/"><span class="brand__ux">ux</span><span class="brand__rest">.sgit.ai</span></a>
    <nav class="site-nav" aria-label="Main"><ul>{nav}</ul></nav>
  </div>
</header>
<main id="main" class="wrap main">
{toc}
<div class="content">
{page['html']}
</div>
</main>
<script>if (matchMedia('(min-width: 64rem)').matches) document.querySelectorAll('[data-open-wide]').forEach(d => d.open = true)</script>
<footer class="site-foot">
  <div class="wrap">
    <p><strong>{esc(s['name'])}</strong>: {esc(s['tagline'])}. By {esc(s['author'])}. <a href="/about/">Why this exists</a>.</p>
    <p>{twin_link}<a href="/llms.txt">For agents: llms.txt</a> · <a href="/data/findings.json">The register as JSON</a> · <a href="/admin/">How it is built</a> · <a href="/admin/versions.html">{esc(self.version)}</a> · <a href="{esc(s['repository'])}" rel="noopener">Source</a></p>
    <p class="muted">Part of the sgit.ai network: {network}. {esc(s['licence'])}</p>
  </div>
</footer>
</body>
</html>
'''

    # ------------------------------------------------------- agent files

    def llms_txt(self):
        s, c = self.site, self.counts()
        lines = [
            f'# {s["name"]}: {s["title"]}',
            '',
            f'> {s["tagline"]}. A register of UX failures and gaps across the sgit.ai sites, each measured on the',
            '> live site with a date and version, the principle it breaks, the fix, and (where one exists) a working',
            '> prototype of the fix in three design directions.',
            '',
            f'Site version: {self.version} ({self.date}). {s["licence"]} Author: {s["author"]}.',
            '',
            '## The headline',
            '',
            f'{c["total"]} findings across {c["sites"]} sites: {c["open"]} still open, {c["high_open"]} of them high severity, '
            f'{c["fixed"]} fixed. {c["failures"]} are failures (something works against the reader) and {c["gaps"]} are gaps '
            '(something the reader needs is not there). Every count on this site is generated from /data/findings.json.',
            '',
            '## Properties agents may rely on',
            '',
            '- /data/findings.json is the register. Every finding page, list, filter and count is generated from it at build, and the gate fails if a page is stale.',
            '- Every finding has a stable page at /findings/<ID>.html and a markdown twin at /findings/<ID>.md.',
            '- Every page has a markdown twin: replace .html with .md, or append index.md to a directory URL.',
            '- /findings/?site=&area=&severity=&status=&kind=&principle=&q= is a linkable filter (comma-separate values for OR).',
            '- Statuses carry the date and version they were last checked. Nothing here claims to be current beyond that date.',
            '- /llms-full.txt is the whole site in one fetch.',
            '',
            '## The pages',
            '',
        ]
        for p in sorted((p for p in self.pages if p['sitemap'] and not p['path'].startswith('findings/UX-')), key=lambda p: p['path']):
            lines.append(f'{self.url_of(p["path"])}  ({"/" + p["path"][:-5] + ".md"})')
            lines.append(f'  {p["description"]}')
        lines += ['', '## The findings', '']
        for f in self.sorted_findings():
            lines.append(f'{self.finding_href(f)}  [{f["status"]}, {f["severity"]}, {f["kind"]}, {f["site"]}] {f["title"]}')
        lines += ['', '## The sibling sites', '']
        lines += [f'{n["url"]}: {n["what"]}' for n in s['network']]
        lines += ['', f'Repository: {s["repository"]}', '']
        return '\n'.join(lines)

    def llms_full(self, llms):
        parts = [llms, '']
        for p in sorted(self.pages, key=lambda p: p['path']):
            if p['twin']:
                parts += ['', '=' * 78, f'{self.url_of(p["path"])}  ·  /{p["path"][:-5]}.md', '=' * 78, '', p['md']]
        return '\n'.join(parts)

    def sitemap(self):
        urls = ''.join(f'  <url><loc>{esc(self.site["origin"] + self.url_of(p["path"]))}</loc><lastmod>{self.date}</lastmod></url>\n'
                       for p in sorted(self.pages, key=lambda p: p['path']) if p['sitemap'])
        return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'

    # ------------------------------------------------------------------ run

    def build(self):
        self.read_content()
        self.finding_pages()
        known = {p['path'][:-5] + '.md' for p in self.pages if p['twin']}
        for p in self.pages:
            p['md'] = re.sub(r'(?<!!)\]\(([^)\s]+)\)', lambda m: '](' + self.twin_link(m.group(1), known) + ')', p['md'])
            self.files[p['path']] = self.layout(p)
            if p['twin']:
                self.files[p['path'][:-5] + '.md'] = p['md']
        llms = self.llms_txt()
        self.files['llms.txt']      = llms
        self.files['llms-full.txt'] = self.llms_full(llms)
        self.files['sitemap.xml']   = self.sitemap()
        self.files['robots.txt']    = f'User-agent: *\nAllow: /\n\nSitemap: {self.site["origin"]}/sitemap.xml\n'
        return self.files


def generated_paths():
    """Every path the build owns, so the gate can find orphans."""
    return set(Site().build())


def main():
    check = '--check' in sys.argv
    files = Site().build()
    stale = []
    for rel, text in sorted(files.items()):
        path = ROOT / rel
        if check:
            if not path.exists() or path.read_text(encoding='utf-8') != text:
                stale.append(rel)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding='utf-8') != text:
            path.write_text(text, encoding='utf-8')
    if check:
        if stale:
            print(f'STALE: {len(stale)} generated files differ from the build: ' + ', '.join(stale[:10]))
            sys.exit(1)
        print(f'fresh: {len(files)} generated files match the build')
    else:
        print(f'built {len(files)} files ({sum(1 for f in files if f.endswith(".html"))} pages)')


if __name__ == '__main__':
    main()
