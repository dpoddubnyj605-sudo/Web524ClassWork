import asyncio


async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("Done")
    return "Result"


async def main():
    task = asyncio.create_task(my_coroutine())

    # Проверяем, завершена ли таска
    print(f'Task done: {task.done()}')

    # Ждем завершения
    await task

    print(f'Task done: {task.done()}')
    result = task.result()
    print(f'Task result: {result}')


if __name__ == '__main__':
    asyncio.run(main())
