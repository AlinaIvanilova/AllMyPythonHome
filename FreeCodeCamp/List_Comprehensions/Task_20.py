"""Крок 20
Розуміння списків приймають умовні інструкції, щоб оцінювати наданий вираз лише тоді, коли виконуються певні умови:

Приклад коду
spam = [i * 2 for i in iterable if i > 0]
Як ви можете бачити з вихідних даних, список символів, згенерований з pascal_or_camel_cased_string, було об’єднано. Оскільки вираз в межах розуміння списку оцінюється для кожного символу, результатом є рядок у нижньому регістрі з усіма символами, розділеними знаком підкреслення.

Дотримуйтесь прикладу вище, щоб додати умову if до розуміння списку, щоб вираз виконувався лише тоді, коли символ знаходиться у верхньому регістрі."""

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

    snake_cased_char_list = ['_' + char.lower() for char in pascal_or_camel_cased_string if char.isupper()]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()