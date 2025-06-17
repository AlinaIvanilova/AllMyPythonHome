"""Крок 65
Метод .index() ідентичний методу .find(), але він створює виняток ValueError, якщо не вдається знайти підрядок.

ValueError — це вбудований виняток, який виникає, якщо до функції передано аргумент правильного типу, але неприйнятного значення.
я збільшення key_index, оголосіть змінну з назвою offset. Знайдіть індекс, який має key_char в алфавіті, і присвойте його змінній offset.Використайте метод .index() для знаходження індексу.
Після збільшення `key_index`, оголосіть змінну з назвою `offset`. Знайдіть індекс, який має `key_char` в алфавіті, і присвойте його змінній `offset`. Використайте метод `.index()` для знаходження індексу.
"""


text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():

        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)
