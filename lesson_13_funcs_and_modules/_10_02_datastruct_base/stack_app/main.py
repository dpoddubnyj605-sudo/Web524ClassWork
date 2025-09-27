from ClassStack import MyStack

if __name__ == '__main__':
    task_stack = MyStack()

    while True:
        command = input('Введите команду (1 - add, 2 - complete, 3 - show, 4 - exit): ').strip()

        if command == '1':
            task = input("Введите задачу: ")
            task_stack.push(task)
            print(f'Задача {task} добавлена')

        elif command == '2':
            completed = task_stack.pop_stack()
            if completed:
                print(f'Задача {completed} завершена')
            else:
                print(f'Нет задач для завершения')

        elif command == '3':
            tasks = task_stack.is_stack()
            if tasks:
                print(f'Текущие задачи: {', '.join(tasks)}')
            else:
                print(f'Нет активных задач')

        elif command == '4':
            print(f'Работа завершена')
            break

        else:
            print('Неизвестная команда. Попробуйте снова.')
