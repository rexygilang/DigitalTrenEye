# Contract: CLI

**Feature**: `001-lokalisasi-id`

## Perintah yang ada

| Perintah | Fungsi |
|---|---|
| `uv run python -m trendradar` | Menjalankan alur crawl dan laporan |
| `uv run python -m trendradar --doctor` | Pemeriksaan mandiri konfigurasi dan lingkungan |
| `uv run python -m trendradar --show-schedule` | Menampilkan jadwal aktif |
| `uv run python -m trendradar --test-notification` | Mengirim notifikasi percobaan |

## Opsi baru

| Opsi | Sifat | Perilaku |
|---|---|---|
| `--lang <id\|en>` | Tersembunyi dari `--help` | Mengubah bahasa antarmuka. Default mengikuti `app.locale`. Log tidak berubah. |

## Aturan bahasa

- Seluruh teks bantuan, status, hasil pemeriksaan, dan pesan error yang dapat
  ditindaklanjuti berbahasa Indonesia.
- Log runtime, traceback, dan pesan debug berbahasa Inggris.
- Pesan pustaka pihak ketiga dipertahankan verbatim; penjelasan Indonesia
  ditambahkan sebagai kalimat terpisah.
- Aksara CJK dilarang pada seluruh keluaran.

## Aturan keluaran

- Satu pesan per baris; tanpa emoji dekoratif.
- Status pemeriksaan memakai penanda yang dapat dicari: `OK`, `PERINGATAN`,
  `GAGAL` (bukan simbol).
- Exit code: `0` bila tidak ada status `GAGAL`; `1` bila ada `GAGAL`.
- `--lang` tidak boleh mengubah exit code.

## Contoh

```text
$ uv run python -m trendradar --doctor
Memeriksa lingkungan...
OK       Python 3.14.9
OK       Konfigurasi dimuat
PERINGATAN  Kanal notifikasi belum diatur
OK       Penyimpanan lokal dapat digunakan
GAGAL    AI aktif tetapi kredensial belum diisi

Ringkasan: 1 gagal, 1 peringatan
```

## Larangan

- DILARANG menerjemahkan nama opsi, nama kunci konfigurasi, atau nama perintah.
- DILARANG menampilkan `--lang` pada keluaran `--help`.
- DILARANG mengubah format mesin yang sudah dipakai skrip lain.
