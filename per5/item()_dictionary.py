profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
}

# Menggunakan method items() untuk mendapatkan pasangan key-value
print(list(profile.items())) 
# output ➜ [('id', 2), ('name', 'mario'), ('hobbies', ('playing with luigi', 'saving the mushroom kingdom')), ('is_female', False)]