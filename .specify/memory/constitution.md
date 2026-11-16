# DigitalTrenEye Constitution

## Core Principles

### I. Identitas Produk Indonesia (NON-NEGOTIABLE)

Produk ini ditujukan untuk pembaca berita berbahasa Indonesia dan harus terasa
dibangun untuk mereka, bukan diterjemahkan seadanya.

- Nama produk adalah **DigitalTrenEye** dan wajib dipakai pada judul laporan,
  banner HTML, keluaran CLI, dan dokumentasi pengguna.
- Setiap laporan dan notifikasi wajib memuat atribusi:
  "Berdasarkan TrendRadar oleh sansan0; dimodifikasi untuk DigitalTrenEye."
- Permukaan pengguna WAJIB berbahasa Indonesia: laporan HTML, notifikasi,
  keluaran CLI yang dapat ditindaklanjuti, editor konfigurasi web, panduan
  pengguna, dan komentar file konfigurasi.
- Permukaan pengembang WAJIB berbahasa Inggris: log runtime, traceback,
  komentar kode, docstring, nama variabel/fungsi/kelas, nama tes, deskripsi MCP,
  pesan commit, README, dan template issue/PR.
- DILARANG menampilkan aksara CJK pada keluaran yang dilihat pengguna.
- DILARANG menerjemahkan hal yang dibaca mesin: kunci YAML, ID platform, nama
  field API, regex, placeholder format, dan tag HTML.
- Pesan error pustaka pihak ketiga dipertahankan verbatim; penjelasan berbahasa
  Indonesia ditambahkan sebagai kalimat terpisah di atasnya.

Matriks bahasa yang mengikat:

| Permukaan | Bahasa |
|---|---|
| Laporan HTML, notifikasi, CLI | Indonesia |
| Log, traceback | Inggris |
| Komentar config dan timeline | Indonesia |
| Prompt dan keluaran AI | Indonesia |
| Editor konfigurasi web | Indonesia, dengan opsi Inggris |
| Kamus kata kunci dan minat AI | Indonesia |
| README | Inggris |
| Panduan pengguna | Indonesia |
| MCP, komentar kode, docstring, tes, commit | Inggris |
| Kunci config, ID platform, nama field | Inggris |

Rationale: pengguna akhir menilai produk dari bahasa yang mereka baca, sedangkan
pemelihara menilai dari kejelasan kode dan log. Mencampur keduanya menghasilkan
produk yang terasa terjemahan.

### II. Lokalisasi sebagai Infrastruktur

- Seluruh string yang dilihat pengguna WAJIB berasal dari katalog terpusat di
  `trendradar/i18n/`, bukan literal yang tersebar di dalam logika.
- Resolusi string menggunakan fallback berurutan: `id` -> `en` -> nama kunci.
  Kunci yang hilang wajib terdeteksi oleh tes.
- Locale antarmuka disimpan pada `app.locale` dengan default `id`, terpisah dari
  `ai_analysis.language` yang mengatur bahasa keluaran model.
- Format tanggal, angka, dan waktu mengikuti konvensi Indonesia:
  `17 November 2026`, `1.234,5`.
- Timezone default `Asia/Jakarta`; pengguna dapat memilih `Asia/Makassar` atau
  `Asia/Jayapura` melalui konfigurasi.
- Menambah bahasa baru DILARANG menyentuh logika bisnis.

Rationale: tanpa katalog, setiap fitur baru menambah titik lokalisasi dan
memperbesar kemungkinan teks Mandarin tertinggal.

### III. Independensi dan Stabilitas Arsitektur

- Proyek dikembangkan mandiri sebagai turunan independen; tidak ada kewajiban
  menyinkronkan perubahan dengan repositori asal.
- Struktur modul `core/`, `crawler/`, `storage/`, dan `ai/` dipertahankan.
  Penulisan ulang modul hanya boleh dilakukan dengan ADR yang menyebut bug atau
  keterbatasan konkret yang diperbaiki.
- API publik modul dijaga stabil. Perubahan konfigurasi bersifat aditif; kunci
  lama tidak diganti tanpa rencana migrasi.
- Perubahan skema database WAJIB disertai rencana migrasi dan tes.
- Perubahan perilaku, format data, atau kontrak konfigurasi WAJIB dicatat sebagai
  ADR di `docs/adr/`.

Rationale: nilai proyek ada pada kualitas data dan pengalaman Indonesia, bukan
pada penulisan ulang mesin yang sudah stabil.

### IV. AI Opsional dan Degradasi Anggun

- Alur inti crawl -> simpan -> laporan WAJIB berjalan tanpa AI, tanpa API key,
  dan tanpa koneksi ke penyedia model.
- AI mati secara default; hanya aktif bila pengguna mengaktifkannya dan
  menyediakan kredensial.
- Penyedia model bersifat agnostik melalui LiteLLM; logika inti DILARANG
  bergantung pada satu vendor.
- Kegagalan AI DILARANG menggagalkan crawl, penyimpanan, atau pembuatan laporan.
- AI DILARANG dipakai untuk menerjemahkan antarmuka; AI hanya untuk analisis dan
  terjemahan konten berita.
