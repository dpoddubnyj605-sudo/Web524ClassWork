def decorator(func):
    def wrapper(name):
        print('До вызова функции')
        func(name)
        print('После вызова функции')
    return wrapper


@decorator
def say_greet_name(name):
    print(f'Hello {name}!')


if __name__ == '__main__':
    say_greet_name('Ivan')
