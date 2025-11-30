import threading

# Общая переменная, которую будем изменять
counter = 0
# Создаём Lock для синхронизации
lock = threading.Lock()


def increment():
    global counter
    for _ in range(100000):
        with lock:  # Блокируем доступ к counter
            counter += 1


if __name__ == '__main__':
    threads = [threading.Thread(target=increment) for i in range(5)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Counter value: {counter}')
