"""Крок 42
Тепер замість того, щоб друкувати 'space!', використайте оператор додавання з присвоєнням, щоб додати пробіл (наразі зберігається в char) до поточного значення encrypted_text."""


text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)