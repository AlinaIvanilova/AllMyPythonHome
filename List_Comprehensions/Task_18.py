"""Крок 18
Після об’єднання елементів списку snake_cased_char_list потрібно буде видалити будь-який знак підкреслення на початку або в кінці отриманого рядка. Для цього використайте метод strip, аргументом якого є знак підкреслення _.

Виклики методів можуть бути об’єднані разом, тобто результат виклику одного методу можна використовувати як об’єкт для виклику іншого методу.

Приклад коду
words_list = ['hello', 'world', 'this', 'is', 'chained', 'methods']
result = ' '.join(words_list).upper()
У наведеному вище прикладі метод .upper() прив’язано до ' '.join(words_list), тому .upper() викликається на результаті виклику .join().

Змініть інструкцію return, приєднавши виклик методу .strip() до ''.join(snake_cased_char_list), щоб видалити будь-які знаки підкреслення напочатку чи вкінці."""

def convert_to_snake_case(pascal_or_camel_cased_string):
    # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #       converted_character = '_' + char.lower()
    #       snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string

    snake_cased_char_list = []
    return ''.join(snake_cased_char_list).strip('_')
def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()