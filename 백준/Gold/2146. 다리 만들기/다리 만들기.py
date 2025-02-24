from collections import deque
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def bfs_numbering(x, y, continent):
        qu = deque()
        vis[x][y] = 1
        matrix[x][y] = continent
        qu.append((x,y))
        while qu:
            x, y = qu.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx and nx < N and 0 <= ny and ny < N:
                    if matrix[nx][ny] == 1 and vis[nx][ny] == 0:
                        vis[nx][ny] = 1
                        matrix[nx][ny] = continent
                        qu.append((nx, ny))
    
    # 대륙별 번호 부여
    bridges = dict()
    num = 1
    vis = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if vis[i][j] == 0 and matrix[i][j] == 1:
                bridges[num] = 0
                bfs_numbering(i, j, num)
                num += 1
    # 대륙 확장
    def bfs_expand(x, y):
        curr = matrix[x][y]
        qu = deque()
        vis[x][y] = 1
        qu.append((x,y))
        while qu:
            x, y = qu.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx and nx < N and 0 <= ny and ny < N:
                    if vis[nx][ny] == 0:
                        vis[nx][ny] = 1
                        if matrix[nx][ny] == curr:
                            qu.append((nx, ny))
                        else:
                            if numbering[nx][ny] == 0:
                                numbering[nx][ny] = curr
                                is_expanded[0] = True
                            elif numbering[nx][ny] != curr:
                                # 확장 도중에 만난 경우
                                continent = numbering[nx][ny]
                                ans[0] = min(ans[0], bridges[curr] + bridges[continent])


    numbering = [[matrix[i][j] for j in range(N)] for i in range(N)]
    ans = [1e9]
    while ans[0] == 1e9:
        checked_continent = set()
        for i in range(N):
            for j in range(N):
                if matrix[i][j] not in checked_continent and matrix[i][j] != 0:
                    checked_continent.add(matrix[i][j])
                    vis = [[0 for _ in range(N)] for _ in range(N)]
                    is_expanded = [False]
                    bfs_expand(i, j)
                    if is_expanded[0]:
                        bridges[matrix[i][j]] += 1
        
        
        matrix = [[numbering[i][j] for j in range(N)] for i in range(N)]
        
    print(ans[0])
    return

solution()

