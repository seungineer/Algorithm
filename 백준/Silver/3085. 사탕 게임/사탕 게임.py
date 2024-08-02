# 상하좌우로 돌 수 있는지
# 상하좌우로 스왑 했다고 가정하면
# 연속된 게 몇 개인지 카운팅

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
max_res = -1

def countSerialColor(i,j,color):
    # i행에서 color로 연속되는 거 찾기
    cnt = 0
    max_cnt = -float("inf")
    for b in range(n):
        if matrix[i][b] == color:
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(max_cnt, cnt)
    # j열에서 color로 연속되는 거 찾기
    cnt = 0
    for a in range(n):
        if matrix[a][j] == color:
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(max_cnt, cnt)
    return max_cnt

for i in range(n):
    for j in range(n):
        cnt = countSerialColor(i,j,matrix[i][j])
        max_res = max(max_res, cnt)
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                temp_color = matrix[i][j]
                matrix[i][j] = matrix[nx][ny]
                matrix[nx][ny] = temp_color
                cnt = countSerialColor(i,j,matrix[i][j])
                temp_color = matrix[i][j]
                matrix[i][j] = matrix[nx][ny]
                matrix[nx][ny] = temp_color
                max_res = max(max_res, cnt)
    if max_res == n:
        break
print(max_res)