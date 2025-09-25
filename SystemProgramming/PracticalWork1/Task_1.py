"""
def work(): - звичайна синхронна функ.
async def work(): - асинхронна функ

time.sleep(2) - звичайна пауза, через що програма зупиняється на 2 секунди і нічого не відбувається
await asyncio.sleep(2) - асинхронна пауза, ця задача зупиняється на 2 секунди але інші асинхронні задачі можуть працювати в цей час

"""
import asyncio
import random
import time

async def work_with_random_seconds():
    random_number = random.randint(1, 3)
    await asyncio.sleep(random_number)
    print(f"Все завершено протягом {random_number} секунд")

#asyncio.run(work_with_random_seconds())

async def func():
    begin_time = time.time()
    for _ in range(5):
        await work_with_random_seconds()
    end_time = time.time()
    print("Послідовно:", end_time - begin_time, "секунд")

#asyncio.run(func())

async def func2():
    begin_time = time.time()
    just_simple_zmin = [work_with_random_seconds() for _ in range(5)]
    await asyncio.gather(*just_simple_zmin)
    end_time = time.time()
    print("Конкурентно:", end_time - begin_time, "секунд")

#asyncio.run(func2())


"""Завдання 1. Напишіть асинхронну функцію, яка імітує виконання роботи протягом випадкового часу від 1 до 3 секунд та виводить повідомлення про завершення. 
Створіть програму, яка: запускає 5 таких функцій послідовно та вимірює час виконання; запускає 5 таких функцій конкурентно (одночасно) за допомогою asyncio.gather та порівнює час із послідовним виконанням."""