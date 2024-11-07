N, M, R = map(int, input().split())
items = list(map(int, input().split()))
graph = [[1e9 for _ in range(N)] for _ in range(N)]

for idx in range(N):
    graph[idx][idx] = 0

for _ in range(R):
    st, en, distance = map(int, input().split())
    st -= 1
    en -= 1
    graph[st][en] = distance
    graph[en][st] = distance

for k in range(N):
    for st in range(N):
        for en in range(N):
            graph[st][en] = min(graph[st][en], graph[st][k] + graph[k][en])

max_items_cnt = -1e9
for pos in range(N):
    items_cnt = items[pos]
    for en in range(N):
        if pos == en : continue
        if graph[pos][en] <= M:
            items_cnt += items[en]
    max_items_cnt = max(max_items_cnt, items_cnt)
print(max_items_cnt)