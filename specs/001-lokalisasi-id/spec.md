# Feature Specification: Lokalisasi Indonesia

**Feature Branch**: `001-lokalisasi-id`

**Created**: 2026-11-17

**Status**: Draft

**Input**: User description: "Lokalisasi DigitalTrenEye untuk pengguna Indonesia: antarmuka, laporan, CLI, notifikasi, dan konfigurasi berbahasa Indonesia; RSS portal Indonesia; pencocokan kata yang benar untuk bahasa Indonesia; AI tetap opsional dan mati secara default."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Laporan berbahasa Indonesia tanpa sisa Mandarin (Priority: P1)

Seorang pembaca Indonesia menjalankan pemantauan berita, membuka laporan HTML, dan membaca seluruh label, judul bagian, serta format tanggal dalam Bahasa Indonesia. Tidak ada aksara Mandarin yang tersisa di laporan.

**Why this priority**: Tanpa ini, produk tidak dapat digunakan oleh target pengguna sama sekali.

**Independent Test**: Hasilkan satu laporan dari data contoh, lalu periksa bahwa seluruh label berbahasa Indonesia, tanggal terbaca sebagai `17 November 2026`, angka memakai pemisah Indonesia, dan tidak ada aksara CJK.

**Acceptance Scenarios**:

1. **Given** pengguna membuka laporan yang dihasilkan, **When** pengguna membaca seluruh bagian laporan, **Then** semua label dan judul bagian berbahasa Indonesia.
2. **Given** laporan memuat tanggal dan angka, **When** pengguna membacanya, **Then** tanggal tampil seperti `17 November 2026` dan angka seperti `1.234,5`.
3. **Given** laporan memuat berita dari sumber asing, **When** judul berita berbahasa Inggris atau Mandarin ditampilkan, **Then** judul tersebut tampil apa adanya tanpa diterjemahkan.

---

### User Story 2 - Berita yang cocok, bukan sekadar mirip (Priority: P1)

Seorang pengguna menetapkan kata kunci berbahasa Indonesia, lalu menerima daftar berita yang benar-benar relevan. Kata kunci pendek tidak lagi memicu berita yang hanya kebetulan mengandung potongan kata.

**Why this priority**: Laporan berbahasa Indonesia tetap tidak berguna bila isinya berita salah cocok.

**Independent Test**: Uji 50 judul berita Indonesia nyata terhadap seperangkat kata kunci, lalu hitung berapa judul yang cocok secara keliru.

**Acceptance Scenarios**:

1. **Given** kata kunci `demo`, **When** sistem memeriksa judul "Demokrasi Indonesia hari ini", **Then** judul tersebut tidak dianggap cocok.
2. **Given** kata kunci `aksi`, **When** sistem memeriksa judul "Transaksi saham naik", **Then** judul tersebut tidak dianggap cocok.
3. **Given** kata kunci `pemilu`, **When** sistem memeriksa judul "Pemilu 2029 dipersiapkan", **Then** judul tersebut dianggap cocok.
4. **Given** kata kunci berimbuhan seperti `berita`, **When** sistem memeriksa judul "Pemberitaan media berubah", **Then** judul tersebut dapat dikenali sebagai varian kata yang relevan.

---

### User Story 3 - Menjalankan dan memeriksa dari terminal (Priority: P2)

Seorang pengguna menjalankan pemeriksaan mandiri dan membaca status dalam Bahasa Indonesia, sementara log teknis tetap berbahasa Inggris untuk keperluan debugging.

**Why this priority**: Pengguna harus bisa mendiagnosis masalah sendiri tanpa memahami istilah Mandarin atau Inggris.

**Independent Test**: Jalankan pemeriksaan mandiri pada konfigurasi tanpa AI dan tanpa kanal notifikasi, lalu baca seluruh pesan yang muncul.

**Acceptance Scenarios**:

1. **Given** konfigurasi tanpa AI, **When** pengguna menjalankan pemeriksaan mandiri, **Then** seluruh pesan hasil pemeriksaan berbahasa Indonesia dan tidak ada status gagal.
2. **Given** pengguna menjalankan bantuan perintah, **When** daftar opsi ditampilkan, **Then** seluruh deskripsi berbahasa Indonesia dan opsi bahasa Inggris tidak terlihat.
3. **Given** pengguna ingin kembali ke bahasa Inggris untuk debugging, **When** pengguna memakai opsi tersembunyi tersebut, **Then** pesan antarmuka kembali berbahasa Inggris tanpa mengubah bahasa log.

