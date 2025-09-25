"""Крок 17
Ключове слово is в Python перевіряє ідентичність об’єкта. Його використовують, щоб визначити, чи дві змінні вказують на один об’єкт в пам’яті. На відміну від is, оператор рівності (==) визначає, чи значення двох об’єктів одинакові, незалежно від того, чи це однаковий об’єкт в пам’яті.

Поза межами циклу for створіть інструкцію if, щоб перевірити, чи root is None. If it is, print the message 'Failed to converge within {max_iterations} iterations.'. Remember to format the message using an f-string."""
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
        root = None

        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f'Failed to converge within {max_iterations} iterations.')

