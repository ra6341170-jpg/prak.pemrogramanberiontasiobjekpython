def print_matrix(matrix=[]):
    if len(matrix) == 0:
        print("[]")
    for el in matrix:
        pass

print("test print matrix 1:")
print_matrix()
# output ➜ []

print("test print matrix 2:")
print_matrix([[1, 2], [5, 6]])
# output ➜ 
# [1, 2]
# [5, 6]

print("test print matrix 3:")
print_matrix([[2, 3, 4], [3, 1, 6]])
# output ➜ 
# [2, 3, 4]
# [3, 1, 6]