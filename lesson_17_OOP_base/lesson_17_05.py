question_1 = 'My name __ Vova'
correct_1 = 'is'

print(question_1)
answer_1 = input('Введите ваш ответ: ')
if answer_1 == correct_1:
    print('Ответ верный!')
else:
    print(f"Ответ неверный, верный ответ {correct_1}")