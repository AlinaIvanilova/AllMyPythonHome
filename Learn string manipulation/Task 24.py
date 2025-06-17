"""Крок 24
Код, який виконується на кожній ітерації (розміщений після :), становить тіло циклу. Цей код повинен мати відступ.
У Python рекомендується використовувати 4 пробіли на рівень відступу. Цей рівень із відступом є блоком коду.

Приклад коду
for i in text:
    print(i)
В Python використовуються відступи, щоб вказувати блоки коду.
Двокрапка в кінці рядка є сигналом того, що слідуватиме новий блок коду з відступом.

Якщо після останньої двокрапки не знайдено блоку з відступом, виконання коду припиняється та видається IndentationError.
Цей код не показуватиме вивід, а натомість видасть IndentationError:

Приклад коду
for i in text:
print(i)
Give your for loop a body by adding a call to print(i). Remember to indent the loop body."""
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in text:
    print(i)
