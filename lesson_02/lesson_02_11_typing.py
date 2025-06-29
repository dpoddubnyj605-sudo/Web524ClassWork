print("3", 3)

num_1 = '3245'
num_2 = 2
print(int(num_1) + num_2)
num_3 = '35.5'
print(float(num_3) * num_2)

num_4 = '1'
num_5 = '1'
print(num_4 + ' ' + num_5)

print('Python ' * 3)

num_to_str = 12348364
new_str = str(num_to_str)
print(new_str, type(new_str))

numbers_str = input("str: ")
print(type(numbers_str))
numbers = list(map(int, numbers_str.split()))  # ["1", "2", "3", "5", "4", "6", "8"]
print("int:", numbers)
