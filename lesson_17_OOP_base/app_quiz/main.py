from Classes.ClassQuestion import Question

if __name__ == '__main__':
    questions = [
        ['My name __ Vova', 'is'],
        ['I live __ Moscow', 'in'],
    ]
    question_objs = []
    for question, correct_answer in questions:
        question_objs.append(Question(question, correct_answer))

    for question in question_objs:
        print(question.question)
        user_answer = input('Введите ваш ответ: ').strip().lower()
        if question.is_correct(user_answer):
            print(f'{user_answer} это верный ответ!')
        else:
            print(f'{user_answer} это неверно, правильный ответ {question.correct_answer}')
