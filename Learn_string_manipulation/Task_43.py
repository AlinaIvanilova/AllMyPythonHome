"""Крок 43
Умовна інструкція також може мати умову else.
Цю умову можна додати в кінець інструкції if, щоб виконати альтернативний код, якщо умова інструкції if хибна:

Приклад коду
if x != 0:
    print(x)
else:
    print('x = 0')
Як можна побачити в результаті, коли ітерації циклу досягають пробілу, то його додають до зашифрованого рядка.
Потім виконується код поза блоком if і до зашифрованого рядка додається c.

Щоб виправити це, додайте умову else після encrypted_text += char та зробіть відступ для всіх наступних рядків коду, крім виклику print()."""
text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = index + shift
        encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)