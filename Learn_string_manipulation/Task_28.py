"""Крок 28
find знову повертає -1 для літер у верхньому регістрі та пробілу.
Пробілом займемося пізніше.
А зараз, ітерацію text в циклі for змінимо на ітерацію text.lower()."""

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)