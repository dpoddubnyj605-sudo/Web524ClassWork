class OnlyPositiveErrorException(Exception):
    def __init__(self, *args, **kwargs):
        pass


class PartsQuantityException(Exception):
    def __init__(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    try:
        apples = int(input('Введите количество яблок которые у вас есть: '))
        if apples <= 0:
            raise OnlyPositiveErrorException()
    except ValueError:
        print("Количество должно быть целым числом!")
    except OnlyPositiveErrorException:
        print(f'У вас должно быть положительное количество яблок!')
    else:
        print(f'У вас {apples} яблок')
