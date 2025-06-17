"""Крок 49
Функція — це, по суті, багаторазовий блок коду.
Ви вже ознайомилися з деякими вбудованими функціями, такими як print(), find() та len().
Але ви також можете визначити власні функції:

Приклад коду
def function_name():
    <code>
Оголошення функції починається з ключового слова def, після якого йде назва функції (дійсна назва змінної) та пара круглих дужок.
Оголошення закінчується двокрапкою.

Оголосіть функцію під назвою caesar одразу після змінної shift та зробіть відступ для всіх наступних рядків, щоб надати новій функції тіло."""

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