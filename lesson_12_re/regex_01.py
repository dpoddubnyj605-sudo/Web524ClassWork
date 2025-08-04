import re

# """
# Подходят все строки, содержащие фрагменты course, topic, part, a в указанном порядке.
# Между фрагментами должен находиться один произвольный символ, кроме символа новой строки
# """
# reg_01 = re.compile(r'course.topic.part.a')
# string_01 = '1234course/topic/part/a1234'
# string_01_01 = 'course$topic@part*a'
# print(bool(reg_01.findall(string_01)))
# print(bool(reg_01.findall(string_01_01)))
# print()
#
# """
# Подходят все строки, содержащие фрагмент course, сразу после которого должны идти две десятичные цифры
# """
# reg_02 = r'course\d\d'
# reg_02_c = re.compile(r'course\d\d')
# string_02 = 'course12asd'
# string_02_01 = 'mycourse15345'
# print(bool(re.findall(reg_02, string_02)))
# print(bool(re.findall(reg_02_c, string_02_01)))
# print(bool(reg_02_c.findall(string_02)))
# print(bool(reg_02_c.findall(string_02_01)))
# print()

# """
# Подходят все строки, содержащие фрагмент part, сразу после которого должен быть один любой символ,
# кроме десятичной цифры, после которого идет фрагмент 001
# """
# reg_03 = re.compile('part\\D001')
# string_03 = 'part@001_part*001'
# string_03_01 = 'my_part_001_01'
# print(reg_03.findall(string_03))
# print(bool(reg_03.findall(string_03)))
# print(bool(reg_03.findall(string_03_01)))
#
# """
# Подходят все строки, содержащие фрагмент user, сразу после которого должен быть один любой пробельный символ,
# после которого идет фрагмент 24
# """
# reg_04 = re.compile(r'user\s24')
# string_04 = 'my_user 24_01'
# string_04_01 = 'user\t24'
# print(bool(reg_04.findall(string_04)))
# print(bool(reg_04.findall(string_04_01)))
# print()
#
# """
# Подходят все строки, содержащие фрагмент user-, сразу после которого должен быть один любой не пробельный символ,
# после которого идет фрагмент 007
# """
# reg_05 = re.compile(r'user-\S007')
# string_05 = "my_user-s007"
# string_05_01 = 'James user-1007 agent'
# print(bool(reg_05.findall(string_05)))
# print(bool(reg_05.findall(string_05_01)))
# print()
#
# """
# Подходят все строки, содержащие фрагмент из двух любых буквенно-цифровых символов (или символа нижнего подчеркивания),
# сразу после которого идет фрагмент 555
# """
# reg_06 = re.compile(r'\w\w555')
# string_06 = "1s555"
# string_06_01 = "dd555"
# print(bool(reg_06.findall(string_06)))
# print(bool(reg_06.findall(string_06_01)))
# print()
#
# """
# Подходят все строки, содержащие фрагмент Python, сразу после которого идет один символ,
# не относящийся к буквенно-цифровым символам (и не символ нижнего подчеркивания)
# """
# reg_07 = re.compile(r'Python\W')
# string_07 = 'Python*'
# print(bool(reg_07.findall(string_07)))
# print()
#
# """
# Подходят все строки, содержащие фрагмент из двух символов, первый из которых это цифра в диапазоне от 0 до 5,
# а второй — это либо цифра от 0 до 7, либо символ латинского алфавита от «А» до «С», или от «а» до «с»
# """
# reg_08 = re.compile(r'[0-5][0-7A-Ca-c]')
# string_08 = '57'
# string_08_01 = '4A'
# string_08_02 = '3b'
# print(bool(reg_08.findall(string_08)))
# print(bool(reg_08.findall(string_08_01)))
# print(bool(reg_08.findall(string_08_02)))
# print()
#
# """
# Подходят все строки, содержащие фрагмент из одного символа, заключенного в круглые скобки.
# Это должен быть символ латинского алфавита, кроме символов в диапазонах от «B» до «D» и от «b» до «d»
# """
# reg_09 = re.compile(r'\([^B-Db-d]\)')
# string_09 = '(a)'
# string_09_01 = '(b)'
# print(bool(reg_09.findall(string_09)))
# print(bool(reg_09.findall(string_09_01)))

"""
Подходят все строки, содержащие фрагмент student, сразу после которого идет пять десятичных цифр
"""
reg_10 = re.compile(r'student\d{5}')
string_10 = 'student12345'
string_10_01 = 'student12b45'
print(bool(reg_10.findall(string_10)))
print(bool(reg_10.findall(string_10_01)))
print()

"""
Подходят все строки, содержащие фрагмент student, сразу после которого идут от трех до пяти десятичных цифр
"""
reg_11 = re.compile(r'student\d{3,5}')
string_11 = 'student234'
string_11_01 = 'student12'
print(bool(reg_11.findall(string_11)))
print(bool(reg_11.findall(string_11_01)))
print()

"""
Подходят все строки, содержащие фрагмент user, сразу после которого идут десятичные цифры в количестве не менее трех
"""
reg_12 = re.compile(r'user\d{3,}')
string_12 = 'user123456797'
string_12_01 = 'user12a1345'
print(bool(reg_12.findall(string_12)))
print(bool(reg_12.findall(string_12_01)))
print()

"""
Подходят все строки, содержащие фрагмент user, сразу после которого идут десятичные цифры в количестве не более двух
"""
reg_12_01 = re.compile(r'user\d{,2}\D')
string_12_01_01 = 'user12a1345'
string_12_01_02 = 'user123456797'
print(bool(reg_12_01.findall(string_12_01_01)))
print(bool(reg_12_01.findall(string_12_01_02)))
print()
#
"""
Подходят все строки, содержащие фрагмент come, причем последний символ «e» может как присутствовать, так и нет
"""
reg_13 = re.compile(r'come?')
string_13 = 'Income'
string_13_01 = 'outcom'
string_13_02 = 'coming'
string_13_03 = 'ccmi'
print(bool(reg_13.findall(string_13)))
print(bool(reg_13.findall(string_13_01)))
print(bool(reg_13.findall(string_13_02)))
print(bool(reg_13.findall(string_13_03)))
print()

"""
Подходят все строки, содержащие фрагмент user, после которого должна идти как минимум одна десятичная цифра
"""
reg_14 = re.compile(r'user\d+')
string_14 = 'user123'
string_14_01 = 'user_123'
print(bool(reg_14.findall(string_14)))
print(bool(reg_14.findall(string_14_01)))
