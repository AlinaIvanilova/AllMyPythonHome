"""Крок 9
Рядки в регістрі Паскаля починаються з великої літери. Після перетворення всіх символів у нижній регістр та додавання до них знаку підкреслення є ймовірність, що на початку рядка з’явиться зайвий знак підкреслення.

Найпростіший спосіб виправити це — використати метод .strip(), який видаляє з рядка будь-які символи напочатку чи вкінці, передані як аргумент. Наприклад:

Приклад коду
original_string = "_example_string_"

clean_string = original_string.strip('_')
Метод strip() застосовано до original_string. Це видаляє будь-яке підкреслення напочатку чи вкінці. Результатом наведеного вище прикладу буде рядок 'example_string'.

Оголосіть нову змінну під назвою clean_snake_cased_string та призначте до неї результат методу .strip(), застосованого до snake_cased_string, передаючи '_' як аргумент методу."""

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