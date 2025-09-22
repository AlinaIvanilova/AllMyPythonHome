"""Крок 10
Якщо ви хочете ітерувати над значеннями ключів словника, можна використати метод .values().

Змініть цикл for, щоб він ітерував над copper.values(), а не copper та гляньте на результат."""

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'

for i in copper.values():
    print(i)