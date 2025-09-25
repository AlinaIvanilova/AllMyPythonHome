"""Крок 42
Символ крапки — це байдужий символ, який відповідає будь-якому символу в рядку, крім символу нового рядка за замовчуванням. Змініть pattern так, щоб вона відповідала всьому рядку, замінивши поточний шаблон на символ ., після якого напишіть квантор +."""

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
            (nums, '[0-9]'),
            (lowercase, '[a-z]'),
            (uppercase, '[A-Z]'),
            (special_chars, '')
        ]

    return password

# new_password = generate_password(8)
# print(new_password)
pattern = '.+'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))