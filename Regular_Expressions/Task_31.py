"""Крок 31
Як можете побачити з вихідних даних, тепер регулярний вираз відповідає першому l в рядку.

Після символу в шаблоні можна додати квантор, щоб вказати, скільки разів цей символ має повторюватись. Наприклад, квантор + означає, що символ має повторюватися один або більше разів.

Додайте квантор + до шаблону."""

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
pattern = re.compile('l+')
quote = 'Not all those who wander are lost.'
print(pattern.search(quote))