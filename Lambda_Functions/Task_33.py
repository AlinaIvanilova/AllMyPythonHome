"""Крок 33
Цикл **while** — це ще один тип циклу, який виконує певну частину коду доти, доки вказана умова є **True** (істинною). Цикл припиняється, коли умова стає **False** (хибною):

**Приклад коду**

```python
while condition:
    <code>
```

Під списком витрат створіть цикл **while**.
Використайте **True** як умову та виведіть рядок `'\nExpense Tracker'` всередині тіла циклу, щоб показати назву програми.
"""

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