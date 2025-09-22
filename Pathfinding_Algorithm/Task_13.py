"""Крок 13
Ви можете видалити пару ключ-значення зі словника, використовуючи ключове слово del:

Приклад коду

my_dict = {
    'name': 'Michael',
    'occupation': 'Lumberjack'
}

del my_dict['occupation']


Безпосередньо перед вашим циклом for використайте ключове слово del, щоб видалити ключ 'age' та його значення зі словника copper."""

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'

del copper['age']

for i, j in copper.items():
    print(i, j)