# External sources

Every external source this repository uses (eegfaktura supply-chain rule: fixed versions, nothing younger than
7 days when pinned, licence compatible with the AGPL-3.0 stack; a new source only after asking).
Decided 2026-10-26: same tools as the member-onboarding user guide.

## Python packages (PyPI)

Pinned in `requirements-docs.txt` (site build) and `requirements-screenshots.txt` (screenshot generator),
direct and transitive. Install with `pip install --no-deps -r …` so nothing unpinned is pulled in.
`requests` (and with it certifi, charset-normalizer, idna, urllib3) is left out on purpose: mkdocs-material declares
it, but uses it only in its info, privacy and social plugins, which this site does not enable (`pip check` reports
it as missing — expected). Fewer packages, and certifi < 2026.10.19 has a critical advisory (PYSEC-2026-4320).

| Package | Version | Published | Licence | Used for |
|---|---|---|---|---|
| babel | 2.18.0 | 2026-02-01 | BSD-3-Clause | Site build |
| backrefs | 8.1 | 2026-10-10 | MIT | Site build |
| click | 8.5.0 | 2026-08-26 | BSD-3-Clause | Site build |
| colorama | 0.4.6 | 2022-10-25 | BSD-3-Clause | Site build |
| ghp-import | 2.1.0 | 2022-05-02 | Apache-2.0 | Site build |
| Jinja2 | 3.1.6 | 2025-03-05 | BSD-3-Clause | Site build |
| Markdown | 3.11.1 | 2026-10-13 | BSD-3-Clause | Site build |
| MarkupSafe | 3.0.4 | 2026-10-02 | BSD-3-Clause | Site build |
| mergedeep | 1.3.4 | 2021-02-05 | MIT | Site build |
| mkdocs | 1.6.1 | 2024-08-30 | BSD-2-Clause | Site build |
| mkdocs-get-deps | 0.2.2 | 2026-03-10 | MIT | Site build |
| mkdocs-material | 9.7.7 | 2026-07-17 | MIT | Site build |
| mkdocs-material-extensions | 1.3.1 | 2023-11-22 | MIT | Site build |
| packaging | 26.3 | 2026-08-04 | Apache-2.0 OR BSD-2-Clause | Site build |
| paginate | 0.5.7 | 2024-08-25 | MIT | Site build |
| pathspec | 1.1.1 | 2026-04-27 | MPL-2.0 | Site build |
| platformdirs | 4.13.4 | 2026-10-17 | MIT | Site build |
| Pygments | 2.21.0 | 2026-08-17 | BSD-2-Clause | Site build |
| pymdown-extensions | 11.0.1 | 2026-07-02 | MIT | Site build |
| python-dateutil | 2.9.0.post0 | 2024-03-01 | Apache-2.0 OR BSD-3-Clause | Site build |
| PyYAML | 6.0.3 | 2025-09-25 | MIT | Site build |
| pyyaml_env_tag | 1.1 | 2025-05-13 | MIT | Site build |
| six | 1.17.0 | 2024-12-04 | MIT | Site build |
| tzdata | 2026.5 | 2026-10-03 | Apache-2.0 | Site build |
| watchdog | 6.0.0 | 2024-11-01 | Apache-2.0 | Site build |
| greenlet | 3.5.6 | 2026-09-14 | MIT AND PSF-2.0 | Screenshots |
| playwright | 1.64.0 | 2026-10-13 | Apache-2.0 | Screenshots |
| pyee | 14.0.0 | 2026-08-13 | MIT | Screenshots |
| typing_extensions | 4.16.0 | 2026-07-02 | PSF-2.0 | Screenshots |

## Other sources

| Source | Version | Published | Licence | Used for |
|---|---|---|---|---|
| Chromium build for Playwright (`playwright install chromium`, Microsoft CDN) | bundled with playwright 1.64.0 | 2026-10-13 | BSD-3-Clause (Chromium) | Screenshots (local only, not in CI) |
| GitHub Action `actions/checkout` | v7.0.1 (`3d3c42e5aac5ba805825da76410c181273ba90b1`) | 2026-07-20 | MIT | CI |
| GitHub Action `actions/setup-python` | v7.0.0 (`5fda3b95a4ea91299a34e894583c3862153e4b97`) | 2026-07-20 | MIT | CI |
| GitHub Pages (`gh-pages` branch) | — | — | — | Hosting |
| Trivy (release binary, SHA256 checked) | 0.75.0 | — | Apache-2.0 | CI scan (same version as eegfaktura-web) |
| OSV-Scanner (release binary, SHA256 checked) | 2.6.0 | — | Apache-2.0 | CI scan (same version as eegfaktura-web) |
| Fonts Roboto (v51) and Roboto Mono (v31), latin + latin-ext, downloaded once from Google Fonts on 2026-10-26 and committed in `docs/assets/fonts/` | v51 / v31 | — | OFL-1.1 (texts in `docs/assets/fonts/`) | Theme font |

Not used on purpose: Mermaid (mkdocs-material would load `mermaid@11` unpinned from unpkg.com, so `mkdocs.yml` has
no mermaid fence), Google Fonts at build or read time (`theme.font: false`, fonts committed) and the theme's
repository link (`repo_url` would make the reader's browser call api.github.com). The published site makes no
external request.
