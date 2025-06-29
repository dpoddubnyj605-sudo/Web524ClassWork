weather = input("Введите какая сегодня погода: 1 - хорошая/2 - плохая: ")

if weather == "1":
    print("Идем гулять!")
else:
    tickets = input("Есть ли билеты: 1 - да/2 - нет: ")
    if tickets == '1':
        print('Идем в кино')
    else:
        table = input("Есть ли столик: да - 1/нет - 2\n")
        if table == '1':
            print('Идем в ресторан')
        else:
            print('Вечер пиццы и настолок!')
