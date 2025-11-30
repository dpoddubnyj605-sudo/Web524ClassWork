import threading

counter = 0


def increment():
    global counter
    for _ in range(100000):
        counter += 1


if __name__ == '__main__':
    threads = [threading.Thread(target=increment) for i in range(5)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Counter value: {counter}')
