N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append([cost, a, b])
    
edges.sort()

parents = [i for i in range(N+1)]

def find(node):
    parent = parents[node]
    if parent != node:
        parent = find(parent)
        parents[node] = parent
    
    return parent

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a < parent_b: parents[parent_b] = parent_a
    else: parents[parent_a] = parent_b

ans = 0
for i in range(M):
    cost, a, b = edges[i]
    if find(a) == find(b): continue
    union(a, b)
    ans += cost
    max_cost = cost

print(ans - max_cost)
