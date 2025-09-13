user_name = input('Как вас зовут: ')
user_language = input('Какой язык вы изучаете: ')
user_time = input('Как долго: ')
user_institution = input('Где: ')

user_answers = [user_name, user_language, user_time, user_institution]

with open(r'data_files\user_data.txt', 'a', encoding='utf-8') as file:
    for answer in user_answers:
        file.write(f'{answer}\n')
    file.write('\n')
print("Ответы записаны!")

"""
Для работы с уже подготовленными данными
"""
# user_answers_wl = [user_name, user_language, user_time, user_institution]
# with open(r'data_files\user_data.txt', 'a', encoding='utf-8') as file:
#     file.writelines(user_answers)
# print("Ответы записаны!")
