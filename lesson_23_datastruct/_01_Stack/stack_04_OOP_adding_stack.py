from stack_04_OOP import Stack


# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.stack_sum = 0
#
#     def push(self, val):
#         if isinstance(val, int) or isinstance(val, float):
#             self.stack_sum += val
#             Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.stack_sum -= val
#         return val


class AddingStack(Stack):
    def __init__(self):
        super().__init__()
        self.stack_sum = 0

    def push(self, val):
        if isinstance(val, int) or isinstance(val, float):
            self.stack_sum += val
            super().push(val)

    def pop(self):
        val = super().pop()
        if val:
            self.stack_sum -= val
        return val

    def __str__(self):
        return f'Содержимое стека: {self.stack}. Сумма значений {self.stack_sum}'


if __name__ == '__main__':
    stack = AddingStack()
    for i in range(1, 6):
        stack.push(i)
    print(f"Сумма значений стека: {stack.stack_sum}")
    for i in range(6):
        val = stack.pop()
        if val:
            print(f'Извлекли {val}. {stack}')
        else:
            break
