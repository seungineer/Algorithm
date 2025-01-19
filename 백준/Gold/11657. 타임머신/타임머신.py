N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])
distances = [int(1e9) for _ in range(N+1)]
distances[1] = 0
def bm():
    for k in range(N):
        for i in range(M):
            a, b, cost = edges[i]
            if distances[a] != int(1e9) and distances[b] > distances[a] + cost:
                distances[b] = distances[a] + cost
                if k == N -1 :
                    return False
    return True
if bm():
    for i in range(2, N+1):
        if distances[i] == int(1e9): print(-1)
        else: print(distances[i])
else:
    print(-1)