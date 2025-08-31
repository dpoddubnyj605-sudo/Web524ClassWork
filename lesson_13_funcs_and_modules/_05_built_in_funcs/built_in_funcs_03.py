my_list = [x for x in range(6)]
map_obj = map(lambda x: 2 ** x, my_list)
print(map_obj)
squares_list_from_map = list(map_obj)
print(squares_list_from_map)

for x in map(lambda x: 2 ** x, my_list):
    print(x, end=' ')


def my_func(x):
    return 2 ** x


print()

for x in map(my_func, my_list):
    print(x, end=' ')
