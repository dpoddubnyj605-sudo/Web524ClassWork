import asyncio


async def my_coroutine(task_num, delay):
    print(f'Start {task_num}')
    await asyncio.sleep(delay)
    print(f'End {task_num}')


async def main():
    # Создаём таску из корутины
    task1 = asyncio.create_task(my_coroutine(1, 3))
    task2 = asyncio.create_task(my_coroutine(2, 1))

    # Ждём завершения таски
    await task1
    await task2


if __name__ == '__main__':
    asyncio.run(main())
