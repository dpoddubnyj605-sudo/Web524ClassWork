import os

path_learning = r'data_files'

print(os.path.isabs(path_learning))
print(os.path.isfile(path_learning))
print(os.path.isdir(path_learning))
print(os.path.islink(path_learning))
print()

path_learning = r'data_files/example.txt'

print(os.path.isabs(path_learning))
print(os.path.isfile(path_learning))
print(os.path.isdir(path_learning))
print(os.path.islink(path_learning))
print()

path_learning = os.path.abspath(r'data_files/example.txt')
print(os.path.isabs(path_learning))
print(os.path.isfile(path_learning))
print(os.path.isdir(path_learning))
print(os.path.islink(path_learning))