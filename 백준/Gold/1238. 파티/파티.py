import heapq
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
graph_rev = [[] for _ in range(n+1)]
for _ in range(m):
    st, en, w = map(int, input().split())
    graph[st].append([w, en]) # [[], [[2, 4], [3, 2], [4, 7]], [[1, 1], [3, 5]], [[1, 2], [4, 4]], [[2, 3]]]
    graph_rev[en].append([w, st])

queue = []

heapq.heappush(queue, [0, x])
vis = [float("inf") for _ in range(n+1)]
while queue:
    length, st = heapq.heappop(queue)
    if vis[st] < length:
        continue
    vis[st] = length
    for d, en in graph[st]:
        if vis[en] > d + length:
            heapq.heappush(queue, [d+length, en])
vis2 = [float("inf") for _ in range(n+1)]
heapq.heappush(queue, [0, x])
while queue:
    length, st = heapq.heappop(queue)
    if vis2[st] < length:
        continue
    vis2[st] = length
    for d, en in graph_rev[st]:
        if vis2[en] > d + length:
            heapq.heappush(queue, [d+length, en])

print(max([(vis[i]+vis2[i]) for i in range(1, n+1)]))