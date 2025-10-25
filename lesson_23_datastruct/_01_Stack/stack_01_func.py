def push(val):
    stack.append(val)


def pop():
    val = stack.pop()
    return val


if __name__ == '__main__':
    stack = []
    push(3)
    push(2)
    push(1)

    print(pop())
    print(pop())
    print(pop())

