stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

while stack:
    print(stack.pop())
else:
    print("Стек пуст, удаление невозможно.")


stack = []
if stack:
    stack.pop()
else:
    print("Стек пуст, удаление невозможно.")