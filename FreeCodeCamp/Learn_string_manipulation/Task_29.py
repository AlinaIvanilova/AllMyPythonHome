"""Крок 29
В кінці тіла циклу оголосіть змінну під назвою new_index та призначте до неї значення index + shift."""

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)
    new_index = index + shift