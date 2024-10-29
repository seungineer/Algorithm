import heapq
N, E = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
v1, v2 = map(int, input().split())
must_points = [v1-1, v2-1]
answer = []
for k in range(2):
    short = [0 for _ in range(N)]
    qu = []
    heapq.heappush(qu, [0, 0]) # 거리, 시작 지점
    first_point = -1
    while qu:
        distance, st = heapq.heappop(qu)
        short[st] = distance
        if st == must_points[k%2]:
            first_point = st
            first_dist = distance
            break
        for i in range(N):
            if graph[st][i] > 0 and short[i] == 0:
                heapq.heappush(qu, [distance + graph[st][i], i])

    if not st == must_points[k%2]:
        continue
    short = [0 for _ in range(N)]
    qu = []
    # print(k,st, first_dist)
    if first_point == -1: continue
    heapq.heappush(qu, [first_dist, first_point]) # 거리, 시작 지점
    second_point = -1
    while qu:
        distance, st = heapq.heappop(qu)
        short[st] = distance
        if st == must_points[(k+1)%2]:
            second_point = st
            second_dist = distance
            break
        for i in range(N):
            if graph[st][i] > 0 and short[i] == 0:
                heapq.heappush(qu, [distance + graph[st][i], i])
    if not st == must_points[(k+1)%2]:
        continue
    short = [0 for _ in range(N)]
    qu = []
    # print(k,st, second_dist)
    if second_point == -1: continue
    heapq.heappush(qu, [second_dist, second_point]) # 거리, 시작 지점
    while qu:
        distance, st = heapq.heappop(qu)
        # print(distance, st)
        short[st] = distance
        if st == N-1:
            answer.append(distance)
            break
        for i in range(N):
            if graph[st][i] > 0 and short[i] == 0:
                heapq.heappush(qu, [distance + graph[st][i], i])
    #print(answer)
if answer: print(min(answer))
else: print(-1)