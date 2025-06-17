"""Крок 83
Ключове слово pass можна використовувати як заповнювач для майбутнього коду. Воно не впливає на код, але може вберегти від помилок, які виникнуть у разі неповного коду:

Приклад коду
def foo():
    pass
Викликати vigenere з 1, щоб зашифрувати та -1, щоб розшифрувати повідомлення — непогана ідея, але вона може бути трошки загадковою. Створіть нову функцію під назвою encrypt, яка приймає параметри message та key, і використайте pass для заповнення тіла функції."""

text = 'Hello Zaira!'
custom_key = 'python'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
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

encryption = vigenere(text, custom_key)
print(encryption)
decryption = vigenere(encryption, custom_key, -1)
print(decryption)
def encrypt(message, key):
    pass