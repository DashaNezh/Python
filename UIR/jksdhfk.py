from collections import deque

graph = {'CAB': {'CAR': 3, 'CAT': 2},
         'CAR': {'CAB': 3, 'CAT': 4, 'BAR': 2},
         'BAR': {'CAR': 2, 'BAT': 3},
         'BAT': {'CAT': 3, 'BAR': 3, 'MAT': 4},
         'MAT': {'CAT': 5, 'BAT': 4},
         'CAT': {'CAB': 2, 'CAR': 4, 'BAT': 3, 'MAT': 5}}


def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}
    distance = {start: 0}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]

        for next_node, weight in next_nodes.items():
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
                distance[next_node] = distance[cur_node] + weight

    cur_node = goal
    path = []
    while cur_node != start:
        path.append(cur_node + f'({distance[cur_node]})')
        cur_node = visited[cur_node]
    path.append(start + f'({distance[start]})')
    path.reverse()
    return path, distance[goal]

start = 'CAB'
goal = 'BAT'

path, min_distance = bfs(start, goal, graph)

print(f'\nPath from {start} to {goal}: {"--->".join(path)} = {min_distance}')
