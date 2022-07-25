def find_rood(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


towns = int(input())
roads = int(input())
map = []

for _ in range(roads):
    first, second, weight = [int(x) for x in input().split(' - ')]
    map.append((first, second, weight))

parent = [num for num in range(towns)]
total_cost = 0

for first, second, weight in sorted(map, key=lambda r: r[2]):
    first_node_root = find_rood(parent, first)
    second_node_root = find_rood(parent, second)

    if first_node_root == second_node_root:
        continue
    parent[first_node_root] = second_node_root
    total_cost += weight

print(f"Total cost: {total_cost}")
