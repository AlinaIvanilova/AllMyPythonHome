"""Крок 48
Додайте ще один виклик одразу перед викликом print та передайте 'plain text:', text як аргументи до print().
Використайте той самий відступ."""
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
print('plain text:', text)
print('encrypted text:', encrypted_text)