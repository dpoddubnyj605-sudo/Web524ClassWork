"""
Задача: напишите программу, которая принимает от пользователя список чисел
(вводится одной строкой, числа разделены пробелами).
Программа должна:
Использовать итератор для последовательного вывода каждого числа.
Определить сумму всех чисел, используя цикл с итератором.
После завершения вывода всех чисел сообщить: «Все числа выведены. Сумма: {сумма}».
"""


def display_numbers_and_sum(nums_list):
    nums_iterator = iter(nums_list)
    total = 0
    while True:
        try:
            number = next(nums_iterator)
            print(number)
            total += number
        except StopIteration:
            print(f'Все числа выведены, их сумма: {total}')
            break


def make_ints_list(nums_list):
    nums_int = []
    for num in nums_list:
        if num.isdigit():
            nums_int.append(int(num))
    return nums_int


if __name__ == '__main__':
    user_nums_list = input('Введите числа через пробел: ').split()
    user_nums_int_list = make_ints_list(user_nums_list)
    display_numbers_and_sum(user_nums_int_list)
