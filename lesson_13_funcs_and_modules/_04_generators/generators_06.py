def fib_gen(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    for number in fib_gen(56):
        print(number)
