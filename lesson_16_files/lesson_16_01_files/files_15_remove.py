import os
import shutil

my_path = r'dir_2/file_01_new_place.txt'

try:
    os.remove(my_path)
except FileNotFoundError:
    print(f'В указанном расположении: {os.path.abspath(my_path)}\nфайл не найден!')
else:
    print(f'Файл успешно удален!')

my_path = r'dir_2'
try:
    shutil.rmtree(my_path)
except FileNotFoundError:
    print(f'В указанном расположении: {os.path.abspath(my_path)}\nфайл не найден!')
else:
    print(f'Файл успешно удален!')
