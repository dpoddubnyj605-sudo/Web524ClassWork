import os

# path_learning = r'D:\work_Top_Academy_web\Web524ClassWork\lesson_16_files'
#
# # for path, dirnames, filenames in os.walk(path_learning):
# #     print(f'path >> {path}')
# #     print(f'dirnames >> {dirnames}')
# #     print(f'filenames >> {filenames}')
#
# disk = 'D:\\'
# dir_01 = 'work_Top_Academy_web'
# dir_02 = 'Web524ClassWork'
# dir_03_01 = 'lesson_15_tuples_sets_dicts'
# dir_03_02 = 'lesson_16_files'
#
# path_lesson_15 = os.path.join(disk, dir_01, dir_02, dir_03_01)
# path_lesson_16 = os.path.join(disk, dir_01, dir_02, dir_03_02)
# # print(path_lesson_15)
# # print(path_lesson_16)
#
# for path, dirnames, filenames in os.walk(path_lesson_15):
#     print(f'path >> {path}')
#     print(f'dirnames >> {dirnames}')
#     print(f'filenames >> {filenames}')
# print()
#
# for path, dirnames, filenames in os.walk(os.path.join(disk, dir_01, dir_02, dir_03_02)):
#     print(f'path >> {path}')
#     print(f'dirnames >> {dirnames}')
#     print(f'filenames >> {filenames}')

base_dir = '..'
data_dir = 'data_files'

path_data_dir = os.path.join(base_dir, data_dir)
print(path_data_dir)

for path, dirnames, filenames in os.walk(path_data_dir):
    print(f'path >> {path}')
    print(f'dirnames >> {dirnames}')
    print(f'filenames >> {filenames}')

print(os.path.abspath('..'))
print(os.path.abspath('files_01.py'))
print(os.path.abspath(r'data_files/example.txt'))
print(f'Путь к текущему: {os.path.abspath(__file__)}')