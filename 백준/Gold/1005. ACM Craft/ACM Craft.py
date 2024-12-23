import sys
from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    cost = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(n)]
    edges_cnt = [0 for _ in range(n)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a-1].append(b-1)
        edges_cnt[b-1] += 1
        
    W = int(sys.stdin.readline())
    queue = deque([])

    dp = [0 for _ in range(n)]
    
    for i in range(n):
        if edges_cnt[i] == 0:
            queue.append(i)
            dp[i] = cost[i]

    while queue:
        c_n = queue.popleft()
        for i in graph[c_n]:
            dp[i] = max(dp[i], dp[c_n] + cost[i])
            edges_cnt[i] -= 1
            if edges_cnt[i] == 0:
                queue.append(i)

    print(dp[W-1])