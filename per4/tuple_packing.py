first_name = "aerith gainsborough"
rank = 11
win = False

row_data = (first_name, rank, win)

print(row_data)
# output -> ('aerith gainsborough', 11, False)

# dengan ()
row_data = (first_name, rank, win)

# tanpa ()
row_data = first_name, rank, win

# fungsi print() dengan satu argument berisi tuple (first_name, rank, win)
print((first_name, rank, win))

# fungsi print() dengan isi 3 argument: first_name, rank, win
print(first_name, rank, win)