"""Крок 24
Далі ви будете реалізовувати таку ж логіку у межах функції total_expenses.

Наразі видаліть функцію test та виклик print()."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass



expenses = []