my_animals = {'Cat', 'Dog', 'Snake'}
shop_animals = {'Cat', 'Turtle', 'Snake'}
wild_animals = {'Fox', 'Owl', 'Snake'}

same_animals_1 = my_animals.intersection(shop_animals)
print(same_animals_1)
same_animals_2 = my_animals.intersection(shop_animals).intersection(wild_animals)
print(same_animals_2)
shop_animals_3 = my_animals & shop_animals
print(shop_animals_3)
print()

my_animals = {'Cat', 'Dog', 'Snake'}
shop_animals = ['Cat', 'Turtle', 'Snake']
wild_animals = ('Fox', 'Owl', 'Snake')
same_animals_4 = my_animals.intersection(shop_animals).intersection(wild_animals)
print(same_animals_4)
