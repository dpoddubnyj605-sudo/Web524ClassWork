import os

base_path = r'dir_2/file_03.txt'
new_path = r'dir_3/file_03.txt'

try:
    os.replace(base_path, new_path)
except FileNotFoundError:
    print(f'Файл не найден!')
except FileExistsError:
    print(f'Такой файл уже существует!')
else:
    print(f"Файл успешно перемещен/переименован:\n{os.path.abspath(new_path)}")
finally:
    print('Программа завершила свою работу!')
