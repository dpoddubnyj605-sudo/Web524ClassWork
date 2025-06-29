# weather = input("Введите какая сегодня погода: 1 - хорошая/2 - плохая: ")
# tickets = input("Есть ли билеты: 1 - да/2 - нет: ")
# table = input("Есть ли столик: да - 1/нет - 2: ")
#
# if weather == '1':
#     print("Идем гулять!")
# elif tickets == '1':
#     print('Идем в кино')
# elif table == '1':
#     print('Идем в ресторан')
# else:
#     print('Вечер пиццы и настолок!')

# user_choice = input(
#     "Введите какая сегодня погода:\n1 - для прогулок\n2 - для кино\n3 - для ресторана\n0 - для сиденья дома\n")
#
# if user_choice == '1':
#     print("Идем гулять!")
# elif user_choice == '2':
#     print('Идем в кино')
# elif user_choice == '3':
#     print('Идем в ресторан')
# elif user_choice == '0':
#     print('Вечер пиццы и настолок!')
# else:
#     print('Ошибка ввода! Перезапустите программу!')

evalution_map = {
    '*': 'Ужасно',
    '**': 'Очень плохо',
    '***': 'Средненько',
    '****': 'Всё в порядке',
    '*****': 'Прекрасная поездка'
}

stars = input()
print(evalution_map.get(stars, 'Неизвестная оценка'))
if stars in evalution_map.keys():
    print(evalution_map[stars])
else:
    print('Неизвестная оценка')
