"""Крок 44
Python надає певний тип рядка, який називають необробленим рядком. Необроблені рядки мають префікс r. Ключова відмінність від звичайних рядків полягає в тому, як вони обробляють символ оберненої скісної риски: в необроблених рядках вони розглядаються як буквальні символи, а не символи екранування. Під час написання регулярних виразів добре використовувати необроблені рядки, оскільки зазвичай вони можуть містити багато символів \.

Перетворіть рядок pattern на необроблений рядок, додавши до нього префікс r."""

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
pattern = r'\.'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))