a = set('abracadabra') # {'c', 'a', 'r', 'd', 'b'}
b = set('alacazam')    # {'c', 'z', 'a', 'm', 'l'}

# Operasi or (|)
res_or = a | b
print("res_or (a | b):", res_or)
# output ➜ {'c', 'z', 'a', 'r', 'd', 'b', 'm', 'l'}

# Operasi and (&)
res_and = a & b
print("res_and (a & b):", res_and)
# output ➜ {'c', 'a'}

# Operasi exclusive or (^)
res_xor = a ^ b
print("res_xor (a ^ b):", res_xor)
# output ➜ {'z', 'r', 'b', 'd', 'm', 'l'}