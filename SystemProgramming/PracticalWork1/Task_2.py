"""Завдання 2. Створіть програму, яка запускає кілька асинхронних задач, що працюють випадковий час від 0.1 до 3 секунд. Реалізувати це можна за допомогою функції uniform з модуля random.
Використайте asyncio.wait_for() та конструкцію try/except, щоб обмежити загальний час виконання до 2 секунд. Якщо задачі не встигли завершитись – обробіть виняток asyncio.TimeoutError і виведіть повідомлення про перевищення часу.
"""
import asyncio
import random


async def wait_random_time(chas):
    sleep_time = random.uniform(0.1, 3)
    print(f"Робота {chas} почалася і працюватиме {sleep_time} секунд.")
    await asyncio.sleep(sleep_time)
    print(f"Робота {chas} закінчилася")
    return chas

async def main():
    tasks = [wait_random_time(i) for i in range(1, 6)]

    try:
        results = await asyncio.wait_for(asyncio.gather(*tasks), timeout=2)
        print("результат:", results)
    except asyncio.TimeoutError:
        print("Час виконання перевищено більше ніж 2 секунди")

if __name__ == "__main__":
    asyncio.run(main())