def push(stack, data):
    stack.append(data)
    return True


def pop_stack(stack):
    if stack:
        return stack.pop()
    return None


def is_stack(stack):
    if stack:
        return stack
    return None


if __name__ == '__main__':
    task_stack = []

    while True:
        command = input('Введите команду (1 - add, 2 - complete, 3 - show, 4 - exit): ').strip()

        if command == '1':
            task = input("Введите задачу: ")
            push(task_stack, task)
            print(f'Задача {task} добавлена')

        elif command == '2':
            completed = pop_stack(task_stack)
            if completed:
                print(f'Задача {completed} завершена')
            else:
                print(f'Нет задач для завершения')

        elif command == '3':
            tasks = is_stack(task_stack)
            if tasks:
                print(f'Текущие задачи: {', '.join(tasks)}')
            else:
                print(f'Нет активных задач')

        elif command == '4':
            print(f'Работа завершена')
            break

        else:
            print('Неизвестная команда. Попробуйте снова.')