---

### User Story 4 - Notifikasi Telegram berbahasa Indonesia (Priority: P2)

Seorang pengguna menerima ringkasan berita melalui Telegram berisi judul, sumber, waktu WIB, dan tautan, seluruhnya dalam Bahasa Indonesia.

**Why this priority**: Notifikasi adalah cara utama pengguna memantau berita tanpa membuka laporan.

**Independent Test**: Kirim satu notifikasi percobaan dan periksa isi pesan, zona waktu, serta tautan.

**Acceptance Scenarios**:

1. **Given** kanal Telegram aktif, **When** pengguna mengirim notifikasi percobaan, **Then** pesan berbahasa Indonesia memuat judul, sumber, waktu WIB, dan tautan berita.
2. **Given** tidak ada berita baru, **When** jadwal notifikasi berjalan, **Then** sistem tidak mengirim pesan kosong.

---

### User Story 5 - Mengubah pengaturan tanpa membaca Mandarin (Priority: P3)

Seorang pengguna membuka file konfigurasi dan editor konfigurasi web, lalu memahami setiap pilihan karena penjelasan dan antarmukanya berbahasa Indonesia. Platform bawaan asal Tiongkok tidak lagi aktif secara default.

**Why this priority**: Konfigurasi yang tidak terbaca membuat pengguna bergantung pada bantuan eksternal.

**Independent Test**: Ikuti panduan pengguna dari nol: ubah zona waktu, tambahkan satu feed, dan matikan satu feed, tanpa membuka dokumentasi berbahasa Mandarin.

**Acceptance Scenarios**:

1. **Given** pengguna membuka file konfigurasi, **When** pengguna membaca komentar setiap bagian, **Then** penjelasan tersedia dalam Bahasa Indonesia dan nama kunci tetap dapat dikenali.
2. **Given** pengguna membuka editor konfigurasi web, **When** halaman dimuat, **Then** antarmuka tampil dalam Bahasa Indonesia dan tersedia pilihan bahasa Inggris.
3. **Given** konfigurasi bawaan, **When** pengguna melihat daftar sumber, **Then** tidak ada platform asal Tiongkok yang aktif.

---

### Edge Cases

- Feed RSS tidak dapat diakses atau mengembalikan format tidak valid: sistem mencatat kegagalan, melewati feed tersebut, dan melanjutkan feed lain.
- Judul berita mencampur Bahasa Indonesia, Inggris, dan istilah asing: pencocokan tetap berjalan pada kata kunci yang ditetapkan pengguna.
- Kata kunci berupa pola khusus: perilaku pola dipertahankan dan tidak diterjemahkan.
- Berita tidak memiliki tanggal yang dikenali: berita tetap disimpan, tetapi ditandai agar tidak salah urut.
- Tidak ada berita yang cocok: laporan tetap dihasilkan dengan pesan kosong berbahasa Indonesia.
- Zona waktu pengguna bukan WIB: seluruh tampilan waktu mengikuti zona waktu yang dipilih.
- AI dimatikan atau kredensial tidak tersedia: seluruh alur tetap berjalan tanpa pesan kegagalan.
- Judul berisi karakter non-ASCII: pencocokan tidak gagal dan tampilan tetap benar.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Seluruh permukaan pengguna WAJIB berbahasa Indonesia: laporan, notifikasi, keluaran perintah yang dapat ditindaklanjuti, editor konfigurasi, panduan pengguna, dan komentar konfigurasi.
- **FR-002**: Log runtime dan traceback WAJIB tetap berbahasa Inggris.
- **FR-003**: Sistem DILARANG menampilkan aksara CJK pada keluaran pengguna.
- **FR-004**: Sistem WAJIB menampilkan tanggal dalam format Indonesia, misalnya `17 November 2026`.
- **FR-005**: Sistem WAJIB menampilkan angka dengan pemisah ribuan titik dan desimal koma, misalnya `1.234,5`.
- **FR-006**: Zona waktu bawaan WAJIB `Asia/Jakarta` dan dapat diubah ke zona waktu Indonesia lainnya melalui konfigurasi.
- **FR-007**: Pencocokan kata kunci WAJIB menghormati batas kata sehingga kata kunci pendek tidak cocok pada potongan kata yang tidak relevan.
- **FR-008**: Pencocokan WAJIB mengenali varian berimbuhan dari kata kunci Bahasa Indonesia.
- **FR-009**: Akurasi pencocokan WAJIB menghasilkan maksimal 1 kesalahan cocok dari 50 judul uji.
- **FR-010**: Sumber berita Indonesia WAJIB tersedia sebagai jalur utama melalui feed RSS, dengan minimal 10 feed terverifikasi aktif.
- **FR-011**: Platform bawaan asal Tiongkok WAJIB dihapus dari daftar sumber aktif; contohnya boleh dipertahankan di komentar.
- **FR-012**: Nama portal WAJIB dipertahankan sesuai merek aslinya.
- **FR-013**: Judul berita dari sumber asing WAJIB ditampilkan apa adanya, tanpa terjemahan otomatis.
- **FR-014**: Notifikasi Telegram WAJIB memuat judul, sumber, waktu dalam zona waktu pengguna, dan tautan berita.
- **FR-015**: Perintah WAJIB menyediakan opsi tersembunyi untuk mengembalikan antarmuka ke Bahasa Inggris tanpa mengubah bahasa log.
- **FR-016**: Konfigurasi WAJIB menyediakan locale antarmuka terpisah dari bahasa keluaran AI.
- **FR-017**: Retensi data lokal bawaan WAJIB 90 hari untuk basis data; laporan HTML tidak dihapus otomatis pada fase ini.
- **FR-018**: Seluruh alur inti WAJIB berjalan tanpa AI, tanpa kredensial, dan tanpa koneksi ke penyedia model.
- **FR-019**: Editor konfigurasi web WAJIB menyediakan Bahasa Indonesia sebagai bahasa bawaan dan Bahasa Inggris sebagai pilihan.
- **FR-020**: Pesan error dari pustaka pihak ketiga WAJIB dipertahankan apa adanya, dengan penjelasan Bahasa Indonesia sebagai kalimat terpisah.

