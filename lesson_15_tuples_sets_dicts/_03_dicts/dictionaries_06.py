# animals_dict = {'cat': 'Кошка', 'dog': 'Собака', 'bird': 'Птица'}
# animals_dict_keys = animals_dict.keys()
# animals_dict_values = animals_dict.values()
# animals_dict_items = animals_dict.items()
#
# print(animals_dict)
# print(type(animals_dict_keys), animals_dict_keys)
# print(type(animals_dict_values), animals_dict_values)
# print(type(animals_dict_items), animals_dict_items)
#
# keys_list = list(animals_dict_keys)
# values_list = list(animals_dict_values)
# items_list = list(animals_dict_items)
# print(keys_list, values_list, items_list, sep='\n')
#
# keys_list = [key for key in animals_dict]
# values_list = [animals_dict[key] for key in animals_dict]
# print(keys_list)
# print(values_list)

animals_dict = {'cat': 'Кошка', 'dog': 'Собака', 'bird': 'Птица'}
for animal in animals_dict:
    print(f"Это ключ - {animal}")
print()

for animal in animals_dict.keys():
    print(f"Это ключ - {animal}")
print()

for animal in animals_dict.values():
    print(f"Это значение - {animal}")
print()


dict_keys = []
dict_values = []

for key, value in animals_dict.items():
    print(f"Это ключ - {key}")
    print(f"Это значение - {value}")
    dict_keys.append(key)
    dict_values.append(value)

print(dict_keys)
print(dict_values)
