"""Крок 17
У Python важливо знати, що той самий тип лапок, якими визначається рядок, не можна використовувати всередині нього. Наприклад, рядок 'I'm a string!' некоректний. Щоб використовувати апостроф всередині такого рядка, слід:

Екранувати лапку, додавши перед нею зворотній слеш: 'I\'m a string!'

Або використовувати подвійні лапки для визначення рядка: "I'm a string!" (бажано).

До значень у словнику можна звертатися через ключі. Для цього потрібно використовувати квадратні дужки і вказувати ключ у них:

Приклад коду

python
Копіювати
Редагувати
my_dict = {'amount': 50.0, 'category': 'Food'}
my_dict['amount']  # 50.0
Зараз ви інтерполюєте словник expense у вашому f-рядку. Змініть вираз у f-рядку так, щоб звертатися до значень за ключами 'amount' і 'category' у словнику expense."""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

expenses = []