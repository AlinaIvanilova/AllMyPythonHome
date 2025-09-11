"""Крок 51
Оскільки знак підкреслення є дійсним символом для назв змінних, його включено до символьного класу \w (еквівалентний [a-zA-Z0-9_]), який можна використовувати для зіставлення назв змінних.

Таким чином, символьний клас \W еквівалентний [^a-zA-Z0-9_] зі знаком підкреслення, який не збігається. З цієї причини його не можна використовувати, щоб знайти відповідність всім спеціальним символам.

Видаліть три останні рядки коду."""

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
            (special_chars, r'\W')
        ]

    return password

# new_password = generate_password(8)
# print(new_password)
