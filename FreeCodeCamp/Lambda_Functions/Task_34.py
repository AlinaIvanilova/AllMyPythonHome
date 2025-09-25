"""Крок 34
Цикл while, який ви створили в попередньому кроці, є нескінченним циклом, що дозволить програмі постійно показувати параметри меню, доки користувач не вирішить вийти.

Додайте ще один виклик print() після виклику print(), щоб надрукувати рядок '1. Add an expense'."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')