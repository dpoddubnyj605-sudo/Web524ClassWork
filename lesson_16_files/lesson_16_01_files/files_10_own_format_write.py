def write_managers_data_own_format(filename: str, data_to_write: dict, divider: str) -> bool:
    with open(fr'data_files\{filename}.txt', 'w', encoding='utf-8') as file:
        for companies, manager in data_to_write.items():
            file.write(f'{manager}{divider}{companies[0]}{divider}{companies[1]}\n')
    print("Данные успешно записаны!")
    return True


if __name__ == '__main__':
    managers_to_write = {
        ('Bethesda', 'Microsoft'): 'Тодд Говард',
        ('ID Software', 'Microsoft'): 'Джон Кармак',
        ('AMD', 'AMD'): 'Лиза Су'
    }
    file_name = input('Введите имя файла для сохранения: ')
    user_divider = input('Введите разделитель: ')
    write_managers_data_own_format(file_name, managers_to_write, user_divider)
