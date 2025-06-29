print(3 + 5)
print(5 - 3)
print(3 * 5)
print(3 ** 3)
print(6 / 3)
print()

print(11 // 3)
print(11 % 3)
print()

num_4_digits = 1234
digit_1 = num_4_digits // 1000
#            1234      // 1000
print(digit_1)
digit_2 = num_4_digits % 1000 // 100
print(digit_2)
digit_3 = num_4_digits % 1000 % 100 // 10
digit_4 = num_4_digits % 1000 % 100 % 10
print(digit_1 + digit_2 + digit_3 + digit_4)
print()

num_1 = 10

if num_1 % 2 == 0:
    print('even')
else:
    print('odd')


