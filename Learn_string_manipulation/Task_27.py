"""Крок 27
Наразі функція print() приймає один аргумент char, але вона може приймати кілька аргументів, розділених комою.

Додайте другий аргумент до print(char), щоб функція друкувала символ та його індекс в межах alphabet."""

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in text:
    index = alphabet.find(char)
    print(char, index)