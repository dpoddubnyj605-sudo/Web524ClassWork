even_square_list = [i * i for i in range(10) if i % 2 == 0]
print(even_square_list)

even_square_list_simple = []
for i in range(10):
    if i % 2 == 0:
        even_square_list_simple.append(i * i)
print(even_square_list_simple)
print()

customers = ["Bob", "Joe", "Anna", "Bob", "Nick"]
customers_filtered = [customer for customer in customers if customer != 'Bob' and customer != 'Joe']
print(customers_filtered)

customers = ["Bob", "Joe", "Anna", "Bob", "Nick"]
customers_filtered_simple = []
for customer in customers:
    if customer != 'Bob' and customer != 'Joe':
        customers_filtered_simple.append(customer)
print(customers_filtered_simple)
print()
# def my_sum(a, b):
#     return a + b
#
#
# print(my_sum(a=3, b=5))  # a = 3, b = 5

product_list = [i * j for i in range(1, 4) for j in range(1, 5)]
print(product_list)

product_list_simple = []
for i in range(1, 4):
    for j in range(1, 5):
        product_list_simple.append(i * j)
print(product_list_simple)

my_matrix = [[i * j for i in range(1, 4)] for j in range(1, 5)]
print(my_matrix)

my_matrix_simple = []
for j in range(1, 5):
    inside_list = []
    for i in range(1, 4):
        inside_list.append(i * j)
    my_matrix_simple.append(inside_list)
print(my_matrix_simple)

my_matrix_simple = [
    ["Петр", 11, 12],
    ["Иван", 10, 8],
    ["Дмитрий", 9, 11],
]
print()

for name, mark1, mark2 in my_matrix_simple:
    print(f'Имя: {name}. оценка 1: {mark1}. Оценка 2: {mark2}')
    print()
