class Car:
    __wheels = 4

    def __init__(self, brand, color, doors):
        self.brand = brand
        self.color = color
        self.doors = doors

    def drive(self):
        print(f'Автомобиль {self.brand}. Цвет {self.color}. Двери {self.doors} едет!')

    def change_doors_quantity(self, doors_new_quantity):
        if Car.check_int_data_type(doors_new_quantity):
            self.doors = doors_new_quantity

    @classmethod  # что для работы с @classmethod вместо self используем cls везде в теле данного метода
    def describe(cls):
        print(f'Легковые автомобили имеют {cls.__wheels} колеса')

    @classmethod
    def change_wheels_quantity(cls, wheels_num):
        if cls.check_int_data_type(wheels_num):
            cls.__wheels = wheels_num

    @staticmethod
    # Если не используются атрибуты (класса или экземпляра) используем >> @staticmethod
    # Вызов через self или объект не вызывает ошибку, но это плохой код поэтому вызываем его через класс
    def general_info():
        print('Машины - это транспортные средства.')

    @staticmethod
    def check_int_data_type(wheels):
        if isinstance(wheels, int):
            return True
        raise ValueError('Данные могут быть только целым числом')


if __name__ == '__main__':
    car = Car('Toyota', 'красный', 4)
    car.drive()
    Car.describe()
    Car.general_info()
    Car.change_wheels_quantity(6)
    Car.describe()
    car.drive()
    car.change_doors_quantity(2)
    car.drive()

    car.wheels = 4
    # присваиваем новый (неожиданный) атрибут к конкретному объекту
    # (и теперь он отличается от остальных, что может далее вызвать проблемы)
    # не делайте так! Это не меняет значение атрибута класса,
    # если нужно изменить атрибут класса меняйте его через класс (или @classmethod) если он предусмотрен.
    print(car.__dict__)
    Car.describe()
    car2 = Car('Honda', 'синий', 4)
    print(car2.__dict__)
    # Car.change_wheels_quantity(6.5)
    # car.change_doors_quantity(2.5)
