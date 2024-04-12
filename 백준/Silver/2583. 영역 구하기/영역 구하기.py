from collections import deque

m, n, k = map(int, input().split()) # 세로, 가로, 개수

matrix = [[0 for _ in range(n)] for _ in range(m)]
# 패딩으로 둘러 싸지 않고, 갈 수 있는 범위로 지정해야겠다.
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split()) # 0 2 4 4
    
    for j in range(y2, y1, -1):
        for k in range(x1, x2):
            matrix[m-j][k] = 1



def bfs(x, y):

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    num_zero_cnt = 0
    matrix[y][x] = 1
    queue.append([x, y]) # x, y, num_zero    
    
    while queue:
        x, y = map(int, queue.popleft())
        num_zero_cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0 or matrix[ny][nx] == 1 :
                continue
            else:
                matrix[ny][nx] = 1
                queue.append([nx, ny])
          
    return num_zero_cnt

res = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:            
            res.append(bfs(j, i))

print(len(res))
print(*sorted(res))