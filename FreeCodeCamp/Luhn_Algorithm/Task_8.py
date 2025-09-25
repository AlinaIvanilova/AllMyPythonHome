"""Крок 8
Викличте функцію verify_card_number в межах функції main та передайте змінну translated_card_number як аргумент."""


def verify_card_number(card_number):
    pass


def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    print(translated_card_number)

    verify_card_number(translated_card_number)
    print(verify_card_number)


main()