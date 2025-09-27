def liner_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            print(f'Элемент найден его индекс: {index}')
            return True
    print(f'Элемент не найден')
    return False


if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    liner_search(numbers, 40)
    liner_search(numbers, 60)
