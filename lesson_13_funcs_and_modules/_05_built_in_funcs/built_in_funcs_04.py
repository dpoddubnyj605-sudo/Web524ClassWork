def get_evens(nums_list):
    evens_list = []
    for num in nums_list:
        if num % 2 == 0:
            evens_list.append(num)
    return evens_list


if __name__ == '__main__':
    new_list = list(range(8 + 1))
    print(get_evens(new_list))
    filtered_nums = list(filter(lambda x: x % 2 == 0, new_list))
    print(filtered_nums)
