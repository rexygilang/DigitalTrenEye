# Implementation Plan: Lokalisasi Indonesia

**Branch**: `terjemahan-id` | **Date**: 2026-11-17 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-lokalisasi-id/spec.md`

## Summary

Mengubah DigitalTrenEye agar layak dipakai pembaca berita Indonesia: antarmuka,
laporan, CLI, notifikasi, dan konfigurasi berbahasa Indonesia; pencocokan kata
yang benar untuk bahasa Indonesia; RSS portal Indonesia sebagai sumber utama;
AI tetap opsional dan mati secara default. Pendekatan: katalog string terpusat,
modul pencocokan berbasis token, injeksi label ke generator laporan yang ada,
dan perubahan konfigurasi yang bersifat aditif. Tidak ada perubahan skema
basis data.

## Technical Context

**Language/Version**: Python `>=3.12` (mesin pengujian: 3.14.9)

**Primary Dependencies**: `requests`, `PyYAML`, `feedparser`, `litellm`,
`pytz`, `boto3` (sudah ada). Tambahan: `Sastrawi==1.0.1` (stemming, pure Python)
dan `pytest` pada grup `dev`.

**Storage**: SQLite lokal via `trendradar/storage/`; tanpa perubahan skema.
Retensi `storage.local.retention_days` diubah dari `0` menjadi `90`.

**Testing**: `pytest` (baru dideklarasikan) di atas tes `unittest` yang sudah
ada. Baseline: 29 tes + 35 subtes lulus.

**Target Platform**: Windows lokal, dijalankan manual dari terminal. Tanpa
server, tanpa Docker, tanpa cron.

**Project Type**: CLI + laporan HTML statis.

**Performance Goals**: `--doctor` selesai < 10 detik tanpa AI. Overhead
pencocokan < 5% dibanding substring pada 150 judul per run. Pembuatan laporan
tidak lebih lambat dari baseline.

**Constraints**: Alur inti harus berjalan tanpa AI dan tanpa kredensial.
Laporan harus dapat dibuka offline. Tidak ada telemetri. Semua file UTF-8 tanpa
BOM. Tanpa perubahan skema database.

**Scale/Scope**: 10–15 feed RSS, ±150 artikel per run, satu pengguna lokal.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Prinsip | Gerbang | Status |
|---|---|---|
| I. Identitas Produk Indonesia | Nama DigitalTrenEye, atribusi, UI Indonesia, log Inggris, nol CJK | PASS |
| II. Lokalisasi sebagai Infrastruktur | Katalog `trendradar/i18n/`, fallback `id→en→key`, `app.locale` terpisah dari bahasa AI, format tanggal/angka Indonesia | PASS |
| III. Independensi dan Stabilitas Arsitektur | Tanpa penulisan ulang modul inti, API publik stabil, config aditif, tanpa perubahan skema | PASS |
| IV. AI Opsional | AI mati default, kegagalan AI tidak menggagalkan alur inti, tanpa ketergantungan vendor | PASS |
| V. Kualitas Terukur | Baseline tes dicatat, tes regresi wajib, ambang 1/50, UTF-8 tanpa BOM | PASS |
| Keamanan, Data, Lisensi | Tanpa kredensial di file terlacak, `docker/.env` sudah dilepas, GPL-3.0 dipertahankan | PASS |

Tidak ada pelanggaran yang memerlukan Complexity Tracking.

**Re-check setelah Phase 1 design**: PASS. Desain menambah paket `i18n/`,
`core/text.py`, `cli/output.py`, dan `notification/templates.py` tanpa mengubah
skema, nama paket, atau API publik. Katalog string dan format lokal tercakup
dalam kontrak. Tidak ada ketergantungan AI pada alur inti.

## Project Structure

### Documentation (this feature)

```text
specs/001-lokalisasi-id/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   ├── cli.md
│   ├── config.md
│   ├── report-labels.md
│   └── notification-telegram.md
├── checklists/
│   └── requirements.md
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
trendradar/
├── i18n/                     # BARU: katalog string dan format lokal
│   ├── __init__.py           # t(), set_locale(), get_locale()
│   ├── id.py                 # katalog Indonesia (default)
│   ├── en.py                 # katalog Inggris (cadangan)
│   └── format.py             # tanggal, angka, waktu
├── core/
│   ├── text.py               # BARU: normalisasi, token, batas kata, varian imbuhan
│   ├── frequency.py          # UBAH: pakai core/text.py
│   ├── loader.py             # UBAH: APP_LOCALE, retensi
│   └── scheduler.py          # tidak berubah
├── report/
│   ├── labels.py             # BARU: label laporan
│   ├── html.py               # UBAH: label dari katalog
│   └── generator.py          # UBAH: teruskan locale
├── notification/
│   ├── templates.py          # BARU: template pesan
│   ├── formatters.py         # UBAH: pakai template
│   └── senders.py            # UBAH kecil: Telegram
├── cli/
│   └── output.py             # BARU: ui() Indonesia, log() Inggris
├── commands/                 # UBAH: pesan doctor/status/test-notification
└── __main__.py               # UBAH: ui/log, opsi --lang tersembunyi

config/
├── config.yaml               # UBAH: locale, WIB, retensi, RSS Indonesia, komentar
├── timeline.yaml             # UBAH: komentar Indonesia
└── frequency_words.txt       # UBAH: kamus Indonesia + grup topik

docs/
├── assets/i18n.js            # UBAH: locale id
└── panduan-id.md             # BARU: panduan pengguna

tests/
├── test_i18n.py              # BARU
├── test_text_id.py           # BARU
├── test_frequency_id.py      # BARU
├── test_report_labels.py     # BARU
├── test_cli_language.py      # BARU
├── data/judul_id.csv         # BARU: 50 judul uji
└── (tes lama dipertahankan)

tools/
└── check_cjk.py              # BARU: pemindai CJK
```

**Structure Decision**: Proyek tunggal. Semua kode berada di paket `trendradar`
yang sudah ada. Modul baru ditambahkan sebagai paket/direktori baru tanpa
mengubah struktur paket lama, sehingga impor dan perintah yang ada tetap
berjalan.

## Complexity Tracking

Tidak ada pelanggaran konstitusi; tabel ini tidak digunakan.
