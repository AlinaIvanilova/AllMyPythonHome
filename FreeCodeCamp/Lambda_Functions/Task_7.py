"""Крок 7
Метод pop() можна використати для видалення елемента зі списку. За замовчуванням він видаляє останній елемент списку. Ви можете передати індекс як аргумент методу, і тоді він видалить елемент за вказаним індексом.

Приклад коду

python
Копіювати
Редагувати
fruits_list = ["cherry", "lemon", "tomato", "apple", "orange"]

fruits_list.pop(2)

print(fruits_list)  # ["cherry", "lemon", "apple", "orange"]
У цьому випадку fruits_list.pop(2) видаляє елемент із індексом 2 зі списку.

Завдання:
Використайте pop(), щоб видалити останній елемент зі my_list, а потім виведіть my_list."""

my_list = [1, 2]

my_list.append(3)
print(my_list)

print(my_list[0])

my_list[0] = 0
print(my_list)

my_list.insert(1, 1)
print(my_list)

my_list.pop()
print(my_list)