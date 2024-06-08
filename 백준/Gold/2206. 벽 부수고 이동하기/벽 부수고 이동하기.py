from collections import deque

n, m = map(int, input().split())
matrix = [[[0,0] for _ in range(m)]for _ in range(n)]
for i in range(n):
    str = input()
    for j in range(len(str)):
        matrix[i][j] = ([str[j],str[j]])
#bfs, 상태를 첨부한 bfs

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
wait_lst = deque()
wait_lst.append([0,0,False,1]) #[x(n), y(m), 벽 부쉈었는지 여부, 거리]

while wait_lst:
    x, y, isBroken, cnt = wait_lst.popleft()
    if x == n-1 and y == m-1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if isBroken:
            if matrix[nx][ny][1] == '1':
                continue
            else:
                wait_lst.append([nx, ny, True, cnt+1])
                matrix[nx][ny][1] = '1'
        else:
            if matrix[nx][ny][0] == '1':
                wait_lst.append([nx, ny, True, cnt+1])
                continue
            else:
                wait_lst.append([nx, ny, False, cnt+1])
                
                matrix[nx][ny][0] = '1'

if x == n-1 and y == m-1:
    print(cnt)
else:
    print(-1)