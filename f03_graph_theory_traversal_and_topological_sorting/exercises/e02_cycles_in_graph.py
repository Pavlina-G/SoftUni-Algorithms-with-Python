def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    cycles.remove(node)


graph = {}

while True:
    line = input()
    if line == 'End':
        break
    parent_node, child_node = line.split('-')
    if parent_node not in graph:
        graph[parent_node] = []
    if child_node not in graph:
        graph[child_node] = []
    graph[parent_node].append(child_node)

try:
    visited = set()
    cycles = set()
    for node in graph:
        dfs(node, graph, visited, cycles)
    print("Acyclic: Yes")
except Exception:
    print("Acyclic: No")
