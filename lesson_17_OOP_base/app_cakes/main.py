from Classes.ClassCake import CakeForm

if __name__ == '__main__':
    cake_01 = CakeForm('Пшеничное', 'Круглая', 'Ром', 'Марципан')
    print(cake_01.make_dough())
    print(cake_01.make_form())
    print(cake_01.add_ingredient("Изюм"))
    print(cake_01.add_ingredients('Курага', 'Чернослив'))
    print()
    print(cake_01.cook_cake())
    print(cake_01.cook_cake(100))
    print()

    cake_2 = CakeForm('Овсяное', 'Квадратная')
    print(cake_2.make_dough())
    print(cake_2.make_form())
    print(cake_2.cook_cake())
    print(cake_2.cook_cake(100))
