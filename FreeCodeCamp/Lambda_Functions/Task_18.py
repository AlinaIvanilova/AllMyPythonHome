"""Крок 18
Вам знадобиться функція для підрахунку загальної суми витрат.

Визначте функцію під назвою total_expenses, яка приймає один параметр expenses. Наразі заповніть тіло функції інструкцією pass."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
def total_expenses(expenses):
    pass

expenses = []