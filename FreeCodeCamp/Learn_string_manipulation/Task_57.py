"""Крок 57
Наразі кожна літера завжди шифрується тією самою літерою, залежно від зазначеного зсуву. Що, якби зсув для літер був різним? Так було б набагато важче виконати розшифрування. Цей алгоритм називається шифром Віженера, де зсув для кожної літери визначається іншим текстом, який називається ключем.

Щоб розпочати перетворювати шифр Цезаря на шифр Віженера, видаліть два виклики функції."""

text = 'Hello Zaira'
shift = 3

def caesar(message, offset):
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

