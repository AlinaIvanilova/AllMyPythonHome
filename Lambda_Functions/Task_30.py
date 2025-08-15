"""Крок 30
Функція filter() дозволяє вибрати елементи з ітерованого об’єкта (наприклад, списку) на основі результату функції:

Приклад коду
filter(my_function, my_list)
filter() приймає функцію як перший аргумент та ітерований об’єкт як другий аргумент. Вона повертає ітератор, який є спеціальним об’єктом, що дозволяє ітерувати над елементами колекції (наприклад, списку).

Результатом прикладу вище є ітератор, який містить елементи з my_list, для якого my_function повертає True.

У межах функції filter_expenses_by_category викличте filter(), передавши функцію lambda, яку ви написали на попередньому кроці, як перший аргумент, а список expenses — як другий аргумент."""


def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    filter(lambda expense: expense['category'] == category, expenses)

expenses = []