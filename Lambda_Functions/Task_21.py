"""Крок 21
Лямбда-функції можна поєднати з функцією map(), яка виконує певну функцію для кожного елемента в колекції об’єктів, як-от список:

Приклад коду
map(lambda x: x * 2, [1, 2, 3])
Функція, яку потрібно виконати, передається як перший аргумент, а ітерабельний об’єкт — як другий аргумент.

Результатом прикладу вище буде [2, 4, 6], де кожен елемент у списку, переданому до map(), було подвоєно дією лямбда-функції.

Змініть виклик print(), щоб він виводив результат виклику map() з test як першим аргументом і [2, 3, 5, 8] як другим аргументом. Наразі ви не зможете побачити читабельний вивід."""


def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass

test = lambda x: x * 2
print(map(test, [2, 3, 5, 8]))

expenses = []