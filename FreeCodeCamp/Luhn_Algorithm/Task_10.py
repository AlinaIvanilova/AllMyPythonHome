"""Крок 10
Раніше ви отримали елементи (символи) рядка за допомогою оператора індексу []. Оператор індексу також можна використати, щоб отримати символи рядка в діапазоні. Для цього використайте string[start:stop:step]:

Приклад коду
my_string = 'camperbot'
my_string[0:6] == 'camper' # True
my_string[0:6:3] == 'cp' # True
Де start — початковий індекс (включно), stop — кінцевий індекс (виключно), а step — кількість символів, які потрібно пропустити. Якщо не вказано, step за замовчанням дорівнює 1.

Створіть змінну під назвою card_number_reversed та призначте до неї значення перших 4 символів card_number."""

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[0:4]
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    print(translated_card_number)

    verify_card_number(translated_card_number)

main()