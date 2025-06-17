"""Крок 37
Тепер замініть new_char на encrypted_text.
Також змініть виклик print() на print('char:', char, 'encrypted text:', encrypted_text), щоб відтворити зміни."""
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text = alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)