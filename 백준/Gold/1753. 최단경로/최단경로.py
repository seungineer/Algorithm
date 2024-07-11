import heapq
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
st = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    try:
        graph[a].append([w,b]) #[[가중치, a->b]]
    except:
        graph[a] = [[w,b]] #[[], [[2, 2], [3, 3]], [[3, 4], [4, 5]], [[4, 6]], [], [[1, 1]]]

res = []
vis = [0 for _ in range(v+1)]
for i in range(len(graph[st])):
    heapq.heappush(res, [graph[st][i][0], graph[st][i][1]])

while res:
    nw, nst = heapq.heappop(res)
    if vis[nst] != 0: # new_start 노드 방문 안 했었으면,
        continue
    vis[nst] = nw
    for i in range(len(graph[nst])):
        if vis[graph[nst][i][1]] == 0:
            heapq.heappush(res, [graph[nst][i][0] + nw, graph[nst][i][1]])

for i in range(1, v+1):
    if i == st:
        print(0)
    else:
        if vis[i] == 0:
            print("INF")
        else:
            print(vis[i]) 