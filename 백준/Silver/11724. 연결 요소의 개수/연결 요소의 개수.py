# dfs를 돌아서 완전한 하나의 연결 요소를 만든다.
# 남은 노드에서 dfs를 시작한다
# dfs에서 완전한 하나의 연결요소를 만든다.
N, M = map(int, input().split())
visited = [0] * (N+1)
graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(V):
    visited[V] = 1
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited[i] == 0:
            dfs(i)
cnt = 0
for j in range(1, N+1):
    if visited[j] == 0:
        dfs(j)
        cnt += 1

print(cnt)