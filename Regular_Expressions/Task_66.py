"""Крок 66
Це працює, але ще є кілька моментів, які можна покращити. Перш за все, виклик функції з 5 аргументами може створювати плутанину щодо того, яке значення буде призначене якому параметру.

Ви можете викликати функцію, використовуючи іменовані аргументи — тобто явно вказуючи назву параметра, після чого знак присвоєння та значення. Наприклад:

def add(x, y):
    return x + y

add(x=1, y=7) # 8


Змініть виклик вашої функції так, щоб використовувати іменовані аргументи"""

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

new_password = generate_password(length=8, nums=1, special_chars=1, uppercase=1, lowercase=1)
print(new_password)