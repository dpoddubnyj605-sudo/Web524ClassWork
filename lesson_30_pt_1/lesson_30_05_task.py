import asyncio
from datetime import datetime


async def fetch_data(task_id, delay):
    print(f'Task {task_id} started')
    await asyncio.sleep(delay)
    print(f'Task {task_id} finished')
    return f'Data from task {task_id}'


async def main():
    print(datetime.now())

    tasks = [
        asyncio.create_task(fetch_data(1, 3)),
        asyncio.create_task(fetch_data(2, 1)),
        asyncio.create_task(fetch_data(3, 2))
    ]

    results = []
    for task in tasks:
        await task
        results.append(task.result())

    print(results)
    print(datetime.now())


# async def main():
#     tasks = [
#         fetch_data(1, 2),
#         fetch_data(2, 1),
#         fetch_data(3, 3)
#     ]
#     task_list = []
#     task_results = []
#
#     for task in tasks:
#         t = asyncio.create_task(task)
#         task_list.append(t)
#
#     for task in task_list:
#         await task
#         task_results.append(task.result())
#
#     print(task_results)

if __name__ == '__main__':
    asyncio.run(main())
