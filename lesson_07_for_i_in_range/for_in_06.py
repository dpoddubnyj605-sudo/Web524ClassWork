symbol_string = ''
symbol = input("Введите символ для заполнения: ")
str_len = int(input("Введите длину строки: "))

for i in range(str_len):
    symbol_string += symbol

print(symbol_string)
