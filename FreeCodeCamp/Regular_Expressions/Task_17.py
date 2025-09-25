"""Крок 17
Далі напишіть цикл for з i як змінною циклу. Використайте функцію range(), щоб ітерувати над значенням length.

В межах циклу використайте оператор додавання з присвоєнням, щоб додати випадковий символ з all_characters до поточного значення password.
Для цього використайте функцію choice() з модуля secrets."""

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
    for i in range(length):
        password += secrets.choice(all_characters)