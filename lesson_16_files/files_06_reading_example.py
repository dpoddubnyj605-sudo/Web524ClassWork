def guests_manager(file_path):
    guests_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        guests_list = file.readlines()
    return len(guests_list), guests_list


if __name__ == '__main__':
    file_path = r'data_files\guests.txt'
    guest_count = 0
    guests = []

    try:
        guest_count, guests = guests_manager(r'data_files\guests.txt')
    except FileNotFoundError:
        print(f'Список гостей не найден в указанном месторасположении: {file_path}')

    print(f'Всего гостей: {guest_count}')
    print(f'Список гостей:\n{''.join(guests)}')
