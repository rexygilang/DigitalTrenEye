# Research: Lokalisasi Indonesia

**Feature**: `001-lokalisasi-id` | **Date**: 2026-11-17

## 1. Mekanisme katalog string

**Decision**: Modul dict internal di `trendradar/i18n/` dengan fungsi `t(key, **kwargs)`.
Fallback `id` → `en` → nama kunci.

**Rationale**: Tanpa dependensi tambahan; mudah diuji; cocok untuk proyek satu
pengguna. Kebutuhan format tanggal/angka Indonesia sederhana dan tidak
memerlukan pustaka locale penuh.

**Alternatives considered**:
- `gettext`: standar, tetapi menambah langkah kompilasi `.mo` dan lebih rumit
  untuk kontributor tunggal.
- Babel: format tanggal/angka lengkap, tetapi dependensi baru besar untuk
  kebutuhan yang bisa ditangani 12 nama bulan dan 7 nama hari.

## 2. Pencocokan kata Bahasa Indonesia

**Decision**: Normalisasi → tokenisasi → pencocokan frasa berbasis token dengan
batas kata. Varian imbuhan dihasilkan dari kata kunci (bukan menstem seluruh
judul) memakai antarmuka `Stemmer`; implementasi bawaan Sastrawi.

**Rationale**: Menstem setiap judul mahal dan menambah false positive. Menghasilkan
varian dari kata kunci jauh lebih murah dan dapat di-cache. Batas kata
menghilangkan kasus `demo` vs `demokrasi`.

**Alternatives considered**:
- Substring seperti sekarang: cepat, tetapi menghasilkan false positive yang
  menjadi masalah utama fitur ini.
- Regex word boundary saja: lebih baik, tetapi gagal pada kata berimbuhan.
- Stemming penuh pada judul dan kata kunci: cakupan luas, tetapi over-match dan
  biaya CPU lebih tinggi.

**Catatan implementasi**:
- Frasa multi-kata dicocokkan sebagai urutan token yang berurutan.
- Pola regex pengguna dipertahankan apa adanya.
- Cache varian per kata kunci dibangun sekali per run.
- Bila Sastrawi tidak tersedia, pencocokan tetap berjalan dengan batas kata saja
  dan mencatat peringatan di log.

## 3. Format tanggal dan angka

**Decision**: Fungsi manual `format_date`, `format_datetime`, `format_number`.

**Rationale**: Nama bulan/hari Indonesia berjumlah kecil dan stabil. Pemisah
ribuan `.` dan desimal `,` cukup satu fungsi.

**Alternatives considered**: Babel (dependensi baru), `locale` modul Python
(tidak konsisten di Windows).

**Aturan**:
- `17 November 2026`
- `1.234,5`
- Waktu memakai zona dari konfigurasi, bukan zona sistem.

## 4. Injeksi label laporan

**Decision**: Ekstrak label ke `report/labels.py`, lalu suntikkan ke f-string
`render_html_content`. Struktur HTML tidak dipecah.

**Rationale**: `report/html.py` berukuran 3.221 baris dalam satu fungsi. Pemecahan
template berisiko tinggi dan tidak diperlukan untuk mencapai FR-001.

**Alternatives considered**:
- Jinja2: menambah dependensi dan menulis ulang seluruh generator.
- Pemecahan fungsi: lebih rapi, tetapi menjadi pekerjaan tersendiri; ditunda ke
  ADR terpisah.

## 5. Sumber RSS Indonesia

**Decision**: RSS sebagai jalur utama, minimal 10 feed terverifikasi. Verifikasi
dilakukan saat implementasi, bukan diasumsikan di plan.

**Kandidat awal** (belum terverifikasi):
Detik, Kompas, Tempo, CNN Indonesia, CNBC Indonesia, Bisnis.com, Antara,
Katadata, Tirto, Kumparan, Republika, Media Indonesia, Suara.com, IDN Times,
Jawa Pos.

**Kriteria verifikasi**:
- HTTPS dan dapat diakses tanpa autentikasi.
- Mengembalikan RSS/Atom valid dengan minimal 5 item.
- Memuat tanggal terbit yang dapat diparse.
- Domain sesuai dengan nama portal.

**Alternatives considered**: API berbayar, scraping HTML penuh (ditolak karena
rawan diblokir dan melanggar ketentuan sebagian portal).

## 6. Notifikasi Telegram

**Decision**: Pertahankan pengirim Telegram yang ada; pindahkan format pesan ke
`notification/templates.py`. Pesan berisi judul, sumber, waktu zona pengguna, dan
tautan.

**Rationale**: Pengirim sudah menangani batas panjang dan pemecahan pesan.
Perubahan hanya pada isi dan bahasa.

**Alternatives considered**: WhatsApp (berbayar, verifikasi bisnis), email
(kuota harian, kurang instan).

## 7. Retensi data

**Decision**: `storage.local.retention_days: 90`. Pembersihan memakai
`cleanup_old_data` yang sudah ada. Jumlah data yang dihapus dicatat di log.
Laporan HTML tidak dibersihkan otomatis.

**Rationale**: Mekanisme sudah tersedia; tidak perlu kode baru selain log dan
nilai konfigurasi.

## 8. Strategi pengujian

**Decision**: `pytest` untuk tes baru; tes `unittest` lama tetap dipertahankan.
Tambahkan `pytest` ke grup `dev`.

**Rationale**: Baseline sudah dijalankan dengan `uv run --with pytest`. Tanpa
deklarasi dependensi, reproduksi bergantung pada flag manual.

**Data uji**: 50 judul berita Indonesia nyata dikumpulkan saat tugas T007 dari
feed terverifikasi, lalu disimpan sebagai `tests/data/judul_id.csv` agar tes
tidak memerlukan jaringan.

## 9. Kompatibilitas konfigurasi

**Decision**: Tambah `app.locale` dan ubah nilai default yang sudah ada; tidak
mengganti nama kunci.

**Rationale**: Konfigurasi pengguna lama tetap terbaca. Perubahan perilaku
terbatas pada nilai default dan bahasa tampilan.

**Kunci baru**:
- `app.locale: "id"` (default)
- Kunci lama `ai_analysis.language` tetap dipakai untuk bahasa keluaran AI.

## 10. Pemisahan UI dan log

**Decision**: Modul `trendradar/cli/output.py` menyediakan `ui()` dan `log()`.
`ui()` memakai katalog dan menghormati `--lang`. `log()` selalu Inggris.

**Rationale**: Saat ini keduanya memakai `print`. Pemisahan mencegah pesan
debug ikut diterjemahkan dan menjaga log tetap dapat dicari.

## 11. Rollback

**Decision**: Rollback berbasis git per tugas. Tidak ada migrasi data, sehingga
`git revert` cukup. Sebelum implementasi, baseline diberi tag.

**Rationale**: Perubahan bersifat aditif dan tidak mengubah skema. Satu-satunya
operasi merusak adalah pembersihan retensi; data lama harus dicadangkan sebelum
menjalankan pembersihan pertama.

**Rencana**:
- Tag `baseline-lokalisasi` pada commit sebelum T003.
- Satu tugas satu commit.
- `git revert <commit>` untuk membatalkan tugas tertentu.
- Cadangkan `output/` sebelum mengaktifkan retensi 90 hari.
