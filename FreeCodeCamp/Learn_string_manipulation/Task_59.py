"""Крок 59
Видаліть змінну shift. Потім оголосіть нову змінну під назвою custom_key та призначте цій змінній значення рядка 'python'."""

text = 'Hello Zaira'
custom_key = 'python'
def vigenere(message, key):
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
