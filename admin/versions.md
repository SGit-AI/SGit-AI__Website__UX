# Versions

The current version is v0.2.0. Newest first.

## v0.2.0 · 2026-10-18

The register is indexed nine ways, and the first reports from readers arrive: two Firefox-on-iPad findings about a page that will not hold still.

- `data/taxonomy.json`: problem (24), visibility (4) and recommendation (17) vocabularies; every existing finding backfilled
- `data/site.json`: sites become products, with a type (site, platform, prototype, browser); Firefox on iPad added
- `data/findings.json`: UX-056 (scroll up focuses the address bar and opens the keyboard) and UX-057 (toolbars return on any scroll up), with screenshots in findings/img/
- `data/principles.json`: new principle, nothing moves that the reader did not move; UX-051 moved to it
- `content/browse/index.md`: every facet with counts, each value a link to the filtered list
- `admin/build/`: facets drive filters, finding pages, browse and llms.txt; the gate checks the taxonomy and evidence images

## v0.1.0 · 2026-10-18

The first release: a register of UX failures and gaps, seeded from the newsroom review, with the review, the design lab and the method it was made by.

- `data/findings.json`: 55 findings (newsroom.sgit.ai, the vault host, and the lab's own prototypes), each with evidence, impact, fix, status and the principle it breaks
- `data/principles.json`: 14 principles, each listing the findings that break it
- `content/reviews/newsroom-2026-10-11.md`: the newsroom UX review of 11 October 2026, published whole
- `content/lab/index.md + lab/shots/`: the Newsroom Design Lab, its four vaults with read keys, and 24 phone screenshots in three directions
- `content/method/index.md`: the reader path, the panel, severity, and how a finding is filed
- `admin/build/`: build.py, md.py and gate.py, stdlib only
