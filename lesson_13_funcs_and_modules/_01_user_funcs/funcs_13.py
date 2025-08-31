import string as sm


def remove_from_string(string, *args):
    for symbol in args[0]:
        string = string.replace(symbol, '')
    return string


print(remove_from_string('О! Смотри, можно удалить - все знаки препинания сразу!', sm.punctuation))
