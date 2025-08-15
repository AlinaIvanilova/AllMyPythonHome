"""Крок 28
Потім визначте функцію під назвою filter_expenses_by_category, яка приймає два параметри: expenses та category. Використайте pass, щоб заповнити тіло функції."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    pass

expenses = []