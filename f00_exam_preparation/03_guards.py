def create_graph(nodes, edges):
    graph = {}
    for n in range(1, nodes + 1):
        graph[n] = []

    for _ in range(edges):
        first, second = [int(x) for x in input().split()]
        graph[first].append(second)

    return graph


def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)


def find_visited_nodes(start_node, graph, visited):
    for node in range(len(graph)):
        dfs(start_node, graph, visited)


nodes = int(input())
edges = int(input())

graph = create_graph(nodes, edges)
start_node = int(input())

visited = set()

find_visited_nodes(start_node, graph, visited)

for node in graph:
    if node not in visited:
        print(node, end=' ')
