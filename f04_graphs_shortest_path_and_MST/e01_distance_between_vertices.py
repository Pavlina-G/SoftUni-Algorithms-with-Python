from collections import deque


def find_parent(graph, source, destination):
    parent = {source: None}

    queue = deque([source])
    visited = {source}

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if child in visited:
                continue
            visited.add(child)
            queue.append(child)
            parent[child] = node

    return parent


def find_path_size(parent, destination):
    path = deque()
    node = destination
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    return len(path) - 1


nodes = int(input())
pairs = int(input())

graph = {}

for _ in range(nodes):
    info = input().split(':')
    node = int(info[0])
    children = [int(x) for x in info[1].split(' ')] if info[1] != '' else []
    graph[node] = children

for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]
    parent = find_parent(graph, source, destination)

    if destination not in parent:
        print(f"{{{source}, {destination}}} -> -1")
        continue

    path_size = find_path_size(parent, destination)

    print(f"{{{source}, {destination}}} -> {path_size}")
