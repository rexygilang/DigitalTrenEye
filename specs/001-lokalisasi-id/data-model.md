# Data Model: Lokalisasi Indonesia

**Feature**: `001-lokalisasi-id` | **Date**: 2026-11-17

Tidak ada perubahan skema basis data. Model di bawah menjelaskan entitas logis,
sumber datanya, dan aturan validasi yang mengikat implementasi.

## Article

Representasi satu berita dari feed atau platform.

| Field | Sumber | Aturan |
|---|---|---|
| `title` | feed | Wajib; ditampilkan apa adanya, tanpa terjemahan |
| `url` | feed | Wajib; harus HTTPS bila sumber mendukung |
| `source` | konfigurasi feed | Nama merek portal dipertahankan |
| `published_at` | feed | Opsional; bila tidak dikenali, artikel tetap disimpan dan ditandai |
| `feed_id` | konfigurasi | Wajib; menghubungkan artikel ke feed |
| `fetched_at` | sistem | Waktu pengambilan, memakai zona konfigurasi |
| `matched_group` | hasil pencocokan | Grup kata kunci yang cocok, bila ada |

**Validasi**: judul kosong ditolak. URL duplikat dalam satu run diabaikan.
Karakter non-ASCII diperbolehkan.

**Lifecycle**: diambil → disimpan → dicocokkan → ditampilkan → dihapus saat
retensi.

## Feed

Sumber berita RSS.

| Field | Aturan |
|---|---|
| `id` | Unik, stabil, huruf kecil |
| `name` | Nama merek portal, tidak diterjemahkan |
| `url` | HTTPS, dapat diakses tanpa autentikasi |
| `enabled` | Boolean; default sesuai konfigurasi |
| `max_age_days` | Opsional; menimpa batas global |

**Validasi**: minimal 10 feed aktif pada konfigurasi bawaan. Feed yang gagal
diakses dicatat dan dilewati; tidak menggagalkan run.

**Relasi**: satu Feed memiliki banyak Article.

## KeywordGroup

Satu kelompok kata kunci yang ditampilkan sebagai satu bagian laporan.

| Field | Aturan |
|---|---|
| `name` | Opsional; alias grup |
| `keywords` | Minimal satu; OR di dalam grup |
| `required_terms` | Opsional; semua harus cocok (`+kata`) |
| `excluded_terms` | Opsional; salah satu cocok berarti artikel dibuang (`!kata`) |
| `max_items` | Opsional; batas tampilan (`@angka`) |
| `aliases` | Opsional; nama tampilan per kata kunci (`kata => alias`) |
| `patterns` | Opsional; regex pengguna (`/pola/`), tidak diterjemahkan |

**Validasi**: grup tanpa kata kunci diabaikan dengan peringatan. Regex tidak
valid dilaporkan dan grup terkait dilewati, bukan menggagalkan run.

**Relasi**: satu grup cocok dengan banyak Article; satu Article dapat cocok
dengan lebih dari satu grup.

## GlobalFilter

Daftar istilah yang selalu dibuang sebelum pencocokan.

**Aturan**: istilah cocok secara batas kata; pola regex dipertahankan. Filter
global berlaku untuk semua grup.

## Report

Kumpulan artikel yang disajikan per run.

| Aspek | Aturan |
|---|---|
| Label | Seluruhnya dari katalog `id` |
| Tanggal | Format `17 November 2026` |
| Angka | Pemisah ribuan `.`, desimal `,` |
| Zona waktu | Mengikuti konfigurasi pengguna |
| Kondisi kosong | Tetap dihasilkan dengan pesan kosong berbahasa Indonesia |
| Urutan | Mengikuti perilaku laporan yang ada; tidak diubah fitur ini |

**Relasi**: Report berisi Article yang lolos filter dan pencocokan.

## Notification

Ringkasan Report yang dikirim ke kanal pesan.

| Field | Aturan |
|---|---|
| `channel` | Telegram sebagai bawaan |
| `items` | Judul, sumber, waktu zona pengguna, tautan |
| `empty_state` | Tidak mengirim pesan bila tidak ada artikel baru |
| `language` | Indonesia |

**Validasi**: pesan mengikuti batas panjang kanal; pemecahan memakai mekanisme
yang sudah ada.

## Retention

| Aspek | Aturan |
|---|---|
| Cakupan | Basis data lokal |
| Default | 90 hari |
| Tindakan | Hapus otomatis saat pembersihan |
| Log | Jumlah data yang dihapus dicatat |
| Laporan HTML | Tidak dihapus otomatis |

**Catatan**: operasi ini merusak. Cadangkan `output/` sebelum pembersihan
pertama dijalankan pada data lama.

## Locale

| Field | Aturan |
|---|---|
| `app.locale` | Default `id`; nilai lain: `en` |
| `app.timezone` | Default `Asia/Jakarta`; alternatif Indonesia: `Asia/Makassar`, `Asia/Jayapura` |
| `ai_analysis.language` | Tetap terpisah; mengatur bahasa keluaran AI |

## Perubahan Penyimpanan

Tidak ada. Seluruh field baru berada di konfigurasi atau dihasilkan saat runtime.
Kolom basis data yang ada tidak diubah, ditambah, atau dihapus.
