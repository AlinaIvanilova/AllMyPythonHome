"""Крок 38
Замість того, щоб призначати alphabet[new_index] до encrypted_text, призначте до цієї змінної поточне значення encrypted_text плюс alphabet[new_index]."""
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text = encrypted_text + alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)