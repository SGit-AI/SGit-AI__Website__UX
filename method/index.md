# Method

A finding is only as good as its evidence. Everything here is measured on the live site, at a stated date and version, by someone using it as a stranger would. Opinion is welcome as long as it is labelled as one; the register holds what was seen.

## The reader's path

Every page is judged by which step it moves a reader to next. The path is the one the people these sites are written for actually take:

1. **Arrive** through a link someone sent, usually on a phone, with one question and a few minutes.
2. **Read** the first piece, and rate it.
3. **Come back**: a new pick, the newsletter, a reading board.
4. **Ask**: what is missing, a new version, a topic.
5. **Act**: try the product, start a conversation, put their own agents on a problem.

A finding is anything that stops a reader at one of these steps, or makes the next step harder than it needs to be.

## The stranger test

The cheapest test there is, and the one that finds most first-visit failures:

- Open the page on a phone (390×844), in a private window, with no history.
- Without scrolling: what is this, who is it for, and where do I go?
- Tap the first thing that looks like a way in. Did it go anywhere?
- Open the thing the site most wants you to read. How long is it? Did anything tell you before you opened it?
- Find every number. Is each one labelled, and do they agree with each other?

## The panel

A full review reads the same evidence through six roles, each with its own question. They disagree usefully: the Architect wanted the "For agents" strip on every page and the Designer wanted it off the first screen, and the answer (the page head and the footer) satisfied both.

| Role | The question it asks |
| --- | --- |
| Architect | Is there one pipeline, one source of truth, and URLs that will last? |
| Librarian | Can a reader find everything on a subject, and is the catalogue consistent? |
| Historian | Can a newcomer follow the arc of ideas from the start to now? |
| Designer | Does the first screen and the reading page serve a stranger on a phone? |
| Editor | Is the front page choosing for the reader, and is the voice consistent? |
| Journalist | Would a contact understand the story, trust it, and come back? |

Synthetic users (invented readers driven through the site by agents) add a seventh view, and a score that can be compared between releases. The newsroom's third run scored 2.4 out of 5; the next should add a CISO, who is most of the audience.

## Indexed nine ways

Every finding is indexed by **product** (whose fault it is), **area** (where in the visit), **problem** (what kind of thing goes wrong, one or more), **visibility** (how the reader experiences it), **recommendation** (the shape of the fix), **principle** (the rule it breaks), **severity**, **status** and **kind**. [Browse](/browse/index.md) shows every value of each with its count; the [findings list](/findings/index.md) filters by any combination, and the address is the filter.

| Visibility | Means |
| --- | --- |
| **Obvious** | Every reader sees it, every time they reach that point |
| **Intermittent** | Some readers, some of the time: depends on a gesture, a device or a state, and is hard to reproduce on demand |
| **Subtle** | Felt more than seen: costs attention or trust, but is not noticed as a bug |
| **Silent** | No symptom on screen: found only by measuring, or by its consequences |

Visibility is not severity. A silent failure (ratings that never reach anyone) can be the most serious on the site; an obvious one can be cosmetic. It says how a finding will be found, and therefore who will report it.

## Reports from readers

Most of the register will come from people using the sites and saying where they got stuck: a screenshot, a sentence, the page they were on. A report becomes a finding when it has been written up with the evidence, the device and browser, what the reader expected, and the fix, and indexed like any other. The report is the source; the finding page credits it.

A report about the browser rather than the page still goes in, with the browser as its product. Readers cannot tell whose fault a jumping toolbar is, and they blame the page they were reading, so knowing what the browser does is part of designing the page.

## Failure or gap

| Kind | Means | Example |
| --- | --- | --- |
| **Failure** | Something on the site works against the reader | Rating scales that start on 3; a balance that drops without notice |
| **Gap** | Something the reader needs is not there | No way to share a filtered list; no reading time on cards |

## Severity

| Severity | Means |
| --- | --- |
| **High** | Loses the reader, or the reader's trust, on the first visit. Or the site cannot learn from its readers at all |
| **Medium** | Costs the reader effort, or a return visit, or makes the site look unkept |
| **Low** | Polish and consistency: noticed by the careful, forgiven by most, fixed cheaply |

## Status, and what "checked" means

| Status | Means |
| --- | --- |
| **Open** | Still true when last checked |
| **Partly fixed** | Some of it changed; the finding says what is left |
| **Fixed** | No longer true, with the version that fixed it |

Every finding carries the date and version it was **observed** and the date and version it was **last checked**. A status is a claim about that date, not about today. Re-checking a finding means visiting it again, and updating both.

## Filing a finding

The register is one file, [/data/findings.json](/data/findings.json). A finding is one entry; the build turns it into a page, a markdown twin, a row in every list and filter, and a line in [llms.txt](/llms.txt). The fields:

```
{
 "id":        "UX-056",                       next free number, never reused
 "title":     "What is wrong, as a sentence",
 "product":   "newsroom.sgit.ai",             whose fault it is: a key of "products" in data/site.json
                                              (a site, the platform, a prototype, or a browser)
 "where":     "https://…/the/page.html",      the URL, or a description if there is none
 "area":      "first-visit",                  first-visit, navigation, findability, article,
                                              feedback, money, personas, trust, consistency, platform
 "problems":  ["unexpected-movement"],        one or more, from data/taxonomy.json
 "visibility": "intermittent",                obvious | intermittent | subtle | silent
 "recommendation": "keep-the-ui-still",       the shape of the fix, from data/taxonomy.json
 "kind":      "failure",                      failure | gap
 "severity":  "high",                         high | medium | low
 "status":    "open",                         open | partly-fixed | fixed
 "principle": "stranger-first-screen",        an id in data/principles.json
 "observed":  {"date": "2026-10-18", "version": "v0.7.3"},
 "checked":   {"date": "2026-10-18", "version": "v0.7.3"},
 "evidence":  "What was seen, measured: sizes, counts, the exact words on the page",
 "impact":    "Why it matters to the reader, in one or two sentences",
 "fix":       "The smallest change that removes it",
 "prototype": null,                           or {"vault": "newsroom-proto-front", "route": "front"}
 "source":    {"href": "/reviews/…", "label": "Where it was found"},
 "environment": "optional: device, browser, orientation, the page it happened on",
 "images":    [{"src": "/findings/img/UX-056-….webp", "alt": "…", "caption": "…"}],
 "status_note": "optional: what changed, and in which version"
}
```

Then `python3 admin/build/build.py` and `python3 admin/build/gate.py`. The gate fails on a missing field, an unknown site, area or principle, a duplicate id, a date that is not a date, a source link that goes nowhere, or a generated page that is out of date.

If a finding does not fit any [principle](/principles/index.md), add the principle: it earns its place by having a finding that breaks it.

## Rules for the register itself

- **Measure, then write.** Sizes, counts and the exact words on the page, not impressions of them.
- **Date every status.** A finding with no "last checked" is a rumour.
- **Name the fix.** A finding without a proposed fix is a complaint; the fix can be wrong, and that is fine.
- **Our own work is in scope.** The lab's prototypes and this site are reviewed like any other.
- **Content exists once.** The review is published whole and never edited; the register is where status changes.
