# Changelog

All notable changes to this guide. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- First version (decided 2026-10-26): MkDocs Material in the style of the member-onboarding user guide, deploy to
  GitHub Pages, Playwright screenshot script against a local stack with fixture data. Chapters: Überblick,
  Anmeldung & Oberfläche, Mitglieder & Zählpunkte, E-Mail-Texte.
- Differences to the onboarding guide: the theme font is committed (Roboto, no request to Google), no repository link
  in the header, no Mermaid diagrams (would load an unpinned script from unpkg.com) — the published site makes no
  external request. CI scans the pinned packages with Trivy and OSV-Scanner; only the deploy job can write.
- CI scan findings fixed before the first release: pymdown-extensions 10.21.3 → 11.0.1 (PYSEC-2026-3609, -3654);
  `requests` with certifi (PYSEC-2026-4320) dropped, it is only used by plugins this site does not enable.
