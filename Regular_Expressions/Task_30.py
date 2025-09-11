"""Крок 30
Повертається значення None, оскільки в межах аналізованого рядка не знайдено 'i'.

Тепер змініть рядок, переданий до re.compile(), на 'l' та гляньте на результат."""

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
pattern = re.compile('l')
quote = 'Not all those who wander are lost.'
print(pattern.search(quote))