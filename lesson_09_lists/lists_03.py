my_list = [2 ** i for i in range(10)]
print(my_list)

my_list_simple = []
for i in range(10):
    my_list_simple.append(2 ** i)
print(my_list_simple)
print()

square_list = [i * i for i in range(10)]
print(square_list)

square_list_simple = []
for i in range(10):
    square_list_simple.append(i * i)
print(square_list_simple)
print()

list_from_str = [sym + '*' for sym in 'my_string']
print(list_from_str)

list_from_str_simple = []
for sym in 'my_string':
    list_from_str_simple.append(sym + '*')
print(list_from_str_simple)
print()

list_from_str_duplicate = [sym * 5 for sym in "my_string"]
print(list_from_str_duplicate)

list_from_str_duplicate_simple = []
for sym in "my_string":
    list_from_str_duplicate_simple.append(sym * 5)
print(list_from_str_duplicate_simple)