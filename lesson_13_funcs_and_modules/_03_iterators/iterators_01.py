numbers_list = [1, 2, 3, 4]
numbers_iterator = iter(numbers_list)

print(numbers_iterator)
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
# numbers_iterator = iter(numbers_list)
# print(next(numbers_iterator))

for number in numbers_list:
    print(number, end=' ')
print()

numbers_iterator = iter(numbers_list)
for number in numbers_iterator:
    print(number, end=' ')
print()

numbers_iterator = iter(numbers_list)
for i in range(10):
    try:
        print(next(numbers_iterator))
    except StopIteration:
        print('Итератор истощен')
        break
print()

numbers_iterator = iter(numbers_list)
while True:
    try:
        print(next(numbers_iterator))
    except StopIteration:
        print('Итератор истощен')
        break




