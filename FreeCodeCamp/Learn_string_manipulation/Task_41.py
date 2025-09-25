"""Крок 41
Наразі пробіли шифруються як 'c'.
Щоб зберегти вихідний інтервал в повідомленні, вам знадобиться умовна інструкція if.
Вона складається з ключового слова if, умови та двокрапки :.

Приклад коду
if x != 0:
    print(x)
Умовою інструкції if в прикладі вище є x != 0. Код print(x) в межах тіла інструкції if виконується лише тоді, коли умова оцінюється як True (у цьому прикладі це означає, що x не дорівнює нулю).

Замініть print(char == ' ') у верхній частині циклу for на інструкцію if.
Умова цієї інструкції if має оцінюватись як True, якщо char є пробілом або False, якщо навпаки.
Усередині тіла if надрукуйте рядок 'space!'.
Не забудьте зробити відступ для цього рядка."""
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        print('space!')
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)