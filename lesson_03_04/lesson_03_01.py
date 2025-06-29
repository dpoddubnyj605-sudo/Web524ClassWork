print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(0))
print(bool(0.0))
print(bool(None))
print()

print(bool("Some data"))
print(bool(['item', 2, 2.5]))
print(bool(('item', 2, 2.5)))
print(bool({'item', 'item1', 'item2'}))
print(bool({'key_1': 'value_1', 'key_2': 'value_2'}))
print(bool(2))
print(bool(0.05))
print()


data = ['item', 2, 2.5]
if data:
    print(f'Обработка данных')
else:
    print(f'Ничего не делаем/сообщаем об ошибке')
