"""Крок 9
Функція max() у Python повертає найбільше вхідне значення.

Приклад коду
max(1, 2, 3) # Output: 3
Змінні low та high будуть використовуватися для визначення початкового інтервалу, де знаходиться квадратний корінь.

В межах умови else ініціалізуйте змінну low як 0, а змінну high — як максимум 1 або square_target, оскільки квадратний корінь числа завжди менший або дорівнює самому числу."""

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    else:
        low = 0
        high = max(1, square_target)