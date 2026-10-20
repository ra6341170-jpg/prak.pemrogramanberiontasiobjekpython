# 🪪 Program Manajemen Data KTP (Python + SQLite)

Program berbasis *Command Line Interface* (CLI) sederhana yang dibangun menggunakan Python dan SQLite. Program ini mensimulasikan pencatatan dan pengelolaan data Kartu Tanda Penduduk (KTP) dengan format detail yang menyerupai KTP asli di Indonesia. 

Proyek ini dibuat untuk memenuhi tugas/kuis mata kuliah pemrograman.

## ✨ Fitur Utama
- **Create (Tambah Data):** Menambahkan data KTP baru dengan sistem validasi ketat:
  - Validasi NIK wajib 16 digit angka.
  - Validasi format Tanggal Lahir (`dd-mm-yyyy`).
  - Auto-konversi input Jenis Kelamin (L/P menjadi LAKI-LAKI/PEREMPUAN).
  - Format alamat lengkap (RT/RW, Kel/Desa, Kecamatan).
- **Read (Tampilkan & Cari):** Menampilkan daftar singkat KTP dan mencari KTP berdasarkan NIK dengan *layout* cetak menyerupai KTP fisik.
- **Update (Ubah Data):** Memperbarui data KTP tertentu (Nama, Alamat, Kelurahan, dll) tanpa harus mengisi ulang seluruh data.
- **Delete (Hapus Data):** Menghapus data KTP dari database berdasarkan NIK.
- **Database Permanen:** Menggunakan `sqlite3` bawaan Python sehingga data tetap tersimpan meski program ditutup.