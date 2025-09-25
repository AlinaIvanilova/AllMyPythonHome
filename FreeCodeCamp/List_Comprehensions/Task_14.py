"""Крок 14
Наразі у цьому проєкті ви використовували цикл for, щоб ітерувати над вхідним рядком та перетворити його на бажані вихідні дані. Тепер ви почнете переходити від циклу for до розуміння списку.

Для початку закоментуйте всі рядки коду в межах функції convert_to_snake_case(). Не видаляйте їх, оскільки вони будуть корисними під час впровадження логіки за допомогою розуміння списків.

Не забудьте додати ключове слово pass до тіла функції, щоб запобігти несправності коду під час тестів."""

def convert_to_snake_case(pascal_or_camel_cased_string):
    pass
#    snake_cased_char_list = []
#    for char in pascal_or_camel_cased_string:
#        if char.isupper():
#            converted_character = '_' + char.lower()
#            snake_cased_char_list.append(converted_character)
#        else:
#            snake_cased_char_list.append(char)
#    snake_cased_string = ''.join(snake_cased_char_list)
#    clean_snake_cased_string = snake_cased_string.strip('_')

#    return clean_snake_cased_string
def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()
