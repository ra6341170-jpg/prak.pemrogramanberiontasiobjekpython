# Menggunakan teknik penulisan string literal sebaris
text = "hello " "python"
print(text)
# output ➜ hello python

# Menggunakan operator +
text_one = "hello"
text_two = "python"
text = text_one + " " + text_two
print(text)
# output ➜ hello python

# Penggabungan dengan data non-string (menggunakan fungsi str())
text = "hello"
number = 123
yes = True
message = text + " " + str(number) + " " + str(yes)
print(message)

# Menggunakan method join()
text = " ".join(["hello", "python"])
print(text)
# output ➜ hello python