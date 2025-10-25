def push(stack, val):
    stack.append(val)


def pop(stack):
    if stack:
        val = stack.pop()
        return val
    print('Stack is empty')
    return None


if __name__ == '__main__':
    stack1 = []
    stack2 = []
    push(stack1, 1)
    push(stack1, 2)
    push(stack1, 3)

    while stack1:
        val = pop(stack1)
        if val:
            push(stack2, val)

    print(stack2)

    print(pop(stack2))
    print(pop(stack2))
    print(pop(stack2))
    print()

    push(stack1, 1)
    push(stack1, 2)
    push(stack1, 3)
    push(stack1, 4)
    push(stack1, 5)

    for i in range(3):
        val = pop(stack1)
        if val:
            push(stack2, val)

    print(stack2)
