def print_all(message, *numbers, **others):
    print(f"message: {message}")
    print(f"numbers: {numbers}")
    print(f"others: {others}")

# Menyimpan fungsi print_all ke dalam variabel display
display = print_all

# Menjalankan fungsi melalui variabel display
display(
    "hello world", 
    1, 
    2, 
    3, 
    4, 
    name="nokia 3310", 
    discontinued=True, 
    year_released=2000
)

# output ↓
# message: hello world
# numbers: (1, 2, 3, 4)
# others: {'name': 'nokia 3310', 'discontinued': True, 'year_released': 2000}