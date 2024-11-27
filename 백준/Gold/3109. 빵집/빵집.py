import sys
input = sys.stdin.readline
R, C = map(int, input().split())
matrix = [list(map(str, input())) for _ in range(R)]

def dfs_upward(x, y):
    if y == C - 1:
        return True
    dy = [1,1,1]
    dx = [-1,0,1] # 위쪽 방향 우선
    isFind = False
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < R and 0 <= ny and ny < C:
            if matrix[nx][ny] == '.':
                if ny == C - 1: return True
                matrix[nx][ny] = 'x'
                isFind = dfs_upward(nx, ny)
                if isFind: break 
    return isFind

def dfs_downward(x, y):
    if y == C - 1:
        return True
    dy = [1,1,1]
    dx = [1,0,-1] # 아래쪽 방향 우선
    isFind = False
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx and nx < R and 0 <= ny and ny < C:
            if matrix[nx][ny] == '.':
                matrix[nx][ny] = 'x'
                isFind = dfs_downward(nx, ny)
                if isFind: break 
    return isFind

answer = 0
for i in range(R):
    if i % 2 == 0:
        i //= 2
        matrix[i][0] = 'x'
        isFind = dfs_upward(i, 0)
        if not isFind:
            matrix[i][0] = '.'
        else:
            answer += 1
    else:
        i += 1
        i //= 2
        i = R - i
        matrix[i][0] = 'x'
        isFind = dfs_downward(i, 0)
        if not isFind:
            matrix[i][0] = '.'
        else:
            answer += 1

print(answer)