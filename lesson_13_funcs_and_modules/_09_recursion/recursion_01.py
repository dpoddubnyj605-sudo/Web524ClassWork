# базовый случай
def calculate_factorial_base_case(n):
    if n == 1:
        return 1


# рекурсивный случай
def calculate_factorial_recursive_case(n):
    if n == 1:
        return 1
    return n * calculate_factorial_recursive_case(n - 1)
    """
    1) 5 * calculate_factorial_recursive_case(4)
    2) 5 * (4 * calculate_factorial_recursive_case(3))
    3) 5 * (4 * (3 * calculate_factorial_recursive_case(2)))
    4) 5 * (4 * (3 * (2 * (calculate_factorial_recursive_case(1))))
    4) 5 * (4 * (3 * (2 * (1))))

    5) 120 # возвращаем произведение: 5 * 4 * 3 * 2 * 1
    """



if __name__ == '__main__':
    print(calculate_factorial_recursive_case(5))
    factorial_5 = 1 * 2 * 3 * 4 * 5
