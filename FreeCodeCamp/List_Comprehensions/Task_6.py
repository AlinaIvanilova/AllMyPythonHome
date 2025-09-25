"""Крок 6
В межах інструкції if ви будете додавати перетворений символ до списку, який створили раніше.

Для цього буде використано метод .append(). Цей метод додає наданий об’єкт в кінець списку, на якому його викликають.

Використайте метод .append() на snake_cased_char_list, щоб додати converted_character до списку."""
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)