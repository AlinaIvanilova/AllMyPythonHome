"""Крок 15
Якщо різниця не знаходиться в межах вказаного допуску, створіть інструкцію elif, щоб перевірити, чи square_mid менше за square_target.

Присвойте значення mid змінній low, оскільки квадратний корінь тепер буде знаходитись між mid і high."""

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