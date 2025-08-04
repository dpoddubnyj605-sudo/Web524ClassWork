import re

# my_str = "Мои номера телефонов: А1 +375(29)6234567; МТС +375(33)3334455"
# my_reg = re.compile(r'А1 \+375\(29\)(\d\d\d\d\d\d\d); МТС \+375\(33\)(\d\d\d\d\d\d\d)')
#
# match = my_reg.search(my_str)
# print(match)
# print(match.group())
# print(match.group(1))
# print(match.group(2))

# my_str_by = "Мои номера телефонов: А1 +375(29)6234567; МТС +375(33)3334455"
# my_reg_by = re.compile(r'А1 \+\d{1,3}\((\d{1,3})\)(\d{7}); МТС \+\d{1,3}\((\d{1,3})\)(\d{7})')
# match_by = my_reg_by.search(my_str_by)
# print(match_by)
# print(match_by.group())
# print(match_by.group(1))
# print(match_by.group(2))
# print(match_by.group(3))
# print(match_by.group(4))
# print()
#
# my_str_ru = "Мои номера телефонов: МТС +7(902)6234567; Билайн +7(912)3334455"
# my_reg_ru = re.compile(r'\w+ \+\d{1,3}\((\d{1,3})\)(\d{7}); \w+ \+\d{1,3}\((\d{1,3})\)(\d{7})')
# match_ru = my_reg_ru.search(my_str_ru)
# print(match_ru)
# print(match_ru.group())
# print(match_ru.group(1))
# print(match_ru.group(2))
# print(match_ru.group(3))
# print(match_ru.group(4))
# print()


my_str_ru = "Мои номера телефонов: МТС +7(902)6234567; Билайн +7(912)3334455"
my_reg_ru = re.compile(r'(\w+) \+\d{1,3}\((\d{1,3})\)(\d{7}); (\w+) \+\d{1,3}\((\d{1,3})\)(\d{7})')
match_ru = my_reg_ru.search(my_str_ru)
print(match_ru.group(1, 2, 3))
print(match_ru.group(4, 5, 6))
print('start - end')
print(match_ru.start(), match_ru.end())
print(match_ru.start(1), match_ru.end(1))
print(match_ru.start(1), match_ru.end(3))
print()

print('span')
print(match_ru.span())
print(match_ru.span(1))
print(match_ru.span(3))
