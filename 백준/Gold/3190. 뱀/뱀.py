N = int(input())
matrix = [[0 for _ in range(N+2)] for _ in range(N+2)]
for i in range(N+2):
    for j in range(N+2):
        if i == 0 or i == N+1:
            matrix[i][j] = 2
        else:
            if j == 0 or j == N+1:
                matrix[i][j] = 2

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    matrix[a][b] = 1
turn_dic = {}
L = int(input())
for _ in range(L):
    sec, direction = input().split()
    turn_dic[int(sec)] = direction

head_x = 1
head_y = 1

# 기본은 동쪽 바라봄
# L 오면 왼쪽 바라봄(북쪾) 또 L오면 서쪾 또 L오면 남쪽
# D 오면 아래쪽 바라봄(남쪾) 또 D오면 서쪾 또 D오면 북쪽
## 0에서 L이 오면 +1
## 0에서 D가 오면 -1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
le = 0
from collections import deque
answer = 0
qu = deque()
qu.append([head_x, head_y]) # 시작 지점
while True:
    if matrix[head_x][head_y] != 1:
        a, b = qu.popleft()
        matrix[a][b] = 0
    qu.append([head_x, head_y])
    matrix[head_x][head_y] = 2
    if answer in turn_dic.keys():
        if turn_dic[answer] == 'L':
            le += 1
            if le == 4: le = 0
        else:
            le -= 1
            if le == -1: le = 3

    nh_x = head_x + dx[le]
    nh_y = head_y + dy[le]
    if matrix[nh_x][nh_y] == 2:
        answer += 1
        break
    else:
        head_x, head_y = nh_x, nh_y
        answer += 1 #가능하니까 반복문 돈 거임

print(answer)