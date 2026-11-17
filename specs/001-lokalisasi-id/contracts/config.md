# Contract: Konfigurasi

**Feature**: `001-lokalisasi-id`

## Kunci baru

| Kunci | Tipe | Default | Keterangan |
|---|---|---|---|
| `app.locale` | string | `"id"` | Bahasa antarmuka: `id` atau `en` |
| `app.timezone` | string | `"Asia/Jakarta"` | Zona waktu tampilan dan penjadwalan |
| `storage.local.retention_days` | integer | `90` | Retensi basis data lokal; `0` berarti permanen |

## Kunci yang berubah nilai default

| Kunci | Lama | Baru |
|---|---|---|
| `app.timezone` | `Asia/Shanghai` | `Asia/Jakarta` |
| `storage.local.retention_days` | `0` | `90` |
| `platforms.sources` | 11 platform Tiongkok aktif | Dihapus dari daftar aktif, contoh di komentar |
| `rss.feeds` | Hacker News, Yahoo Finance | Minimal 10 feed Indonesia terverifikasi |

## Kunci yang tidak berubah

- `ai_analysis.language` tetap `"Indonesian"` dan tetap terpisah dari
  `app.locale`.
- `ai_translation.language` tetap `"Indonesian"`.
- Seluruh nama kunci, ID platform, dan nama field tidak diterjemahkan.
- Kunci lama tidak diganti nama; konfigurasi pengguna lama tetap terbaca.

## Aturan kompatibilitas

- Bila `app.locale` tidak ada, sistem memakai `id`.
- Bila `app.locale` berisi nilai tidak dikenal, sistem memakai `id` dan mencatat
  peringatan.
- Bila `storage.local.retention_days` tidak ada, sistem memakai `90`.
- Nilai `retention_days: 0` tetap dihormati sebagai "simpan permanen".

## Komentar

Seluruh komentar penjelasan berbahasa Indonesia. Nama kunci tetap Inggris.
Setiap kunci baru wajib memiliki komentar yang menjelaskan nilai yang sah dan
dampaknya.

## Larangan

- DILARANG menyimpan kredensial pada `config.yaml`.
- DILARANG menerjemahkan nilai yang dibaca mesin (`id` feed, ID platform).
- DILARANG menghapus contoh platform lama sepenuhnya; simpan sebagai komentar.
