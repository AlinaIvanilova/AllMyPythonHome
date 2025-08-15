"""Крок 15
Створіть цикл for в межах функції print_expenses, який ітерує над кожним елементом в списку expenses. Використайте expense як змінну циклу та перемістіть pass до тіла циклу."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        pass

expenses = []