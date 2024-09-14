import heapq as hq
N, M = map(int, input().split())
graph = {}
vis = [float("inf") for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if a in graph.keys(): graph[a].append([b, c])
    else:
        graph[a] =[[b, c]]
    
    if b in graph.keys(): graph[b].append([a, c])
    else:
        graph[b] =[[a, c]]
qu = []
hq.heappush(qu, [0, 1]) # 소의 개수, 노드

while qu:
    cnt, from_node = hq.heappop(qu)
    vis[from_node] = cnt
    if vis[N] != float("inf") : break
    for to_node, cow in graph[from_node]:
        if vis[to_node] > cnt + cow:
            hq.heappush(qu, [cnt+cow, to_node])
print(vis[N])