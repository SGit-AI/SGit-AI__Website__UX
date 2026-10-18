# The Newsroom Design Lab

A finding says what is wrong. The lab shows what right could look like. Built 11 to 13 October 2026, it is four [SGit vaults](https://sgit.ai/), each a self-contained app, that try the fixes from the [newsroom review](/reviews/newsroom-2026-10-11.md) on the real newsroom data (a byte-faithful snapshot of 73 articles), **in three design directions each**, so that a direction can be chosen by looking rather than by arguing. Nothing in the lab changes the live site.

Every view in the lab says which step of the reader's path it moves them to: **arrive** through a link someone sent, **read** and rate, **come back**, **ask**, **act**.

## Three directions

A direction is a different design, not a recolour: different hierarchy, type, density and interaction, over the same data. Every vault has a switch in its top bar, and a Compare view that shows all three at phone width.

| Direction | The idea | Looks like |
| --- | --- | --- |
| **A · Broadsheet** | A serious publication. Editorial hierarchy, one lead, a named author with a stated purpose. | Serif headlines, warm paper, rules between columns, kickers, restrained colour. FT / Guardian long-read feel. |
| **B · Briefing** | Answers first. Every unit opens with the news in two sentences, then labelled blocks: the news, our view, the evidence, room for disagreement. | Sans, compact cards with reading time and format, bold labels, one accent colour. Semafor / Axios feel. |
| **C · Your desk** | The reader's own newsroom. The persona is the front page; the board, highlights, notes and questions are first-class. | App-like: left rail, side column, chips and progress. Readwise / Arc feel. |

## The same screen, three ways

Screenshots at phone width (390 px) from the published vaults, rendered from their own snapshot with the network off. Tap one for the full page.

### The first phone screen, today against the proposal

Arrive: does a stranger know in one screen what this is?. Route `first-screen` in [Front page & personas](#newsroom-proto-front).

- [A · Broadsheet](/lab/shots/first-screen__broadsheet__390.webp)
- [B · Briefing](/lab/shots/first-screen__briefing__390.webp)
- [C · Your desk](/lab/shots/first-screen__desk__390.webp)

### The front page as the neutral persona

Arrive: lead, doors and desks instead of 59 screens. Route `front` in [Front page & personas](#newsroom-proto-front).

- [A · Broadsheet](/lab/shots/front__broadsheet__390.webp)
- [B · Briefing](/lab/shots/front__briefing__390.webp)
- [C · Your desk](/lab/shots/front__desk__390.webp)

### The founder mini-site

Arrive through a persona link: story, note, start here, sections. Route `persona/founder` in [Front page & personas](#newsroom-proto-front).

- [A · Broadsheet](/lab/shots/persona-founder__broadsheet__390.webp)
- [B · Briefing](/lab/shots/persona-founder__briefing__390.webp)
- [C · Your desk](/lab/shots/persona-founder__desk__390.webp)

### An article, reordered

Read: short version first, byline that says how it was made. Route `article/hope-or-enforcement` in [Article & reader primitives](#newsroom-proto-article).

- [A · Broadsheet](/lab/shots/article-hope-or-enforcement__broadsheet__390.webp)
- [B · Briefing](/lab/shots/article-hope-or-enforcement__briefing__390.webp)
- [C · Your desk](/lab/shots/article-hope-or-enforcement__desk__390.webp)

### Feedback that starts empty and reaches someone

Rate: unselected scales, consent, a receipt. Route `feedback` in [Article & reader primitives](#newsroom-proto-article).

- [A · Broadsheet](/lab/shots/feedback__broadsheet__390.webp)
- [B · Briefing](/lab/shots/feedback__briefing__390.webp)
- [C · Your desk](/lab/shots/feedback__desk__390.webp)

### The reading board

Return: New, Reading, Follow-up, Done. Route `board` in [Article & reader primitives](#newsroom-proto-article).

- [A · Broadsheet](/lab/shots/board__broadsheet__390.webp)
- [B · Briefing](/lab/shots/board__briefing__390.webp)
- [C · Your desk](/lab/shots/board__desk__390.webp)

### A desk page: start here, series, the rest

Find: a way in chosen by audience. Route `desk/security` in [Findability](#newsroom-proto-find).

- [A · Broadsheet](/lab/shots/desk-security__broadsheet__390.webp)
- [B · Briefing](/lab/shots/desk-security__briefing__390.webp)
- [C · Your desk](/lab/shots/desk-security__desk__390.webp)

### Search with the filters in the address

Find and share: every result set is a link. Route `search` in [Findability](#newsroom-proto-find).

- [A · Broadsheet](/lab/shots/search__broadsheet__390.webp)
- [B · Briefing](/lab/shots/search__briefing__390.webp)
- [C · Your desk](/lab/shots/search__desk__390.webp)

## The four vaults

Each opens read only in the vault host, with a published read key. A read key is derived one way from a vault key the publisher holds; publishing it grants reading and nothing else.

### The lab · `3bf2p46v`

The brief, the three directions, the map from review to prototype, the decisions, the reviews.

- Open: [newsroom-design-lab in the vault host](https://dev.vault.sgraph.ai/#sgit_public_read_b7d938b9d9c57853ed28015309f0c7ff5537da9667bf4b4da16688df892e7297%3A3bf2p46v)
- Read key: `sgit_public_read_b7d938b9d9c57853ed28015309f0c7ff5537da9667bf4b4da16688df892e7297:3bf2p46v`
- Clone: `sgit clone sgit_public_read_b7d938b9d9c57853ed28015309f0c7ff5537da9667bf4b4da16688df892e7297:3bf2p46v`

### Front page & personas · `m1m66ace`

First visit; a publication with a heart; the purpose page; publication and workshop; personas as the core primitive; the founder mini-site.

Routes: `front`, `first-screen`, `personas`, `persona/founder`, `purpose`, `masthead`, `menu`

- Open: [newsroom-proto-front in the vault host](https://dev.vault.sgraph.ai/#sgit_public_read_47f49bdabb39be07282e69f4f88cb1323ebb9c94875f7f626bff62d8e70502ea%3Am1m66ace)
- Read key: `sgit_public_read_47f49bdabb39be07282e69f4f88cb1323ebb9c94875f7f626bff62d8e70502ea:m1m66ace`
- Clone: `sgit clone sgit_public_read_47f49bdabb39be07282e69f4f88cb1323ebb9c94875f7f626bff62d8e70502ea:m1m66ace`

### Article & reader primitives · `vdcj8hpl`

The article page reordered; the short version first; the side column; highlights and notes; ratings that start unselected; ask the article; the reading board; the reader's record.

Routes: `articles`, `article/hope-or-enforcement`, `feedback`, `ask`, `board`, `record`

- Open: [newsroom-proto-article in the vault host](https://dev.vault.sgraph.ai/#sgit_public_read_4b40a9541792eeb2052ccdcc425e14ebcb739438b66b463044856648fd6bad78%3Avdcj8hpl)
- Read key: `sgit_public_read_4b40a9541792eeb2052ccdcc425e14ebcb739438b66b463044856648fd6bad78:vdcj8hpl`
- Clone: `sgit clone sgit_public_read_4b40a9541792eeb2052ccdcc425e14ebcb739438b66b463044856648fd6bad78:vdcj8hpl`

### Findability · `xvq3z35u`

Five desks by audience; 42 controlled tags from 339 raw ones; 11 series with part numbers; linkable search; reading time and format on every card; the Librarian's audit.

Routes: `find`, `desks`, `desk/security`, `series`, `tags`, `search`, `archive`, `cards`, `catalogue-audit`

- Open: [newsroom-proto-find in the vault host](https://dev.vault.sgraph.ai/#sgit_public_read_2d4ca142def8d0e089fcddcf5b7ef529ec01d8152d7553c7605bf0100cba4c56%3Axvq3z35u)
- Read key: `sgit_public_read_2d4ca142def8d0e089fcddcf5b7ef529ec01d8152d7553c7605bf0100cba4c56:xvq3z35u`
- Clone: `sgit clone sgit_public_read_2d4ca142def8d0e089fcddcf5b7ef529ec01d8152d7553c7605bf0100cba4c56:xvq3z35u`

## From finding to prototype

Each finding in the register that a prototype answers, with the finding's status on the live site. A prototype existing does not make a finding fixed: only the live site can do that.

| Finding | Status | Prototype |
| --- | --- | --- |
| [UX-001](/findings/UX-001.md) The first phone screen explains how the site is built, not what it is about | Open | Front page & personas: `first-screen` |
| [UX-002](/findings/UX-002.md) The home page is 59 phone screens long, with 845 links | Open | Front page & personas: `front` |
| [UX-024](/findings/UX-024.md) All three rating scales start on 3 | Open | Article & reader primitives: `feedback` |
| [UX-025](/findings/UX-025.md) Ratings never reach the author | Open | Article & reader primitives: `feedback` |
| [UX-028](/findings/UX-028.md) The £5.00 balance chip has no label | Open | Front page & personas: `first-screen` |
| [UX-044](/findings/UX-044.md) The founder page says "the picks above" and no picks render on a phone | Open | Front page & personas: `persona/founder` |
| [UX-003](/findings/UX-003.md) The masthead line describes a method, not a subject | Open | Front page & personas: `masthead` |
| [UX-004](/findings/UX-004.md) The edition label is older than the articles under it | Open | Front page & personas: `front` |
| [UX-009](/findings/UX-009.md) Two navigation bars, and a 60-link menu that mixes reading with building | Open | Front page & personas: `menu` |
| [UX-013](/findings/UX-013.md) One topic holds more than half the articles | Open | Findability: `desks` |
| [UX-014](/findings/UX-014.md) Tags are not links, and there are no tag pages | Open | Findability: `tags` |
| [UX-015](/findings/UX-015.md) Filters cannot be shared | Open | Findability: `search` |
| [UX-016](/findings/UX-016.md) Series are invisible | Open | Findability: `series` |
| [UX-017](/findings/UX-017.md) There is no "start here" path | Open | Findability: `desk/security` |
| [UX-018](/findings/UX-018.md) Cards do not show reading time or format | Open | Findability: `cards` |
| [UX-020](/findings/UX-020.md) The best reader feature is buried under metadata and a long italic abstract | Open | Article & reader primitives: `article/hope-or-enforcement` |
| [UX-022](/findings/UX-022.md) The byline names one human; the AI authorship is in the footer | Open | Article & reader primitives: `article/hope-or-enforcement` |
| [UX-023](/findings/UX-023.md) There is no page that says why the publication exists | Open | Front page & personas: `purpose` |
| [UX-027](/findings/UX-027.md) Articles join the reader's list without being asked | Open | Article & reader primitives: `feedback` |
| [UX-043](/findings/UX-043.md) Opening a persona link adds it to the browser without asking | Open | Front page & personas: `personas` |
| [UX-045](/findings/UX-045.md) Persona pages are a list, with no story, opinion or next step | Open | Front page & personas: `persona/founder` |
| [UX-005](/findings/UX-005.md) The version number is shown three times on the first screen | Open | Front page & personas: `front` |
| [UX-006](/findings/UX-006.md) A "For agents /llms.txt" strip sits above the masthead | Open | Front page & personas: `front` |
| [UX-019](/findings/UX-019.md) Search only matches titles, teasers and tags | Open | Findability: `search` |
| [UX-026](/findings/UX-026.md) There is no way to say what was missing | Open | Article & reader primitives: `record` |
| [UX-031](/findings/UX-031.md) "You pay the price" reads as a warning | Open | Article & reader primitives: `feedback` |
| [UX-049](/findings/UX-049.md) Query strings break inside the vault host, so filters must live in the route path | Open | Findability: `search` |
| [UX-052](/findings/UX-052.md) A highlight across paragraphs is cut at the first paragraph | Open | Article & reader primitives: `article/hope-or-enforcement` |
| [UX-053](/findings/UX-053.md) Search results show no snippets | Open | Findability: `search` |
| [UX-054](/findings/UX-054.md) Stacked tables on a phone lose their column labels | Open | Findability: `catalogue-audit` |
| [UX-055](/findings/UX-055.md) "Ask the article" has never run against a real on-device model | Open | Article & reader primitives: `ask` |

## The decisions it exists to settle

The lab's hub vault lets the editor pick one option per decision, kept in the browser and downloadable as JSON. These are the questions, as the lab asks them.

1. **Which direction should the live front page take?** Everything else follows from it: type, density, how much the reader's own data shows. Options: A · Broadsheet; B · Briefing; C · Your desk; Mix: A for the publication, C for a signed-in reader.
2. **Which masthead line names the heart?** The tagline today describes a method, not a subject. Options: Field notes on AI agents, security and the next generation of publishing, by Dinis Cruz; Open thinking on agentic AI: what to build, how to secure it, and how to ship it; The agentic era, written in the open.
3. **How many doors on the first screen?** Three is easier to choose from; five covers everyone you send links to. Options: Three (security, builders, news); Five personas plus 'just looking'.
4. **What opens every article?** Readers have three minutes on a phone; the median article is about 4,500 words. Options: A boxed 'In brief' (the Explainer's short version); Labelled blocks: the news, our view, the evidence, room for disagreement; The article with the reader's side column.
5. **How should a rating reach you?** Today it stays in the reader's browser unless they send their whole reading. Options: One tap, anonymous, with plain consent; One tap, with an optional email for a reply; Kept locally, sent weekly with the reader's consent.
6. **Desks by audience or by subject?** Topics today overlap and one holds 38 of 73 articles. Options: Five desks by audience (proposed); Keep the six topics, add tag pages.
7. **Ship the reading board in the first release?** It gives a returning reader a reason to come back, and it is the most app-like piece. Options: Yes, on every persona page; Later, once ratings flow.

## What building the lab measured

Building apps that run inside the vault host turned up failures that are not about the newsroom at all: they are traps in the platform, and in the lab's own prototypes. They are in the register like any other finding.

- [UX-046](/findings/UX-046.md) · high · open · Setting location.hash inside a vault app re-navigates the frame: every link silently dead (dev.vault.sgraph.ai)
- [UX-047](/findings/UX-047.md) · medium · open · localStorage throws inside the vault app frame, so reader data is lost on reload (dev.vault.sgraph.ai)
- [UX-048](/findings/UX-048.md) · low · open · A vault app can load images and scripts from a site but cannot fetch its data (dev.vault.sgraph.ai)
- [UX-049](/findings/UX-049.md) · low · open · Query strings break inside the vault host, so filters must live in the route path (dev.vault.sgraph.ai)
- [UX-052](/findings/UX-052.md) · low · open · A highlight across paragraphs is cut at the first paragraph (newsroom-design-lab)
- [UX-053](/findings/UX-053.md) · low · open · Search results show no snippets (newsroom-design-lab)
- [UX-054](/findings/UX-054.md) · low · open · Stacked tables on a phone lose their column labels (newsroom-design-lab)
- [UX-055](/findings/UX-055.md) · low · open · "Ask the article" has never run against a real on-device model (newsroom-design-lab)
- [UX-050](/findings/UX-050.md) · medium · fixed · File-path pills scrolled the whole page sideways at 390 px (newsroom-design-lab)
- [UX-051](/findings/UX-051.md) · medium · fixed · Re-rendering the whole view on every save lost the reader's place (newsroom-design-lab)

## How it is built

A shared kit (v0.1.3, vendored into each vault): native web components with no framework, a bundler that packs each app into one `index.html` (the vault-app contract), an escaping template every view renders through, a router that never assigns `location.hash` inside the host, a reader store that uses the host's `sg.state` because the frame refuses `localStorage`, and a release gate that renders every route in every direction at 390 and 1280 px and fails on any page error, any colour outside the theme file, or any sideways scroll on a phone. Built by a lead with an architect agent and three developer agents, one vault each.

Reader data in the prototypes stays in the browser. Every "send" button is simulated, and says so, showing the receipt the real encrypted append lane would give.
