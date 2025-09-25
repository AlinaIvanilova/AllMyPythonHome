"""Крок 4
Визначення перекладу саме по собі не перекладає рядок. Метод translate потрібно викликати на рядку, який потрібно перекласти, де аргументом є таблиця перекладу:

Приклад коду
my_string = "tamperlot"
translation_table = str.maketrans({'t': 'c', 'l': 'b'})
translated_string = my_string.translate(translation_table)
Створіть змінну під назвою translated_card_number та призначте до неї результат виклику методу translate на card_number, де аргументом є card_translation."""

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)