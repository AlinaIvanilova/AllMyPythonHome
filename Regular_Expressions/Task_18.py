"""Крок 18
Окремий знак підкреслення використовують для представлення значення, яке вам байдуже або яке не використовуватиметься у коді. Змінна ітерації фактично не використовується.

Змініть змінну i на знак підкреслення."""

import secrets
import string


def generate_password(length):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    password = ''
    # Generate password
    for _ in range(length):
        password += secrets.choice(all_characters)
