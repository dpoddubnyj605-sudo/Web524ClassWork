def display_my_space_address_all_params(name, age=35, city=None, *args, **kwargs):
    print(name)
    print(age)
    if city:
        print(city)
    else:
        print('город не указан')
    if args:
        for item in args:
            print(item)
    if kwargs:
        for key, value in kwargs.items():
            print(f'{key}: {value}')


if __name__ == '__main__':
    display_my_space_address_all_params('Dmitry', 36, 'Minsk', 'Belarus', 'Eastern Europe', planet='Earth', star='Sun')
    print()
    display_my_space_address_all_params('Dmitry', planet='Earth', star='Sun')

