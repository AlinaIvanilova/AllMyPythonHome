"""Крок 10
Функція choice() з модуля random приймає послідовність та повертає випадковий елемент послідовності.

Змініть виклик print(), щоб використовувати функцію choice() та передайте all_characters як аргумент."""

import random
import string


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)
print(random.choice(all_characters))