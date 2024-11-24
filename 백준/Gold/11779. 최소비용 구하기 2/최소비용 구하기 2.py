# n개 도시
# m개 버스(n1 -> n2)
# A -> B 비용 최소 경로
# 경로까지 출력해야 하는 문제
import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = dict()
for _ in range(M):
    st, en, cost = map(int, input().split())
    if st in graph: graph[st].append([cost, en])
    else: graph[st] = [[cost, en]]

START, END = map(int, input().split())

# 최소 비용 구하기
qu = []
st = START
min_cost = [float("inf") for _ in range(N+1)]
path = [st]
hq.heappush(qu, [0, st, path])
while qu:
    prev_cost, st, history = hq.heappop(qu)
    if min_cost[st] <= prev_cost: continue
    
    min_cost[st] = prev_cost

    if min_cost[END] != float("inf"):
        print(min_cost[END])
        print(len(history))
        print(*history)
        break
    
    if not st in graph: continue
    vis = [1e9 for _ in range(N+1)]
    for cost, j in graph[st]:
        if prev_cost + cost <= vis[j]:
            vis[j] = prev_cost + cost
            new_his = [h for h in history]
            new_his.append(j)
            hq.heappush(qu, [prev_cost + cost, j, new_his]) # [비용, 도착지, 경로]
