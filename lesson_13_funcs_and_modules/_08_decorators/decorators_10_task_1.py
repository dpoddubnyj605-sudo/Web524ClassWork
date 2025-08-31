def call_counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Функция "{func.__name__}" вызвана {count} раз(а).')
        return func(*args, **kwargs)

    return wrapper


@call_counter
def say_hello():
    print("Hello!")


if __name__ == '__main__':
    say_hello()
    say_hello()
    say_hello()
