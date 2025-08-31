with open('students/students.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

print(data)
print("Первые 6 строк:")
print(''.join(data[:6]))

with open('students/students.txt', 'r', encoding='utf-8') as file:
    data_iterator = iter(file)
    for _ in range(6):
        try:
            print(next(data_iterator).strip())
        except StopIteration:
            break
