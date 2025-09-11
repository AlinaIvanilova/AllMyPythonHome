"""Крок 62
Наразі all() приймає порожній список як аргумент. Заповніть цей порожній список, використавши синтаксис розуміння, щоб в списку зберігались результати обчислення виразу constraint <= len(re.findall(pattern, password)) для кожного кортежу constraint-pattern в списку constraints.

Таким чином цикл while припинить виконуватись лише тоді, коли всі умови виконано."""

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
        if all([constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints]):
            break

    return password

# new_password = generate_password(8)
# print(new_password)