from collections import deque
def solution():
    N, M, K = map(int, input().split())
    matrix = [['.' for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        matrix[x][y] = '#'
    
    def bfs(x, y):
        qu = deque()
        qu.append((x, y))
        matrix[x][y] = '.'
        cnt = 1
        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]
        while qu:
            x, y = qu.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx and nx < N and 0 <= ny and ny < M:
                    if matrix[nx][ny] == '#':
                        matrix[nx][ny] = '.'
                        cnt += 1
                        qu.append((nx, ny))
        
        ans[0] = max(ans[0], cnt)
        
    ans = [0]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '#':
                bfs(i, j)
    
    print(ans[0])

solution()