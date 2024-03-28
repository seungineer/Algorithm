import sys
sys.setrecursionlimit(10**9)

N = int(input())
matrix = [[] for _ in range(N)]
for i in range(N):
    seq = str(input().strip())
    for j in seq:
        matrix[i].append(j)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 시작 지점 0, 0
cnt = 0
def dfs(x, y, area_number):
    if not (0<=x<=N-1 and 0<=y<=N-1) or matrix[x][y] == '0':
        return
    
    # cnt += 1
    area_number = matrix[x][y]
    matrix[x][y] = '0'
    tot_area_lst[0] += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny, area_number)

restart_x = 0
restart_y = 0 # 초기 시작 지점
tot_area_lst = [0]
answer = []

while True:
    flag = False       
    x, y = restart_x , restart_y
    area_number = matrix[x][y]
    
    dfs(x, y, area_number)
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '1':
                restart_x, restart_y = i, j
                flag = True
                
                break
        if flag:
            break
    
    #print(tot_area_cnt) # 토탈 지역 수
    # print(tot_area_lst[0]) # 토탈 지역 수  
    if tot_area_lst[0] != 0:
        answer.append(tot_area_lst[0])
    tot_area_lst[0] = 0
    if flag == False:    
        break

print(len(answer))
answer.sort()
for temp in answer:
    print(temp)

    
