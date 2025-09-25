"""Крок 45
Коли цикл досягає літери Z, сума index + shift перевищує останній індекс рядка alphabet. Таким чином, alphabet[new_index] намагається використати недійсний індекс, що спричиняє помилку IndexError.

Можна помітити, що вивід у терміналі зупиняється на місці одразу перед Z — останнім print перед помилкою.

У цьому випадку оператор модулювання (%) можна використати для отримання остачі від ділення двох чисел. Наприклад: 5 % 2 дорівнює 1, тому що 5 поділене на 2 має частку 2 і остачу 1.

Обгорни вираз index + shift у дужки та застосуй модуль 26 до цього виразу, оскільки 26 — це довжина абетки."""
text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % 26
        encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)