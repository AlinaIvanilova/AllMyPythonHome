"""Крок 26
Кортеж — ще одна вбудована структура даних у Python. Кортежі дуже схожі на списки, але їх визначають за допомогою круглих дужок (), а не квадратних. Крім того, кортежі незмінні, на відміну від списків.

Приклад коду
my_tuple = ('larch', 1, True)
Список constraints зберігатиме кортежі. Перший елемент кожного кортежу буде параметром обмеження.

Змініть присвоєння списку constraints, додавши кортеж до списку. Використайте nums як перший елемент та порожній рядок як другий елемент."""

import secrets
import string


def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        constraints = [(nums, '')]

    return password

# new_password = generate_password(8)
# print(new_password)