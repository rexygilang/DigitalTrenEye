# Contract: Notifikasi Telegram

**Feature**: `001-lokalisasi-id`

## Format pesan

```text
📰 DigitalTrenEye — 17 November 2026, 14.30 WIB

1. Judul berita pertama
   Kompas · 14.05 WIB
   https://contoh.id/berita-1

2. Judul berita kedua
   Tempo · 13.50 WIB
   https://contoh.id/berita-2

Total: 2 berita
```

Aturan:

- Bahasa Indonesia untuk seluruh teks tetap.
- Judul berita apa adanya, termasuk bila berbahasa asing.
- Nama portal sesuai merek.
- Waktu memakai zona pengguna dan singkatan `WIB`, `WITA`, atau `WIT`.
- Tautan ditulis sebagai URL utuh agar dapat diklik.
- Tanpa tabel dan tanpa HTML kompleks.

## Kasus kosong

- Tidak ada artikel baru: pesan tidak dikirim.
- Tidak ada kanal aktif: `--test-notification` melaporkan `GAGAL` dengan
  penjelasan Indonesia.

## Batas dan pemecahan

- Pesan mengikuti batas panjang Telegram.
- Pemecahan memakai mekanisme yang sudah ada; pemecahan tidak boleh memotong
  URL.
- Bila pesan dipecah, setiap bagian memuat konteks tanggal.

## Larangan

- DILARANG mengirim pesan berisi aksara CJK.
- DILARANG menerjemahkan judul berita.
- DILARANG menampilkan kredensial atau token di pesan maupun log.
