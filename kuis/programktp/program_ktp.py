import sqlite3
import os
from datetime import datetime

class ProgramKTP:
    def __init__(self):
        self.db_name = 'data_ktp.db'
        self.buat_tabel()

    def koneksi(self):
        return sqlite3.connect(self.db_name)

    def buat_tabel(self):
        with self.koneksi() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ktp (
                    nik TEXT PRIMARY KEY,
                    nama TEXT,
                    tempat_tgl_lahir TEXT,
                    jenis_kelamin TEXT,
                    gol_darah TEXT,
                    alamat TEXT,
                    rt_rw TEXT,
                    kel_desa TEXT,
                    kecamatan TEXT,
                    agama TEXT,
                    status TEXT,
                    pekerjaan TEXT,
                    kewarganegaraan TEXT
                )
            ''')
            conn.commit()

    def bersihkan_layar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def tambah_data(self):
        print("\n--- TAMBAH DATA KTP ---")
        
        while True:
            nik = input("NIK (16 Digit Angka): ").strip()
            if len(nik) == 16 and nik.isdigit():
                break
            print("-> Error: NIK harus persis 16 digit dan hanya berupa angka!\n")
        
        with self.koneksi() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ktp WHERE nik=?", (nik,))
            if cursor.fetchone():
                print(f"-> Error: NIK {nik} sudah terdaftar di database!")
                return

        nama = input("Nama Lengkap: ")
        tempat_lahir = input("Tempat Lahir: ")
        
        while True:
            tgl_lahir = input("Tanggal Lahir (format dd-mm-yyyy): ").strip()
            try:
                datetime.strptime(tgl_lahir, "%d-%m-%Y")
                break
            except ValueError:
                print("-> Format salah! Harap gunakan format dd-mm-yyyy.\n")
        
        ttl = f"{tempat_lahir}, {tgl_lahir}"
        
        while True:
            jk_input = input("Jenis Kelamin (L/P): ").strip().upper()
            if jk_input == 'L':
                jk = "LAKI-LAKI"
                break
            elif jk_input == 'P':
                jk = "PEREMPUAN"
                break
            else:
                print("-> Harap ketik 'L' atau 'P'.\n")

        gol_darah = input("Golongan Darah (A/B/AB/O/-): ").strip().upper()
        if not gol_darah:
            gol_darah = "-"

        alamat = input("Alamat: ")
        rt_rw = input("  RT/RW (cth: 001/002): ")
        kel_desa = input("  Kel/Desa: ")
        kecamatan = input("  Kecamatan: ")
        
        agama = input("Agama: ")
        status = input("Status Perkawinan: ")
        pekerjaan = input("Pekerjaan: ")
        warga = input("Kewarganegaraan (WNI/WNA): ")

        with self.koneksi() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO ktp VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nik, nama, ttl, jk, gol_darah, alamat, rt_rw, kel_desa, kecamatan, agama, status, pekerjaan, warga))
            conn.commit()
        print("\nData KTP berhasil ditambahkan!")

    def tampilkan_data(self):
        print("\n--- DAFTAR KTP ---")
        with self.koneksi() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nik, nama, alamat, kel_desa FROM ktp")
            data = cursor.fetchall()
            
            if not data:
                print("Belum ada data KTP di dalam database.")
                return

            print(f"{'NIK':<20} | {'NAMA':<25} | {'ALAMAT & DESA'}")
            print("-" * 75)
            for baris in data:
                alamat_lengkap = f"{baris[2]}, {baris[3]}"
                print(f"{baris[0]:<20} | {baris[1]:<25} | {alamat_lengkap}")

    def cari_data(self):
        print("\n--- CARI DATA KTP ---")
        nik = input("Masukkan NIK yang dicari: ")
        
        with self.koneksi() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ktp WHERE nik=?", (nik,))
            data = cursor.fetchone()
            
            if data:
                print("\n================ PROVINSI ===================")
                print("================ KABUPATEN/KOTA =============\n")
                print(f"NIK              : {data[0]}")
                print(f"Nama             : {data[1]}")
                print(f"Tempat/Tgl Lahir : {data[2]}")
                print(f"Jenis Kelamin    : {data[3]:<15} Gol. Darah : {data[4]}")
                print(f"Alamat           : {data[5]}")
                print(f"      RT/RW      : {data[6]}")
                print(f"      Kel/Desa   : {data[7]}")
                print(f"      Kecamatan  : {data[8]}")
                print(f"Agama            : {data[9]}")
                print(f"Status Perkawinan: {data[10]}")
                print(f"Pekerjaan        : {data[11]}")
                print(f"Kewarganegaraan  : {data[12]}")
                print(f"Berlaku Hingga   : SEUMUR HIDUP")
                print("\n=============================================")
            else:
                print("Data KTP tidak ditemukan!")

    def ubah_data(self):
        print("\n--- UBAH DATA KTP ---")
        nik = input("Masukkan NIK yang ingin diubah: ")
        
        with self.koneksi() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ktp WHERE nik=?", (nik,))
            if not cursor.fetchone():
                print("Data KTP tidak ditemukan!")
                return

            print("\nMasukkan data baru (tekan Enter untuk melewati jika tidak ingin diubah):")
            nama = input("Nama Lengkap baru: ")
            alamat = input("Alamat baru: ")
            rt_rw = input("RT/RW baru: ")
            kel_desa = input("Kel/Desa baru: ")
            kecamatan = input("Kecamatan baru: ")

            updates = []
            values = []

            if nama: updates.append("nama=?"); values.append(nama)
            if alamat: updates.append("alamat=?"); values.append(alamat)
            if rt_rw: updates.append("rt_rw=?"); values.append(rt_rw)
            if kel_desa: updates.append("kel_desa=?"); values.append(kel_desa)
            if kecamatan: updates.append("kecamatan=?"); values.append(kecamatan)

            if updates:
                values.append(nik)
                query = f"UPDATE ktp SET {', '.join(updates)} WHERE nik=?"
                cursor.execute(query, tuple(values))
                conn.commit()
                print("\nData KTP berhasil diperbarui!")
            else:
                print("\nTidak ada data yang diubah.")

    def hapus_data(self):
        print("\n--- HAPUS DATA KTP ---")
        nik = input("Masukkan NIK yang ingin dihapus: ")
        
        with self.koneksi() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ktp WHERE nik=?", (nik,))
            if not cursor.fetchone():
                print("Data KTP tidak ditemukan!")
                return
            
            yakin = input(f"Yakin ingin menghapus KTP dengan NIK {nik}? (y/n): ")
            if yakin.lower() == 'y':
                cursor.execute("DELETE FROM ktp WHERE nik=?", (nik,))
                conn.commit()
                print("Data KTP berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")

    def jalankan(self):
        while True:
            print("\n" + "="*30)
            print("  SISTEM INFORMASI DATA KTP")
            print("="*30)
            print("1. Tambah Data KTP")
            print("2. Tampilkan Semua KTP")
            print("3. Cari Data KTP (Detail Lengkap)")
            print("4. Ubah Data KTP")
            print("5. Hapus Data KTP")
            print("0. Keluar")
            
            pilihan = input("\nPilih menu (0-5): ")
            
            self.bersihkan_layar()
            
            if pilihan == '1':
                self.tambah_data()
            elif pilihan == '2':
                self.tampilkan_data()
            elif pilihan == '3':
                self.cari_data()
            elif pilihan == '4':
                self.ubah_data()
            elif pilihan == '5':
                self.hapus_data()
            elif pilihan == '0':
                print("Terima kasih telah menggunakan program ini!")
                break
            else:
                print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    app = ProgramKTP()
    app.jalankan()