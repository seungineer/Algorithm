# n+1 세대 드래곤 커브는 끝점을 기준으로 시계 방향으로 90도 회전
# 이 끝점이라고 하는 것은 n세대의 시작점임
N = int(input())
matrix = [[0 for _ in range(101)] for _ in range(101)] #101범위까지 필요

cmd = [] #[[x, y, dir, gen]] 도달해야 하는 gen 
for _ in range(N):
    cmd.append(list(map(int, input().split())))

def addTransformPoints(points, x_st, y_st, x, y): #1,1
    x_en = float("inf")
    y_en = float("inf")
    temp_res = []
    for p in points:
        x1, y1 = p # 4, 2
        # ( cos90, -sin90)
        # ( sin90, cos90 )
        vx, vy = x1 - x, y1- y # 0, 1 
        temp_x, temp_y = x - vy ,y + vx
        matrix[temp_y][temp_x] = 1
        temp_res.append([temp_x, temp_y])
        if x1 == x_st and y1 == y_st:
            x_en = temp_x
            y_en = temp_y
    for t in temp_res:
        points.append(t)
    return x_en, y_en, x_st, y_st

dict = {
    0: [1,0],
    1: [0, -1],
    2: [-1, 0],
    3: [0, 1],
}
for c in cmd:
    x_st, y_st, direction, generation = c
    gen = 0
    points = []
    matrix[y_st][x_st] = 1
    points.append([x_st, y_st])
    matrix[y_st + dict[direction][1]][x_st + dict[direction][0]] = 1
    points.append([x_st + dict[direction][0], y_st + dict[direction][1]])
    x_en, y_en = x_st + dict[direction][0], y_st + dict[direction][1]
    # 0세대 그리기 완료
    if generation != 0:
        while True:
            x_en, y_en, x_st, y_st = addTransformPoints(points, x_st, y_st, x_en, y_en) # 90도 회전하면서 매트릭스에 표시하기
            
            gen += 1
            if gen == generation:
                break
    # 추가 세대 그리기 완료

dr = [-1, -1, 0]
dc = [0, 1, 1]
answer = 0
for r in range(1, 101):
    for c in range(101):
        cnt1 = 0
        if matrix[r][c] == 1:
            cnt1 += 1
            for k in range(3):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr and nr < 101 and 0 <= nc and nc < 101:
                    if matrix[nr][nc] == 1:
                        cnt1 += 1
            if cnt1 == 4:
                answer += 1

print(answer)