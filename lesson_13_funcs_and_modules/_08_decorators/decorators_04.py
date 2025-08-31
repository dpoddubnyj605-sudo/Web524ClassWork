def decorator1(func):
    def wrapper(name):
        print('Декоратор1')
        func(name)
    return wrapper

def decorator2(func):
    def wrapper(name):
        print('Декоратор2')
        func(name)
    return wrapper


@decorator1
@decorator2
def say_greet_name(name):
    print(f'Hello {name}!')


if __name__ == '__main__':
    say_greet_name('Ivan')
