import math

# --- BAGIAN 1: Kumpulan Fungsi Rumus Aritmatika ---

def luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang (p x l)."""
    return panjang * lebar

def luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran (pi x r^2)."""
    return math.pi * (jari_jari ** 2)

def luas_persegi(sisi):
    """Menghitung luas persegi (sisi x sisi)."""
    return sisi ** 2

def pythagoras(alas, tinggi):
    """Mencari panjang sisi miring segitiga siku-siku (c = akar(a^2 + b^2))."""
    return math.sqrt((alas ** 2) + (tinggi ** 2))


# --- BAGIAN 2: Implementasi Keyword 'for' dan 'range' ---

print("=== Program Penghitung Rumus Bangun Datar & Pythagoras ===")

# Menentukan berapa kali program/menu akan diulang menggunakan range()
jumlah_perulangan = 3 

# Loop for akan mengulang blok kode di bawahnya sebanyak 'jumlah_perulangan'
for iterasi in range(jumlah_perulangan):
    print(f"\n--- Perhitungan ke-{iterasi + 1} dari {jumlah_perulangan} ---")
    print("Pilih rumus yang ingin dihitung:")
    print("1. Luas Persegi Panjang")
    print("2. Luas Lingkaran")
    print("3. Luas Persegi")
    print("4. Pythagoras")
    
    # Meminta input pengguna
    pilihan = input("Masukkan angka pilihan (1-4): ")
    
    # Pengkondisian berdasarkan pilihan pengguna
    if pilihan == '1':
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        hasil = luas_persegi_panjang(p, l)
        print(f"Hasil Luas Persegi Panjang: {hasil}")
        
    elif pilihan == '2':
        r = float(input("Masukkan jari-jari: "))
        hasil = luas_lingkaran(r)
        # Menampilkan hasil dengan 2 angka di belakang koma
        print(f"Hasil Luas Lingkaran: {hasil:.2f}") 
        
    elif pilihan == '3':
        s = float(input("Masukkan panjang sisi: "))
        hasil = luas_persegi(s)
        print(f"Hasil Luas Persegi: {hasil}")
        
    elif pilihan == '4':
        a = float(input("Masukkan sisi alas: "))
        t = float(input("Masukkan sisi tinggi (tegak): "))
        hasil = pythagoras(a, t)
        print(f"Hasil Sisi Miring (Pythagoras): {hasil:.2f}")
        
    else:
        print("Pilihan tidak valid, silakan masukkan angka 1-4.")

print("\nSelesai! Semua jatah perhitungan dalam loop telah digunakan.")