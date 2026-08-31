<p align="center">
  <img src="https://raw.githubusercontent.com/jerkgram/Jerkgram-iOS/main/assets/readme/hero.svg" alt="Jerkgram — Telegram, with more control." width="100%">
</p>

<p align="center">
  <strong>Official website repository for Jerkgram.</strong><br>
  <sub>Telegram, with more control.</sub>
</p>

<p align="center">
  <a href="https://jerkgram.github.io/"><strong>Open website</strong></a> ·
  <a href="https://github.com/jerkgram/Jerkgram-iOS"><strong>iOS source</strong></a> ·
  <a href="https://github.com/jerkgram/Jerkgram-iOS/releases"><strong>Releases</strong></a> ·
  <a href="https://t.me/JerkgramApp"><strong>Stable channel</strong></a> ·
  <a href="https://t.me/JerkgramCommunity"><strong>Community</strong></a>
</p>

# Jerkgram website

This repository publishes the official Jerkgram website at **[jerkgram.github.io](https://jerkgram.github.io/)** through GitHub Pages.

The website is the product-facing home of Jerkgram: it presents the client, real interface material, release entry points, community links and source transparency without duplicating the full application source tree.

## Repository role

```text
index.html            Production website
latest.json           Public pointer to the canonical Stable release
altstore-source.json  Official AltStore Classic / SideStore source metadata
mirrors.json          Canonical and mirror distribution metadata
.nojekyll             GitHub Pages static-site configuration
```

Application source, release provenance, build documentation and issue tracking belong in **[`jerkgram/Jerkgram-iOS`](https://github.com/jerkgram/Jerkgram-iOS)**.

## Release integration

Stable versions are published through **[GitHub Releases](https://github.com/jerkgram/Jerkgram-iOS/releases)** and **[@JerkgramApp](https://t.me/JerkgramApp)**.

For a Stable release, the website is intended to expose two distinct actions:

- **Download IPA** — direct download of the IPA asset attached to the matching GitHub Release;
- **View on GitHub** — the canonical GitHub Release page containing release notes, provenance and source links.

AltStore Classic and SideStore use the same official source metadata at [`altstore-source.json`](altstore-source.json). Both installation/update channels point to the same canonical GitHub Release IPA; SideStore does not use a separate Jerkgram feed.

[`mirrors.json`](mirrors.json) records the canonical distribution endpoint and can later distinguish verified mirrors from third-party distribution without changing GitHub Releases as the release authority.

The website repository does not act as a separate IPA archive.

## Project

Jerkgram is an independent alternative Telegram client for iOS focused on recovery, message context, customization and additional control.

Jerkgram is not an official Telegram application and is not affiliated with, endorsed by, or produced by Telegram.

---

<p align="center">
  <strong>Jerkgram</strong><br>
  <sub>Familiar. Not ordinary.</sub>
</p>
