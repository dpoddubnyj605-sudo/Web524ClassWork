"""
Тип ошибки 1:  Удаление элемента из списка во время итерации — RuntimeError

Ошибка возникает, когда при выполнении сортировки или поиска попытаться изменить список,
по которому в данный момент выполняется итерация.
"""

numbers = [10, 20, 30, 40]
for num in numbers:
    if num % 20 == 0:
        numbers.remove(num)  # RuntimeError: list changed size during iteration
print(numbers)

"""
Решение:

Используйте копию списка для итерации
Создайте копию списка и выполняйте изменения в исходном списке.
"""

numbers = [10, 20, 30, 40]
for num in numbers[:]:
    if num % 20 == 0:
        numbers.remove(num)
print(numbers)