def get_shopping_data(filename):
    items_count = 0
    items_sum = 0
    row_index = 0
    try:
        with open(filename, encoding='utf-8') as file:
            for item_data in file:
                row_index += 1
                if item_data.count(' || ') < 2:
                    print(f'Ошибка в строке {row_index} >> {item_data.strip()} ')
                    continue
                temp_data = item_data.strip().split('||')
                item, quantity, price = temp_data
                items_count += 1
                items_sum += float(quantity) * float(price)
    except FileNotFoundError:
        print(f'Файл: {filename} не найден')
        return False
    return items_count, items_sum


if __name__ == '__main__':
    my_file = r'data_files/shopping_list.txt'
    my_count, my_sum = get_shopping_data(my_file)
    print(f'В списке {my_count} позиций, общая сумма {my_sum} рублей.')
