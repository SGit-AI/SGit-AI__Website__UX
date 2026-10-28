/**
 * @module findings
 * The findings finder. The list is complete HTML without this script; this only hides rows.
 * The search and every filter live in the address (?q=…&severity=high&status=open,partly-fixed), so every view is a link.
 * As you type the best match is highlighted: arrow keys move it, Enter opens it.
 */
(() => {
    const form  = document.querySelector('[data-findings-filters]')
    const list  = document.querySelector('[data-findings]')
    if (!form || !list) return

    const rows    = [...list.querySelectorAll('.finding')]
    const count   = form.querySelector('[data-findings-count]')
    const empty   = document.querySelector('[data-findings-empty]')
    const active  = form.querySelector('[data-findings-active]')
    const fields  = [...form.querySelectorAll('[data-filter]')]
    const search  = form.querySelector('[data-filter="q"]')
    const reset   = form.querySelector('[data-findings-reset]')
    const toggle  = form.querySelector('[data-filters-toggle]')
    const panel   = form.querySelector('[data-filters-panel]')
    const badge   = form.querySelector('[data-filters-n]')
    const quicks  = [...form.querySelectorAll('[data-quick]')]
    const text    = new Map(rows.map(row => [row, row.textContent.toLowerCase()]))
    const titles  = new Map(rows.map(row => [row, row.querySelector('.finding__title')]))
    const plain   = new Map([...titles].map(([row, el]) => [row, el.textContent]))
    let   current = null

    const read = () => {
        const params = new URLSearchParams(location.search)
        const state  = {}
        for (const field of fields) state[field.dataset.filter] = params.get(field.dataset.filter) || ''
        return state
    }

    const write = (state) => {
        const params = new URLSearchParams()
        for (const [key, value] of Object.entries(state)) if (value) params.set(key, value)
        const query = params.toString()
        history.replaceState(null, '', location.pathname + (query ? '?' + query : '') + location.hash)
    }

    const escapeHtml = (t) => t.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]))
    const highlight = (row, words) => {
        const el = titles.get(row), source = plain.get(row)
        if (!words.length) { el.textContent = source; return }
        const re = new RegExp('(' + words.map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')', 'gi')
        el.innerHTML = escapeHtml(source).replace(re, '<mark>$1</mark>')
    }

    const setCurrent = (row, scroll = false) => {
        current?.classList.remove('finding--active')
        current = row
        if (row) { row.classList.add('finding--active'); if (scroll) row.scrollIntoView({ block: 'nearest' }) }
    }

    const rank = (row, words) => {
        const title = plain.get(row).toLowerCase(), id = row.querySelector('.finding__id').textContent.toLowerCase()
        return words.reduce((sum, w) => sum + (id === w ? 50 : title.startsWith(w) ? 20 : title.includes(' ' + w) ? 14 : title.includes(w) ? 10 : 2), 0)
    }

    const show = (state) => {
        const words = state.q.toLowerCase().split(/\s+/).filter(Boolean)
        const shown = []
        for (const row of rows) {
            let match = true
            for (const [key, value] of Object.entries(state)) {
                if (!value || key === 'q') continue
                const have = row.dataset[key].split(' ')
                if (!value.split(',').some(v => have.includes(v))) match = false
            }
            if (match && words.length) match = words.every(word => text.get(row).includes(word))
            row.hidden = !match
            highlight(row, match ? words : [])
            if (match) shown.push(row)
        }
        // best title match first while searching; the register's own order (open, then severity) when not
        const order = words.length ? [...shown].sort((a, b) => rank(b, words) - rank(a, words) || rows.indexOf(a) - rows.indexOf(b)) : rows
        list.append(...order, ...rows.filter(r => !order.includes(r)))
        shown.splice(0, shown.length, ...(words.length ? order : shown))
        const filters = fields.filter(f => f.dataset.filter !== 'q' && state[f.dataset.filter])
        count.textContent = `${shown.length} of ${rows.length}`
        active.textContent = filters.length ? '· ' + filters.map(f => f.selectedOptions[0]?.textContent).join(', ') : ''
        badge.hidden = !filters.length
        badge.textContent = filters.length
        reset.hidden = !(filters.length || state.q)
        for (const chip of quicks) {
            const [key, value] = chip.dataset.quick.split('=')
            chip.setAttribute('aria-pressed', String(state[key] === value))
        }
        if (empty) empty.hidden = shown.length !== 0
        setCurrent(words.length ? shown[0] || null : null)
    }

    const sync = (state) => {
        for (const field of fields) {
            const value = state[field.dataset.filter]
            if (field.tagName === 'SELECT' && value && !field.querySelector(`option[value="${CSS.escape(value)}"]`)) {
                const option       = document.createElement('option')
                option.value       = value
                option.textContent = value.split(',').map(v => v.replace(/-/g, ' ')).join(' or ')
                field.append(option)
            }
            field.value = value
        }
    }

    const fromForm = () => {
        const state = {}
        for (const field of fields) state[field.dataset.filter] = field.value.trim()
        return state
    }

    const apply = (state) => { sync(state); write(state); show(state) }

    const initial = read()
    sync(initial)
    show(initial)
    const open = (on) => { panel.hidden = !on; toggle.setAttribute('aria-expanded', String(on)) }
    open(fields.some(f => f.dataset.filter !== 'q' && initial[f.dataset.filter]))

    form.addEventListener('input', () => { const s = fromForm(); write(s); show(s) })
    form.addEventListener('submit', (e) => e.preventDefault())
    toggle.addEventListener('click', () => open(panel.hidden))
    reset.addEventListener('click', () => { apply(Object.fromEntries(fields.map(f => [f.dataset.filter, '']))); search.focus() })
    form.querySelector('[data-copy-link]').addEventListener('click', (e) => {
        navigator.clipboard?.writeText(location.href).then(() => { e.target.textContent = 'Copied' ; setTimeout(() => { e.target.textContent = 'Copy link' }, 1500) })
    })
    for (const chip of quicks) {
        chip.addEventListener('click', () => {
            const [key, value] = chip.dataset.quick.split('=')
            const state = fromForm()
            state[key]  = state[key] === value ? '' : value
            apply(state)
            if (state[key]) open(true)
        })
    }

    search.addEventListener('keydown', (e) => {
        const visible = rows.filter(r => !r.hidden)
        const at      = visible.indexOf(current)
        if (e.key === 'ArrowDown' && visible.length) { e.preventDefault(); setCurrent(visible[Math.min(at + 1, visible.length - 1)], true) }
        else if (e.key === 'ArrowUp' && visible.length) { e.preventDefault(); setCurrent(visible[Math.max(at - 1, 0)], true) }
        else if (e.key === 'Enter' && current) { e.preventDefault(); current.querySelector('.finding__title').click() }
        else if (e.key === 'Escape' && search.value) { search.value = ''; const s = fromForm(); write(s); show(s) }
    })
    window.addEventListener('pageshow', () => { const s = read(); sync(s); show(s) })
})()
