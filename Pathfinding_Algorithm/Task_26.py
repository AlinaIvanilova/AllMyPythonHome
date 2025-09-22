"""Крок 26
Створіть цикл for, щоб ітерувати над графом та використайте метод .append(), щоб додати всі вузли до кінця списку unvisited."""

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path(graph, start):
    unvisited = []
    for i in graph:
        unvisited.append(i)