def process_text(text):
    # Изменение текста    
    sentences = text.replace('\n', '')
    sentences = sentences.split('. ')
    new_list = []
    for sentence in sentences:
        if '!' in sentence:
            sentence = sentence.split('! ')
            new_list.extend(sentence)
        else:
            new_list.append(sentence)

    # print(new_list)
    capitalized_sentences = [sentence.strip().capitalize() for sentence in new_list]
    processed_text = '. '.join(capitalized_sentences)

    # Подсчет количества цифр в тексте
    digit_count = sum(char.isdigit() for char in text)

    # Подсчёт количества знаков препинания в тексте
    punctuation_count = sum(char in '.,!?;:' for char in text)

    # Подсчет количества восклицательных знаков в тексте
    exclamation_count = text.count('!')

    return capitalized_sentences, digit_count, punctuation_count, exclamation_count


text = """В 1982 году Гвидо ван Россум окончил университет и попал в команду разработчиков института CWI, где до 1986 года занимался проектированием языка ABC — прототипа Python. aBC задумывался как инструмент для пользователей, которые до этого не программировали и не разбирались в устройстве компьютеров! должен был получиться удобный язык с простым синтаксисом, на котором легко учиться писать программы. в 1987 году проект ABC закрылся. по мнению Гвидо, главная причина заключалась в отсутствии доступного интернета — язык медленно распространялся и не получал оперативной обратной связи от пользователей! из-за этого команда не добавляла улучшения, которые учитывали бы потребности разработчиков. Сами программисты не могли присоединиться к сообществу и поучаствовать в развитии проекта. Язык ABC опередил своё время и мог стать заменой Python!"""

# Обработка текста
capitalized_sentences, digit_count, punctuation_count, exclamation_count = process_text(text)

# Вывод результатов
[print(sent) for sent in capitalized_sentences]

# print("Обработанный текст: ")
# print(processed_text)
# print(f"Количество цифр: {digit_count}")
# print(f"Количество знаков препинания: {punctuation_count}")
# print(f"Количество восклицательных знаков: {exclamation_count}")

#
