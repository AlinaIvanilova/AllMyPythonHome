"""Крок 12
Although the effect might seem equal to random.choice(), secrets ensures you the most secure source of randomness that your operating system can provide.

Тепер видаліть обидва виклики print()."""

import secrets
import string


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols
