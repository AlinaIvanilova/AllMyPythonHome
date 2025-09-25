"""Крок 9
Головоломку «Вежа Ханоя» можна розв’язати за 2**n − 1 ходів, де n — кількість дисків.
Оголосіть змінну з назвою number_of_moves та присвойте їй загальну кількість ходів.

Оператор піднесення до степеня у Python — **."""

NUMBER_OF_DISKS = 3

number_of_moves = 2 ** NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}
def move():
    pass