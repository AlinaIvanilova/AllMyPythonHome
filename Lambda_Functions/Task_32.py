"""Крок 32
Наступний крок — визначити головну функцію, яка буде входовою точкою інтерактивної програми для відстеження витрат.

Визначте функцію під назвою main без параметрів. Заповніть тіло функції списком expenses, який ви створили на початку цього проєкту. Ви використовуватимете цей список, щоб зберігати записи про витрати."""

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