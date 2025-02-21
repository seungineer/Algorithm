import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[False for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    
for k in range(1, N+1):
    for x in range(1, N+1):
        for y in range(1, N+1):
            if graph[x][k] and graph[k][y]:
                graph[x][y] = True

ans = 0
for x in range(1, N+1):
    cnt = 0
    for y in range(1, N+1):
        if graph[x][y]: cnt +=1
        if graph[y][x]: cnt +=1
    if cnt == N-1: ans+=1
    
print(ans)