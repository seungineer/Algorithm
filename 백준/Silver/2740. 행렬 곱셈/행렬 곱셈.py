import sys
read = sys.stdin.readline

cond = list(map(int, read().split()))
w = [list(map(int, read().split())) for _ in range(cond[0])]
cond2 = list(map(int, read().split()))
m = [list(map(int, read().split())) for _ in range(cond2[0])]

n = [[0 for _ in range(cond2[1])] for _ in range(cond[0])]
# 행렬 계산
for k in range(cond[0]): # 3
    for i in range(cond[1]): # 2
        for j in range(cond2[1]): # 3
            n[k][j] += w[k][i] * m[i][j]

for i in range(cond[0]):
    for j in range(cond2[1]):
        print(n[i][j], end=" ")
    print("")