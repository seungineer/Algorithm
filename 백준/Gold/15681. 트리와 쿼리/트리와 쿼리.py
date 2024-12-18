import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N, R, Q = map(int, input().rstrip().split())
trees = dict()
for _ in range(N-1):
    u, v = map(int, input().rstrip().split())
    if u in trees: trees[u].append(v)
    else: trees[u] = [v]
    if v in trees: trees[v].append(u)
    else: trees[v] = [u]

queries = []
for _ in range(Q):
    queries.append(int(input().rstrip()))

size = [0 for _ in range(N+1)]
vis = [0 for _ in range(N+1)]
def dfs(node):
    vis[node] = 1
    for next_node in trees[node]:
        if vis[next_node] == 0:
            vis[next_node] = 1
            dfs(next_node)
            size[node] += size[next_node]
    size[node] += 1

vis[R] = 1
dfs(R)
for q in queries: print(size[q])