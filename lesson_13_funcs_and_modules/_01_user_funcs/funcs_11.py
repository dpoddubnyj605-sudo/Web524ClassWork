# print(sum([1, 2, 3, 4]))

def new_sum(*args):
    print(args)
    print(type(args))
    args_list = list(args)
    sum_ = 0

    for num in args_list:
        if type(num) is int or type(num) is float:
            sum_ += num
        else:
            continue
    return sum_


print(new_sum(2, 3, 4, 5, "a", 6, 7, 8, 9))
print(new_sum())
