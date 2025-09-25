"""Крок 60
Оскільки ключ коротший за текст, який потрібно зашифрувати, то його потрібно повторити, щоб створити весь зашифрований текст. На початку тіла функції оголосіть змінну key_index зі значенням 0."""

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)