# Contract: Label Laporan

**Feature**: `001-lokalisasi-id`

## Label wajib

| Kunci | Teks Indonesia |
|---|---|
| `report.title` | Laporan Berita |
| `report.generated_at` | Dibuat pada |
| `report.period` | Periode |
| `report.total_articles` | Jumlah berita |
| `report.source` | Sumber |
| `report.published_at` | Waktu terbit |
| `report.matched_keywords` | Kata kunci cocok |
| `report.rank` | Peringkat |
| `report.no_results` | Tidak ada berita yang cocok pada periode ini |
| `report.group_default` | Grup |
| `report.rss_section` | Berita RSS |
| `report.hotlist_section` | Daftar populer |
| `report.footer` | Berdasarkan TrendRadar oleh sansan0; dimodifikasi untuk DigitalTrenEye |

Daftar ini minimum. Label tambahan yang sudah ada wajib masuk katalog, bukan
literal.

## Aturan format

- Tanggal: `17 November 2026`.
- Waktu: `17 November 2026, 14.30 WIB`.
- Angka: `1.234` dan `1.234,5`.
- Nama zona waktu ditampilkan sebagai `WIB`, `WITA`, atau `WIT` sesuai konfigurasi.
- Judul berita dan nama portal tidak diubah.

## Aksesibilitas

- Atribut `lang` pada elemen HTML utama bernilai `id`.
- Judul halaman memakai Bahasa Indonesia.
- Tidak ada label yang hanya berupa ikon tanpa teks alternatif.

## Larangan

- DILARANG menyisakan aksara CJK pada label, judul bagian, atau pesan kosong.
- DILARANG menerjemahkan judul berita dan nama merek portal.
- DILARANG mengubah struktur HTML yang sudah ada pada fase ini.
