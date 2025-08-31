from functools import reduce

nums_list = [i + 1 for i in range(5)]
print(nums_list)

reduce_summ = reduce(lambda x, y: x + y, nums_list)
print(reduce_summ)
reduce_product = reduce(lambda x, y: x * y, nums_list)
print(reduce_product)

reduce_summ_init = reduce(lambda x, y: x + y, nums_list, 10)
print(reduce_summ_init)
