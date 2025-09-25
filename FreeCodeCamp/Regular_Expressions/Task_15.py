"""Крок 15
У кінці вашої функції оголосіть змінну password і присвойте їй порожній рядок."""
import secrets
import string


def generate_password(length):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    password = ""