"""Крок 50
Якщо ви спробуєте розкоментувати виклик функції, у вас не вийде. Вам потрібно виправити пару помилок. Перша помилка трапляється через те, що ви намагаєтесь використати у вкладеній інструкції if елемент, якого може не існувати в списку paths[node]. Отже, перед доступом до paths[node][-1] потрібно переконатися, що paths[node] не порожній.

Додайте додаткову умову до вкладеної інструкції if, щоб переконатися, що paths[node] не порожній, перш ніж отримати доступ до paths[node][-1]."""

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
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

#shortest_path(my_graph, 'A')
