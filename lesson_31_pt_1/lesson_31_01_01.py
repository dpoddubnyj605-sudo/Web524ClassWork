import threading
import time


def print_numbers():
    for i in range(10):
        print(f'Number: {i}')
        time.sleep(1.0)


if __name__ == '__main__':
    # Создаём поток
    thread = threading.Thread(target=print_numbers)
    thread.start()

    # Основной поток продолжает выполнять свои задачи
    print("Поток запущен!")
    # user_input = input("Введите, что-нибудь: ")

    # Ждем пока завершится поток
    thread.join()
    print("Поток завершен")
