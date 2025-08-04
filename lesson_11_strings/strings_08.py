# string_alnum = "123abc"
# print(string_alnum.isalnum())
# string_alnum = "123abc**"
# print(string_alnum.isalnum())
#
# user_password = input('Введите желаемый пароль: ')
# if user_password.isalnum():
#     if 8 <= len(user_password) <= 12:
#         if user_password not in ['qwerty12345']:
#             print('Ваш пароль сохранен')
#         else:
#             print("Ваш пароль ненадежен")
#     else:
#         print('Длина пароля должна быть от 8 до 12 знаков включительно')
# else:
#     print(f'Допустимы только буквы и цифры')

string_alpha = 'abcdfe'
print(string_alpha.isalpha())
string_alpha = 'abcdfe123'
print(string_alpha.isalpha())
print()

string_digit = "1234567890"
print(string_digit.isdigit())

if string_digit.isdigit():
    print(int(string_digit))
print()

string_space = "   \n\t\r   "
print(string_space.isspace())

string_lower = "абвгд112346"
print(string_lower.islower())
string_lower = "абвгдA112346"
print(string_lower.islower())

string_upper = "HELLO"
print(string_upper.isupper())
string_upper = "HELLaO"
print(string_upper.isupper())

string_title = "Hello World"
print(string_title.istitle())
string_title = "Hello world"
print(string_title.istitle())
