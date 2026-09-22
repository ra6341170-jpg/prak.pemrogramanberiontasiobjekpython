while True:
    n = int(input("Enter a number divisible by 3: "))
    
    if n % 3 != 0:
        break
        
    print("%d is divisible by 3" % (n))