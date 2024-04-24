from collections import deque

graph = {'S': {'G': 3, 'X': 2},
         'G': {'S': 3, 'F': 4, 'H': 2},
         'X': {'S': 2, 'H': 3, 'M': 5},
         'H': {'X': 3, 'G': 2},
         'M': {'X': 5, 'F': 4},
         'F': {'G': 4, 'M': 4}}


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

start = 'S'
goal = 'F'

path, min_distance = bfs(start, goal, graph)

print(f'\nPath from {start} to {goal}: {"--->".join(path)} = {min_distance}')
