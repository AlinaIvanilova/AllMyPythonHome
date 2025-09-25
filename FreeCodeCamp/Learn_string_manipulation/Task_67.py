"""Крок 67
Зараз функція друкує деякі рядки, але ці значення не можуть використовуватися іншими частинами коду для виконання будь-яких дій.

Для цього потрібно використати інструкцію return:

Приклад коду
def foo():
    return 'spam'
Вам потрібно написати return, а потім пробіл та значення, яке має повернути функція. Як тільки оператор return виконується, його значення повертається, і виконання функції зупиняється. Далі програма продовжує виконання з наступного рядка коду після виклику функції. Функція foo повертає рядок 'spam' в прикладі вище.

Видаліть два виклики print() із вашої функції та поверніть encrypted_text за допомогою оператора return."""
text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():

        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text