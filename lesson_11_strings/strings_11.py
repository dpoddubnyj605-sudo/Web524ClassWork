import os

normal_string = "Это строка \n - обычная строка"
print(normal_string)

raw_string = r"Это строка \n - сырая строка"
print(raw_string)

err_raw = r'abc\\\abc'
print(err_raw)

print(os.path.exists(r'.\strings_01.py'))

data = 'my_data'

print(fr'.\filename_{data}.txt')
