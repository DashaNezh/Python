from collections import deque

graph = {'S': {'N', 'P', 'D'},
         'P': {'S', 'M', 'K'},
         'D': {'S', 'M', 'C'},
         'K': {'P', 'M', 'B', 'N'},
         'N': {'S', 'K', 'R'},
         'R': {'N', 'B'},
         'B': {'K', 'M', 'R', 'F'},
         'C': {'M', 'D'},
         'M': {'P', 'D', 'C', 'K', 'B'},
         'F': {'B'}}


def bfs_all_paths(start, goal, graph): # Функция для нахождения всех минимальных путей от стартовой вершины к целевой вершине в графе
    queue = deque([(start, [start])]) # Используем deque для хранения вершин, которые предстоит посетить
    paths = [] # Список для хранения всех минимальных путей
    min_length = None # Переменная для хранения длины минимального пути

    while queue:
        cur_node, cur_path = queue.popleft() # Получаем текущую вершину и путь до неё из очереди

        if cur_node == goal:  #Если текущая вершина - целевая вершина
            if min_length is None:  # Проверяем, является ли этот путь первым найденным минимальным путем
                min_length = len(cur_path) # Устанавливаем длину минимального пути
            if len(cur_path) == min_length: # Если длина текущего пути минимальна
                paths.append(cur_path) # Добавляем путь в список минимальных путей
            continue #Переходим к следующей итерации цикла

        if min_length is not None and len(cur_path) > min_length:  # Если длина текущего пути превысила минимальную длину
            break # Завершаем цикл (нет необходимости исследовать дальше)

        next_nodes = graph[cur_node] # Получаем список смежных вершин для текущей вершины из графа

        for next_node in next_nodes: # Перебираем смежные вершины
            if next_node not in cur_path: # Если смежная вершина ещё не содержится в текущем пути
                queue.append((next_node, cur_path + [next_node])) # Добавляем смежную вершину и путь до неё в очередь

    return paths # Возвращаем список минимальных путей


start = 'S' # Стартовая вершина
goal = 'F' # Целевая вершина

all_paths = bfs_all_paths(start, goal, graph) # Находим все минимальные пути от стартовой вершины до целевой вершины

print(f'\nAll minimum paths from {start} to {goal}:')
for path in all_paths:  # Перебираем список минимальных путей
    path_str = '->'.join(path)  # Преобразуем путь в строку
    print(path_str) # Выводим каждый минимальный путь