import heapq as hq
V, E = map(int, input().split())
edges = dict()
for _ in range(E):
    st, en, cost = map(int, input().split())
    if st in edges: edges[st].append([en, cost])
    else: edges[st] = [[en, cost]]
    if en in edges: edges[en].append([st, cost])
    else: edges[en] = [[st, cost]]

vis = [0 for _ in range(V+1)]
waits = []
vis[1] = 1
for next_node, cost in edges[1]:
    hq.heappush(waits, [cost, next_node])
answer = 0
cnt = 0
while waits:
    cost, node = hq.heappop(waits)
    if vis[node] == 1: continue

    vis[node] = 1
    answer += cost
    cnt += 1
    if cnt == V - 1: break

    for next_node, cost in edges[node]:
        if vis[next_node] == 0:
            hq.heappush(waits, [cost, next_node])

print(answer)
