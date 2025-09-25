"""Крок 9
Алгоритм Луна виглядає наступним чином:

Справа наліво помножте значення кожної другої цифри на два. Якщо добуток більший за 9, додайте цифри добутків.
Візьміть суму всіх цифр.
Якщо сума всіх цифр кратна 10, то число дійсне, якщо ні — недійсне.
Як приклад розглянемо номер рахунку 7992739871, до якого буде додано контрольну цифру, що утворить 7992739871x:

Приклад коду
Account number      7   9  9  2  7  3  9   8  7  1  x
Double every other  7  18  9  4  7  6  9  16  7  2  x
Sum 2-char digits   7   9  9  4  7  6  9   7  7  2  x
Замініть інструкцію pass на змінну під назвою sum_of_odd_digits та зі значенням 0."""

def verify_card_number(card_number):
    sum_of_odd_digits = 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    print(translated_card_number)

    verify_card_number(translated_card_number)

main()