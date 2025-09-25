"""Крок 23
Функція sum() повертає суму елементів ітерованого об’єкта, який передається як аргумент. Ви використовуватимете sum() разом із функціями map() та lambda, щоб отримати загальну суму витрат.

Поки зробіть невеличкий тест та змініть наявний виклик print(), замінивши виклик list() на виклик до функції sum(), передавши тест як аргумент до поточного виклику map()."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass

test = lambda x: x * 2
print(sum(map(test, [2,3,5,8])))

expenses = []