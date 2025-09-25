"""Крок 21
Наразі сценарій видає помилку TypeError, оскільки ви намагаєтесь додати рядок до цілого числа. Це можна виправити, перетворивши змінну digit на ціле число за допомогою вбудованої функції int, перш ніж додавати її до sum_of_odd_digits:

Приклад коду
my_string = '123'
my_int = int(my_string)
Перетворіть змінну digit на ціле число, перш ніж додати її до sum_of_odd_digits. Потім перемістіть виклик print у кінець функції verify_card_number, щоб надрукувати значення sum_of_odd_digits."""

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    print(sum_of_odd_digits)
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()