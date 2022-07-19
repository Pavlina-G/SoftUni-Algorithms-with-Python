def dfs(node, town, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in town[node]:
        dfs(child, town, visited)


buildings = int(input())
streets = int(input())

town = []
[town.append([]) for b in range(buildings)]

edges_streets = []

for _ in range(streets):
    first, second = [int(x) for x in input().split(' - ')]
    town[first].append(second)
    town[second].append(first)
    edges_streets.append((min(first, second), max(first, second)))

print(f"Important streets:")

for first, second in edges_streets:
    town[first].remove(second)
    town[second].remove(first)

    visited = [False] * buildings
    dfs(0, town, visited)

    if not all(visited):
        print(first, second)

    town[first].append(second)
    town[second].append(first)
