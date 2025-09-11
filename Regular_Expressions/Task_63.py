"""Крок 63
Наявність all([expression for i in iterable]) означає, що новий список створений шляхом оцінення expression кожної i в iterable. Після того, як функція all() ітерує над щойно створеним списком, список автоматично видаляється, оскільки він більше не потрібний.

Пам’ять можна зберегти за допомогою виразу генератора. Вирази генератора дотримуються синтаксису розуміння списків, але вони використовують круглі дужки замість квадратних.

Змініть розуміння списку на вираз генератора, видаливши квадратні дужки."""

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

        # Check constraints
        count = 0
        if all(

                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints

        ):
            break

    return password

# new_password = generate_password(8)
# print(new_password)