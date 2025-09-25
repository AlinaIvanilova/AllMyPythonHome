"""Крок 61
При написанні коду важлива читабельність. Коментарі служать ефективними примітками, які пояснюють логіку коду. Вони стають цінними, якщо через деякий час ви повертаєтесь до проєкту, а також допомагають колегам зрозуміти код.

Коментар в Python можна написати за допомогою #. Усе, що стоїть після #, не буде виконано.

Додайте коментар Append space to the message перед інструкцією if."""

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
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)