from collections import deque
n, m = map(int, input().split())

matrix = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

queue = deque()
min_sum = float("inf")
for st in range(n):
    vis = [-1 for _ in range(n)]
    vis[st] = 0
    queue.append(st)
    depth = 0
    while queue:
        a = queue.popleft()
        for i in range(n):
            if matrix[a][i] == 1 and vis[i] == -1:
                vis[i] = vis[a] + 1
                queue.append(i)
    total = sum(vis)
    if min_sum > total:
        min_sum = min(min_sum, total)
        res = st+1
print(res)