"""Крок 26
Тепер викличте map(), передавши функцію lambda як перший аргумент та список expenses як другий аргумент."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    map(lambda expense: expense['amount'], expenses)

expenses = []