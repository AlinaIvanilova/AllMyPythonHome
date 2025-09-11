"""Крок 69
Коли ви поєднуєте аргументи за замовчуванням з іменованими аргументами, ви можете передавати явно менше аргументів, ніж вимагає функція. Ті аргументи, які не були явно передані у виклику функції, отримають свої значення за замовчуванням.

Змініть виклик вашої функції generate_password(), щоб він приймав лише length=8."""

import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
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
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password

new_password = generate_password(length=8)
print(new_password)