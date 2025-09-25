"""Крок 35
Трохи почистьте вивід.
Видаліть print(char, index) і замініть останній виклик print() на print('char:', char, 'new char:', new_char)."""

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    new_char = alphabet[new_index]
    print('char:', char, 'new char:', new_char)