<div class="hero">
<h1>Where our sites fail their readers, measured, and what fixes it</h1>
<p class="lede">A public register of UX failures and gaps across the sgit.ai sites and the browsers they are read in. Each one measured on the live site, dated, tied to the principle it breaks, and paired with its fix.</p>
<p class="byline">By Dinis Cruz, written with AI agents. <a href="/about/">Why this exists</a>.</p>
</div>

<div class="doors">
<a class="door" href="/findings/"><span class="door__title">I want the list</span><span class="door__body">Every finding, filterable by site, area, severity and status. Every filter is a link you can send.</span></a>
<a class="door" href="/principles/"><span class="door__title">I build sites</span><span class="door__body">The principles the findings break, each with a test you can run on your own page in a minute.</span></a>
<a class="door" href="/lab/"><span class="door__title">Show me the fixes</span><span class="door__body">The Newsroom Design Lab: four vaults trying the fixes on real data, in three design directions.</span></a>
</div>

- **63** findings in the register
- **55** still open
- **16** open and high severity
- **8** fixed, with the version that fixed it

## Open, and high severity

These lose a reader or a reader's trust on the first visit. Each links to its evidence and its fix.

- [UX-001](/findings/UX-001.md) · high · open · The first phone screen explains how the site is built, not what it is about (newsroom.sgit.ai)
- [UX-002](/findings/UX-002.md) · high · open · The home page is 59 phone screens long, with 845 links (newsroom.sgit.ai)
- [UX-024](/findings/UX-024.md) · high · open · All three rating scales start on 3 (newsroom.sgit.ai)
- [UX-025](/findings/UX-025.md) · high · open · Ratings never reach the author (newsroom.sgit.ai)
- [UX-029](/findings/UX-029.md) · high · open · Opening an article charges a penny with no notice (newsroom.sgit.ai)
- [UX-032](/findings/UX-032.md) · high · open · Nothing shows real money moving (newsroom.sgit.ai)
- [UX-033](/findings/UX-033.md) · high · open · It is unclear how a writer gets paid (newsroom.sgit.ai)
- [UX-034](/findings/UX-034.md) · high · open · No contact for a pilot on the Replicate page (newsroom.sgit.ai)
- [UX-037](/findings/UX-037.md) · high · open · Two domains claim to be canonical for the same article (newsroom.sgit.ai)
- [UX-044](/findings/UX-044.md) · high · open · The founder page says "the picks above" and no picks render on a phone (newsroom.sgit.ai)
- [UX-046](/findings/UX-046.md) · high · open · Setting location.hash inside a vault app re-navigates the frame: every link silently dead (dev.vault.sgraph.ai)
- [UX-056](/findings/UX-056.md) · high · open · Scrolling back up a little puts focus in the address bar and opens the keyboard (Firefox on iPad)
- [UX-059](/findings/UX-059.md) · high · open · A security prompt that asks you to approve a command it does not explain, and cuts off (Claude app (iPhone and iPad))
- [UX-060](/findings/UX-060.md) · high · open · One unlabelled X throws away the whole recording, with no confirmation (Claude app (iPhone and iPad))
- [UX-063](/findings/UX-063.md) · high · open · The live transcript sometimes stops while you are still speaking, and nothing says whether it is still recording (Claude app (iPhone and iPad))
- [UX-028](/findings/UX-028.md) · high · partly fixed · The £5.00 balance chip has no label (newsroom.sgit.ai)

[All 63 findings →](/findings/index.md)

## By product

Whose fault it is. Most findings are on our own sites; some belong to the platform under them or to the browser a reader uses, and are here because readers blame us for them anyway. [Browse every index →](/browse/index.md)

| Product | Findings | Open | Means |
| --- | --- | --- | --- |
| newsroom.sgit.ai | [45](/findings/?product=newsroom.sgit.ai) | 39 | The publication: articles on AI agents, security and publishing, written with an agent newsroom (site) |
| dev.vault.sgraph.ai | [4](/findings/?product=dev.vault.sgraph.ai) | 4 | The vault host: opens a vault by its key and runs its app in a sandboxed frame (platform) |
| Newsroom Design Lab | [6](/findings/?product=newsroom-design-lab) | 4 | This site's own prototypes: four vaults trying the newsroom fixes in three directions |
| Firefox on iPad | [3](/findings/?product=firefox-ipad) | 3 | Firefox for iOS on iPad: the browser, not any site in it (browser) |
| Claude app (iPhone and iPad) | [5](/findings/?product=claude-app-ios) | 5 | The Claude app on iOS and iPadOS, used here to run and supervise Claude Code sessions, often by voice (app) |

## How a finding gets here

Someone uses the site as a stranger would: a phone, a link, three minutes. What gets in their way is written down with the evidence, the date and the version, then named against a [principle](/principles/index.md). The [method](/method/index.md) has the details. The first source was the [newsroom UX review of 11 October 2026](/reviews/newsroom-2026-10-11.md); new findings come from the same kind of look at any site in the network.

This site follows its own principles, or it is a finding too: the first screen says what it is, every view is a link, every count is generated from [one file](/data/findings.json), and the content is there without JavaScript.
