import threading
import time

counter = 0


def increase(by):
    global counter

    local_counter = counter
    local_counter += by
    time.sleep(0.5)

    counter = local_counter
    print(f'Значение counter: {counter} - ')


thread1 = threading.Thread(target=increase, args=(10,))
thread2 = threading.Thread(target=increase, args=(20,))

threads = [thread1, thread2]

thread1.start()
thread2.start()

for thread in threads:
    thread.join()

print(f'Значение counter в итоге: {counter}')
