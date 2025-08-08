"""Крок 28
Частиною алгоритму є подвоєння кожної другої цифри, починаючи справа. Якщо результат подвоєння числа більший або дорівнює 10, то додайте ці дві цифри. Наприклад, якщо цифра дорівнює 6, то при її подвоєнні вийде 12. Додайте 1 та 2, щоб отримати 3. Для цього можна використати цілочислове ділення, щоб отримати першу цифру, та оператор ділення з остачею (%), щоб отримати другу цифру:

Приклад коду
my_number = 12
first_digit = my_number // 10
second_digit = my_number % 10
Завдяки цілочисловому діленню ви отримаєте частку від ділення, заокруглену до меншого значення.

Призначте результат number // 10 (цілочислове ділення) плюс ділення з остачею number та 10 до number в межах інструкції if."""

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = number // 10 + number % 10
            sum_of_even_digits += number

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()