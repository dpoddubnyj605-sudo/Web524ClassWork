squares = (x ** 2 for x in range(5))
print(next(squares))
print(next(squares))
print(next(squares))
print(list(squares))

squares_dict = {f"{x}": x ** 2 for x in range(6)}
print(squares_dict)

squares_set = {x ** 2 for x in range(6)}
print(squares_set)

even_numbers = [x for x in range(11) if x % 2 == 0]
print(even_numbers)

odd_squares_dict = {x: x for x in range(11) if x % 2 != 0}
print(odd_squares_dict)
