"""md.py: the small markdown renderer this site is built with.

Stdlib only, so the build runs anywhere Python 3.11+ does. It covers what the
content uses and nothing more: headings (with ids), paragraphs, ordered and
unordered lists (with [ ] / [x] task items), tables, fenced code, blockquotes,
rules, raw HTML blocks, and inline code, bold, italic, links, images and
autolinks. Anything else is rendered as text, escaped.
"""

import html
import re

_ENTITY      = re.compile(r'&(#\d+|#x[0-9a-fA-F]+|[a-zA-Z]+);')
_CODE_SPAN   = re.compile(r'`([^`]+)`')
_IMAGE       = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)\)')
_LINK        = re.compile(r'\[((?:[^\[\]]|\[[^\]]*\])+)\]\(([^)\s]+)\)')
_AUTOLINK    = re.compile(r'<(https?://[^>\s]+)>')
_BOLD        = re.compile(r'\*\*(.+?)\*\*')
_ITALIC_STAR = re.compile(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])')
_ITALIC_US   = re.compile(r'(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])')
_HEADING     = re.compile(r'^(#{1,6})\s+(.*?)\s*#*\s*$')
_OL_ITEM     = re.compile(r'^(\s*)(\d+)[.)]\s+(.*)$')
_UL_ITEM     = re.compile(r'^(\s*)[-*+]\s+(.*)$')
_TABLE_SEP   = re.compile(r'^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$')
_HR          = re.compile(r'^\s*(-{3,}|\*{3,}|_{3,})\s*$')
_BLOCK_TAGS  = ('<div', '<figure', '<section', '<aside', '<table', '<nav', '<details',
                '<p ', '<p>', '<ul', '<ol', '<form', '<dl', '<!--', '<h2', '<h3', '<pre')


