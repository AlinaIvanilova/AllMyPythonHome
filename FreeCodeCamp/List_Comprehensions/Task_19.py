"""Крок 19
Спискове включення (list comprehension) у Python — це конструкція, яка дозволяє створити новий список, застосовуючи вираз до кожного елемента наявного ітерованого об’єкта, а також додатково фільтрувати елементи за умовою. Такий спосіб не лише стислий, але й часто виконується швидше.

Базове спискове включення складається з виразу, після якого йде цикл for:

Приклад коду

spam = [i * 2 for i in iterable]


У наведеному прикладі змінна i використовується для ітерації по iterable. Кожен елемент у новому списку отримується шляхом обчислення виразу i * 2 на поточній ітерації.

У цьому кроці вам потрібно заповнити порожній список snake_cased_char_list, використовуючи синтаксис list comprehension.

Перетворіть ваш порожній список на спискове включення, яке буде конвертувати кожен символ із pascal_or_camel_cased_string у нижній регістр та додавати перед ним символ підкреслення. (Код, який ви закоментували раніше, може допомогти скласти вираз). Використовуйте змінну char для ітерації по pascal_or_camel_cased_string."""


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


    snake_cased_char_list = ['_' + char.lower() for char in pascal_or_camel_cased_string]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()