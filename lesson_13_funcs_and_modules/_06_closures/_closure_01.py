def outer(par):
    loc = par
    return loc


var = 1
print(outer(var))

# print(par)
# print(loc)


def outer(par):
    loc = par

    def inner():
        return loc

    return inner


var = 1
result = outer(var)
print(result())
