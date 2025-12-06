from multiprocessing import Process, Queue
import time


# Функция, которая вычисляет квадрат числа и отправляет результат в очередь
def compute_square(x, queue):
    print(f'Процесс {x}: вычисление квадрата {x}')
    result = x ** 2
    queue.put(result)
    time.sleep(2)


if __name__ == '__main__':
    queue = Queue()
    processes = []
    for i in range(1, 4):
        process = Process(target=compute_square, args=(i, queue,))
        processes.append(process)

    for process in processes:
        process.start()

    time.sleep(1)
    print(f'Расчет в процессе....')

    for process in processes:
        process.join()

    # Главный процесс забирает и выводит результаты из очереди
    print("\nРезультаты вычислений:")
    while not queue.empty():
        result = queue.get()  # Получаем результат из очереди
        print(f"Результат: {result}")

    print("Все процессы завершены.")
