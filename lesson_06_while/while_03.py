even_numbers = 0
odd_numbers = 0

while True:
    number = int(input("Введите число или 0, для остановки программы: "))
    if number == 0:
        break
    elif number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

print(f"Четные: {even_numbers}")
print(f"НЕчетные: {odd_numbers}")




