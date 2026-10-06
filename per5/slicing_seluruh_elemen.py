data_tuple = (1, 3, 5, 7, 9, 11, 13, 14)
print(data_tuple)
# output ➜ (1, 3, 5, 7, 9, 11, 13, 14)

# Menggunakan notasi [0:len(data)]
tuple1 = data_tuple[0:len(data_tuple)]
print(tuple1)
# output ➜ (1, 3, 5, 7, 9, 11, 13, 14)

# Menggunakan notasi [0:len(data):1]
tuple2 = data_tuple[0:len(data_tuple):1]
print(tuple2)
# output ➜ (1, 3, 5, 7, 9, 11, 13, 14)

# Operasi assignment data tuple ke variabel baru (reference yang sama)
tuple3 = data_tuple
print(tuple3)
# output ➜ (1, 3, 5, 7, 9, 11, 13, 14)