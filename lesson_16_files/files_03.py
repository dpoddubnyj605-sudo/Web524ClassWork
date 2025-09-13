import os

current_dir = r'.'
new_dir_01 = r'my_new_dir_01'
new_dir_02 = r'my_new_dir_02'


path_new_dir_01 = os.path.join(current_dir, new_dir_01)
print(path_new_dir_01)

# try:
#     os.mkdir(path_new_dir_01)
# except FileExistsError:
#     print(f'Невозможно создать файл, так как он уже существует в указанном расположении')
#
path_new_dir_02 = os.path.join(current_dir, new_dir_02)
# os.makedirs(path_new_dir_02, exist_ok=True)

try:
    os.rmdir(path_new_dir_01)
except FileNotFoundError:
    print('Не удается найти указанную папку')

try:
    os.rmdir(path_new_dir_02)
except FileNotFoundError:
    print('Не удается найти указанную папку')


