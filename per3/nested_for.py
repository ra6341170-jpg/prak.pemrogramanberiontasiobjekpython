max_bintang = int(input("Jumlah bintang: "))

for i in range(max_bintang):
    for j in range(0, max_bintang - i):
        print("*", end=" ")
    print()