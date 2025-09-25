"""Крок 34
За допомогою розуміння словника можна створити словник, починаючи з наявного словника:

Приклад коду
{key: val for key in dict}
У прикладі вище val є значенням, яке матиме key в новому словнику, а dict — це наявний словник.
Ви хочете відстежувати шляхи між початковою вершиною та кожною іншою вершиною.

Після змінної distances створіть змінну paths і призначте їй словник з усіма ключами з graph.
Присвойте порожній список кожному ключу та використайте словникове включення (dictionary comprehension) для побудови цього словника."""

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {}
    paths = {node: [] for node in graph}

    print(f'Unvisited: {unvisited}\nDistances: {distances}')

shortest_path(my_graph, 'A')