import os

base_path = r'dir_1/file_01.txt'
new_path = r'dir_2/file_01_new_place.txt'

try:
    os.rename(base_path, new_path)
except FileNotFoundError:
    print(f'Файл не найден!')
except FileExistsError:
    print(f'Такой файл уже существует!')
else:
    print(f"Файл успешно перемещен/переименован:\n{os.path.abspath(new_path)}")
finally:
    print('Программа завершила свою работу!')

base_path = r'dir_1/file_03.txt'
new_path = r'dir_2/file_02_new_place.txt'

# renames умеет создавать директории если это необходимо, а также удаляет пустую директорию (из которой перемещали файл)
try:
    os.renames(base_path, new_path)
except FileNotFoundError:
    print(f'Файл не найден!')
except FileExistsError:
    print(f'Такой файл уже существует!')
else:
    print(f"Файл успешно перемещен/переименован:\n{os.path.abspath(new_path)}")
finally:
    print('Программа завершила свою работу!')
