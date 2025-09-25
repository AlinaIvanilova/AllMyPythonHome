"""Крок 8
Загальноприйнятою практикою є розміщувати інструкції import на початку вашого коду. Крім того, якщо є декілька інструкцій import, відсортуйте їх в алфавітному порядку для покращення читабельності.

На початку вашого коду імпортуйте модуль random."""

import string
import random

# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)
