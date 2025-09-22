"""Тяжко, однак, дуже цікаво, надіюся більше таких завань буде в майбутньому.
Додам коментарі щоб в майбутньому не забути що я тут робила."""

# Граф задається у вигляді словника:
# ключ — вершина, значення — список кортежів (сусідня вершина, вага ребра)
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    # unvisited — список ще не відвіданих вершин
    unvisited = list(graph)

    # distances — відстань від початкової вершини до кожної іншої
    # стартова вершина має 0, решта — нескінченність
    distances = {node: 0 if node == start else float('inf') for node in graph}

    # paths — словник, де зберігатимуться шляхи у вигляді списків
    paths = {node: [] for node in graph}
    # шлях до стартової вершини — сама вершина
    paths[start].append(start)

    # поки є невідвідані вершини
    while unvisited:
        # вибираємо вершину з найменшою відстанню (жадібний крок)
        current = min(unvisited, key=distances.get)

        # перебираємо всіх сусідів поточної вершини
        for node, distance in graph[current]:
            # перевіряємо, чи можна покращити відстань до сусіда
            if distance + distances[current] < distances[node]:
                # оновлюємо відстань
                distances[node] = distance + distances[current]

                # формуємо шлях: копіюємо шлях до поточної вершини
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                # додаємо самого сусіда
                paths[node].append(node)

        # видаляємо поточну вершину зі списку невідвіданих
        unvisited.remove(current)

    # якщо задано target → виводимо тільки його,
    # інакше виводимо шляхи до всіх вершин графа
    targets_to_print = [target] if target else graph

    for node in targets_to_print:
        # пропускаємо початкову вершину (шлях від себе до себе не виводимо)
        if node == start:
            continue
        # друкуємо відстань і шлях
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    # повертаємо результати, щоб можна було використати далі в коді
    return distances, paths

# Виклик функції: шукаємо найкоротші шляхи зі старту 'A',
# але виводимо лише шлях до 'F'
shortest_path(my_graph, 'A', 'F')
