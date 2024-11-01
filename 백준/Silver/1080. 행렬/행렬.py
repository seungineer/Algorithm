N, M = map(int, input().split())
matrixA = [list(map(int, input())) for _ in range(N)]
mani = [[] for _ in range(N)]
for i in range(N):
    lst = list(map(int, input()))
    for j in range(M):
        if lst[j] != matrixA[i][j]:
            mani[i].append('Y')
        else:
            mani[i].append('N')

if N < 3 or M < 3:
    for i in range(N):
        for j in range(M):
            if mani[i][j] == 'Y':
                print(-1)
                exit()
    print(0)
    exit()

def check(i, j):
    standardx, standardy = i -1, j - 1
    if mani[standardx][standardy] == 'Y':
        return True
    else:
        return False
cnt = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if check(i, j):
            cnt += 1
            dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
            dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
            for k in range(9):
                ni = i + dx[k]
                nj = j + dy[k]
                if mani[ni][nj] == 'Y': mani[ni][nj] = 'N'
                else:  mani[ni][nj] = 'Y'

for i in range(N):
    for j in range(M):
        if mani[i][j] == 'Y':
            print(-1)
            exit()
print(cnt)