### Out of Scope

- Terjemahan otomatis isi berita.
- Integrasi WhatsApp.
- Sumber tren atau hotlist Indonesia di luar RSS.
- Lokalisasi server MCP.
- Pemecahan struktur template laporan.
- Pembersihan otomatis file laporan HTML lama.

### Key Entities

- **Artikel**: Berita yang diambil dari feed, memiliki judul, sumber, waktu terbit, dan tautan.
- **Feed**: Sumber berita dengan nama, alamat, status aktif, dan batas usia artikel.
- **Kata Kunci**: Istilah atau pola yang menentukan berita relevan bagi pengguna.
- **Laporan**: Kumpulan artikel relevan yang disajikan untuk dibaca.
- **Notifikasi**: Ringkasan laporan yang dikirim ke kanal pesan.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Pengguna dapat membaca seluruh laporan tanpa menemukan satu pun aksara CJK pada 5 laporan berturut-turut.
- **SC-002**: Dari 50 judul berita Indonesia yang diuji, maksimal 1 judul salah cocok.
- **SC-003**: 100% label laporan, notifikasi, dan pesan perintah utama tersedia dalam Bahasa Indonesia.
- **SC-004**: Pemeriksaan mandiri selesai dalam waktu kurang dari 10 detik pada mesin pengguna tanpa AI dan tanpa status gagal.
- **SC-005**: Minimal 10 feed berita Indonesia terverifikasi dan masing-masing menghasilkan sedikitnya 1 artikel pada pengujian.
- **SC-006**: Pengguna dapat menyelesaikan alur "ubah zona waktu, tambah feed, matikan feed" dalam waktu kurang dari 10 menit dengan hanya membaca panduan Bahasa Indonesia.
- **SC-007**: Seluruh tes yang sudah ada tetap lulus setelah perubahan.

## Assumptions

- Pengguna menjalankan aplikasi secara lokal di Windows dan tidak memakai server.
- Kanal notifikasi utama adalah Telegram; kanal lain dipertahankan tetapi bukan bawaan.
- AI tetap mati secara default dan tidak menjadi syarat kelayakan fitur.
- Retensi 90 hari hanya berlaku untuk basis data, bukan berkas laporan HTML.
- Feed RSS menyediakan tanggal terbit dalam format standar; feed yang tidak menyediakannya ditandai, bukan digagalkan.
- Tidak ada perubahan skema basis data pada fase ini.
- Nama paket dan perintah teknis tetap dipertahankan; hanya identitas tampilan yang berubah.
