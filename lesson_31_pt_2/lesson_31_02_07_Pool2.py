from multiprocessing import Pool
import math
from datetime import datetime
import sys
sys.set_int_max_str_digits(1000000)

def compute_factorial(n):
    return math.factorial(n)


if __name__ == '__main__':
    numbers = [1000000, 1534600, 1234000, 1515300, 1357100]
    print(datetime.now())
    with Pool(processes=4) as pool:
        results = pool.map(compute_factorial, numbers)

    for n, result in zip(numbers, results):
        # print(f'Факториал {n}: {result}')
        pass
    print(datetime.now())
    print()

    print(datetime.now())
    for number in numbers:
        result = compute_factorial(number)
        # print(result, end='')
    print(datetime.now())
