profile = { 
    "id": 2, 
    "name": "mario", 
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"), 
    "is_female": False, 
    "affiliations": [ 
        { 
            "name": "luigi", 
            "affiliation": "brother" 
        }, 
        { 
            "name": "mushroom kingdom", 
            "affiliation": "protector" 
        }, 
    ] 
}

print("name:", profile["name"]) 
print("hobbies:", profile["hobbies"]) 
print("affiliations:")

for item in profile["affiliations"]: 
    print(" ➜ %s (%s)" % (item["name"], item["affiliation"]))

# output ↓ 
# 
# name: mario 
# hobbies: ('playing with luigi', 'saving the mushroom kingdom') 
# affiliations: 
# 
# ➜ luigi (brother)
# 
# ➜ mushroom kingdom (protector)

# --- Mengakses value nested item dictionary ---
value1 = profile["affiliations"][0]["name"], profile["affiliations"][0]["affiliation"] 
print(" ➜ %s (%s)" % (value1)) 
# output ➜ luigi (brother)

value2 = profile["affiliations"][1]["name"], profile["affiliations"][1]["affiliation"] 
print(" ➜ %s (%s)" % (value2)) 
# output ➜ mushroom kingdom (protector)