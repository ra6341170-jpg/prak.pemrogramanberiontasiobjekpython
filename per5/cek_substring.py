# Menggunakan method startswith()
print("hello world".startswith("hell")) 
# output ➜ True

# Menggunakan method endswith()
print("hello world".endswith("orld")) 
# output ➜ True
print("hello world".endswith("worl")) 
# output ➜ False

# Menggunakan method count() untuk mengecek keberadaan
print("hello world".count("ello")) 
# output ➜ 1

# Mengkombinasikan dengan operasi logika
print("hello world".count("ello") > 0)
# output ➜ True