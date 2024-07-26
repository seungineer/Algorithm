def bellman_ford(n, edges):
    dist = [10001] * (n + 1)
    dist[1] = 0
    for i in range(n):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n - 1:  # n번째 반복에서 갱신이 일어나면 음의 사이클 존재
                    return True
    return False

tc = int(input())
for _ in range(tc):
    N, M, W = map(int, input().split())
    edges = []
    
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))
    
    if bellman_ford(N, edges):
        print("YES")
    else:
        print("NO")