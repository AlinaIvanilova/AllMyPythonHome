"""Крок 13
Додайте ще одну пару ключ-значення до словника, який додаєте до списку expense. Використайте рядок 'category' як ключ, а параметр category як значення."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

expenses = []