"""Крок 19
Оголосіть нову змінну shifted.
Використайте дужкову нотацію, щоб отримати доступ до значення змінної alphabet за індексом index та призначте його до нової змінної."""
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index]

