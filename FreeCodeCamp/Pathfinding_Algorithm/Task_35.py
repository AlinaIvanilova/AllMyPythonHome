"""Крок 35
Розуміння словників також підтримує умовний синтаксис if/else:

Приклад коду
{key: val_1 if condition else val_2 for key in dict}
dict з прикладу вище є наявним словником. Якщо condition оцінюється як True, то key матиме значення val_1, а в іншому випадку — val_2.

Використайте розуміння словника, щоб створити словник на основі graph та призначте його до змінної distances. Присвойте ключу значення нуль, якщо вершина збігається з початковою, і нескінченність в іншому випадку.
Для задання нескінченності використайте float('inf'). """

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    print(f'Unvisited: {unvisited}\nDistances: {distances}')

shortest_path(my_graph, 'A')