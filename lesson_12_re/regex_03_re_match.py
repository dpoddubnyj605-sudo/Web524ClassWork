import re

my_str_ru = "Мои номера телефонов: МТС +7(902)6234567; Билайн +7(912)3334455"
my_reg_ru = re.compile(r'(\w+) \+\d{1,3}\((\d{1,3})\)(\d{7}); (\w+) \+\d{1,3}\((\d{1,3})\)(\d{7})')
match_ru = my_reg_ru.match(my_str_ru)
print(match_ru)

my_str_ru = "Мои номера телефонов: МТС +7(902)6234567; Билайн +7(912)3334455 Мои номера телефонов"
my_reg_ru = re.compile(r'Мои номера телефонов: (\w+) \+\d{1,3}\((\d{1,3})\)(\d{7}); (\w+) \+\d{1,3}\((\d{1,3})\)(\d{7})')
match_ru = my_reg_ru.match(my_str_ru)
print(match_ru)

print(match_ru.group())
print(match_ru.group(1))
print(match_ru.group(2))
print(match_ru.group(3))
