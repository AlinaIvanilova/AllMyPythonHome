"""Крок 54
Python забезпечує стислий спосіб запису умовних інструкцій if/else за допомогою тернарного синтаксису:

Приклад коду
val_1 if condition else val_2
Наведений вище вираз обчислюється як val_1, якщо condition має значення true, а в іншому випадку — як val_2.

Видаліть виклик print та створіть зміну під назвою targets_to_print після циклу while. Використайте тернарний синтаксис, щоб призначити до неї [target], якщо target оцінюється як true, або graph, якщо навпаки."""

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    targets_to_print  = [target] if target else graph

shortest_path(my_graph, 'A')