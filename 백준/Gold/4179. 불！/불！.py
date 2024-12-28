from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
matrix = [list(map(str, input().rstrip())) for _ in range(N)]

fires = [[int(1e9) for _ in range(M)] for _ in range(N)]
jihoons = [[int(1e9) for _ in range(M)] for _ in range(N)]

qu = deque()
qu2 = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'F':
            fires[i][j] = 0
            qu.append([i, j, 0])
        if matrix[i][j] == 'J':
            jihoons[i][j] = 0
            if i == 0 or i == N-1 or j == 0 or j == M-1:        
                print(1)
                exit()
            qu2.append([i, j, 0])
      
while qu:
    x, y, time = qu.popleft()
    fires[x][y] = min(fires[x][y], time)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < N and 0 <= ny and ny < M:
            if matrix[nx][ny] != '#':
                if time + 1 < fires[nx][ny]:
                    fires[nx][ny] = time + 1
                    qu.append([nx, ny, time + 1])

while qu2:
    x, y, time = qu2.popleft()
    
    if time < fires[x][y]:
        jihoons[x][y] = min(jihoons[x][y], time)
    else:
        continue
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < N and 0 <= ny and ny < M:
            if matrix[nx][ny] != '#':
                if time + 1 < jihoons[nx][ny] and time + 1 < fires[nx][ny]:
                    jihoons[nx][ny] = time + 1
                    qu2.append([nx, ny, time + 1])

ans = int(1e10)
for i in range(N):
    for j in range(M):
        if i != 0 and i != N-1:
            if j == 0 or j == M-1:
                ans = min(ans, jihoons[i][j])
            else: continue
        else:
            ans = min(ans, jihoons[i][j])

if ans == int(1e9): print("IMPOSSIBLE")
else: print(ans+1)