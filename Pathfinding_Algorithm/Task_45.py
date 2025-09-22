"""Крок 45
Як тільки в словнику distances встановлено відстань до вузла, потрібно відстежувати шлях до цього вузла. Якщо відстань для вузла в обробленому кортежі оновлено, останнім елементом на шляху є сам вузол.

Вкладіть ще одну інструкцію if в межах умовної інструкції, яка запускатиметься, якщо останній елемент paths[node] дорівнює node. Використайте pass, щоб заповнити тіло інструкції if."""

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
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node][-1] == node:
                    pass
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

#shortest_path(my_graph, 'A')