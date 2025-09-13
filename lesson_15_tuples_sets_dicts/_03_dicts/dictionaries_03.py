# animals_dict = {'cat': 'кот', 'dog': 'собака'}
# # print(animals_dict['bird'])
#
# word = 'bird'
# if word in animals_dict:
#     print(animals_dict[word])
# else:
#     print("Не знаю таких слов!")
#
#
# word = 'bird'
# try:
#     print(animals_dict[word])
# except KeyError:
#     print(f'Значения {word} нет в словаре.')
# finally:
#     print('Программа завершила свою работу.')


animals_dict = {'cat': 'кот', 'dog': 'собака'}
get_animal = animals_dict.get('cat')
print(get_animal)
get_animal_1 = animals_dict.get('bird')
print(get_animal_1)
get_animal_2 = animals_dict.get('bird', 'нет такого слова')
print(get_animal_2)
print(animals_dict)
print()

animal_default_1 = animals_dict.setdefault('dog')
print(animal_default_1)
print(animals_dict)


animal_default_2 = animals_dict.setdefault('bird')
print(animal_default_2)
print(animals_dict)

animal_default_3 = animals_dict.setdefault('snake', 'змея')
print(animal_default_3)
print(animals_dict)
