"""Крок 18
Видаліть останній виклик print().
Потім передайте text[0].lower() (замість text[0]) як аргумент до виклику .find() і перегляньте результат."""
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)


