"""Крок 28
Регулярний вираз — це шаблон, який використовується для відповідності певній комбінації символів у рядку. Це дійсна альтернатива умовним інструкціям if/else, якщо потрібно зіставити або знайти шаблони в межах рядка з метою валідації, заміни символів тощо.

Функція compile() з модуля re компілює рядок, переданий як аргумент до об’єкта регулярного виразу, який можуть використовувати інші методи re.

Оголосіть нову змінну pattern та призначте до неї значення re.compile('i')."""

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
            (nums, '')
        ]

    return password

# new_password = generate_password(8)
# print(new_password)
pattern = re.compile('i')