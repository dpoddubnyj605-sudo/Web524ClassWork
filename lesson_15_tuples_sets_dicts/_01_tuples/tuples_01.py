# my_tuple_01 = ('Cat', 'Turtle', 'Snake', 'Dog')
# my_tuple_02 = 'Cat', 'Turtle', 'Snake', 'Dog'
# print(my_tuple_01 == my_tuple_02)
#
# my_tuple_01 = ('Cat', 'Turtle', 'Snake', 'Dog')
# my_tuple_02 = 'Cat', 'Turtle', 'Dog', 'Snake'
# print(my_tuple_01 == my_tuple_02)
#
# my_tuple_03 = tuple(['Cat', 'Turtle', 'Snake', 'Dog'])
# print(my_tuple_03)
# print(type(my_tuple_03))
#
# my_tuple_04 = ('Cat',)
# my_tuple_05 = 'Cat',
# print(my_tuple_04)
# print(my_tuple_05)
#
# animal_01, animal_02, animal_03, animal_04 = my_tuple_01
# print(animal_01)
# print(animal_02)
# print(animal_03)
# print(animal_04)
# print()
#
# animal_01, animal_02 = animal_02, animal_01
# print(animal_01)
# print(animal_02)

nums_tuple_01 = (1, 2, 3)
nums_tuple_02 = (1, 2, 4)
print(nums_tuple_01 < nums_tuple_02)

nums_tuple_01 = (1, 2, 3)
nums_tuple_02 = (1, 2, 3, 0)
print(nums_tuple_01 < nums_tuple_02)

nums_tuple_01 = (1, 3, 1)
nums_tuple_02 = (1, 2, 3, 1)
print(nums_tuple_01 > nums_tuple_02)

my_tuple_1 = ('Cat', 'Dog')
my_tuple_2 = ('Cat', 'Parrot')
print(my_tuple_1 < my_tuple_2)

animals_tuple_1 = ('Cat', 'Turtle', 'Snake', 'Dog')
animals_tuple_2 = 'Cat', 'Turtle', 'Snake', 'Dog', 'Parrot'
print(animals_tuple_1 < animals_tuple_2)

# my_tuple_1 = (1, 2, 3)
# my_tuple_2 = ('Cat', 'Parrot')
# print(my_tuple_1 < my_tuple_2)
