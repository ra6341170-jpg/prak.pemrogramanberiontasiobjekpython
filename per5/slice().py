data_list = [2, 4, 6, 7, 9, 11, 13]
print(data_list)
# output ➜ [2, 4, 6, 7, 9, 11, 13]

# Slicing dengan notasi standar
list1 = data_list[2:6:1]
print(list1)
# output ➜ [6, 7, 9, 11]

# Slicing dengan pemanggilan fungsi slice() langsung di dalam index
list2 = data_list[slice(2, 6, 1)]
print(list2)
# output ➜ [6, 7, 9, 11]

# Menyimpan nilai fungsi slice() ke dalam variabel terlebih dahulu
sl = slice(2, 6)
list3 = data_list[sl]
print(list3)
# output ➜ [6, 7, 9, 11]