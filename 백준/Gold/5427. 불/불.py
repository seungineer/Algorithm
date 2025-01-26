import sys
from collections import deque
input = sys.stdin.readline

def solution():
    M, N = map(int, input().rstrip().split())
    matrix = list(list(map(str, input().rstrip())) for _ in range(N))
    fires = [[1000001 for _ in range(M)] for _ in range(N)]
    moves = [[0 for _ in range(M)] for _ in range(N)]
    
    # 불 위치 qu에 담기 / 상근이 시작지점 찾기
    qu = deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '*': qu.append((i,j,0)) # (x, y, 시간)
            if matrix[i][j] == '@': st_x, st_y = i, j # 상근이 시작지점
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while qu:
        x, y, time = qu.popleft()
        if fires[x][y] <= time: continue
        fires[x][y] = time
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if matrix[nx][ny] != '#': # 벽만 아니면 됨
                    if time + 1 < fires[nx][ny]:
                        qu.append((nx, ny, time+1))
    
    # 상근이는 fires의 숫자보다 더 작은 경우 qu에 추가
    qu.append((st_x, st_y, 0))
    isEscape = False
    while qu:
        x, y, time = qu.popleft()
        moves[x][y] = 1
        if fires[x][y] < time: continue
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if matrix[nx][ny] == '.' and moves[nx][ny] == 0:
                    moves[nx][ny] = 1
                    if time + 1 < fires[nx][ny]:
                        qu.append((nx, ny, time+1))
            else:
                print(time+1) # 탈출 성공
                isEscape = True
                break
        if isEscape: break
    if not isEscape:
        print("IMPOSSIBLE")

TC = int(input())
for _ in range(TC): solution()