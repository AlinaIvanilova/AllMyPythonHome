"""Крок 36
Зараз зашифрований символ оновлюється на кожній ітерації.
Було б краще зберегти зашифрований рядок у новій змінній.
Перед циклом for оголосіть змінну під назвою encrypted_text та призначте до неї порожній рядок ('')."""
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    new_char = alphabet[new_index]
    print('char:', char, 'new char:', new_char)