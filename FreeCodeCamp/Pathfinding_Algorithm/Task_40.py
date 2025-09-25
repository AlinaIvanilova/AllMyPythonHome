"""Крок 40
Перше, що потрібно зробити в межах циклу while — визначити поточний вузол, який потрібно відвідати. Для цього можна скористатися функцією min(). Вона повертає найменший елемент з ітерованого об’єкта, переданого як аргумент.

Видаліть pass, потім створіть змінну під назвою current і призначте до неї min(unvisited)."""

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
    paths[start].append(start)
    while unvisited:
        current = min(unvisited)
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

#shortest_path(my_graph, 'A')
