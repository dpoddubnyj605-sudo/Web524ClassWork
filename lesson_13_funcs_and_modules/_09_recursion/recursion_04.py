"""
Что делать если необходимо более 996 повторений рекурсии
"""

import sys


def calculate_factorial(n):
    if n == 1:
        return 1
    return n * calculate_factorial(n - 1)


if __name__ == '__main__':
    factorial_num = 1501
    if factorial_num > 996:
        sys.setrecursionlimit(factorial_num + 1)
    print(calculate_factorial(factorial_num))
