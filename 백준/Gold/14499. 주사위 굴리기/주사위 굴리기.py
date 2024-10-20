n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
inst = list(map(int, input().split()))
dice = [[0] * 3 for _ in range(4)]

for i in inst:
    if i == 4:
        if x + 1 >= n:
            continue
        x += 1
        cur = dice[0][1]
        for j in range(1, 4):
            temp = dice[j][1]
            dice[j][1] = cur
            cur = temp
        dice[0][1] = cur

    if i == 3:
        if x - 1 < 0:
            continue
        cur = dice[3][1]
        for j in range(2, -1, -1):
            temp = dice[j][1]
            dice[j][1] = cur
            cur = temp
        dice[3][1] = cur
        x -= 1

    if i == 2:
        if y - 1 < 0:
            continue
        y -= 1
        cur = dice[3][1]
        for j in range(2, -1, -1):
            temp = dice[1][j]
            dice[1][j] = cur
            cur = temp
        dice[3][1] = cur

    if i == 1:
        if y + 1 >=m:
            continue
        y += 1
        cur = dice[3][1]
        for j in range(0, 3):
            temp = dice[1][j]
            dice[1][j] = cur
            cur = temp
        dice[3][1] = cur
    if arr[x][y] == 0:
        arr[x][y] = dice[3][1]
    else:
        dice[3][1] = arr[x][y]
        arr[x][y] = 0
    print(dice[1][1])