"""Крок 7
Потрібно обробити символи, які вже знаходяться у нижньому регістрі, додаючи їх до списку перетворених символів.

Одразу після оператора if у циклі for додайте гілку else та використайте метод .append(), щоб додати char до змінної snake_cased_char_list."""

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)