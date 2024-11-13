# dfs로 순회하면서 치즈 속에 포함된 영역 표시
## 가장 자리로 갈 수 있으면 포함 영역이 아님
# 임시 매트릭스에 가두리로 지울 부분 표시
# 실제로 지우기
## 치즈가 없을 때까지 반복
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
original_matrix = [list(map(int, input().split())) for _ in range(N)]
qu = deque()

def bfs(i, j):
    qu.append([i, j])
    while qu:
        i, j = qu.popleft()
    
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if original_matrix[nx][ny] == 0:
                    qu.append([nx, ny])
                    original_matrix[nx][ny] = 2

def deleteOuter():
    for i in range(1, N-1):
        for j in range(1, M-1):
            if original_matrix[i][j] == 1:
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]
                air_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx and nx < N and 0 <= ny and ny < M:
                        if original_matrix[nx][ny] == 2: air_cnt += 1
                if air_cnt >= 2: original_matrix[i][j] = 0
    

isStop = False
answer = 0
while not isStop:
    # print(original_matrix)
    vis = [[0 for _ in range(M)] for _ in range(N)]
    vis[0][0] = 1
    bfs(0, 0)
    deleteOuter()
    isStop = True
    for c in range(N):
        for d in range(M):
            if original_matrix[c][d] == 1: isStop = False
            if original_matrix[c][d] == 2: original_matrix[c][d] = 0
    
    if not isStop: answer += 1
    else: break

print(answer + 1)
