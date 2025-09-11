"""Крок 9
Модуль random містить генератор псевдовипадкових чисел. Більшість його можливостей залежить від функції random(), яка повертає число з рухомою комою в діапазоні від 0.0 (включно) до 1.0 (виключно).

Викличте функцію random() з модуля random та надрукуйте результат."""

import random
import string


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)
print(random.random())