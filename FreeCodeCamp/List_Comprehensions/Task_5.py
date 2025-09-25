"""Крок 5
Перетворіть будь-який символ у верхньому регістрі в тілі інструкції if на нижній регістр та додайте перед ним знак підкреслення.

Використайте метод .lower(), щоб перетворити верхній регістр символа на нижній. Потім додайте знак підкреслення перед символом. Призначте результати до змінної під назвою converted_character."""

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
