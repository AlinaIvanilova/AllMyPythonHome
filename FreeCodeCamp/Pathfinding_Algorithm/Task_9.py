"""Крок 9
Щоб ітерувати над ключами словника, можна просто додати словник до циклу for. Код нижче надрукує всі ключі зі словника dict:

Приклад коду
for i in dict:
   print(i)
Замініть виклик print() на цикл for, який ітерує над copper та надрукує всі ключі."""

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'

for i in copper:
    print(i)