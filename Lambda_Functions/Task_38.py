"""Крок 38
Ви використовуватимете умовні інструкції, щоб перевірити вибір користувача. Якщо користувач вибрав '1', то він хоче додати витрати.

Напишіть інструкцію if в циклі while під змінною choice, щоб перевірити, чи choice дорівнює рядку '1'. Якщо так, то це буде відправною точкою для додавання нових витрат.

Оголосіть змінну amount в межах тіла інструкції if та передайте до неї порожній виклик input()."""

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
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            amount = input()