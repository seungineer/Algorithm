from collections import deque
cog = [list(map(int, input())) for _ in range(4)]

K = int(input())

for _ in range(K):
    num, direction = map(int, input().split())
    if direction == 1: clockwise = True
    else: clockwise = False
    rotate_seq = deque()
    rotate_seq.append([num-1, clockwise])
    vis = [0,0,0,0]
    vis[num-1] = 1
    while rotate_seq:
        num, clockwise = rotate_seq.popleft()
        side = [-1, 1]
        for i in range(2):
            new_num = num + side[i]
            if 0 <= new_num and new_num < 4 and vis[new_num] == 0:
                if i == 0: # 뉴넘은 왼쪽
                    if cog[new_num][2] != cog[num][6]:
                        vis[new_num] = 1
                        rotate_seq.append([new_num, not clockwise])
                else: # 뉴넘은 오른쪽
                    if cog[new_num][6] != cog[num][2]:
                        vis[new_num] = 1
                        rotate_seq.append([new_num, not clockwise])
        # num을 clockwise로 돌려
        if clockwise:   
            temp = cog[num][7]
            cog[num].append(temp)
            for i in range(7):
                cog[num].append(cog[num][i])
            cog[num] = cog[num][8:16]
        else:
            temp = cog[num][0]
            for i in range(1, 8):
                cog[num].append(cog[num][i])
            cog[num].append(temp)
            cog[num] = cog[num][8:16]
        
answer = 0
for i in range(4):
    if cog[i][0] == 1: answer += 2**i
print(answer)