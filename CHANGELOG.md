# Changelog

All notable changes to this guide. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Removed
- Überblick: the role "Mitglied mit Zugang" — eegFaktura has no member login today; the guide names EEG-Admins only.

### Added
- Aspects of the previous guide (docs.eegfaktura.at), each checked against the code: new page Einrichtung & Hilfe
  (connection via the VFEEG KEP, members' data release with links to the grid-operator guides, data protection,
  support channels); Excel master-data import and practical cases in chapter 2; protocol codes, rejection reasons
  with what to do and typical lead times in chapter 8; measurement series and typical data effects in chapter 6;
  document contents, `##` line breaks and SEPA terms in chapter 5. Not taken over: statements the code contradicts
  (e.g. a placeholder e-mail for members without e-mail, cells as text in the import, a QoV sheet, 16:00 limit).
- Chapters Tarife, Abrechnung, Energiedaten, Nachrichten and Prozesse beim Netzbetreiber; section Dokumente in
  Mitglieder & Zählpunkte. `scripts/prepare-local-stack.sql` adds the demo data they need to the local stack (a consumer
  tariff, tariffs on all metering points, billing settings); the billing screenshots create a preview and, once, a final
  billing run there.

- First version (decided 2026-10-26): MkDocs Material in the style of the member-onboarding user guide, deploy to
  GitHub Pages, Playwright screenshot script against a local stack with fixture data. Chapters: Überblick,
  Anmeldung & Oberfläche, Mitglieder & Zählpunkte, E-Mail-Texte.
- Differences to the onboarding guide: the theme font is committed (Roboto, no request to Google), no repository link
  in the header, no Mermaid diagrams (would load an unpinned script from unpkg.com) — the published site makes no
  external request. CI scans the pinned packages with Trivy and OSV-Scanner; only the deploy job can write.
- CI scan findings fixed before the first release: pymdown-extensions 10.21.3 → 11.0.1 (PYSEC-2026-3609, -3654);
  `requests` with certifi (PYSEC-2026-4320) dropped, it is only used by plugins this site does not enable.

### Changed
- Brought in line with the production release of 28.10.2026 (web 1.14.0, backend 1.10.0, billing 1.5.0), each
  point checked against the code: member list filters Alle/Aktive/Inaktive and the new sort options (chapter 2);
  mail texts: font size, image size, pasting/dropping images, fixed footer, link rules, 3 images and no PDF for
  member mails (chapter 3); dashboard membership fees (chapter 1); 0 % VAT for tariffs without „Umsatzsteuer
  anführen“ (chapter 4); ZIP file names (chapter 5); direction and equipment name in the process selections, date
  and time in the process history (chapter 8); „Was ist neu?“ now describes the production state instead of
  „pilot only“. Screenshots retaken on the local stack at the release state.
- Screenshots: window 1440 px wide; a page is shot in full height (the window grows to the content, up to 2400 px)
  instead of being cut off at 800 px. A failed step leaves a debug image in `.cache/`.
