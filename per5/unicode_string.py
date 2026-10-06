# Penulisan text dengan langsung menuliskan karakternya
message = "⯑⯑⯑⯑⯑ 😀"
print(message)
# output ➜ ⯑⯑⯑⯑⯑ 😀  

# Menggunakan notasi special character \uXXXX (encoding 16-bit)
message = "\uC548\uB155\uD558\uC138\uC694"
print(message)
# output ➜ ⯑⯑⯑⯑⯑ 

# Menggunakan notasi special character \UXXXXXXXX (encoding 32-bit untuk karakter lebar/emoji)
message = "\U0000C548\U0000B155\U0000D558\U0000C138\U0000C694 \U0001F600"
print(message)

# Menggunakan notasi special character \N{NAME}
message_name = "\N{HANGUL SYLLABLE AN}\N{HANGUL SYLLABLE NYEONG} \N{GRINNING FACE}"
print(message_name)
# output ➜ ⯑⯑ 😀