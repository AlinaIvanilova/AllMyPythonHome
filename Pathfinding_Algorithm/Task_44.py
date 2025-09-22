"""Крок 44
Якщо умова нової інструкції if правдива, то найкоротший шлях до сусіднього вузла знайдено.
Усередині нового блоку if видали pass і перевизнач (онови) відстань для сусіднього вузла так, щоб вона дорівнювала сумі відстані до поточного вузла та довжини ребра до сусіднього вузла.»"""


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
    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

#shortest_path(my_graph, 'A')

