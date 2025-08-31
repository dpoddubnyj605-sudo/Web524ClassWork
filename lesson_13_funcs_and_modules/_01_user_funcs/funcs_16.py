def display_my_space_address(*args, **kwargs):
    if args:
        for item in args:
            print(item)
    if kwargs:
        for key, value in kwargs.items():
            print(f'{key}: {value}')


if __name__ == '__main__':
    display_my_space_address('Дмитрий', 36, planet='Земля', star='Солнце')
