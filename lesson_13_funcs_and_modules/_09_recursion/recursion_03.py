def count_workers(sp):
    res = 0
    for item in sp:
        if isinstance(item, int):
            res += item
        else:
            res += count_workers(item)
    return res


if __name__ == '__main__':
    emp_angola = 18
    emp_new_york = [20, [10, 7]]
    emp_chicago = 15
    emp_usa = [emp_new_york, emp_chicago]
    emp_all = [emp_angola, emp_usa]
    print(emp_all)
    print(count_workers(emp_all))
