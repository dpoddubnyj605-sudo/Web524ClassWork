def calc_result(numbers: list):
    sum_ = 0
    for number in numbers:
        sum_ += int(number)
    return sum_


def prepare_numbers(numbers: str):
    numbers_list = numbers.split()
    return numbers_list


def main():
    user_numbers = input('Введите число через пробел: ')
    user_numbers_list = prepare_numbers(user_numbers)
    user_result = calc_result(user_numbers_list)
    print(user_result)


if __name__ == '__main__':
    main()
