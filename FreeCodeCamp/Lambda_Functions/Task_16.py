"""Крок 16
Далі ви відтворите деталі всіх витрат.

Замініть pass на виклик print() в межах циклу for та передайте до нього наступний f-рядок: f'Amount: {expense}, Category: {expense}'."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense}, Category: {expense}')

expenses = []