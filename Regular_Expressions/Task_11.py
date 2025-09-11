"""Крок 11
Кожного разу, коли виконується код, ви повинні бачити випадковий символ із рядка all_characters. Саме цього потрібно досягти, створюючи випадковий пароль.

Однак алгоритм, на який покладається random, робить згенеровані псевдовипадкові числа передбачуваними. Тому, хоча модуль random підходить для найпоширеніших програм, його не можна використовувати для криптографії через детерміновану природу.

Імпортуйте модуль secrets замість random. Потім змініть виклик print(), щоб використати secrets.choice(all_characters)"""

import secrets
import string


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)
print(secrets.choice(all_characters))