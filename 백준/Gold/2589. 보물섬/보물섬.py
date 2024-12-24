# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
# matrix 순회하면서 'L'이면 출발
## 가장 멀리 갈 수 있는 거리 업데이트 하기
### 시간 복잡도 O(N^4)

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
matrix = []
for _ in range(N): matrix.append(list(map(str, input().rstrip())))

def bfs(x, y):
    vis = [[0 for _ in range(M)] for _ in range(N)]
    vis[x][y] = 1
    
    qu = deque()
    qu.append([x, y, 0])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while qu:
        x, y, depth = qu.popleft()
        max_len[0] = max(max_len[0], depth)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if vis[nx][ny] == 0 and matrix[nx][ny] == 'L':
                    vis[nx][ny] = 1
                    qu.append([nx, ny, depth + 1])
        
max_len = [-1]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'L':
            bfs(i, j)
print(max_len[0])