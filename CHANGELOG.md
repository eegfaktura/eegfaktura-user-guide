# Changelog

All notable changes to this guide. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Chapters Tarife, Abrechnung, Energiedaten, Nachrichten and Prozesse beim Netzbetreiber; section Dokumente in
  Mitglieder & Zählpunkte. `scripts/prepare-local-stack.sql` adds the demo data they need to the local stack (a consumer
  tariff, tariffs on all metering points, billing settings); the billing screenshots create a preview and, once, a final
  billing run there.

### Changed
- Screenshots: window 1440 px wide; a page is shot in full height (the window grows to the content, up to 2400 px)
  instead of being cut off at 800 px. A failed step leaves a debug image in `.cache/`.

### Added
- First version (decided 2026-10-26): MkDocs Material in the style of the member-onboarding user guide, deploy to
  GitHub Pages, Playwright screenshot script against a local stack with fixture data. Chapters: Überblick,
  Anmeldung & Oberfläche, Mitglieder & Zählpunkte, E-Mail-Texte.
- Differences to the onboarding guide: the theme font is committed (Roboto, no request to Google), no repository link
  in the header, no Mermaid diagrams (would load an unpinned script from unpkg.com) — the published site makes no
  external request. CI scans the pinned packages with Trivy and OSV-Scanner; only the deploy job can write.
- CI scan findings fixed before the first release: pymdown-extensions 10.21.3 → 11.0.1 (PYSEC-2026-3609, -3654);
  `requests` with certifi (PYSEC-2026-4320) dropped, it is only used by plugins this site does not enable.
