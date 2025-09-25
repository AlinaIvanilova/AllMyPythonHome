"""Крок 25
У функції total_expenses тепер потрібно використати лямбда-функцію. Замініть pass на лямбда-функцію, яка приймає expense як параметр.

Очікується, що expense буде словником, і ваша лямбда-функція повинна повертати значення ключа 'amount' у цьому словнику."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    lambda expense: expense['amount']

expenses = []