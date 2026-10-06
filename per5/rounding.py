pi = 3.141592653589

# Menggunakan fungsi round()
n1 = round(pi, 2)
print(f"n1: {n1}")
# output ➜ n1: 3.14

n2 = round(pi, 5)
print(f"n2: {n2}")
# output ➜ n2: 3.14159

# Pembulatan ke-bawah menggunakan math.floor()
import math
n3 = math.floor(pi)
print(f"n3: {n3}")
# output ➜ n3: 3

# Pembulatan ke-atas menggunakan math.ceil()
n4 = math.ceil(pi)
print(f"n4: {n4}")
# output ➜ n4: 4