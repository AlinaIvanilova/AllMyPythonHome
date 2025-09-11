"""Крок 27
Модуль re дозволяє використовувати регулярні вирази в коді. Незабаром ви дізнаєтеся більше про регулярні вирази.

Наразі додайте інструкцію import у верхній частині коду, щоб імпортувати модуль re."""

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