- Prompt AI berbahasa Indonesia. Bila keluaran terstruktur gagal diparsing pada
  dua rilis berturut-turut, prompt boleh dikembalikan ke bahasa Inggris tanpa
  mengubah bahasa keluaran, dan perubahan tersebut dicatat sebagai ADR.

Rationale: pengguna harus bisa menjalankan produk tanpa biaya berlangganan dan
tanpa ketergantungan layanan pihak ketiga.

### V. Kualitas Terukur (NON-NEGOTIABLE)

- Definisi selesai untuk setiap perubahan: `--doctor` tanpa status gagal,
  seluruh tes lulus, dan tidak ada aksara CJK pada keluaran pengguna.
- Baseline tes yang diakui: 29 tes dan 35 subtes pada Python 3.14. Penurunan
  jumlah tes dianggap regresi kecuali dijelaskan tertulis.
- Tes regresi WAJIB ada untuk: pemetaan label antarmuka, parser RSS Indonesia,
  format tanggal Indonesia, dan pencocokan judul berbahasa Indonesia.
- Ambang mutu pencocokan kata: maksimal 1 false positive dari 50 judul uji.
  Ambang ini menjadi gerbang sebelum pekerjaan laporan dimulai.
- Python minimum `>=3.12`. Target utama 3.12 dan 3.13; 3.14 didukung selama
  seluruh tes lulus.
- Seluruh file teks WAJIB UTF-8 tanpa BOM.

Rationale: lokalisasi tanpa ukuran mudah terasa selesai padahal masih menyisakan
teks lama atau salah cocok berita.

## Keamanan, Data, dan Lisensi

- DILARANG menyimpan kredensial pada file yang dilacak git. Kredensial hanya
  melalui environment variable atau file `.env` yang diabaikan git.
- File konfigurasi contoh WAJIB memiliki nilai kosong untuk seluruh field
  kredensial.
- Log DILARANG menampilkan API key, token, webhook, atau isi kredensial, termasuk
  di dalam pesan error.
- File rahasia yang sudah terlanjur dilacak WAJIB dilepas dari indeks dengan
  `git rm --cached`; menghapus dari commit terbaru tidak cukup.
- Kebocoran kredensial WAJIB diikuti pencabutan dan penerbitan ulang kredensial.
- Retensi data lokal default 90 hari untuk database. File laporan HTML di
  `output/` tidak dihapus otomatis pada fase ini.
- Data pengguna tetap lokal; proyek DILARANG mengirim telemetri.
- Lisensi proyek adalah GPL-3.0. `LICENSE` tidak boleh dihapus atau diganti, dan
  copyright pemilik asli dipertahankan.
- README WAJIB memuat bagian "Perubahan dari versi asli" yang merangkum
  divergensi.
- DILARANG memakai nama atau logo proyek asal sehingga menimbulkan kesan
  dukungan resmi.

## Sumber Data dan Alur Pengembangan

- RSS adalah jalur utama. Sumber berita Indonesia berstatus warga kelas satu;
  sumber internasional tetap didukung dan dapat dinonaktifkan per feed.
- Platform bawaan asal Tiongkok dihapus dari daftar aktif dan contohnya disisakan
  di komentar konfigurasi. Kode platform tidak dihapus.
- Setiap feed WAJIB diverifikasi sebelum diaktifkan: HTTPS, dapat diakses, domain
  sesuai, dan format RSS/Atom valid.
- Proyek menghormati `robots.txt` dan ketentuan layanan sumber. DILARANG
  mengambil data dari balik autentikasi tanpa izin.
- User-Agent WAJIB menyebut identitas proyek dan cara menghubungi pemelihara.
- Kata kunci, timeline, dan minat AI disimpan sebagai konfigurasi berbahasa
  Indonesia yang dapat diedit tanpa menyentuh kode.
- Alur kerja fitur mengikuti urutan: constitution -> specify -> clarify -> plan
  -> checklist -> tasks -> implement -> converge.
- Implementasi dilakukan satu tugas satu commit. Tes ditulis pada commit yang
  sama dengan kode. Pesan commit berbahasa Inggris.
- README berbahasa Inggris; panduan pengguna ringkas berbahasa Indonesia
  disediakan terpisah. Perubahan besar dicatat di changelog.

## Governance

- Konstitusi ini mengikat seluruh kontribusi, termasuk perubahan konfigurasi
  default. Bila kode bertentangan dengan konstitusi, kode yang diubah kecuali
  amandemen disetujui lebih dulu.
- Amandemen diajukan sebagai ADR, disetujui pemelihara, lalu dicatat dengan
  kenaikan versi:
  - MAJOR: penghapusan atau redefinisi prinsip yang tidak kompatibel.
  - MINOR: penambahan prinsip atau bagian baru, atau perluasan material.
  - PATCH: klarifikasi, perbaikan kata, atau penyempurnaan non-semantik.
- Setiap perubahan wajib diverifikasi terhadap gerbang: `--doctor` bersih, tes
  lulus, pemindai CJK bersih, dan tidak ada kredensial pada file yang dilacak.
  Pelanggaran gerbang memblokir penggabungan.
- Konstitusi ditinjau setiap enam bulan.

**Version**: 1.0.0 | **Ratified**: 2026-11-17 | **Last Amended**: 2026-11-17
