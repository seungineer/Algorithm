   
import sys
from collections import deque
read = sys.stdin.readline
N, M, K, start = map(int, read().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)

visited = [0] * (N+1)

# n_d를 리스트로 변경: 거리 K에 해당하는 노드들만 저장하는 리스트
nodes_at_distance_k = []

def bfs(V):
    queue = deque()
    queue.append([V, 0])  # [노드 번호, 시작점으로부터의 거리]
    visited[V] = 1
    while queue:
        v, dist = queue.popleft()
        if dist == K:
            nodes_at_distance_k.append(v)  # 거리가 K인 노드만 저장
        for i in graph[v]:
            if visited[i] == 0:
                queue.append([i, dist + 1])  # 거리를 1 증가시켜 큐에 추가
                visited[i] = 1

bfs(start)

if nodes_at_distance_k:
    nodes_at_distance_k.sort()
    for node in nodes_at_distance_k:
        print(node)
else:
    print(-1)
