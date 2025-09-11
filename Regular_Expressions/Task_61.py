"""Крок 61
Замість того, щоб використовувати цикл та лічильник, можна застосувати інший підхід, який ви виконаєте в наступних кроках.

all() — це вбудована функція Python, яка повертає True, якщо всі елементи в межах певного ітерованого об’єкта оцінюються як True. В іншому випадку вона повертає False.

Замініть наявний цикл for та дві інструкції if на одну інструкцію if. Для умови if використайте виклик до функції all() та передайте порожній список як аргумент до виклику функції."""

import re
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

        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, fr'[{symbols}]')
        ]


        if all([]):
            break

    return password


# new_password = generate_password(8, 1, 1, 1, 1)
# print(new_password)
