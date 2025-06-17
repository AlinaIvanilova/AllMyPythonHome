"""Крок 26
Усередині циклу for, перш ніж друкувати поточний символ, оголосіть змінну під назвою index і призначте їй значення, яке повертає alphabet.find(char).
"""
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in text:
    index = alphabet.find(char)
    print(char)