# file = open(r'data_files\file_for_reading.txt', 'rt', encoding='utf-8')
# content = file.read()
# file.close()
# print(content)
# print()

# try:
#     with open(r'data_files\file_for_reading1.txt', 'rt', encoding='utf-8') as file:
#         content_ctx = file.read()
# except FileNotFoundError as err:
#     print(err)
# else:
#     print(content_ctx)
# print()


def get_data_from_file(file_path):
    with open(file_path, 'rt', encoding='utf-8') as file:
        content_ctx = file.read()
    return content_ctx


if __name__ == '__main__':
    filepath = r'data_files\file_for_reading1.txt'
    data = ''
    try:
        data = get_data_from_file(filepath)
    except FileNotFoundError as err:
        print(err)
        print(f'Файл не найден в указанном расположении: {filepath}')

    print(data)
