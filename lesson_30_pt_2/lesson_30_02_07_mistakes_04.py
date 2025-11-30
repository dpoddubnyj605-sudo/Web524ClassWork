"""
Тип ошибки 4: Отсутствие await перед asyncio.gather

Возникает при отсутствии await перед вызовом gather.
"""
# import asyncio
#
#
# async def task():
#     await asyncio.sleep(1)
#
#
# async def main():
#     asyncio.gather(task(), task())  # Нет await, задачи не выполнятся
#
#
# asyncio.run(main())
"""
Решение:

всегда используем await с gather.
"""

import asyncio


async def task():
    await asyncio.sleep(1)


async def main():
    await asyncio.gather(task(), task())


asyncio.run(main())
