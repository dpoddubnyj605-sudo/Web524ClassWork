def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            print(f'Элемент найден, его индекс: {mid}')
            return True
        elif lst[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине
    print("Элемент не найден")
    return False


if __name__ == '__main__':
    numbers = [1, 3, 5, 7, 9, 11, 13]
    binary_search(numbers, 11)
    binary_search(numbers, 4)
