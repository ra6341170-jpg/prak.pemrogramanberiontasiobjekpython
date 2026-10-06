# Tipe data nilai balik fungsi (return type) menggunakan Type Hinting

def calculate_circle_area(r: int) -> float:
    area = 3.14 * (r ** 2)
    return area

def calculate_circle_circumference(r: int) -> float:
    return 2 * 3.14 * r

area = calculate_circle_area(788)
print(f"area: {area:.2f}")
# output ➜ area: 1949764.16

circumference = calculate_circle_circumference(788)
print(f"circumference: {circumference:.2f}")
# output ➜ circumference: 4948.64

# Peringatan (warning) jika nilai balik tidak sesuai dengan type hinting
def get_pi() -> int:
    return 3.14

# Fungsi dengan return type None diikuti statement return:
def say_hello() -> None:
    print("hello world")
    return None

# Fungsi dengan return type None tanpa diikuti statement return:
def say_hello() -> None:
    print("hello world")

# Fungsi dengan tanpa return type maupun return statement:
def say_hello():
    print("hello world")