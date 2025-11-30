import threading
import queue


# Функция для обработки файла
def process_file(q, result, lock):
    while not q.empty():
        file_path = q.get()
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                line_count = len(lines)

            with lock:
                result['total_lines'] += line_count
                result['file_results'][file_path] = line_count

            print(f'Обработан файл {file_path}: {line_count} строк.')

        except Exception as ex:
            print(f"Ошибка в обработке файла {file_path}: {ex}")

        finally:
            q.task_done()


def main():
    file_paths = [
        r'files\file1.txt',
        r'files\file2.txt',
        r'files\file3.txt',
    ]

    # Очередь задач
    task_queue = queue.Queue()

    # Заполняем очередь задачами (путями к файлам)
    for path in file_paths:
        task_queue.put(path)

    result = {
        'total_lines': 0,
        'file_results': {}
    }

    result_lock = threading.Lock()

    num_threads = 3
    threads = [
        threading.Thread(target=process_file, args=(task_queue, result, result_lock)) for _ in range(num_threads)
    ]

    for thread in threads:
        thread.start()

    task_queue.join()

    print(f'\nРезультат')
    for file_path, line_count in result['file_results'].items():
        print(f'{file_path}: {line_count} строк')
    print(f'Всего строк: {result['total_lines']}')


if __name__ == '__main__':
    main()
