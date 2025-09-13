def display_data_from_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            print(line, end='')


def get_data_from_file(file_path: str) -> list[str]:
    content = []
    with open(file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            content.append(line.rstrip())
    return content


def get_data_from_file_rl(file_path: str) -> list[str]:
    content = []
    with open(file_path, 'rt', encoding='utf-8') as file:
        content = file.readlines()
    return content


if __name__ == '__main__':
    filepath = r'data_files\file_for_reading.txt'
    display_data_from_file(filepath)
    print()

    data = []
    try:
        data = get_data_from_file(filepath)
    except FileNotFoundError as err:
        print(err)
        print(f'Файл не найден в указанном расположении: {filepath}')

    print(data)

    data_rl = []
    try:
        data_rl = get_data_from_file_rl(filepath)
    except FileNotFoundError as err:
        print(err)
        print(f'Файл не найден в указанном расположении: {filepath}')

    print(data_rl)
