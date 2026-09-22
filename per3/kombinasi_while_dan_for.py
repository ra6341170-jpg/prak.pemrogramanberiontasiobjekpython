n = int(input("Enter max data: "))

for i in range(n):
    j = 0
    while j < n - i:
        print("*", end=" ")
        j += 1
    print()