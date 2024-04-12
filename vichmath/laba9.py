"""
реализовать структуру данных - дерево
задать рандомно дерево и посчитать его наибольшую глубину
"""


def dfs(node, graph, visited, max_depth, current_depth):
    """
    Обход в глубину графа, начиная с указанной вершины.

    Аргументы:
        node: str
            Текущая вершина для обхода.
        graph: dict
            Граф в виде словаря смежности.
        visited: set
            Множество посещённых вершин.
        max_depth: list
            Список для хранения максимальной глубины.
        current_depth: int
            Текущая глубина обхода.
    """
    # Обновляем максимальную глубину, если текущая глубина больше
    if current_depth > max_depth[0]:
        max_depth[0] = current_depth

    # Добавляем текущую вершину в множество посещённых
    visited.add(node)

    # Рекурсивно обходим соседей текущей вершины
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, max_depth, current_depth + 1)


def find_max_depth(graph):
    """
    Нахождение максимальной глубины в графе.

    Аргументы:
        graph: dict
            Граф в виде словаря смежности.

    Возвращает:
        int: Максимальная глубина в графе.
    """
    max_depth = [0]  # Список для хранения максимальной глубины
    visited = set()  # Множество посещённых вершин

    # Начинаем обход с каждой вершины, если она ещё не была посещена
    for node in graph:
        if node not in visited:
            dfs(node, graph, visited, max_depth, 0)

    return max_depth[0]


def main():
    graph = {
        'S': {'G', 'X'},
        'G': {'S', 'F', 'H'},
        'X': {'S', 'H', 'M'},
        'H': {'X', 'G'},
        'M': {'X', 'F'},
        'F': {'G', 'M'}
    }

    # Находим максимальную глубину графа
    max_depth = find_max_depth(graph)
    print("Максимальная глубина:", max_depth)


if __name__ == "__main__":
    main()
