def calculate_circle_area(r):
    area = 3.14 * (r ** 2)
    print("area of circle:", area)

calculate_circle_area(788)
# output ➜ area of circle: 1949764.1600000001

# Parameter fungsi dengan penentuan tipe data (Type Hinting)
def calculate_circle_area(message: str, r: int):
    area = 3.14 * (r ** 2)
    print(message, area)