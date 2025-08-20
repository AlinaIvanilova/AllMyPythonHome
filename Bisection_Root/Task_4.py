"""Крок 4
Інструкція raise дозволяє видати конкретний виняток. Вона складається з ключового слова raise, після якого вказано тип винятку, та дозволяє надати власне повідомлення для користувача:

Приклад коду
raise ValueError("Invalid value")
Коли код вище запускається, виникає помилка ValueError, а користувачу відтворюється повідомлення "Invalid value".

Якщо square_target менше за 0, неможливо обчислити дійснозначний корінь. Тому має виникнути помилка ValueError з повідомленням 'Square root of negative number is not defined in real numbers'. Не забудьте видалити ключове слово pass."""


def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
