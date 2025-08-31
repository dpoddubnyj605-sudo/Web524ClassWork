def calculate_way(v, t):
    way = v * t
    return way


if __name__ == '__main__':
    data_list1 = [60, 2]
    data_list2 = [40, 2]
    data_list3 = [100, 2]
    data_matrix = [data_list1, data_list2, data_list3]
    data_tuple = (50, 3)
    print(f'Дистанция из списка: {calculate_way(*data_list1)}')
    print(f'Дистанция из кортежа: {calculate_way(*data_tuple)}')
    print()
    for data in data_matrix:
        print(f'Дистанция из матрицы: {calculate_way(*data)}')
