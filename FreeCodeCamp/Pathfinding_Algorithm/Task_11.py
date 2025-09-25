"""Крок 11
Зрештою, якщо ви хочете отримати пари ключ-значення, можна використати метод .items().

Змініть цикл for, щоб ітерувати над copper.items(), а не copper.values()."""

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'

for i in copper.items():
    print(i)