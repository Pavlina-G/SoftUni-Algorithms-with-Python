from collections import deque


def dfs(node, graph, visited, cycled, sorted_nodes):
    if node in cycled:
        return
    if node not in visited:

        visited.add(node)
        cycled.add(node)
        for child in graph[node]:
            dfs(child, graph, visited, cycled, sorted_nodes)

        cycled.remove(node)
        sorted_nodes.appendleft(node)


graph = {}

while True:
    command = input()
    if command == 'End':
        break
    node, children = command.split(' ->')
    children = [] if children == '' else children.strip().split(' ')
    graph[node] = children

visited = set()
cycled = set()
sorted_nodes = deque()

for node in graph:
    dfs(node, graph, visited, cycled, sorted_nodes)
print(f"{' '.join(sorted_nodes)}")
