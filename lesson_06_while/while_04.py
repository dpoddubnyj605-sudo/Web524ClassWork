odd_numbers = 0
even_numbers = 0

number = int(input("Введите число или 0, для остановки программы: "))

# 0 - прекращает цикл

while number != 0:

    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

    try:
        number = int(input("Введите число или 0, для остановки программы: "))
    except ValueError:
        print(f'ОШИБКА!!! Можно вводить только целые числа!')
        break

else:
    print('Цикл был завершен без прерываний')

print(f"Четные: {even_numbers}")
print(f"НЕчетные: {odd_numbers}")
