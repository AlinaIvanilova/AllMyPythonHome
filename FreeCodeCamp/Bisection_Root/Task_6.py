"""Крок 6
Якщо square_target дорівнює 1, то оголосіть змінну root та призначте до неї значення 1 . Також надрукуйте повідомлення 'The square root of {square_target} is 1'. Не забудьте відформатувати повідомлення за допомогою f-рядка."""

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')