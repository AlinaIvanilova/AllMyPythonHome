"""Крок 23
Далі ви надасте функції більше параметрів, які діятимуть як обмеження для згенерованого пароля.

Змініть оголошення функції, додавши nums, special_chars, uppercase та lowercase (в такому ж порядку) після наявного параметра length."""

import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
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

    return password

# new_password = generate_password(8)
# print(new_password)