# Fungsi ord()
text = "N"
codePoint = ord(text)
print(f'code point of {text} in decimal: {codePoint}')
# output ➜ code point of N in decimal: 78

text = "⯑"
codePoint = ord(text)
print(f'code point of {text} in decimal: {codePoint}')
# output ➜ code point of ⯑ in decimal: 50504

# Fungsi chr()
codePoint = chr(50504)
print(codePoint)
# output ➜ ⯑

codePoint = chr(0xC548)
print(codePoint)
# output ➜ ⯑