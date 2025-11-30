import asyncio
import random
from datetime import datetime


async def fetch_data(api_id):
    print(f'Запрос к API {api_id} начат.')
    sleep_time = random.randint(1, 3)
    await asyncio.sleep(sleep_time)
    print(f'Запрос к API {api_id} завершен, время запроса {sleep_time} секунд')
    return f'Данные {api_id}'


async def main():
    print(datetime.now())
    tasks = [fetch_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    print(f'Все запросы выполнены: {', '.join(results)}')
    print(datetime.now())


# async def main_step():
#     print(datetime.now())
#     result1 = await fetch_data(1)
#     result2 = await fetch_data(2)
#     result3 = await fetch_data(3)
#     print(f'Все запросы выполнены')
#     print(f'Результаты {', '.join([result1, result2, result3])}')
#     print(datetime.now())


if __name__ == '__main__':
    asyncio.run(main())
    # asyncio.run(main_step())
