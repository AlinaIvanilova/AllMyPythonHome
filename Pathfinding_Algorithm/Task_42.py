"""Крок 42
Створіть цикл for після присвоєння змінної current, щоб ітерувати над кортежами в списку graph[current]. Для цього вам знадобляться дві змінні ітерації. Не забудьте використати pass, щоб заповнити тіло циклу."""

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
        current = min(unvisited, key=distances.get)
        for i,j in graph[current]:
            pass
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

#shortest_path(my_graph, 'A')
