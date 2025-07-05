total_amount = 0

while True:
    try:
        amount = float(input('Введите сумму транзакции или 0 для остановки ввода: '))
        if amount == 0:
            break
    except ValueError:
        print(f'ОШИБКА!!! Необходимо ввести числовое значение суммы!')
    else:
        description = input('Введите описание транзакции: ')
        print(f'Введена транзакция: {description}. Сумма транзакции: {amount}')
        total_amount += amount

print(f'Общая сумма транзакций: {total_amount}')
