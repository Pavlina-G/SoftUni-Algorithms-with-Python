from collections import deque


def find_parent_by_node(nodes, graph):
    visited = [False] * (nodes)
    parent = [None] * (nodes)

    visited[start_node - 1] = True
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node == end_node:
            break
        for child in graph[node - 1]:
            if visited[child - 1]:
                continue
            visited[child - 1] = True
            queue.append(child)
            parent[child - 1] = node

    return parent


def find_shortest_path(parent, end_node):
    path = deque()
    node = end_node
    while node is not None:
        path.appendleft(node)
        node = parent[node - 1]

    return path


nodes = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges_count):
    source, destination = [int(x) for x in input().split()]
    graph[source - 1].append(destination)

start_node = int(input())
end_node = int(input())

parent = find_parent_by_node(nodes, graph)
path = find_shortest_path(parent, end_node)

print(f"Shortest path length is: {len(path) - 1}")
print(*path, sep=' ')
