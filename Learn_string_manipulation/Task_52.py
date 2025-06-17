"""Крок 52
Щоб виконати функцію, її потрібно викликати (або звернутися до неї), додавши пару круглих дужок після її назви:

Приклад коду
function_name()
У кінці коду викличте функцію caesar. Зверніть увагу на відступи."""
text = 'Hello Zaira'
shift = 3
def caesar():
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

caesar()