"""Крок 47
Потім змініть виклик print(), щоб надрукувати 'encrypted text:', encrypted_text та розмістіть його поза циклом for, щоб зашифрований рядок друкувався один раз."""
text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        encrypted_text += alphabet[new_index]
print('encrypted text:', encrypted_text)