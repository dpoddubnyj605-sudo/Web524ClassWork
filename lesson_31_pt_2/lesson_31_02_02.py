from multiprocessing import Process
import time


def long_task():
    print('Процесс начал работу.')
    time.sleep(10)
    print('Процесс завершил работу.')


if __name__ == '__main__':
    process = Process(target=long_task)
    process.start()

    # Проверяем, работает ли процесс
    time.sleep(2)
    if process.is_alive():
        user_choice = input('Процесс все еще работает. Прерываем его? (1 - да, 2 - нет): ')
        if user_choice == '1':
            process.terminate()
            print(f'Процесс принудительно завершен')
        else:
            print(f'Процесс продолжает работу.')

    process.join()
    print(f'Работа завершена.')
