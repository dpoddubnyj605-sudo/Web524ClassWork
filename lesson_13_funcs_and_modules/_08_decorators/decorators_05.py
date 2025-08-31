def log(func):
    def wrapper(*args, **kwargs):
        print(f'Вызов функции {func.__name__} с аргументами {args} и {kwargs}')
        return func(*args, **kwargs)
    return wrapper


@log
def greet_deeply_curried(greeting):
    @log
    def w_separator(separator):
        @log
        def w_emphasis(emphasis):
            @log
            def w_name(name):
                print(greeting + separator + name + emphasis)

            return w_name

        return w_emphasis

    return w_separator


if __name__ == '__main__':
    greet = greet_deeply_curried('Привет!')('/.../')("!!!")
    greet('Дмитрий')
    greet('Петр')


