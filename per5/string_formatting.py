name = "Aiden Pearce"
occupation = "IT support"

# Menggunakan f-strings (formatted string literals)
text = f"hello, my name is {name}, I'm an {occupation}"
print(text)
# output ➜ hello, my name is Aiden Pearce, I'm an IT support

# Menggunakan method .format() dengan keyword argument
text = "hello, my name is {name}, I'm an {occupation}".format(name=name, occupation=occupation)
print(text)
# output ➜ hello, my name is Aiden Pearce, I'm an IT support

# Menggunakan method .format() dengan index numerik
text = "hello, my name is {0}, I'm an {1}".format(name, occupation)
print(text)
# output ➜ hello, my name is Aiden Pearce, I'm an IT support

# Menggunakan method .format() dengan urutan parameter kosong {}
text = "hello, my name is {}, I'm an {}".format(name, occupation)
print(text)
# output ➜ hello, my name is Aiden Pearce, I'm an IT support