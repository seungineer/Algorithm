# 다익스트라 시뮬레이션 버전 느낌?
import sys
input = sys.stdin.readline
import heapq as hq
cnt = 0
while True:
    cnt += 1
    N = int(input())
    if N == 0: break
    matrix = []
    matrix =[list(map(int, input().split())) for _ in range(N)]
    vis = [[0 for _ in range(N)] for _ in range(N)]
    target = matrix[-1][-1]
    heapq = []
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    hq.heappush(heapq, [matrix[0][0], 0, 0])
    while heapq:
        length, i, j = hq.heappop(heapq)
        if vis[i][j] == 1: continue
        vis[i][j] = 1
        if i == N - 1 and j == N-1:
            print(f"Problem {cnt}: {length}")
            break
        matrix[i][j] = length
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni and ni < N and 0 <= nj and nj < N:
                if vis[ni][nj] == 0:
                    hq.heappush(heapq, [length + matrix[ni][nj], ni, nj])
