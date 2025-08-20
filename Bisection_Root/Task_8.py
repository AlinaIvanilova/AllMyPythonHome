"""Крок 8
Далі ви працюватимете з випадками, де square_target є додатним числом, крім 1 чи 0.

Створіть умову else для обробки таких випадків."""

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
        pass
