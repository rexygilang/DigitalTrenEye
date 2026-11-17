# Quickstart: Validasi Lokalisasi Indonesia

**Feature**: `001-lokalisasi-id` | **Date**: 2026-11-17

Panduan ini membuktikan fitur bekerja dari ujung ke ujung. Tidak berisi kode
implementasi.

## Prasyarat

- Windows dengan PowerShell.
- `uv` terpasang.
- Dependensi proyek tersedia: `uv sync`.
- Tidak perlu API key AI.

## Validasi dasar

```powershell
uv run python -m pytest -q
uv run python -m trendradar --doctor
```

Hasil yang diharapkan:

- Seluruh tes lulus, termasuk baseline 29 tes + 35 subtes.
- `--doctor` menampilkan pesan Indonesia dan tidak ada status `GAGAL`.
- Tidak ada aksara CJK pada keluaran.

## Skenario 1 — Laporan berbahasa Indonesia

```powershell
uv run python -m trendradar
Start-Process output\index.html
```

Periksa:

- Seluruh label berbahasa Indonesia.
- Tanggal berbentuk `17 November 2026`.
- Angka berbentuk `1.234`.
- Tidak ada aksara CJK.
- Judul berita asing tampil apa adanya.

Pemeriksaan otomatis:

```powershell
uv run python tools/check_cjk.py output\
```

Hasil yang diharapkan: `0 temuan`.

## Skenario 2 — Pencocokan kata Indonesia

```powershell
uv run python -m pytest tests/test_frequency_id.py -q
```

Periksa:

- Kata kunci `demo` tidak cocok pada "Demokrasi Indonesia hari ini".
- Kata kunci `aksi` tidak cocok pada "Transaksi saham naik".
- Kata kunci `pemilu` cocok pada "Pemilu 2029 dipersiapkan".
- Kata kunci `berita` cocok pada "Pemberitaan media berubah".
- Frasa `pemilu 2029` tidak cocok pada "Pemilu baru 2029 digelar".
- Total salah cocok maksimal 1 dari 50 judul.

## Skenario 3 — CLI dan log

```powershell
uv run python -m trendradar --help
uv run python -m trendradar --doctor
uv run python -m trendradar --show-schedule
```

Periksa:

- Seluruh deskripsi berbahasa Indonesia.
- `--lang` tidak muncul di `--help`.
- Log yang muncul selama crawl berbahasa Inggris.
- `--lang en` mengubah antarmuka ke Inggris, log tetap Inggris.

## Skenario 4 — Notifikasi Telegram

```powershell
uv run python -m trendradar --test-notification
```

Periksa:

- Pesan berbahasa Indonesia.
- Memuat judul, sumber, waktu WIB, dan tautan.
- Tidak ada aksara CJK.

## Skenario 5 — Konfigurasi dan editor

1. Buka `config/config.yaml` di editor UTF-8.
2. Pastikan komentar berbahasa Indonesia dan `app.locale: "id"`.
3. Pastikan `storage.local.retention_days: 90`.
4. Pastikan tidak ada platform Tiongkok aktif.
5. Buka `docs/index.html` di browser; antarmuka berbahasa Indonesia dengan opsi
   Inggris.

## Skenario 6 — Retensi

```powershell
Copy-Item output output-backup -Recurse
uv run python -m trendradar
```

Periksa log:

- Jumlah data yang dihapus dicatat.
- Data lebih tua dari 90 hari hilang dari basis data.
- Berkas HTML lama tetap ada.

## Rollback

Persiapan sebelum implementasi:

```powershell
git tag baseline-lokalisasi
git status
```

Membatalkan satu tugas:

```powershell
git log --oneline -5
git revert <commit>
uv run python -m pytest -q
```

Membatalkan seluruh fitur:

```powershell
git revert --no-commit baseline-lokalisasi..HEAD
git commit -m "revert: rollback Indonesian localization"
```

Pulihkan data:

```powershell
Remove-Item output -Recurse
Rename-Item output-backup output
```

Catatan:

- Tidak ada migrasi basis data, sehingga rollback tidak memerlukan skrip khusus.
- Satu-satunya operasi merusak adalah pembersihan retensi. Cadangkan `output/`
  sebelum menjalankannya.
- Tag `baseline-lokalisasi` wajib dibuat sebelum tugas T003.
