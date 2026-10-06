data_str = "hello world"
print(data_str)
# output ➜ hello world

# Slicing element index ke-0 hingga ke-2 (end=3)
slice1 = data_str[0:3]
print(slice1)
# output ➜ hel

# Slicing element index ke-2 hingga ke-7 (start=2, end=8)
slice2 = data_str[2:8]
print(slice2)
# output ➜ llo wo

# Slicing element hingga index ke-4 (tanpa start, default 0)
slice3 = data_str[:5]
print(slice3)
# output ➜ hell

# Slicing element dimulai index ke-3 hingga ke-6 dengan pengembalian setiap 1 element
slice5 = data_str[3:7:1]
print(slice5)
# output ➜ lo

# Slicing element dimulai index ke-2 hingga ke-8 dengan pengembalian setiap 2 element
slice6 = data_str[2:9:2]
print(slice6)
# output ➜ low

# Slicing seluruh element (ekuivalen dengan data_str[0:len(data_str)])
slice7 = data_str[:]
print(slice7)
# output ➜ hello world

# Slicing seluruh element dengan pengembalian setiap 2 element
slice8 = data_str[::2]
print(slice8)
# output ➜ hlowr