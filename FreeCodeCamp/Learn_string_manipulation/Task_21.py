"""Крок 21
Як бачите з результату, 'h' в рядку alphabet має індекс 7.
Тепер вам потрібно знайти літеру за індексом 7 плюс значення shift.
Для цього можна використати оператор додавання +, так само як і в математичному додаванні.

Змініть змінну shifted, щоб вона зберігала значення alphabet за індексом index + shift."""

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index + shift]
print(shifted)