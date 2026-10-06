# Konversi string ke set
data_str = set('abcda')
print('data_str: ', data_str)
# output ➜ data_str: {'c', 'b', 'a', 'd'}

# Konversi list ke set
data_list = set(['a', 'b', 'c', 'd', 'a'])
print('data_list: ', data_list)
# output ➜ data_list: {'c', 'b', 'a', 'd'}

# Konversi tuple ke set
data_tuple = set(('a', 'b', 'c', 'd', 'a'))
print('data_tuple: ', data_tuple)
# output ➜ data_tuple: {'c', 'b', 'a', 'd'}

# Konversi range ke set
data_range = set(range(1, 5))
print('data_range: ', data_range)
# output ➜ data_range: {1, 2, 3, 4}