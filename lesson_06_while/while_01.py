odd_numbers = 0
even_numbers = 0

try:
    number = int(input('Введите число или 0, для остановки программы: '))
except ValueError:
    print('Необходимо ввести целое число или 0')
else:
    while number != 0:
        if number % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
        while True:
            try:
                number = int(input('Введите число или 0, для остановки программы: '))
                break
            except ValueError:
                print('Необходимо ввести целое число или 0')

print(f'Количество четных: {even_numbers}')
print(f'Количество нечетных: {odd_numbers}')
