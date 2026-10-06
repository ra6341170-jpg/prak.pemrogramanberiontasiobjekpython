def say_hello():
    print("hello")

# Memanggil fungsi berkali-kali
say_hello()
say_hello()
say_hello()
# output ➜
# hello
# hello
# hello

# Fungsi dengan banyak statement
def print_something():
    print("hello")
    today = "Thursday"
    print(f"happy {today}")
    for i in range(5):
        print(f"i: {i}")

print_something()
# output ➜ 
# hello
# happy Thursday
# i: 0
# i: 1
# i: 2
# i: 3
# i: 4