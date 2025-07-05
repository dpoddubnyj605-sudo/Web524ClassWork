shopping_matrix = []

while True:
    user_input = input("Введите вашу покупку: ").strip().lower()
    user_sum = 0
    if user_input == 'стоп':
        break
    while True:
        try:
            user_sum = float(input("Введите сумму покупки: "))
            break
        except ValueError:
            print('Ошибка ввода! Введите число: ')

    shopping_matrix.append([user_input, user_sum])

if shopping_matrix:
    user_choice = input('Вывести только покупки - 1\nВывести только суммы - 2\nВывести все + итог - 3\nВаш выбор: ')
    if user_choice == '1':
        print('Список покупок:')
        for purchase, price in shopping_matrix:
            print(purchase)
    elif user_choice == '2':
        print('Список сумм:')
        for purchase, price in shopping_matrix:
            print(price)
    elif user_choice == '3':
        total_sum = 0
        print("Покупки и суммы:")
        for purchase, price in shopping_matrix:
            print(f'Покупка: {purchase}. Цена: {price}')
            total_sum += price
        print(f'Итого покупок на сумму: {total_sum}')
    else:
        print('Ошибка ввода!')
else:
    print('Вы ничего не купили!')

