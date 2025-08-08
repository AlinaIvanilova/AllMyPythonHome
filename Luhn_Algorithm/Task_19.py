"""Крок 19
Використайте цикл for, щоб ітерувати над кожною цифрою в списку odd_digits. Перемістіть виклик print з попереднього кроку до циклу for та змініть його так, щоб він друкував кожну цифру."""

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    for dig in odd_digits:
        print(dig)

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()