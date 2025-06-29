# num_1 = 1
# num_2 = 2
# num_3 = 3
#
# print(num_2 > num_1 and num_3 > num_2)
# print(num_3 > num_2 > num_1)
# print(num_1 < num_2 < num_3)
# print(num_1 < num_3 < num_3)

# competent = True
# responsible = True
# careful = True
# print(competent and responsible and careful)
# print()
#
# competent = True
# responsible = False
# careful = True
# print(competent and responsible and careful)
# print()
#
# competent = False
# responsible = False
# careful = True
#
# print(competent or responsible or careful)
# print()
#
# competent = False
# responsible = True
# careful = True
#
# print(competent or responsible and careful)
# #      False    or   True

# previously_fired = True
# print(not previously_fired)
#
# previously_fired = False
# print(not previously_fired)
# print()
#
# previously_fired = False
# competent = False
# responsible = True
# careful = True
#
# print(competent or responsible and careful and not previously_fired)
# #                              True                 True
# #       False                             True

time = int(input("Введите время в часах")) % 24

large_luggage = False
ticket = False
money = False

print(money or ticket and not large_luggage and time > 6)
print((money or ticket) and not large_luggage and time > 6)
