"""Крок 6
Змінна all_characters — це рядок, який складається з всіх малих та великих літер, 10 цифр та декількох спеціальних символів.

Додайте коментар Combine all characters одразу перед нею."""

import string


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

#Combine all characters
all_characters = letters + digits + symbols