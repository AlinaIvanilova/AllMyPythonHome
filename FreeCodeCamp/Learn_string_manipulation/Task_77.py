"""Крок 77
Функції можна викликати з аргументами за замовчуванням. Аргумент за замовчуванням вказує значення, яке має приймати функція, якщо аргумент не передано. Наприклад, наведена нижче функція приймає три аргументи, але ви можете викликати її, передаючи два аргументи. Третій прийме вказане значення за замовчуванням:

Приклад коду
def foo(a, b, c=value):
    <code>
Змініть функцію vigenere так, щоб її параметр direction мав значення за замовчуванням 1."""

text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key, direction =1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append space to the message
        if char == ' ':
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

encryption = vigenere(text, custom_key, 1)
print(encryption)
decryption = vigenere(encryption, custom_key, -1)
print(decryption)