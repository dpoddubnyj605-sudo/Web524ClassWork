def find_longest_word(*args):
    leader = ""

    for word in args:
        if len(word) > len(leader):
            leader = word
    return leader


print(find_longest_word('Python', 'Java', 'Программирование'))


def remove_from_string(string, *args):
    for symbol in args:
        string = string.replace(symbol, '')
    return string


print(remove_from_string('О! Смотри, можно удалить - все знаки препинания сразу!', '?', "!", ",", '.', "-"))



