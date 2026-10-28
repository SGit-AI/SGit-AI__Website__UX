/**
 * @module finder
 * Type-ahead search over the whole register, in two places: the field on the home page and a palette that opens
 * from any page (the Search button, or / or Ctrl/Cmd+K). The page works without it: both are plain links and forms
 * that go to /findings/?q=. The best match is highlighted as you type, the arrow keys move, Enter opens it.
 */
(() => {
    const INDEX = '/assets/search.json'
    const SHOWN = 7
    let   index = null
    const load  = () => index || (index = fetch(INDEX).then(r => r.json()).catch(() => []))

    const esc  = (text) => text.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]))
    const mark = (text, words) => {
        if (!words.length) return esc(text)
        const re = new RegExp('(' + words.map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')', 'gi')
        return esc(text).replace(re, '<mark>$1</mark>')
    }

    const score = (item, words) => {
        const title = item.t.toLowerCase(), id = item.i.toLowerCase(), meta = item.m.toLowerCase(), more = item.x.toLowerCase()
        let total = 0
        for (const w of words) {
            if (id === w)                        total += 50
            else if (id.startsWith(w))           total += 30
            else if (title.startsWith(w))        total += 20
            else if (title.includes(' ' + w))    total += 14
            else if (title.includes(w))          total += 10
            else if (meta.includes(w))           total += 5
            else if (more.includes(w))           total += 2
            else return 0
        }
        return total
    }

    const search = (items, query) => {
        const words = query.toLowerCase().split(/\s+/).filter(Boolean)
        if (!words.length) return { words, hits: items.slice(0, SHOWN), total: items.length, start: true }
        const hits = items.map((item, n) => ({ item, n, s: score(item, words) })).filter(h => h.s)
                          .sort((a, b) => b.s - a.s || a.n - b.n)
        return { words, hits: hits.slice(0, SHOWN).map(h => h.item), total: hits.length, start: false }
    }

    const attach = (root, { startList }) => {
        const input = root.querySelector('[data-finder-input]')
        const list  = root.querySelector('[data-finder-list]')
        let   rows  = [], at = 0

        const choose = (n) => {
            at = (n + rows.length) % Math.max(rows.length, 1)
            rows.forEach((row, i) => {
                row.setAttribute('aria-selected', String(i === at))
                if (i === at) { input.setAttribute('aria-activedescendant', row.id); row.scrollIntoView({ block: 'nearest' }) }
            })
        }

        const draw = async () => {
            const query = input.value.trim()
            if (!query && !startList) { list.hidden = true; rows = []; return }
            const { words, hits, total, start } = search(await load(), query)
            const head  = start ? '<li class="finder__empty">Most serious open findings first. Type to search all of it.</li>' : ''
            const body  = hits.map((h, i) =>
                `<li role="presentation"><a class="finder__opt" role="option" id="${list.id || 'fl'}-o${i}" href="${esc(h.u)}" aria-selected="false">` +
                `<span class="finder__opt-title">${h.i && h.k !== 'Page' ? `<strong>${esc(h.i)}</strong> ` : ''}${mark(h.t, words)}</span>` +
                `<span class="finder__opt-kind">${esc(h.k)}</span>` +
                `<span class="finder__opt-meta">${mark(h.m.length > 110 ? h.m.slice(0, 107) + '…' : h.m, words)}</span></a></li>`).join('')
            const more  = !start && total > SHOWN
                ? `<li role="presentation"><a class="finder__opt" role="option" id="${list.id || 'fl'}-more" href="/findings/?q=${encodeURIComponent(query)}" aria-selected="false"><span class="finder__opt-title">See all ${total} matches in the register</span><span class="finder__opt-kind">→</span></a></li>`
                : ''
            const none  = !hits.length ? `<li class="finder__empty">Nothing matches “${esc(query)}”. <a href="/findings/">Browse the whole register</a>.</li>` : ''
            const foot  = '<li class="finder__foot" aria-hidden="true"><span><kbd>↑</kbd> <kbd>↓</kbd> to move</span><span><kbd>Enter</kbd> to open</span><span><kbd>Esc</kbd> to close</span></li>'
            list.innerHTML = head + body + more + none + (hits.length ? foot : '')
            list.hidden    = false
            rows           = [...list.querySelectorAll('.finder__opt')]
            choose(0)
        }

        input.setAttribute('role', 'combobox')
        input.setAttribute('aria-expanded', 'true')
        input.addEventListener('input', draw)
        input.addEventListener('focus', () => { if (input.value.trim() || startList) draw() })
        input.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowDown' && rows.length) { e.preventDefault(); choose(at + 1) }
            else if (e.key === 'ArrowUp' && rows.length) { e.preventDefault(); choose(at - 1) }
            else if (e.key === 'Enter' && rows.length && !list.hidden && input.value.trim()) { e.preventDefault(); location.href = rows[at].href }
            else if (e.key === 'Escape' && !startList) { list.hidden = true }
        })
        if (!startList) {
            document.addEventListener('pointerdown', (e) => { if (!root.contains(e.target)) list.hidden = true })
        }
        return { input, draw }
    }

    for (const root of document.querySelectorAll('[data-finder]')) attach(root, { startList: false })

    // --- the palette
    let dialog = null
    const palette = () => {
        if (dialog) return dialog
        dialog = document.createElement('dialog')
        dialog.className = 'palette'
        dialog.setAttribute('aria-label', 'Search the register')
        dialog.innerHTML =
            '<form class="finder" data-finder action="/findings/" method="get" role="search">' +
            '<div class="finder__field"><svg class="finder__icon" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="9" cy="9" r="5.5"/><path d="M13.2 13.2 17 17"/></svg>' +
            '<input class="finder__input" type="search" name="q" placeholder="Search findings, principles, pages" autocomplete="off" aria-label="Search the register" data-finder-input></div>' +
            '<ul class="finder__list" id="palette-list" role="listbox" data-finder-list></ul></form>'
        document.body.append(dialog)
        const api = attach(dialog.querySelector('[data-finder]'), { startList: true })
        dialog.addEventListener('click', (e) => { if (e.target === dialog) dialog.close() })
        dialog.api = api
        return dialog
    }
    const open = () => {
        const d = palette()
        if (!d.open) d.showModal()
        d.api.input.focus()
        d.api.input.select()
        d.api.draw()
    }

    for (const trigger of document.querySelectorAll('[data-palette-open]')) {
        trigger.addEventListener('click', (e) => { e.preventDefault(); open() })
    }
    document.addEventListener('keydown', (e) => {
        const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName) || document.activeElement?.isContentEditable
        const hotkey = (e.key === '/' && !typing && !e.metaKey && !e.ctrlKey) || (e.key.toLowerCase() === 'k' && (e.metaKey || e.ctrlKey))
        if (!hotkey) return
        e.preventDefault()
        const here = document.querySelector('[data-findings-filters] [data-filter="q"]')
        if (here && !e.metaKey && !e.ctrlKey) here.focus()
        else open()
    })
})()
