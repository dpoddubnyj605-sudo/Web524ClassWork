my_dict_01 = {}
print(type(my_dict_01))
my_dict_02 = dict()

personnel_dict = {'Петр': 201, 'Мария': 201}
some_dict = {'Петр': 'Имя', "Python": "Язык программирования"}
dict_keys_num = {1: "Имя", 2.5: "Язык программирования"}

keyword_dict = dict(name="Петр", python="Язык программирования")
animals_dict = dict((('cat', 'кот'), ('dog', 'собака'), ('snake', 'змея')))

print(keyword_dict)
print(animals_dict)

explanations = {True: "Ответ верный!", False: "Нет это неверно!"}

# if 3 < 2:
#     print(explanations[True])
# else:
#     print(explanations[False])

print(explanations[3 > 2])
print(explanations[3 < 2])
