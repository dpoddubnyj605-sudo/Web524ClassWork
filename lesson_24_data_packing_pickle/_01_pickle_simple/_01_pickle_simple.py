import pickle

data = {
    'nums': [1, 2, 3, 4, 5 + 5],
    'strings': ['character string', b'byte_string'],
    'other': [None, True, False]
}

# для обычной работы
my_data_s = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
print(my_data_s)
print(type(my_data_s))

my_data_ds = pickle.loads(my_data_s)
print(my_data_ds)
print(type(my_data_ds))

# для работы с файлами, для сохранения промежуточного состояния программы
with open('data_pickle.pdf', 'wb') as file:
    pickle.dump(my_data_ds, file, protocol=5)

try:
    with open('data_pickle.pdf', 'rb') as fp:
        my_data_ff = pickle.load(fp)
except FileNotFoundError:
    print(f'Файл не найден')

print(my_data_ff)
