"""Крок 19
Лямбда-функції — це лаконічні анонімні функції в Python, ідеальні для простих одноразових завдань. Їх визначають за допомогою ключового слова lambda, використовуючи такий синтаксис:

Приклад коду
lambda x: expr
x у прикладі вище представляє параметр, який буде використано у виразі expr та який поводиться як будь-який інший параметр традиційної функції. expr — це вираз, який оцінюється та повертається, якщо викликано лямбда-функцію.

Створіть змінну під назвою test та призначте до неї лямбда-функцію, яка приймає параметр x та повертає x * 2."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    pass

test = lambda x: x * 2

expenses = []