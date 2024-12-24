from collections import defaultdict

datas = []
with open("Day23.txt", "r") as file:
    for line in file:
        datas.append(tuple(sorted(line.strip().split('-'))))

network_set = set(datas)

graph = defaultdict(set)
for a, b in network_set:
    graph[a].add(b)
    graph[b].add(a)

def dfs(node, path, visited, results):
    if len(path) == 3:
        a, b, c = sorted(path)  
        if b in graph[a] and c in graph[a] and c in graph[b]:
            if any(computer.startswith('t') for computer in (a, b, c)):
                results.add((a, b, c))
        return

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(neighbor, path + [neighbor], visited, results)
            visited.remove(neighbor)

results = set()
for start_node in graph:
    dfs(start_node, [start_node], {start_node}, results)

print(len(results))

## Part 2

from collections import defaultdict

datas = []
with open("Day23.txt", "r") as file:
    for line in file:
        datas.append(tuple(sorted(line.strip().split('-'))))

network_set = set(datas)

graph = defaultdict(set)
for a, b in network_set:
    graph[a].add(b)
    graph[b].add(a)

def bron_kerbosch(r, p, x, cliques):
    if not p and not x:
        cliques.append(r)
        return
    for node in list(p):
        bron_kerbosch(
            r.union({node}),
            p.intersection(graph[node]),
            x.intersection(graph[node]),
            cliques
        )
        p.remove(node)
        x.add(node)

cliques = []
bron_kerbosch(set(), set(graph.keys()), set(), cliques)

largest_clique = max(cliques, key=len)

password = ','.join(sorted(largest_clique))

print("Password to the LAN party:", password)
