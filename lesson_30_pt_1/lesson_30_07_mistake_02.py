"""
Тип ошибки 2: Некорректное использование asyncio.run

Ошибка возникает, когда asyncio.run вызывается внутри другой корутины.

Пример ошибки:
"""
import asyncio


# async def my_coroutine():
#     print("Start")
#     await asyncio.sleep(1)  # Правильно: используем await
#     print("End")
#
#
#
# async def main():
#     asyncio.run(my_coroutine())
#
# asyncio.run(main())

"""
Решение:
"""


async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)  # Правильно: используем await
    print("End")


async def main():
    await my_coroutine()  # Правильно: используем await


asyncio.run(main())
