"""Крок 13
Оголосіть функцію generate_password та запишіть увесь код, окрім рядків import, в межах тіла функції."""

import secrets
import string


def generate_password():
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols