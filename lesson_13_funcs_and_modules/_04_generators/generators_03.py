import sys

numbers_list = [x ** 2 for x in range(1000)]
numbers_generator = (x ** 2 for x in range(1000))

# print(numbers_list)
# print(numbers_generator)

print(f"Размер списка: {sys.getsizeof(numbers_list)} байт")
print(f"Размер генератора: {sys.getsizeof(numbers_generator)} байт")
