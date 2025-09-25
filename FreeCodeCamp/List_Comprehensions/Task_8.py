"""Крок 8
Наразі змінна snake_cased_char_list містить список перетворених символів. Щоб об’єднати ці символи в один рядок, можна використати метод .join().

Метод join об’єднує всі елементи списку в один рядок, де вони розділені визначеним рядком (відомий як роздільник).

Приклад коду
result_string = ''.join(characters)
Наведений вище приклад об’єднує елементи списку characters в один рядок, де елементи об’єднані за допомогою роздільника у вигляді порожнього рядка.

Тепер одразу після циклу for скористайтеся методом .join(), щоб об’єднати елементи в snake_cased_char_list, використовуючи порожній рядок як роздільник. Призначте результат до нової змінної під назвою snake_cased_string."""

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = "".join(snake_cased_char_list)