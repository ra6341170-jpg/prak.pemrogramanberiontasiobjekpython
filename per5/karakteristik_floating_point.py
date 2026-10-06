# Sifat unik float dimana penyimpanannya tidak pasti (not fixed)
n = 3.14 + 2.8
print(f"3.14 + 2.8: {n}")
# output ➜ 3.14 + 2.8: 5.9399999999999995


# Menampilkan angka fixed dengan suffix :f
print(f"3.14 + 2.8: {n:f}")
# output ➜ 3.14 + 2.8: 5.940000


# Menampilkan fixed point sesuai jumlah digit dengan suffix :{n}f
print(f"3.14 + 2.8: {n:.2f}")
# output ➜ 3.14 + 2.8: 5.94