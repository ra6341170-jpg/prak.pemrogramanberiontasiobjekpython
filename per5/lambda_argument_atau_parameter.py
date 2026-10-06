# Fungsi biasa dengan parameter
def get_full_name1(first_name, last_name):
    return f"{first_name} {last_name}"

res = get_full_name1("Darion", "Mograine")
print(res)
# output ➜ Darion Mograine

# Lambda dengan parameter
get_full_name2 = lambda first_name, last_name: f"{first_name} {last_name}"

res = get_full_name2("Sally", "Whitemane")
print(res) 
# output ➜ Sally Whitemane

# Lambda dengan optional argument
get_full_name3 = lambda first_name, last_name = "": f"{first_name} {last_name}".strip()