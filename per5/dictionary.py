profile = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False,
}

# Memunculkan data dictionary ke layar
print("data:", profile)
print("total keys:", len(profile))

# Memunculkan nilai item tertentu berdasarkan key-nya
print("name:", profile["name"])
# output ➜ name: john wick

print("hobbies:", profile["hobbies"])
# output ➜ ['playing with pencil']