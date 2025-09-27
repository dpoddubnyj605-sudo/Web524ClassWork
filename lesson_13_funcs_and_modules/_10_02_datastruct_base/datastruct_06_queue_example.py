from collections import deque


def enqueue(queue, data):
    queue.append(data)
    return True


def dequeue(queue):
    if queue:
        data = queue.popleft()
        return data
    return None


def queue_data(queue):
    if queue:
        return list(queue)
    return None


if __name__ == '__main__':
    shop_queue = deque()
    while True:
        command = input('Введите команду: 1 - add, 2 - serve, 3 - show, 4 - exit: ').strip()

        if command == '1':
            customer = input('Введите имя покупателя: ')
            enqueue(shop_queue, customer)
            print(f'Покупатель {customer} добавлен в очередь')

        elif command == '2':
            served = dequeue(shop_queue)
            if served:
                print(f'Покупатель {served} обслужен')
            else:
                print(f'В очереди нет покупателей')

        elif command == '3':
            customers = queue_data(shop_queue)
            if customers:
                print(f'Текущая очередь: {', '.join(customers)}')
            else:
                print(f'Очередь пуста.')

        elif command == '4':
            print('Работа завершена')
            break

        else:
            print(f'Неизвестная команда, попробуйте еще раз.')
