# Source removal top-sort algorith
# create an empty list
# repeat until the graph is empty
# find a node without incoming edges
# print this node or add it to a collection
# remove the edge from the graph

def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    return result


nodes = int(input())
graph = {}

for _ in range(nodes):
    node, children = input().split(' ->')
    children = [] if children == '' else children.strip().split(', ')
    graph[node] = children

dependency_by_node = find_dependencies(graph)


def find_node_without_dependencies(dependency_by_node):
    for node, dependency in dependency_by_node.items():
        if dependency == 0:
            return node
    return None


has_cycle = False
sorted_nodes = []
while dependency_by_node:
    node_to_remove = find_node_without_dependencies(dependency_by_node)
    if node_to_remove is None:
        has_cycle = True
        break
    for child in graph[node_to_remove]:
        dependency_by_node[child] -= 1
    sorted_nodes.append(node_to_remove)
    dependency_by_node.pop(node_to_remove)

if has_cycle:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")
