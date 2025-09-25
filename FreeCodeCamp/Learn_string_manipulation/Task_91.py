"""Крок 91
У Python можна легко відформатувати рядки. f-рядки дозволяють інтерполювати значення в рядках.

Інтерполяція — це написання заповнювачів, які будуть замінені вказаними значеннями під час виконання програми. Наприклад, ви можете отримати той самий результат для 'Encrypted text: ' + text, що й за допомогою f'Encrypted text: {text}'. Щоб створити f-рядок, вам потрібно використати f перед лапками, та написати у фігурних дужках змінні чи вирази, які потрібно інтерполювати.

Змініть перший виклик print(), використавши f-рядок."""
text = 'mrttaqrhknsw ih puggrur'
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

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)
print(f'Encrypted text: {text}')
print('Key: ' + custom_key)
#decryption = decrypt(encryption, custom_key)
#print(decryption)