# Changelog

All notable changes to this guide. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed
- EEG page without the card „Einstellungen“ (platform#245, pilot): the interval is „Abrechnungsintervall“ under
  „Allgemeines“ (chapters Anmeldung & Oberfläche, Abrechnung, „Was ist neu?“ with the pilot hint). The section keeps the
  id `abrechnungszeitraum-wechseln`, so the help link of eegfaktura-web and older links still land there. The
  screenshot of the EEG page still shows the earlier state.
- CI: the dependency scan (Trivy + OSV-Scanner) no longer gates the deploy. It runs for pull requests, weekly and by
  hand; a merge to `main` publishes after the strict build only. On 08.11.2026 a 504 from the OSV-Scanner download
  held back the published guide (the pilot hints stayed online) although the build was green.

### Changed
- Production release of 08.11.2026: the pilot features of 06.–08.11.2026 are live everywhere. The hint „Derzeit nur in
  der Pilot-Zone“ is removed from all sections (`--8<-- "pilot.md"`), „Was ist neu?“ lists them under „Herbst 2026
  (seit 08.11.2026)“. `snippets/pilot.md` stays for the next pilot features. Screenshots of the user menu, the
  community picker and the dashboard still show the earlier state (follow-up).

### Added
- Standard for features that run only in the pilot zone (README „Features in the pilot zone“): shared hint
  `snippets/pilot.md` („Derzeit nur in der Pilot-Zone“), included with `--8<-- "pilot.md"` (pymdownx.snippets, part
  of the pinned pymdown-extensions) under each heading; removed by deleting those lines at the production release.
- Pilot features of 06.–08.11.2026, each with the hint: Abrechnungszeitraum wechseln with the 12-month gap rule and the
  first open period after the change (web 1.20.0–1.21.0, backend 1.16.0–1.17.0); Zählpunkt abmelden — inactive only
  after the grid operator's answer, reason of a rejection (platform#238); Dashboard „Übersicht EEG“ with today's
  state; EEG-Seite „Modell“ (long form) and „Nahebereich“ (ElWG names), P2P/EVA without billing (platform#229);
  „Gemeinschaft wechseln“ with a search field and „Aktuelle Gemeinschaft“ in the user menu (platform#241). „Was ist
  neu?“ lists them under „In der Pilot-Zone“.
- Abrechnung: section „Abrechnungszeitraum wechseln“ (vfeeg-development/eegfaktura-platform#230; the dialog in
  eegfaktura-web links to its anchor `#abrechnungszeitraum-wechseln`): who can change the interval, from when the new
  one applies (start of the period after the last final billing, everything before billed; example monthly →
  quarterly), what blocks it (open periods, a running calculation; a preview does not), what stays (documents,
  numbers, exports) and that membership fee, metering-point fee and free kWh are charged per run, so the yearly amount
  changes with the interval. The decision and informing the members are the community's matter. Anmeldung → EEG-Seite
  no longer calls the interval „fest eingestellt“ and links the section. Published with the pilot hint (see above).

### Removed
- Mitglieder & Zählpunkte, Prozesse: the offline registration with an activation code (checkbox
  „Offline-Registrierung“, field „Aktivierungs-Code“, ONLINE/OFFLINE switch in „Zulassen“) — grid operators no longer
  support it; eegFaktura registers metering points online only (eegfaktura-web#246, eegfaktura-backend#129).
  „Was ist neu?“ has a short note.
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
- Brought in line with the production release of 29.10.2026 (web 1.18.0, backend 1.13.0, billing 1.7.0), each point
  checked against the code: joining fee in the member tariff, its status line and actions in the member details and the
  two export columns (chapters 2, 4, 5, 6); member list „Anzeige“ (Standard / Alle / Aktive / Inaktive) and tooltips;
  billing always covers the whole community, € switch tooltip, no run without energy, final runs one at a time
  (chapter 5); drag & drop and the sheet name in the import dialog, drag & drop for contracts (chapters 2, 6); grouped,
  sorted and searchable tariff list (chapter 4); new mail images start small (chapter 3); „Was ist neu?“ lists the
  release. Screenshots of the changed screens retaken on the local stack at the release state;
  `scripts/prepare-local-stack.sql` gives the fixture member tariff a joining fee, the screenshot scripts follow the new
  member list (no check boxes, „Anzeige“) and add `tarife-beitrittsgebuehr.png`.
- Brought in line with the production release of 28.10.2026 (web 1.14.0, backend 1.10.0, billing 1.5.0), each
  point checked against the code: member list filters Alle/Aktive/Inaktive and the new sort options (chapter 2);
  mail texts: font size, image size, pasting/dropping images, fixed footer, link rules, 3 images and no PDF for
  member mails (chapter 3); dashboard membership fees (chapter 1); 0 % VAT for tariffs without „Umsatzsteuer
  anführen“ (chapter 4); ZIP file names (chapter 5); direction and equipment name in the process selections, date
  and time in the process history (chapter 8); „Was ist neu?“ now describes the production state instead of
  „pilot only“. Screenshots retaken on the local stack at the release state.
- Screenshots: window 1440 px wide; a page is shot in full height (the window grows to the content, up to 2400 px)
  instead of being cut off at 800 px. A failed step leaves a debug image in `.cache/`.
