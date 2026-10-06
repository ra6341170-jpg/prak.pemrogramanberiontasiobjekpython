def print_data(**data):
    print(f"type: {type(data)}")
    print(f"data: {data}")

    for key in data:
        print(f"param: {key}, value: {data[key]}")

print_data(phone="nokia 3310", discontinue=False, year=2000, networks=["GSM", "TDMA"])
# output ↓
# type: <class 'dict'>
# data: {'phone': 'nokia 3310', 'discontinue': False, 'year': 2000, 'networks': ['GSM', 'TDMA']}
#
# param: phone, value: nokia 3310
# param: discontinue, value: False
# param: year, value: 2000

# Kombinasi positional argument dan kwargs
# Positional argument harus selalu ditulis sebelum parameter **kwargs
def print_data(message, number, **data):
    print(f"message : {message}")
    print(f"number : {number}")
    print()
    for key in data:
        print(f"param : {key}, value : {data[key]}")

print_data("sesuk prei", 2023, phone="nokia 3315", networks=["GSM", "TDMA"])
# output ↓
# message: sesuk prei
# number: 2023
#
# param: phone, value: nokia 3315
# param: networks, value: ['GSM', 'TDMA']

# Kombinasi positional argument, args, dan kwargs
# Ketentuan urutan: positional argument ditulis terlebih dahulu, diikuti *args, lalu **kwargs
def print_all(message, *params, **others):
    print(f"message: {message}")
    print(f"params: {params}")
    print(f"others: {others}")

print_all(
    "hello world", 
    1, 
    True, 
    ("yesn't", "nope"), 
    name="nokia 3310", 
    discontinued=True, 
    year_released=2000
)

# output ↓
# message: hello world
# params: (1, True, ("yesn't", 'nope'))
# others: {'name': 'nokia 3310', 'discontinued': True, 'year_released': 2000}

# Kombinasi positional argument, args, keyword argument, dan kwargs
# Keyword argument khusus bisa dituliskan di antara *args dan **kwargs (jika di luar itu akan menghasilkan error)
def print_all(message, *params, say_something, **others):
    print(f"message: {message}")
    print(f"params: {params}")
    print(f"say_something: {say_something}")
    print(f"others: {others}")

print_all(
    "hello world", 
    1, 
    True, 
    ("yesn't", "nope"), 
    say_something="how are you", 
    name="nokia 3310", 
    discontinued=True, 
    year_released=2000
)

# output ↓
# message: hello world
# params: (1, True, ("yesn't", 'nope'))
# say_something: how are you
# others: {'name': 'nokia 3310', 'discontinued': True, 'year_released': 2000}