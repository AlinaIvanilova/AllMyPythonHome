"""Крок 10
Виведіть змінну, яку ви оголосили на попередньому кроці, і не соромтеся змінювати кількість дисків, щоб побачити, як швидко зростає мінімальна необхідна кількість ходів."""

NUMBER_OF_DISKS = 3
number_of_moves = 2**NUMBER_OF_DISKS - 1
print(number_of_moves)
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def move():
    pass