import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
r, c = map(int, input().split())
matrix = []
for _ in range(r):
    matrix.append(list(map(str, input())))
max_length = [-1]
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]

def dfs(x, y, ban_set, length):
    max_length[0] = max(max_length[0], length)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx <r and 0 <= ny and ny < c:
            if matrix[nx][ny] in ban_set:
                continue
            ban_set.add(matrix[nx][ny])
            dfs(nx, ny, ban_set, length+1)
            ban_set.remove(matrix[nx][ny])
banset = set()
banset.add(matrix[0][0])    
dfs(0,0,banset,1)
print(max_length[0])