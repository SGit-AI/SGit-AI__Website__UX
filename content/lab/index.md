---
title: The Newsroom Design Lab
description: Four encrypted vaults that try the newsroom review's fixes as working prototypes, on the real newsroom data, in three design directions each, before anything changes on the live site.
toc: yes
---

# The Newsroom Design Lab

A finding says what is wrong. The lab shows what right could look like. Built 11 to 13 October 2026, it is four [SGit vaults](https://sgit.ai/), each a self-contained app, that try the fixes from the [newsroom review](/reviews/newsroom-2026-10-11.html) on the real newsroom data (a byte-faithful snapshot of 73 articles), **in three design directions each**, so that a direction can be chosen by looking rather than by arguing. Nothing in the lab changes the live site.

Every view in the lab says which step of the reader's path it moves them to: **arrive** through a link someone sent, **read** and rate, **come back**, **ask**, **act**.

## Three directions

A direction is a different design, not a recolour: different hierarchy, type, density and interaction, over the same data. Every vault has a switch in its top bar, and a Compare view that shows all three at phone width.

{{lab-directions}}

## The same screen, three ways

Screenshots at phone width (390 px) from the published vaults, rendered from their own snapshot with the network off. Tap one for the full page.

{{lab-compare}}

## The four vaults

Each opens read only in the vault host, with a published read key. A read key is derived one way from a vault key the publisher holds; publishing it grants reading and nothing else.

{{lab-vaults}}

## From finding to prototype

Each finding in the register that a prototype answers, with the finding's status on the live site. A prototype existing does not make a finding fixed: only the live site can do that.

{{lab-map}}

## The decisions it exists to settle

The lab's hub vault lets the editor pick one option per decision, kept in the browser and downloadable as JSON. These are the questions, as the lab asks them.

{{lab-decisions}}

## What building the lab measured

Building apps that run inside the vault host turned up failures that are not about the newsroom at all: they are traps in the platform, and in the lab's own prototypes. They are in the register like any other finding.

{{findings-list:product=dev.vault.sgraph.ai,newsroom-design-lab}}

## How it is built

A shared kit (v0.1.3, vendored into each vault): native web components with no framework, a bundler that packs each app into one `index.html` (the vault-app contract), an escaping template every view renders through, a router that never assigns `location.hash` inside the host, a reader store that uses the host's `sg.state` because the frame refuses `localStorage`, and a release gate that renders every route in every direction at 390 and 1280 px and fails on any page error, any colour outside the theme file, or any sideways scroll on a phone. Built by a lead with an architect agent and three developer agents, one vault each.

Reader data in the prototypes stays in the browser. Every "send" button is simulated, and says so, showing the receipt the real encrypted append lane would give.
