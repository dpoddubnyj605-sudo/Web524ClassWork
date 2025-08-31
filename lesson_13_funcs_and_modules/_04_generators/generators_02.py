def count_to_limit(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1


if __name__ == '__main__':
    for number in count_to_limit(6):
        print(number)
