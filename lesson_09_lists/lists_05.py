# category_list = ["Drama", "Comedy", "Fantasy"]
# print(category_list[0])
# print(category_list[1])
# print(category_list[2])
# # print(category[3])
# category_01 = category_list[0]
# print(category_01)

category_list = ["Drama", "Comedy", "Fantasy", "Action", "Scy-Fy"]
nums_list = [3, 1, 2, 11, 25]

print(len(category_list), len(nums_list))
print(max(category_list), max(nums_list))
print(min(category_list), min(nums_list))
# [0-9A-Za-zА-Яа-я]
print(sum(nums_list))

sorted_strings = sorted(category_list)
sorted_nums = sorted(nums_list)
print(sorted_strings)
print(sorted_nums)
print(category_list)
print(nums_list)

sorted_strings_rev = sorted(category_list, reverse=True)
sorted_nums_rev = sorted(nums_list, reverse=True)
print(sorted_strings_rev)
print(sorted_nums_rev)

