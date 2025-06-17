"""Крок 39
Ви можете отримати той самий ефект a = a + b, використовуючи оператор додавання з присвоєнням:

Приклад коду
a += b
Оператор додавання з присвоєнням дозволяє додати значення до змінної, а потім призначити результат до неї.

Використайте оператор +=, щоб одночасно додати значення та призначити його до encrypted_text."""
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)