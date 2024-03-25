import sys
sys.setrecursionlimit(10**9)
read = sys.stdin.readline
N = int(read())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def dfs(V):
    for i in graph[V]:
        if visited[i] == 0 :
            visited[i] = V
            dfs(i)

dfs(1)
for j in range(2, N+1):
    print(visited[j])
