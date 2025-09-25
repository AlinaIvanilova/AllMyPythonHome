"""Крок 10
Щоб завершити функцію, поверніть clean_snake_cased_string. Це завершить функцію та дозволить використовувати її, щоб перетворити рядки в регістрі Паскаля чи верблюдячому регістрі на зміїний регістр.

Додайте інструкцію return у кінець функції, щоб повернути clean_snake_cased_string."""



def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string