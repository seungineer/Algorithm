# 현재 키를 가지고, 획득 가능한 키가 추가로 있는지? 달러 개수 몇개인지? BFS 확인
# 1) 키를 추가로 획득한 경우 다시 한 번 확인
# 2) 키를 추가로 회득 못한 경우 획득한 달러만 가지고 break

# while 추가 키 획득:
#   for 0,0부터 돌면서 들어갈 수 있는지 확인:
#       BFS로 돌면서 추가 키 획득 여부 확인(+ x -> .으로 수정)
#       BFS 동안 먹게 되는 달러 개수 확인(+ $ -> .으로 수정) keyCounts[0] += 1
#       if 먹었으면: break
from collections import deque
def solution():
    N, M = map(int, input().split())
    matrix = list(list(map(str, input())) for _ in range(N))
    key_input = input()
    keys = set([ord('.')])
    if key_input != '0':
        for el in key_input: keys.add(ord(el)-32)

    def BFS(st_x, st_y):
        if matrix[st_x][st_y] == '*': return
        num = ord(matrix[st_x][st_y])
        if 65 <= num <= 90: # 대문자
            if not num in keys: return
        if 97 <= num < 122:
            if not (num - 32) in keys: # 소문자 -> 대문자 변환 후 확인
                newKeys[0] = True
                keys.add(num - 32)
                matrix[st_x][st_y] = '.'
        if 36 == num: # $인 경우
            keyCounts[0] += 1
            matrix[st_x][st_y] = '.'

        vis = [[0 for _ in range(M)] for _ in range(N)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        qu = deque()
        qu.append((st_x, st_y))
        vis[st_x][st_y] = 1
        while qu:
            x, y = qu.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx and nx < N and 0 <= ny and ny < M:
                    if vis[nx][ny] == 1 or matrix[nx][ny] == '*': continue
                    vis[nx][ny] = 1
                    
                    num = ord(matrix[nx][ny])
                    if 97 <= num and num <= 122: # 소문자(열쇠) 경우
                        if not (num - 32) in keys: # 소문자 -> 대문자 변환 후 확인
                            newKeys[0] = True
                            keys.add(num - 32)
                        matrix[nx][ny] = '.'    
                        qu.append((nx, ny))
                    
                    if 65 <= num and num <= 90: # 대문자인 경우
                        if not num in keys: continue
                        matrix[nx][ny] = '.'
                        qu.append((nx, ny))
                    
                    if num == 36: # $인 경우
                        keyCounts[0] += 1
                        matrix[nx][ny] = '.'
                        qu.append((nx, ny))
                    
                    if num == 46: # .인 경우
                        qu.append((nx, ny))

    newKeys = [True]
    keyCounts = [0]
    while newKeys[0]:
        newKeys[0] = False
        for outsideX in range(N):
            for outsideY in range(M):
                if outsideX != 0 and outsideX != N-1:
                    if 0 < outsideY and outsideY < M-1: continue
                    BFS(outsideX, outsideY)
                else:
                    BFS(outsideX, outsideY)
                if newKeys[0] == True: break
            if newKeys[0] == True: break
        
    print(keyCounts[0])
TC = int(input())
for _ in range(TC): solution()

