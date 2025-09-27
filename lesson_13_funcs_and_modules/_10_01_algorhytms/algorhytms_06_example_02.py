def find_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value


if __name__ == '__main__':
    scores_input = input("Введите результаты через пробел: ")
    scores_list = [int(score) for score in scores_input.split()]
    print(f'Результаты участников: {scores_list}')
    max_score = find_max(scores_list)
    print(f"Максимальный результат: {max_score}")
