import json

profile = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False,
}

print(json.dumps(profile, indent=4))