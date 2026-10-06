def aggregate(message, numbers, f):
    res = f(numbers)
    print(f"{message} is {res}")

def sum_func(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def avg_func(numbers):
    if len(numbers) == 0:
        return 0
    return sum_func(numbers) / len(numbers)

numbers_data = [3, 4, 1, 2, 3, 4]

# Pemanggilan ke-1: Menggunakan fungsi sum_func sebagai argumen
aggregate("total", numbers_data, sum_func)
# output ➜ total is 17

# Pemanggilan ke-2: Menggunakan fungsi avg_func sebagai argumen
aggregate("average", numbers_data, avg_func)
# output ➜ average is 2.8333333333333335

# Pemanggilan ke-3: Menggunakan fungsi bawaan max sebagai argumen
aggregate("max", numbers_data, max)
# output ➜ max is 4

# Pemanggilan ke-4: Menggunakan fungsi bawaan min sebagai argumen
aggregate("min", numbers_data, min)
# output ➜ min is 1