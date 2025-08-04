# my_string = "Hello World! Hello Python!"
# number_of_o_elements = my_string.count('o')
# print(number_of_o_elements)
#
# number_of_o_elements = my_string.count('o', 7, 16)
# print(number_of_o_elements)
#
# number_of_Hello_elements = my_string.count('Hello')
# print(number_of_Hello_elements)
#
# number_of_hello_elements = my_string.lower().count('hello')
# print(number_of_hello_elements)

# my_string = "Hello World! Hello Python!"
# element_index = my_string.find('W')
# print(element_index)
# element_index = my_string.find('Python')
# print(element_index)
# element_index = my_string.find('Yello')
# print(element_index)
# element_index = my_string.find('Hello', 10, 20)
# print(element_index)
#
# my_string = "Hello World! Hello Python! Hello Guido!"
# element_index = my_string.rfind('e')
# print(element_index)
# element_index = my_string.rfind('Hello')
# print(element_index)
# element_index = my_string.rfind('Yello')
# print(element_index)
# element_index = my_string.rfind('Hello', 10, 20)
# print(element_index)

my_string = "Hello World! Hello Python!"
element_index = my_string.index('W')
print(element_index)
element_index = my_string.index('Python')
print(element_index)
# element_index = my_string.index('Yello')
# print(element_index)
element_index = my_string.index('Hello', 10, 20)
print(element_index)

my_string = "Hello World! Hello Python! Hello Guido!"
element_index = my_string.rindex('e')
print(element_index)
element_index = my_string.rindex('Hello')
print(element_index)
# element_index = my_string.rindex('Yello')
# print(element_index)
element_index = my_string.rindex('Hello', 10, 20)
print(element_index)
