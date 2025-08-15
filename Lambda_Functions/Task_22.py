"""Крок 22
Ви маєте побачити щось схоже до <map object at 0xd273a8> на консолі, що є рядковим представленням map-об’єкта, повернутого функцією map().

Щоб отримати читабельний вивід, потрібно перетворити map-об’єкт на список. Для цього передайте виклик map() як аргумент до функції list()."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass

test = lambda x: x * 2
print(list(map(test, [2, 3, 5, 8])))

expenses = []