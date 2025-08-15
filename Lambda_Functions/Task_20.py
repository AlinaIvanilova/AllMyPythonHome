"""Крок 20
Щоб викликати лямбда-функцію, можна використати синтаксис звичайної функції з парою круглих дужок після назви змінної.

Викличте лямбда-функцію test та передайте 3 як аргумент. Потім надрукуйте результат."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass

test = lambda x: x * 2
print(test(3))

expenses = []