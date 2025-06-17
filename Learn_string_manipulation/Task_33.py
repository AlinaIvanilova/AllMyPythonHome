"""Крок 33
Тепер вам потрібно створити змінну new_char у кінці тіла циклу.
Встановіть її значення на alphabet[new_index]."""
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift
    new_char = alphabet[new_index]