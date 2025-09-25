"""Крок 8
Такий самий синтаксис можна використовувати, щоб змінити значення наявного ключа.

Отримайте доступ до ключа 'species' одразу перед викликом print() та перепризначте його значення до 'Cavia porcellus'."""

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'
print(copper)