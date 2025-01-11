import sys
sys.setrecursionlimit(10**6)
def solution():
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    slopes = dict()
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx and nx < N and 0 <= ny and ny < N:
                    if matrix[i][j] > matrix[nx][ny]:
                        if (i, j) in slopes: slopes[(i, j)].append((nx, ny))
                        else: slopes[(i,j)] = [(nx, ny)]
    # dfs에서 자신이 받을 수 있는 가장 큰 값을 받아 vis에 할당
    # highest 값이 -1이 아니라면 그 값을 받고 더이상 dfs로 들어가지 않도록 함
    
    def dfs(x, y, depth):
        if highest[x][y] != -1:
            return highest[x][y]
        
        if not (x,y) in slopes:
            highest[x][y] = 1
            return 1
        
        max_h = -1
        for nx, ny in slopes[(x, y)]:
            if highest[nx][ny] != -1:
                max_h = max(max_h, highest[nx][ny] + 1)
            else:
                res = dfs(nx, ny, depth + 1)
                max_h = max(max_h, res + 1)
        
        highest[x][y] = max_h
        return max_h
        
    
    highest = [[-1 for _ in range(N)] for _ in range(N)]
    ans = 1
    for i, j in slopes.keys():
        if highest[i][j] == -1:
            max_h = dfs(i, j, 1)
            ans = max(ans, max_h)
            highest[i][j] = max_h
    
    print(ans)
    
    return
solution()