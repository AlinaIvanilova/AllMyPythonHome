"""Крок 36
Символьні класи також дозволяють вказати діапазон символів для відповідності. Для цього потрібно вказати початковий та кінцевий символи, розділені дефісом -. Символи дотримуються порядку Unicode.

Змініть змінну pattern, щоб вона відповідала будь-якій літері t, перед якою розташована мала літера в змінній quote. Для цього використайте діапазон символів від a до z."""

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
            (nums, '[0123456789]')
        ]

    return password

# new_password = generate_password(8)
# print(new_password)
pattern = r'[a-z]t'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))