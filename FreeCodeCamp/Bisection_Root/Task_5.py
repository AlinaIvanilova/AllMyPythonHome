"""Крок 5
Ви створите окремі випадки для ситуацій, коли square_target дорівнює 0 або 1.

Почніть зі створення інструкції if, щоб перевірити, чи square_target дорівнює 1."""

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    if square_target == 1:
        pass