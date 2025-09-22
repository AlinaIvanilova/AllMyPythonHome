"""Крок 52
Інша помилка є непомітною. Якщо для сусіднього вузла знайдено меншу відстань, то paths[current] призначається до шляху сусіднього вузла — paths[node].

Це означає, що обидві змінні вказують на той самий список. Оскільки списки є змінними, якщо додати сусідній вузол до його шляху, то paths[node] та paths[current] зміняться, оскільки це один список. Це призводить до неправильних шляхів, хоча відстані правильні.

Виправте цю помилку, призначивши копію paths[current] до шляху сусіднього вузла. Для цього можна використати синтаксис розрізу:

Приклад коду
my_list[:]
Де my_list є списком, який потрібно скопіювати. Змініть наявне присвоєння paths[node] = paths[current] в межах блоку if, розрізавши paths[current]."""

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
                    paths[node] = paths[current][:]


                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

shortest_path(my_graph, 'A')
