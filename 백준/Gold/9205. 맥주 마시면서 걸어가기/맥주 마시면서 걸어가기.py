import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N = int(input())
    st_x, st_y = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(N)]
    en_x, en_y = map(int ,input().split())
    matrix = dict()
    for i in range(N):
        x1, y1 = stores[i]
        if abs(x1 - st_x) + abs(y1 - st_y) > 1000: continue
        if (x1, y1) in matrix: matrix[(x1, y1)].append((st_x, st_y))
        else: matrix[(x1, y1)] = [(st_x, st_y)]
        if (st_x, st_y) in matrix: matrix[(st_x, st_y)].append((x1, y1))
        else: matrix[(st_x, st_y)] = [(x1, y1)]

    for i in range(N):
        x1, y1 = stores[i]
        for j in range(N):
            if i == j: continue
            x2, y2 = stores[j]
            if abs(x1-x2) + abs(y1-y2) > 1000: continue
            if (x1, y1) in matrix: matrix[(x1, y1)].append((x2, y2))
            else: matrix[(x1, y1)] = [(x2, y2)]
            if (x2, y2) in matrix: matrix[(x2, y2)].append((x1, y1))
            else: matrix[(x2, y2)] = [(x1, y1)]
    qu = deque()
    vis = set()
    qu.append((st_x, st_y))
    vis.add((st_x, st_y))
    while qu:
        x, y = qu.popleft()
        if abs(x-en_x) + abs(y-en_y) <= 1000:
            print("happy")
            return
        if not (x, y) in matrix: continue
        for nx, ny in matrix[(x, y)]:
            if (nx, ny) in vis: continue
            vis.add((nx, ny))
            qu.append((nx, ny))
    print("sad")
    
TC = int(input().rstrip())
for _ in range(TC):
    solution()