def slugify(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[`*_\[\]()]', '', text).lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    return re.sub(r'[\s-]+', '-', text).strip('-')


def _escape(text):
    """Escape for HTML, leaving entities that are already written as entities."""
    out, last = [], 0
    for m in _ENTITY.finditer(text):
        out.append(html.escape(text[last:m.start()], quote=False))
        out.append(m.group(0))
        last = m.end()
    out.append(html.escape(text[last:], quote=False))
    return ''.join(out)


def inline(text, link_fn=None):
    """Render one line of inline markdown to HTML."""
    stash = []

    def keep(fragment):
        stash.append(fragment)
        return f'\x00{len(stash) - 1}\x00'

    text = re.sub(r'\\([\\`*_\[\]()#+\-.!|<>])', lambda m: keep(_escape(m.group(1))), text)
    text = _CODE_SPAN.sub(lambda m: keep(f'<code>{html.escape(m.group(1), quote=False)}</code>'), text)

    def href(url):
        url = link_fn(url) if link_fn else url
        return html.escape(url, quote=True)

    def image(m):
        alt, url = m.group(1), m.group(2)
        return keep(f'<img src="{href(url)}" alt="{html.escape(alt, quote=True)}" loading="lazy">')

    def link(m):
        label, url = m.group(1), m.group(2)
        external = url.startswith('http://') or url.startswith('https://')
        rel      = ' rel="noopener"' if external else ''
        return keep(f'<a href="{href(url)}"{rel}>{inline(label, link_fn)}</a>')

    text = _IMAGE.sub(image, text)
    text = _LINK.sub(link, text)
    text = _AUTOLINK.sub(lambda m: keep(f'<a href="{href(m.group(1))}" rel="noopener">{html.escape(m.group(1))}</a>'), text)
    text = _escape(text)
    text = _BOLD.sub(r'<strong>\1</strong>', text)
    text = _ITALIC_STAR.sub(r'<em>\1</em>', text)
    text = _ITALIC_US.sub(r'<em>\1</em>', text)
    return re.sub(r'\x00(\d+)\x00', lambda m: stash[int(m.group(1))], text)


def _split_row(line):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|') and not line.endswith('\\|'):
        line = line[:-1]
    cells, cur, i = [], '', 0
    while i < len(line):
        ch = line[i]
        if ch == '\\' and i + 1 < len(line) and line[i + 1] == '|':
            cur += '|'
            i   += 2
            continue
        if ch == '|':
            cells.append(cur.strip())
            cur = ''
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def _task(text):
    m = re.match(r'^\[([ xX])\]\s+(.*)$', text)
    if not m:
        return None, text
    return m.group(1).lower() == 'x', m.group(2)


def render(source, link_fn=None, heading_ids=True):
    """Render a markdown document to HTML. Returns (html, headings)."""
    lines    = source.replace('\r\n', '\n').split('\n')
    out      = []
    headings = []
    used_ids = set()
    i        = 0

    def para(buf):
        if buf:
            out.append(f'<p>{inline(" ".join(s.strip() for s in buf), link_fn)}</p>')

    buf = []
    while i < len(lines):
        line = lines[i]

        if not line.strip():
            para(buf); buf = []
            i += 1
            continue

        if line.startswith('```'):
            para(buf); buf = []
            lang = line[3:].strip()
            code = []
            i   += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i])
                i += 1
            i += 1
            cls = f' class="lang-{html.escape(lang)}"' if lang else ''
            out.append(f'<pre><code{cls}>{html.escape(chr(10).join(code), quote=False)}</code></pre>')
            continue

        m = _HEADING.match(line)
        if m:
            para(buf); buf = []
            level = len(m.group(1))
            text  = m.group(2)
            body  = inline(text, link_fn)
            if heading_ids and level >= 2:
                hid = slugify(text) or f'h{len(headings)}'
                base, n = hid, 2
                while hid in used_ids:
                    hid = f'{base}-{n}'
                    n  += 1
                used_ids.add(hid)
                headings.append((level, text, hid))
                out.append(f'<h{level} id="{hid}">{body}</h{level}>')
            else:
                out.append(f'<h{level}>{body}</h{level}>')
            i += 1
            continue

        if _HR.match(line) and not buf:
            out.append('<hr>')
            i += 1
            continue

        if line.lstrip().startswith(_BLOCK_TAGS):
            para(buf); buf = []
            block = []
            while i < len(lines) and lines[i].strip():
                block.append(lines[i])
                i += 1
            out.append('\n'.join(block))
            continue

        if '|' in line and i + 1 < len(lines) and _TABLE_SEP.match(lines[i + 1]):
            para(buf); buf = []
            head = _split_row(line)
            i   += 2
            rows = []
            while i < len(lines) and lines[i].strip() and '|' in lines[i]:
                rows.append(_split_row(lines[i]))
                i += 1
            th    = ''.join(f'<th scope="col">{inline(c, link_fn)}</th>' for c in head)
            thead = f'<thead><tr>{th}</tr></thead>' if any(head) else ''
            tb    = ''.join('<tr>' + ''.join(f'<td>{inline(c, link_fn)}</td>' for c in r) + '</tr>' for r in rows)
            cls   = ' class="table--wide"' if len(head) > 3 else ''
            out.append(f'<div class="table-wrap"><table{cls}>{thead}<tbody>{tb}</tbody></table></div>')
            continue

        if line.startswith('>'):
            para(buf); buf = []
            quote = []
            while i < len(lines) and lines[i].startswith('>'):
                quote.append(lines[i][1:].lstrip() if len(lines[i]) > 1 else '')
                i += 1
            inner, _ = render('\n'.join(quote), link_fn, heading_ids=False)
            out.append(f'<blockquote>{inner}</blockquote>')
            continue

        ul, ol = _UL_ITEM.match(line), _OL_ITEM.match(line)
        if (ul or ol) and not buf:
            ordered = bool(ol) and not ul
            items   = []
            while i < len(lines):
                cur = lines[i]
                mu, mo = _UL_ITEM.match(cur), _OL_ITEM.match(cur)
                if ordered and mo:
                    items.append(mo.group(3))
                elif not ordered and mu:
                    items.append(mu.group(2))
                elif cur.startswith('  ') and cur.strip() and items:
                    items[-1] += ' ' + cur.strip()
                else:
                    break
                i += 1
            tag    = 'ol' if ordered else 'ul'
            parts  = []
            checks = False
            for item in items:
                done, text = _task(item)
                if done is None:
                    parts.append(f'<li>{inline(text, link_fn)}</li>')
                else:
                    checks = True
                    mark   = 'done' if done else 'todo'
                    label  = 'Done' if done else 'To do'
                    parts.append(f'<li class="task task--{mark}"><span class="task__box" aria-label="{label}"></span>{inline(text, link_fn)}</li>')
            cls = ' class="tasks"' if checks else ''
            out.append(f'<{tag}{cls}>{"".join(parts)}</{tag}>')
            continue

        buf.append(line)
        i += 1

    para(buf)
    return '\n'.join(out), headings
