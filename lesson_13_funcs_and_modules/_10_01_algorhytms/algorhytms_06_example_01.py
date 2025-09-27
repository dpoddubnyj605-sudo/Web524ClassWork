def insertion_sort(grades_list):
    for i in range(1, len(grades_list)):
        key = grades_list[i]
        j = i - 1
        while j >= 0 and key < grades_list[j]:
            grades_list[j + 1] = grades_list[j]
            j -= 1
        grades_list[j + 1] = key
    return grades_list


if __name__ == '__main__':
    # grades_input = input("Введите оценки учеников через пробел")
    # my_grades_list = [int(grade) for grade in grades_input.split()]

    my_grades_list = [7, 4, 6, 5, 4, 8, 9, 2, 3]
    sorted_grades = insertion_sort(my_grades_list)
    print(f'Отсортированные оценки: {sorted_grades}')

    # [7, 4, 6, 5, 4, 8, 9, 2, 3] - 4
    # [4, 7, 6, 5, 4, 8, 9, 2, 3] - 7
    # [4, 6, 7, 5, 4, 8, 9, 2, 3] - 6
    # [4, 5, 6, 7, 4, 8, 9, 2, 3] - 5
