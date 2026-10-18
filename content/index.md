---
title: UX, measured
description: A register of where the sgit.ai sites fail their readers, measured on the live site with a date and a version, the principle each failure breaks, the fix, and a working prototype of it.
layout: home
---

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

{{stats}}

## Open, and high severity

These lose a reader or a reader's trust on the first visit. Each links to its evidence and its fix.

{{findings-list:status=open,partly-fixed;severity=high}}

[All {{count:total}} findings →](/findings/)

## By product

Whose fault it is. Most findings are on our own sites; some belong to the platform under them or to the browser a reader uses, and are here because readers blame us for them anyway. [Browse every index →](/browse/)

{{facet:product}}

## How a finding gets here

Someone uses the site as a stranger would: a phone, a link, three minutes. What gets in their way is written down with the evidence, the date and the version, then named against a [principle](/principles/). The [method](/method/) has the details. The first source was the [newsroom UX review of 11 October 2026](/reviews/newsroom-2026-10-11.html); new findings come from the same kind of look at any site in the network.

This site follows its own principles, or it is a finding too: the first screen says what it is, every view is a link, every count is generated from [one file](/data/findings.json), and the content is there without JavaScript.
