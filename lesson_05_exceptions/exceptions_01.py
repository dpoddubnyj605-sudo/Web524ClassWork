from datetime import datetime

try:
    print('Код который может вызвать ошибку.')
    num = int(input('Введите число: '))
    print(num / 0)
except ValueError:
    print('Введено неверное значение, допустимы только целые числа.')
# except ZeroDivisionError:
#     print('Попытка деления на 0')
except BaseException as BE:
    print(f'Код на случай возникновения исключения.')
    print(type(BE).__name__)
    with open('logging.txt', 'a', encoding='utf-8') as file:
        file.write(f'{type(BE).__name__} - {datetime.now()}\n')
else:
    print('Код который выполняется если исключения не возникло.')
    print(num * 2)
finally:
    print('Код который выполняется в любом случае.')
