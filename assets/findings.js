/**
 * @module findings
 * The findings filter. The list is complete HTML without this script; this only hides rows.
 * The filter lives in the address (?product=…&problem=…&severity=high,medium&q=…), so every view is a link.
 */
(() => {
    const form  = document.querySelector('[data-findings-filters]')
    const list  = document.querySelector('[data-findings]')
    if (!form || !list) return

    const rows    = [...list.querySelectorAll('.finding')]
    const count   = form.querySelector('[data-findings-count]')
    const empty   = document.querySelector('[data-findings-empty]')
    const active  = form.closest('details').querySelector('[data-findings-active]')
    const fields  = [...form.querySelectorAll('[data-filter]')]
    const text    = new Map(rows.map(row => [row, row.textContent.toLowerCase()]))

    const read = () => {
        const params = new URLSearchParams(location.search)
        const state  = {}
        for (const field of fields) {
            state[field.dataset.filter] = params.get(field.dataset.filter) || ''
        }
        return state
    }

    const write = (state) => {
        const params = new URLSearchParams()
        for (const [key, value] of Object.entries(state)) {
            if (value) params.set(key, value)
        }
        const query = params.toString()
        history.replaceState(null, '', location.pathname + (query ? '?' + query : '') + location.hash)
    }

    const show = (state) => {
        const words = state.q.toLowerCase().split(/\s+/).filter(Boolean)
        let shown   = 0
        for (const row of rows) {
            let match = true
            for (const [key, value] of Object.entries(state)) {
                if (!value || key === 'q') continue
                const have = row.dataset[key].split(' ')
                if (!value.split(',').some(v => have.includes(v))) match = false
            }
            if (match && words.length) match = words.every(word => text.get(row).includes(word))
            row.hidden = !match
            if (match) shown += 1
        }
        count.textContent = `${shown} of ${rows.length}`
        const chosen = fields.filter(field => state[field.dataset.filter])
            .map(field => field.tagName === 'SELECT' ? field.selectedOptions[0]?.textContent : `"${state.q}"`)
        active.textContent = chosen.length ? `· ${chosen.join(', ')} · ${shown} of ${rows.length}` : ''
        if (empty) empty.hidden = shown !== 0
    }

    const sync = (state) => {
        for (const field of fields) {
            const value = state[field.dataset.filter]
            if (field.tagName === 'SELECT' && value && !field.querySelector(`option[value="${CSS.escape(value)}"]`)) {
                const option       = document.createElement('option')
                option.value       = value
                option.textContent = value.split(',').join(' or ')
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

    const initial = read()
    sync(initial)
    show(initial)

    form.addEventListener('input', () => {
        const state = fromForm()
        write(state)
        show(state)
    })
    form.addEventListener('submit', (event) => event.preventDefault())
    form.querySelector('[data-findings-reset]')?.addEventListener('click', (event) => {
        event.preventDefault()
        const state = Object.fromEntries(fields.map(field => [field.dataset.filter, '']))
        sync(state)
        write(state)
        show(state)
    })
})()
