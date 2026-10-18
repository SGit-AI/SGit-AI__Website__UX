# Principles

Each principle here is kept because at least one finding breaks it: the list grows from evidence, not from taste. Each has a test you can run on your own page in about a minute. When a new kind of failure does not fit any of them, that is a new principle.

1. [The first screen is for a stranger](/principles/index.md#stranger-first-screen)
2. [Nothing moves that the reader did not move](/principles/index.md#ui-stays-still)
3. [The same gesture gives the same result, so it can be learned](/principles/index.md#same-gesture-same-result)
4. [Label the money, and never surprise with a charge](/principles/index.md#label-the-money)
5. [A default is not an answer](/principles/index.md#defaults-are-not-answers)
6. [Ask before keeping](/principles/index.md#ask-before-keeping)
7. [Every view is a link](/principles/index.md#every-view-is-a-link)
8. [No dead ends](/principles/index.md#no-dead-ends)
9. [One source of truth for every fact](/principles/index.md#one-source-of-truth)
10. [The publication is not the workshop](/principles/index.md#publication-not-workshop)
11. [Feedback reaches someone, and the reader gets a receipt](/principles/index.md#feedback-reaches-someone)
12. [Say how long, and what kind, before the reader commits](/principles/index.md#length-before-commitment)
13. [Say who wrote it, and how](/principles/index.md#say-who-wrote-it)
14. [Content is visible without waiting for scripts](/principles/index.md#content-is-visible)
15. [What a page says about the present is true now](/principles/index.md#state-is-current)
16. [A vault app works inside the host, not just on its own](/principles/index.md#host-safe-apps)

## 1. The first screen is for a stranger

**The rule.** On a phone, the first screen says what this is, who it is for, and where to go next. The lead is on it. Chrome, metadata and method come after.

**Why.** Most readers arrive from a link someone sent, on a phone, with one question and a few minutes. If the first screen does not answer 'what is this', the rest of the page is never read.

**The test.** Open the page at 390×844 with no history. Count the blocks above the lead. Can someone who has never heard of the site say what it is about?

Broken by 8 findings, 6 open:

- [UX-001](/findings/UX-001.md) · open · The first phone screen explains how the site is built, not what it is about
- [UX-002](/findings/UX-002.md) · open · The home page is 59 phone screens long, with 845 links
- [UX-017](/findings/UX-017.md) · open · There is no "start here" path
- [UX-045](/findings/UX-045.md) · open · Persona pages are a list, with no story, opinion or next step
- [UX-007](/findings/UX-007.md) · open · The editor's note is written for someone who read the last two editions
- [UX-054](/findings/UX-054.md) · open · Stacked tables on a phone lose their column labels
- [UX-003](/findings/UX-003.md) · fixed · The masthead line describes a method, not a subject
- [UX-050](/findings/UX-050.md) · fixed · File-path pills scrolled the whole page sideways at 390 px

## 2. Nothing moves that the reader did not move

**The rule.** While the reader is reading, the interface holds still. Toolbars, keyboards, banners and panels appear, move or take focus only on a deliberate gesture made for that purpose, never as a side effect of scrolling or reading.

**Why.** Movement pulls the eye. Every element that moves outside the reader's task forces a glance, a check and a return, which is a context switch the reader did not choose. On a reading page, concentration is the product.

**The test.** Read a long page on a phone or tablet: scroll down, scroll up a little, pause, carry on. Did anything appear, resize, shift or take focus that you did not ask for? Did the text you were reading stay where it was?

Broken by 3 findings, 2 open:

- [UX-056](/findings/UX-056.md) · open · Scrolling back up a little puts focus in the address bar and opens the keyboard
- [UX-057](/findings/UX-057.md) · open · The toolbars come back on any small scroll up, taking screen and moving the page
- [UX-051](/findings/UX-051.md) · fixed · Re-rendering the whole view on every save lost the reader's place

## 3. The same gesture gives the same result, so it can be learned

**The rule.** Every interaction behaves the same way every time, triggered by something the reader controls (where they tap, how far they scroll), never by something they cannot see or repeat (how fast they flicked, what state an animation was in).

**Why.** An interface teaches as it is used. When the same action always gives the same result, the reader learns it once and from then on can depend on it without thinking. When it depends on speed or timing, it can never be learned, and every use costs attention.

**The test.** Do the same thing five times: scroll, flick, tap, at slightly different speeds. Did the interface respond the same way each time? Could you reach the state you wanted on the first try?

Broken by 1 findings, 1 open:

- [UX-058](/findings/UX-058.md) · open · Whether the toolbars hide depends on how fast you scroll, not how far

## 4. Label the money, and never surprise with a charge

**The rule.** Every number that is money says what it is. The first time anything is charged, the reader is told before or as it happens. Wording about balances never reads as debt or threat.

**Why.** An unexplained balance that changes is read as a bill. One confused moment about money ends the visit and the trust.

**The test.** Find every currency figure on the page. Does each have a label? Open a page that charges: did anything say so?

Broken by 5 findings, 4 open:

- [UX-029](/findings/UX-029.md) · open · Opening an article charges a penny with no notice
- [UX-030](/findings/UX-030.md) · open · "Credit can go below zero" reads as a debt
- [UX-031](/findings/UX-031.md) · open · "You pay the price" reads as a warning
- [UX-028](/findings/UX-028.md) · partly fixed · The £5.00 balance chip has no label
- [UX-035](/findings/UX-035.md) · fixed · The top-up page said "simulated" while asking for money

## 5. A default is not an answer

**The rule.** Inputs that ask the reader's opinion start empty. Only what the reader actually did is recorded.

**Why.** A scale preset to 3 cannot tell 'not rated' from 'useful'. The data looks real and means nothing, to the reader and to the author.

**The test.** Open the form fresh. Is any answer already chosen? Submit without touching it: what was recorded?

Broken by 2 findings, 2 open:

- [UX-024](/findings/UX-024.md) · open · All three rating scales start on 3
- [UX-052](/findings/UX-052.md) · open · A highlight across paragraphs is cut at the first paragraph

## 6. Ask before keeping

**The rule.** Nothing is added to the reader's lists, profile or storage because they opened something. Keeping is a tap the reader makes.

**Why.** State the reader did not ask for is clutter at best and surveillance at worst. It also makes the reader's own record useless as a record.

**The test.** Open a page, close it. Did anything appear in the reader's list, board or persona set?

Broken by 2 findings, 2 open:

- [UX-027](/findings/UX-027.md) · open · Articles join the reader's list without being asked
- [UX-043](/findings/UX-043.md) · open · Opening a persona link adds it to the browser without asking

## 7. Every view is a link

**The rule.** Anything a reader can see, they can send: a filter, a search, a tag, a desk, a part of a series. The address changes when the view does.

**Why.** The people who most need a subset of the site are the ones a reader would forward it to. A view without an address cannot be shared, bookmarked or found by search.

**The test.** Choose a filter. Copy the address. Open it in a private window. Is it the same view?

Broken by 4 findings, 3 open:

- [UX-013](/findings/UX-013.md) · open · One topic holds more than half the articles
- [UX-015](/findings/UX-015.md) · open · Filters cannot be shared
- [UX-049](/findings/UX-049.md) · open · Query strings break inside the vault host, so filters must live in the route path
- [UX-042](/findings/UX-042.md) · fixed · Persona links were designed but not live

## 8. No dead ends

**The rule.** Everything that looks like a way in is one: tags link to pages, missing pages offer the way back, each article ends with one next step.

**Why.** A tag that does not link, a default 404 and an article that ends with seven options all stop the reader at the moment they were ready to go further.

**The test.** Click every pill, chip and label on a page. Visit a URL that does not exist. Reach the end of an article: what is the one next step?

Broken by 7 findings, 6 open:

- [UX-010](/findings/UX-010.md) · open · Missing pages show the default GitHub Pages 404
- [UX-014](/findings/UX-014.md) · open · Tags are not links, and there are no tag pages
- [UX-016](/findings/UX-016.md) · open · Series are invisible
- [UX-011](/findings/UX-011.md) · open · Links without extensions in one article
- [UX-012](/findings/UX-012.md) · open · Each article ends with seven next steps instead of one
- [UX-019](/findings/UX-019.md) · open · Search only matches titles, teasers and tags
- [UX-041](/findings/UX-041.md) · fixed · 51 vault images missing across 10 articles

## 9. One source of truth for every fact

**The rule.** Each piece of content is published once, at one canonical address. Every count, date and label is generated from one manifest at build time.

**Why.** Readers notice when two pages disagree, and they stop trusting both. A count that differs between three pages says the site does not know itself.

**The test.** Find the same number on three pages (article count, edition date, version). Do they agree? Does each article have exactly one canonical?

Broken by 4 findings, 3 open:

- [UX-037](/findings/UX-037.md) · open · Two domains claim to be canonical for the same article
- [UX-038](/findings/UX-038.md) · open · Three different article counts
- [UX-039](/findings/UX-039.md) · open · The feed is titled for the old site
- [UX-036](/findings/UX-036.md) · fixed · Articles were published on two domains, and diverged

## 10. The publication is not the workshop

**The rule.** Reader pages carry reader things. How the site is built (versions, author tooling, agent strips, release history, admin) lives in one clearly separate area, one link away.

**Why.** Builder chrome on a reader page spends the reader's attention on something they did not come for, and makes the site look like a demo instead of a publication.

**The test.** List every element on a reader page that only the author or an agent needs. Each one is a finding.

Broken by 4 findings, 4 open:

- [UX-009](/findings/UX-009.md) · open · Two navigation bars, and a 60-link menu that mixes reading with building
- [UX-005](/findings/UX-005.md) · open · The version number is shown three times on the first screen
- [UX-006](/findings/UX-006.md) · open · A "For agents /llms.txt" strip sits above the masthead
- [UX-021](/findings/UX-021.md) · open · Author tooling is shown to every reader

## 11. Feedback reaches someone, and the reader gets a receipt

**The rule.** Every rating, request or 'what is missing' goes somewhere a person reads it, by default and with plain consent, and the reader keeps a receipt of what was sent.

**Why.** Feedback kept only in the reader's browser teaches the author nothing, and a reader who is never answered stops answering.

**The test.** Rate something. Where did it go? Who reads it, and when? What does the reader have to show they sent it?

Broken by 3 findings, 3 open:

- [UX-025](/findings/UX-025.md) · open · Ratings never reach the author
- [UX-034](/findings/UX-034.md) · open · No contact for a pilot on the Replicate page
- [UX-026](/findings/UX-026.md) · open · There is no way to say what was missing

## 12. Say how long, and what kind, before the reader commits

**The rule.** Every card and every link to a long piece shows reading time and format. Every long piece opens with a short version.

**Why.** A reader with three minutes will not start a 25-minute piece blind. Telling them lets them choose; not telling them makes them leave.

**The test.** Look at a list of articles. Can you tell which is a five-minute note and which is a 40-minute analysis?

Broken by 3 findings, 3 open:

- [UX-018](/findings/UX-018.md) · open · Cards do not show reading time or format
- [UX-020](/findings/UX-020.md) · open · The best reader feature is buried under metadata and a long italic abstract
- [UX-053](/findings/UX-053.md) · open · Search results show no snippets

## 13. Say who wrote it, and how

**The rule.** The byline names the person and the way the piece was made (with agents, from voice notes), where the reader looks, not in the footer. The purpose of the publication is one link away.

**Why.** Readers judge a piece by who stands behind it. Disclosure in the footer reads as concealment when it is found.

**The test.** From the top of any article, can a reader tell who wrote it, with what help, and why the publication exists?

Broken by 3 findings, 3 open:

- [UX-033](/findings/UX-033.md) · open · It is unclear how a writer gets paid
- [UX-022](/findings/UX-022.md) · open · The byline names one human; the AI authorship is in the footer
- [UX-023](/findings/UX-023.md) · open · There is no page that says why the publication exists

## 14. Content is visible without waiting for scripts

**The rule.** The page renders its content in HTML and shows it at once. Scripts enhance; they never gate what the reader can see.

**Why.** A blank page for a second and a half on a slow phone is the page, for that reader. Agents, readers and search engines that do not run scripts see nothing.

**The test.** Load the page with JavaScript off, and on a throttled connection. Is the content there at once?

Broken by 2 findings, 2 open:

- [UX-044](/findings/UX-044.md) · open · The founder page says "the picks above" and no picks render on a phone
- [UX-008](/findings/UX-008.md) · open · Content is hidden until JavaScript runs

## 15. What a page says about the present is true now

**The rule.** Labels like 'edition of', 'currently', 'broken' and 'live' are dated or generated, and change when the facts do. A fixed problem is marked fixed, with the version.

**Why.** A page that describes a fixed bug as current, or labels today's front page with last week's date, tells the reader the rest may be stale too.

**The test.** Find every claim about now on the page. Is each dated? Is each still true?

Broken by 4 findings, 3 open:

- [UX-032](/findings/UX-032.md) · open · Nothing shows real money moving
- [UX-040](/findings/UX-040.md) · open · The study page reports a fixed bug as current
- [UX-055](/findings/UX-055.md) · open · "Ask the article" has never run against a real on-device model
- [UX-004](/findings/UX-004.md) · fixed · The edition label is older than the articles under it

## 16. A vault app works inside the host, not just on its own

**The rule.** An app is tested where readers open it: inside the vault host's sandboxed frame. Routing never assigns location.hash, storage goes through the host, and network reads come from the vault.

**Why.** The host frame behaves unlike a normal page. An app that works standalone can ship with every link dead and every saved note lost on reload.

**The test.** Open the published vault in the host, click every link, save something, reload. Check the console.

Broken by 3 findings, 3 open:

- [UX-046](/findings/UX-046.md) · open · Setting location.hash inside a vault app re-navigates the frame: every link silently dead
- [UX-047](/findings/UX-047.md) · open · localStorage throws inside the vault app frame, so reader data is lost on reload
- [UX-048](/findings/UX-048.md) · open · A vault app can load images and scripts from a site but cannot fetch its data
