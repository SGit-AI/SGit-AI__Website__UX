# Browse the register

The same findings, indexed nine ways. Each value links to the [findings list](/findings/index.md) filtered to it, and filters combine: `/findings/?problem=unexpected-movement&visibility=intermittent` is a link you can send. The vocabularies live in [/data/taxonomy.json](/data/taxonomy.json) and grow only when a finding needs a value that is not there yet.

[Product](#by-product) · [Area](#by-area) · [Problem](#by-problem) · [Visibility](#by-visibility) · [Recommendation](#by-recommendation) · [Principle](#by-principle) · [Severity](#by-severity) · [Status](#by-status) · [Kind](#by-kind)

And the other direction: [what good looks like](/exemplars/index.md), things that work, each linked to the findings it answers.

## By product

Whose fault it is: one of our sites, the platform under them, our own prototypes, or the browser the reader uses.

| Product | Findings | Open | Means |
| --- | --- | --- | --- |
| newsroom.sgit.ai | [45](/findings/?product=newsroom.sgit.ai) | 39 | The publication: articles on AI agents, security and publishing, written with an agent newsroom (site) |
| dev.vault.sgraph.ai | [4](/findings/?product=dev.vault.sgraph.ai) | 4 | The vault host: opens a vault by its key and runs its app in a sandboxed frame (platform) |
| Newsroom Design Lab | [6](/findings/?product=newsroom-design-lab) | 4 | This site's own prototypes: four vaults trying the newsroom fixes in three directions |
| Firefox on iPad | [3](/findings/?product=firefox-ipad) | 3 | Firefox for iOS on iPad: the browser, not any site in it (browser) |

## By area

Where in the reader's visit it happens.

| Area | Findings | Open | Means |
| --- | --- | --- | --- |
| First visit | [7](/findings/?area=first-visit) | 5 |  |
| Navigation | [7](/findings/?area=navigation) | 7 |  |
| Findability | [9](/findings/?area=findability) | 9 |  |
| Article page | [5](/findings/?area=article) | 4 |  |
| Feedback | [4](/findings/?area=feedback) | 4 |  |
| Money | [5](/findings/?area=money) | 4 |  |
| Personas | [4](/findings/?area=personas) | 3 |  |
| Trust | [6](/findings/?area=trust) | 6 |  |
| Consistency | [6](/findings/?area=consistency) | 4 |  |
| Platform | [5](/findings/?area=platform) | 4 |  |

## By problem

What kind of thing goes wrong. A finding can have more than one.

| Problem | Findings | Open | Means |
| --- | --- | --- | --- |
| Unexpected movement | [4](/findings/?problem=unexpected-movement) | 3 | Part of the interface moves when the reader did not move it |
| Focus hijack | [1](/findings/?problem=focus-hijack) | 1 | Focus or input goes somewhere the reader did not send it |
| Unpredictable control | [1](/findings/?problem=unpredictable-control) | 1 | The result of a gesture depends on something the reader cannot see or control, such as its speed, so the state they want cannot be reached on purpose |
| Lost screen space | [2](/findings/?problem=lost-screen-space) | 2 | Chrome takes screen that the content needed |
| Wrong culprit | [1](/findings/?problem=wrong-culprit) | 1 | The reader blames the wrong party: the page for the browser, the site for the platform |
| Buried content | [3](/findings/?problem=buried-content) | 3 | What the reader came for is pushed down or out of view |
| Overload | [4](/findings/?problem=overload) | 4 | Too much at once, so nothing is chosen for the reader |
| Builder chrome | [5](/findings/?problem=builder-chrome) | 5 | Things for the author, an agent or the build, shown to readers |
| Missing signal | [9](/findings/?problem=missing-signal) | 8 | The reader lacks what they need to decide: length, format, who wrote it, whether it is real |
| Missing way in | [4](/findings/?problem=missing-way-in) | 3 | A page or path the reader needs does not exist |
| Dead end | [6](/findings/?problem=dead-end) | 5 | Something that looks like a way in goes nowhere |
| Unshareable view | [2](/findings/?problem=unshareable-view) | 2 | A view the reader can see but cannot link to |
| Unlabelled | [3](/findings/?problem=unlabelled) | 3 | A number, value or control with no label |
| Alarming wording | [3](/findings/?problem=alarming-wording) | 2 | Words that read as a threat, a debt or a trick when they describe something benign |
| Silent change | [1](/findings/?problem=silent-change) | 1 | State changes without telling the reader |
| Preselected input | [1](/findings/?problem=preselected-input) | 1 | An answer is chosen before the reader chooses |
| Unconsented state | [2](/findings/?problem=unconsented-state) | 2 | Something is kept or added because the reader opened something |
| Missing channel | [3](/findings/?problem=missing-channel) | 3 | No way for the reader to reach a person |
| Inconsistent facts | [5](/findings/?problem=inconsistent-facts) | 3 | Two places disagree about the same fact |
| Stale claim | [2](/findings/?problem=stale-claim) | 1 | A statement about the present that is no longer true |
| Hidden until script | [2](/findings/?problem=hidden-until-script) | 2 | Content appears only after scripts or prior state |
| Host trap | [4](/findings/?problem=host-trap) | 4 | The platform behaves unlike a normal page, and the difference is not visible |
| Data loss | [2](/findings/?problem=data-loss) | 2 | Something the reader made or kept is lost or cut |
| Layout overflow | [1](/findings/?problem=layout-overflow) | 0 | Content wider or taller than the screen it is on |
| Untested path | [1](/findings/?problem=untested-path) | 1 | A path shown to readers that nobody has seen work |

## By visibility

How the reader experiences it: seen every time, sometimes, only felt, or not at all.

| Visibility | Findings | Open | Means |
| --- | --- | --- | --- |
| Obvious | [15](/findings/?visibility=obvious) | 11 | Every reader sees it, every time they reach that point |
| Intermittent | [6](/findings/?visibility=intermittent) | 6 | Some readers, some of the time: depends on a gesture, a device or a state, and is hard to reproduce on demand |
| Subtle | [21](/findings/?visibility=subtle) | 19 | Felt more than seen: it costs attention or trust, but is not noticed as a bug |
| Silent | [16](/findings/?visibility=silent) | 14 | No symptom on screen: found only by measuring, or by its consequences |

## By recommendation

The shape of the fix. Findings with the same recommendation are often fixed by the same change.

| Recommendation | Findings | Open | Means |
| --- | --- | --- | --- |
| Keep the UI still | [3](/findings/?recommendation=keep-the-ui-still) | 2 | Nothing moves, appears or takes focus unless the reader asked for it; chrome that hides stays hidden until a deliberate gesture |
| Make it predictable | [1](/findings/?recommendation=make-it-predictable) | 1 | The same gesture always gives the same result, and the reader can set the state directly instead of coaxing it |
| Cut to the essential | [3](/findings/?recommendation=cut-to-the-essential) | 3 | Remove or move down everything that is not the lead, the doors and the next step |
| Write for a stranger | [1](/findings/?recommendation=write-for-a-stranger) | 1 | Rewrite the words for someone arriving for the first time |
| Show it up front | [7](/findings/?recommendation=show-it-up-front) | 6 | Put the signal the reader decides by (length, author, short version, real numbers) where they look first |
| Say what it is | [7](/findings/?recommendation=say-what-it-is) | 6 | Label it, in the reader's terms, at the moment it matters |
| Start empty | [1](/findings/?recommendation=start-empty) | 1 | Inputs start unselected; record only what the reader did |
| Ask first | [2](/findings/?recommendation=ask-first) | 2 | Make keeping, adding or following a tap the reader makes |
| Make it a link | [2](/findings/?recommendation=make-it-a-link) | 2 | Give the view, filter or label an address, and make it go there |
| Build the way in | [8](/findings/?recommendation=build-the-way-in) | 7 | Create the missing page or path: tag pages, series, start here, a branded 404 |
| Open a channel | [3](/findings/?recommendation=open-a-channel) | 3 | Send it to a person by default, with consent, and give the reader a receipt |
| Generate from one source | [4](/findings/?recommendation=generate-from-one-source) | 3 | Publish once and generate every copy, count and label from one manifest |
| Check it at build | [3](/findings/?recommendation=check-at-build) | 1 | Make the release fail when it happens again |
| Move it to the workshop | [4](/findings/?recommendation=move-to-the-workshop) | 4 | Take builder things off reader pages, one link away |
| Render on the first load | [2](/findings/?recommendation=render-on-first-load) | 2 | Show the content in the HTML, with no scripts and no prior visit needed |
| Date the claim | [2](/findings/?recommendation=date-the-claim) | 1 | Generate or date every statement about now, and mark fixes with their version |
| Design for the host | [4](/findings/?recommendation=design-for-the-host) | 4 | Use the host's own mechanisms (route variable, sg.state, vault snapshot) instead of the browser's defaults |
| Test where readers are | [1](/findings/?recommendation=test-where-readers-are) | 1 | Run it on the device, browser and host readers actually use before showing it |

## By principle

The rule it breaks. Each principle has a one-minute test on the principles page.

| Principle | Findings | Open | Means |
| --- | --- | --- | --- |
| The first screen is for a stranger | [8](/findings/?principle=stranger-first-screen) | 6 | On a phone, the first screen says what this is, who it is for, and where to go next. The lead is on it. Chrome, metadata and method come after. |
| Nothing moves that the reader did not move | [3](/findings/?principle=ui-stays-still) | 2 | While the reader is reading, the interface holds still. Toolbars, keyboards, banners and panels appear, move or take focus only on a deliberate gesture made for that purpose, never as a side effect of scrolling or reading. |
| The same gesture gives the same result, so it can be learned | [1](/findings/?principle=same-gesture-same-result) | 1 | Every interaction behaves the same way every time, triggered by something the reader controls (where they tap, how far they scroll), never by something they cannot see or repeat (how fast they flicked, what state an animation was in). |
| Label the money, and never surprise with a charge | [5](/findings/?principle=label-the-money) | 4 | Every number that is money says what it is. The first time anything is charged, the reader is told before or as it happens. Wording about balances never reads as debt or threat. |
| A default is not an answer | [2](/findings/?principle=defaults-are-not-answers) | 2 | Inputs that ask the reader's opinion start empty. Only what the reader actually did is recorded. |
| Ask before keeping | [2](/findings/?principle=ask-before-keeping) | 2 | Nothing is added to the reader's lists, profile or storage because they opened something. Keeping is a tap the reader makes. |
| Every view is a link | [4](/findings/?principle=every-view-is-a-link) | 3 | Anything a reader can see, they can send: a filter, a search, a tag, a desk, a part of a series. The address changes when the view does. |
| No dead ends | [7](/findings/?principle=no-dead-ends) | 6 | Everything that looks like a way in is one: tags link to pages, missing pages offer the way back, each article ends with one next step. |
| One source of truth for every fact | [4](/findings/?principle=one-source-of-truth) | 3 | Each piece of content is published once, at one canonical address. Every count, date and label is generated from one manifest at build time. |
| The publication is not the workshop | [4](/findings/?principle=publication-not-workshop) | 4 | Reader pages carry reader things. How the site is built (versions, author tooling, agent strips, release history, admin) lives in one clearly separate area, one link away. |
| Feedback reaches someone, and the reader gets a receipt | [3](/findings/?principle=feedback-reaches-someone) | 3 | Every rating, request or 'what is missing' goes somewhere a person reads it, by default and with plain consent, and the reader keeps a receipt of what was sent. |
| Say how long, and what kind, before the reader commits | [3](/findings/?principle=length-before-commitment) | 3 | Every card and every link to a long piece shows reading time and format. Every long piece opens with a short version. |
| Say who wrote it, and how | [3](/findings/?principle=say-who-wrote-it) | 3 | The byline names the person and the way the piece was made (with agents, from voice notes), where the reader looks, not in the footer. The purpose of the publication is one link away. |
| Content is visible without waiting for scripts | [2](/findings/?principle=content-is-visible) | 2 | The page renders its content in HTML and shows it at once. Scripts enhance; they never gate what the reader can see. |
| What a page says about the present is true now | [4](/findings/?principle=state-is-current) | 3 | Labels like 'edition of', 'currently', 'broken' and 'live' are dated or generated, and change when the facts do. A fixed problem is marked fixed, with the version. |
| A vault app works inside the host, not just on its own | [3](/findings/?principle=host-safe-apps) | 3 | An app is tested where readers open it: inside the vault host's sandboxed frame. Routing never assigns location.hash, storage goes through the host, and network reads come from the vault. |

## By severity

High loses the reader or their trust on the first visit; medium costs effort or a return; low is polish.

| Severity | Findings | Open | Means |
| --- | --- | --- | --- |
| High | [17](/findings/?severity=high) | 13 |  |
| Medium | [24](/findings/?severity=medium) | 20 |  |
| Low | [17](/findings/?severity=low) | 17 |  |

## By status

As of the date each finding was last checked.

| Status | Findings | Open | Means |
| --- | --- | --- | --- |
| Open | [49](/findings/?status=open) | 49 |  |
| Partly fixed | [1](/findings/?status=partly-fixed) | 1 |  |
| Fixed | [8](/findings/?status=fixed) | 0 |  |

## By kind

A failure works against the reader; a gap is something they need that is not there.

| Kind | Findings | Open | Means |
| --- | --- | --- | --- |
| Failure | [39](/findings/?kind=failure) | 33 | Something works against the reader |
| Gap | [19](/findings/?kind=gap) | 17 | Something the reader needs is not there |
