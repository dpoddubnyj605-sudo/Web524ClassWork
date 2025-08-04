def display_personal_data(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['surname'])
    print(kwargs['age'])
    print(kwargs['phone'])


display_personal_data(name="Иван", surname='Иванов', age=35, phone="+7(901)1234567")
