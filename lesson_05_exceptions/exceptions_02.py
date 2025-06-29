try:
    amount = int(input("Введите количество полученных предметов: "))
    items_type = input("Укажите тип полученных предметов: ")
    parts_quantity = int(input("Введите количество частей на которою будет разбита все партия: "))
    amount_1_part = amount // parts_quantity
    amount_1_part_rest = amount % parts_quantity
except ValueError:
    print('Количество предметов/частей должно быть целым числом.')
except ZeroDivisionError:
    print('Невозможно разбить партию на 0 частей.')
except Exception as ex:
    print(type(ex).__name__)
    # print(ex.__repr__)
else:
    print(f'Партия из {amount} предметов. Тип: {items_type} - сохранена!')
    print(f'Каждая из {parts_quantity} частей состоит из {amount_1_part} указанных предметов.')
    if amount_1_part_rest != 0:
        print(f'Не распределенный остаток: {amount_1_part_rest} указанных предметов.')
finally:
    print("Программа завершила свою работу.")



