import re

my_str = 'abcd abc efgh'
my_str_no_match = 'abc abc efg'
my_reg = re.compile(r'\w{4}')
match_01 = re.search(my_reg, my_str)
match_02 = my_reg.search(my_str)
match_03 = my_reg.search(my_str_no_match)
print(match_01)
print(match_02)
print(match_03)
print(match_01.group())
print(match_02.group(0))

my_str_1 = "abcd abc 123 egfd 456"
my_reg_1 = re.compile(r'\d{3}')
match_1 = re.search(my_reg_1, my_str_1)
print(match_1)
print(match_1.group(0))
