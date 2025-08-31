def multiples(limit, divisor):
    for number in range(1, limit + 1):
        if number % divisor == 0:
            yield number


if __name__ == '__main__':
    user_limit = int(input("Введите верхний предел: "))
    user_divisor = int(input("Введите делитель: "))

    print(f'Числа от 1 до {user_limit}, кратные {user_divisor}:')
    for multiply in multiples(limit=user_limit, divisor=user_divisor):
        print(multiply)
