my_animals = {'Cat', 'Parrot', 'OwL'}
shop_animals = {'Turtle', 'Parrot', 'Rat'}
shelter_animals = {'Dog', 'Cat'}

pets_in_shop_not = shop_animals.difference(my_animals)
pets_both = my_animals.intersection(shelter_animals)
pets_only = my_animals.difference(shop_animals.union(shelter_animals))
all_pets = my_animals.union(shop_animals, shelter_animals)

print("Результаты анализа:")
print(f"1. {pets_in_shop_not}")
print(f"2. {pets_both}")
print(f"3. {pets_only}")
print(f"4. {all_pets}")