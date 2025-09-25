"""Крок 21
Ще не зовсім досягнуто бажаного результату. Потрібно виконувати інший вираз для символів, які відсіюються умовою if. Для цього використовуйте клаузу else:

Приклад коду

spam = [i * 2 if i > 0 else -1 for i in iterable]


Зверніть увагу: на відміну від простої if-умови в кінці comprehension, конструкція if/else розташовується між виразом і ключовим словом for.

Змініть ваше спискове включення так, щоб коли символ не великий, він залишався без змін."""

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

    snake_cased_char_list = [('_' + char.lower()) if char.isupper() else char for char in pascal_or_camel_cased_string]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()