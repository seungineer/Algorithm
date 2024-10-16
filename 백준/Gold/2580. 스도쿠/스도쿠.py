import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

matrix = [list(map(int, input().split()))]
n = len(matrix[0])
for _ in range(1, n):
    matrix.append(list(map(int, input().split())))

def check(i, j, target):
    if target in matrix[i]:
        return False
    for n in range(len(matrix[0])):
        if target == matrix[n][j]:
            return False
    box_i = i // 3
    box_j = j // 3
    for a in range(3 * box_i, 3 * box_i + 3):
        for b in range(3 * box_j, 3 * box_j + 3):
            if target == matrix[a][b]: return False
    return True

def dfs(st_i, st_j):
    for num in range(1, 10):
        if check(st_i, st_j, num):
            matrix[st_i][st_j] = num
            isStop = False
            for i in range(n):
                for j in range(n):
                    if i == st_i and j == st_j: continue
                    if matrix[i][j] == 0:
                        dfs(i, j)
                        matrix[st_i][st_j] = 0
                        isStop = True
                    if isStop: break
                if isStop: break
            if not isStop:
                for m in matrix:
                    print(*m)
                exit()
    
# dfs(0,0)
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0: dfs(i, j)