"""Крок 14
Функція generate_password потребує декількох параметрів. Для початку додайте параметр length."""

import secrets
import string


def generate_password(length):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
