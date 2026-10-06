# Statement 1: Positional argument biasa
obj5 = create_sorcerer("Sukuna", 1000, "incarnation", "heian")
print(obj5)
# output ➜ {'name': 'Sukuna', 'age': 1000, 'race': 'incarnation', 'era': 'heian'}

# Statement 2: Menggunakan keyword argument
obj6 = create_sorcerer(name="Kenjaku", age=1000, race="human", era="1000+ year ago")
print(obj6)
# (output dari obj6 tidak tertulis di halaman dokumen)

# Statement 3: Keyword argument dengan urutan parameter yang diacak
obj8 = create_sorcerer(era="1000+ year ago", age=1000, name="Kenjaku", race="human")
print(obj8)
# output ➜ {'name': 'Kenjaku', 'age': 1000, 'race': 'human', 'era': '1000+ year ago'}

# Statement 4: Kombinasi positional dan keyword argument
obj9 = create_sorcerer("Hajime Kashimo", 400, era="400 year ago", race="human")
print(obj9)
# output ➜ {'name': 'Hajime Kashimo', 'age': 400, 'race': 'human', 'era': '400 year ago'}