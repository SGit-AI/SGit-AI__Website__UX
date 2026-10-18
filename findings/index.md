# Findings

Every UX failure and gap in the register, open first, then by severity. A **failure** works against the reader; a **gap** is something the reader needs that is not there. Each status says when it was last checked, and on which version: nothing here claims to be current beyond that.

| ID | Status | Severity | Product | Problems | Visibility | Finding |
| --- | --- | --- | --- | --- | --- | --- |
| [UX-001](/findings/UX-001.md) | Open | high | newsroom.sgit.ai | buried-content, builder-chrome | obvious | The first phone screen explains how the site is built, not what it is about |
| [UX-002](/findings/UX-002.md) | Open | high | newsroom.sgit.ai | overload | obvious | The home page is 59 phone screens long, with 845 links |
| [UX-024](/findings/UX-024.md) | Open | high | newsroom.sgit.ai | preselected-input | subtle | All three rating scales start on 3 |
| [UX-025](/findings/UX-025.md) | Open | high | newsroom.sgit.ai | missing-channel | silent | Ratings never reach the author |
| [UX-028](/findings/UX-028.md) | Open | high | newsroom.sgit.ai | unlabelled | obvious | The £5.00 balance chip has no label |
| [UX-029](/findings/UX-029.md) | Open | high | newsroom.sgit.ai | silent-change, unlabelled | subtle | Opening an article charges a penny with no notice |
| [UX-032](/findings/UX-032.md) | Open | high | newsroom.sgit.ai | missing-signal | silent | Nothing shows real money moving |
| [UX-033](/findings/UX-033.md) | Open | high | newsroom.sgit.ai | missing-signal | silent | It is unclear how a writer gets paid |
| [UX-034](/findings/UX-034.md) | Open | high | newsroom.sgit.ai | missing-channel | obvious | No contact for a pilot on the Replicate page |
| [UX-037](/findings/UX-037.md) | Open | high | newsroom.sgit.ai | inconsistent-facts | silent | Two domains claim to be canonical for the same article |
| [UX-044](/findings/UX-044.md) | Open | high | newsroom.sgit.ai | hidden-until-script, dead-end | intermittent | The founder page says "the picks above" and no picks render on a phone |
| [UX-046](/findings/UX-046.md) | Open | high | dev.vault.sgraph.ai | host-trap, dead-end | silent | Setting location.hash inside a vault app re-navigates the frame: every link silently dead |
| [UX-056](/findings/UX-056.md) | Open | high | Firefox on iPad | focus-hijack, unexpected-movement, wrong-culprit | intermittent | Scrolling back up a little puts focus in the address bar and opens the keyboard |
| [UX-003](/findings/UX-003.md) | Open | medium | newsroom.sgit.ai | missing-signal | subtle | The masthead line describes a method, not a subject |
| [UX-004](/findings/UX-004.md) | Open | medium | newsroom.sgit.ai | stale-claim | subtle | The edition label is older than the articles under it |
| [UX-008](/findings/UX-008.md) | Open | medium | newsroom.sgit.ai | hidden-until-script | intermittent | Content is hidden until JavaScript runs |
| [UX-009](/findings/UX-009.md) | Open | medium | newsroom.sgit.ai | overload, builder-chrome | obvious | Two navigation bars, and a 60-link menu that mixes reading with building |
| [UX-010](/findings/UX-010.md) | Open | medium | newsroom.sgit.ai | dead-end | intermittent | Missing pages show the default GitHub Pages 404 |
| [UX-013](/findings/UX-013.md) | Open | medium | newsroom.sgit.ai | overload | subtle | One topic holds more than half the articles |
| [UX-014](/findings/UX-014.md) | Open | medium | newsroom.sgit.ai | dead-end | obvious | Tags are not links, and there are no tag pages |
| [UX-015](/findings/UX-015.md) | Open | medium | newsroom.sgit.ai | unshareable-view | silent | Filters cannot be shared |
| [UX-016](/findings/UX-016.md) | Open | medium | newsroom.sgit.ai | missing-way-in | silent | Series are invisible |
| [UX-017](/findings/UX-017.md) | Open | medium | newsroom.sgit.ai | missing-way-in | subtle | There is no "start here" path |
| [UX-018](/findings/UX-018.md) | Open | medium | newsroom.sgit.ai | missing-signal | subtle | Cards do not show reading time or format |
| [UX-020](/findings/UX-020.md) | Open | medium | newsroom.sgit.ai | buried-content | obvious | The best reader feature is buried under metadata and a long italic abstract |
| [UX-022](/findings/UX-022.md) | Open | medium | newsroom.sgit.ai | missing-signal | subtle | The byline names one human; the AI authorship is in the footer |
| [UX-023](/findings/UX-023.md) | Open | medium | newsroom.sgit.ai | missing-signal | silent | There is no page that says why the publication exists |
| [UX-027](/findings/UX-027.md) | Open | medium | newsroom.sgit.ai | unconsented-state | subtle | Articles join the reader's list without being asked |
| [UX-030](/findings/UX-030.md) | Open | medium | newsroom.sgit.ai | alarming-wording | subtle | "Credit can go below zero" reads as a debt |
| [UX-038](/findings/UX-038.md) | Open | medium | newsroom.sgit.ai | inconsistent-facts | subtle | Three different article counts |
| [UX-043](/findings/UX-043.md) | Open | medium | newsroom.sgit.ai | unconsented-state | silent | Opening a persona link adds it to the browser without asking |
| [UX-045](/findings/UX-045.md) | Open | medium | newsroom.sgit.ai | missing-signal | subtle | Persona pages are a list, with no story, opinion or next step |
| [UX-047](/findings/UX-047.md) | Open | medium | dev.vault.sgraph.ai | host-trap, data-loss | intermittent | localStorage throws inside the vault app frame, so reader data is lost on reload |
| [UX-057](/findings/UX-057.md) | Open | medium | Firefox on iPad | unexpected-movement, lost-screen-space | obvious | The toolbars come back on any small scroll up, taking screen and moving the page |
| [UX-005](/findings/UX-005.md) | Open | low | newsroom.sgit.ai | builder-chrome | subtle | The version number is shown three times on the first screen |
| [UX-006](/findings/UX-006.md) | Open | low | newsroom.sgit.ai | builder-chrome, buried-content | obvious | A "For agents /llms.txt" strip sits above the masthead |
| [UX-007](/findings/UX-007.md) | Open | low | newsroom.sgit.ai | missing-signal | subtle | The editor's note is written for someone who read the last two editions |
| [UX-011](/findings/UX-011.md) | Open | low | newsroom.sgit.ai | dead-end | silent | Links without extensions in one article |
| [UX-012](/findings/UX-012.md) | Open | low | newsroom.sgit.ai | overload | subtle | Each article ends with seven next steps instead of one |
| [UX-019](/findings/UX-019.md) | Open | low | newsroom.sgit.ai | missing-way-in | subtle | Search only matches titles, teasers and tags |
| [UX-021](/findings/UX-021.md) | Open | low | newsroom.sgit.ai | builder-chrome | obvious | Author tooling is shown to every reader |
| [UX-026](/findings/UX-026.md) | Open | low | newsroom.sgit.ai | missing-channel | silent | There is no way to say what was missing |
| [UX-031](/findings/UX-031.md) | Open | low | newsroom.sgit.ai | alarming-wording | subtle | "You pay the price" reads as a warning |
| [UX-039](/findings/UX-039.md) | Open | low | newsroom.sgit.ai | inconsistent-facts | subtle | The feed is titled for the old site |
| [UX-040](/findings/UX-040.md) | Open | low | newsroom.sgit.ai | stale-claim | subtle | The study page reports a fixed bug as current |
| [UX-048](/findings/UX-048.md) | Open | low | dev.vault.sgraph.ai | host-trap | silent | A vault app can load images and scripts from a site but cannot fetch its data |
| [UX-049](/findings/UX-049.md) | Open | low | dev.vault.sgraph.ai | host-trap, unshareable-view | silent | Query strings break inside the vault host, so filters must live in the route path |
| [UX-052](/findings/UX-052.md) | Open | low | Newsroom Design Lab | data-loss | subtle | A highlight across paragraphs is cut at the first paragraph |
| [UX-053](/findings/UX-053.md) | Open | low | Newsroom Design Lab | missing-signal | subtle | Search results show no snippets |
| [UX-054](/findings/UX-054.md) | Open | low | Newsroom Design Lab | unlabelled | obvious | Stacked tables on a phone lose their column labels |
| [UX-055](/findings/UX-055.md) | Open | low | Newsroom Design Lab | untested-path | silent | "Ask the article" has never run against a real on-device model |
| [UX-035](/findings/UX-035.md) | Fixed | high | newsroom.sgit.ai | inconsistent-facts, alarming-wording | obvious | The top-up page said "simulated" while asking for money |
| [UX-036](/findings/UX-036.md) | Fixed | high | newsroom.sgit.ai | inconsistent-facts | silent | Articles were published on two domains, and diverged |
| [UX-041](/findings/UX-041.md) | Fixed | high | newsroom.sgit.ai | dead-end | obvious | 51 vault images missing across 10 articles |
| [UX-042](/findings/UX-042.md) | Fixed | high | newsroom.sgit.ai | missing-way-in | silent | Persona links were designed but not live |
| [UX-050](/findings/UX-050.md) | Fixed | medium | Newsroom Design Lab | layout-overflow | obvious | File-path pills scrolled the whole page sideways at 390 px |
| [UX-051](/findings/UX-051.md) | Fixed | medium | Newsroom Design Lab | unexpected-movement | obvious | Re-rendering the whole view on every save lost the reader's place |

Browse the same register [by product, problem, visibility, recommendation and principle](/browse/index.md).

The register is one file, [/data/findings.json](/data/findings.json). This page, every finding page and every count on the site are generated from it. To add a finding, see [the method](/method/index.md#filing-a-finding).
