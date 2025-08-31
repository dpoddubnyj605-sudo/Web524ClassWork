from datetime import datetime


def log(func):
    def wrapper(*args, **kwargs):
        print(f'{datetime.now()} >> Вызов функции {func.__name__} с аргументами {args} и {kwargs}')
        return func(*args, **kwargs)

    return wrapper


def log_to_file(func):
    def wrapper(*args, **kwargs):
        with open('logs/log_file.txt', 'a', encoding='utf-8') as file:
            file.write(f'{datetime.now()} >> Вызов функции {func.__name__} с аргументами {args} и {kwargs}\n')
        return func(*args, **kwargs)

    return wrapper


@log
@log_to_file
def display_my_space_address(*args, **kwargs):
    if args:
        for item in args:
            print(item)
    if kwargs:
        for key, value in kwargs.items():
            print(f'{key}: {value}')


if __name__ == '__main__':
    display_my_space_address('Дмитрий', 36, planet='Земля', star='Солнце')
