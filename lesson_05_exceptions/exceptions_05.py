from exceptions_03 import OnlyPositiveErrorException, PartsQuantityException

try:
    amount = int(input("Введите количество полученных предметов: "))
    if amount <= 0:
        raise OnlyPositiveErrorException("Количество предметов должно быть положительным!!!")
    items_type = "коробка"
    parts_quantity = int(input("Введите количество частей на которою будет разбита все партия: "))
    if parts_quantity < 0:
        raise OnlyPositiveErrorException("Количество частей должно быть положительным!")
    if parts_quantity > amount:
        raise PartsQuantityException('Количество частей не должно превышать количество предметов!')
    # if amount <= 0 or parts_quantity < 0:
    #     if amount <= 0 and parts_quantity <= 0:
    #         message = 'Количество предметов и частей должно быть положительным!'
    #     elif amount <= 0:
    #         message = 'Количество предметов должно быть положительным!'
    #     else:
    #         message = 'Количество частей должно быть положительным!'
    #     raise OnlyPositiveErrorException(message)
    amount_1_part = amount // parts_quantity
    amount_1_part_rest = amount % parts_quantity
except ValueError:
    print('Количество предметов/частей должно быть целым числом.')
except ZeroDivisionError:
    print('Невозможно разбить партию на 0 частей.')
except OnlyPositiveErrorException as OPEEx:
    print(OPEEx)
except PartsQuantityException as PQEx:
    print(PQEx)
except Exception as ex:
    print(type(ex).__name__)
    # print(ex.__repr__)
except:
    print("\nЧто то пошло не так!")
else:
    print(f'Партия из {amount} предметов. Тип: {items_type} - сохранена!')
    print(f'Каждая из {parts_quantity} частей состоит из {amount_1_part} указанных предметов.')
    if amount_1_part_rest != 0:
        print(f'Не распределенный остаток: {amount_1_part_rest} указанных предметов.')
finally:
    print("Программа завершила свою работу.")
