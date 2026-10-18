# SGit-AI__Website__UX

The source of [ux.sgit.ai](https://ux.sgit.ai/): a public register of UX failures and gaps across the
sgit.ai sites, each measured on the live site with a date and version, the principle it breaks, and the
fix. Seeded from the newsroom.sgit.ai UX review of 11 October 2026 and the Newsroom Design Lab built
from it.

## Where things are

| Path | What it is |
| --- | --- |
| `data/findings.json` | **The register.** One entry per finding; every finding page, list, filter and count is generated from it |
| `data/principles.json` | The principles findings break (each must be broken by at least one finding) |
| `data/lab.json` | The Newsroom Design Lab: vaults and published read keys, directions, screenshots, decisions |
| `data/site.json`, `data/versions.json` | Site facts and release history (first entry = current version) |
| `content/**/*.md` | Hand-written pages; `{{directives}}` are filled from the data at build |
| `admin/build/` | `build.py` (generator), `md.py` (markdown renderer), `gate.py` (release gate). Stdlib only |
| everything else at the root | **Generated**: `*.html`, their `.md` twins, `llms.txt`, `llms-full.txt`, `sitemap.xml`, `robots.txt` |

## Build, check, preview

```
python3 admin/build/build.py     # regenerate every page
python3 admin/build/gate.py      # must print GATE PASS (CI runs this on every push)
python3 -m http.server 8000      # http://localhost:8000/
```

Served as static files (GitHub Pages, `CNAME` = ux.sgit.ai, `.nojekyll`). Python 3.11+, no dependencies.

## Adding a finding

Append an entry to `data/findings.json` with the next free id (the schema is on `/method/#filing-a-finding`),
run the build, run the gate. The gate rejects unknown sites, areas, principles or vaults, malformed dates,
duplicate ids, sources that go nowhere, and stale generated files.

Content CC BY 4.0. Code Apache 2.0.
