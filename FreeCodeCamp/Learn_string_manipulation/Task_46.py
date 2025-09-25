""""Крок 46
Якщо ви хочете використати додаткові символи в рядку alphabet (наприклад, цифри чи спеціальні символи), то ви дізнаєтесь, що потрібно вручну змінити правий операнд операції ділення з остачею.

Замініть 26 на len(alphabet), щоб уникнути цієї проблеми."""

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
    print('char:', char, 'encrypted text:', encrypted_text)