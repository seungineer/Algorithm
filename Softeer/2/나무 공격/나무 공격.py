import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
l1, r1 = map(int, input().split())
l2, r2 = map(int, input().split())

attackCounts = [0 for _ in range(N+1)]
for k in range(l1, r1+1):
    attackCounts[k] += 1
for k in range(l2, r2+1):
    attackCounts[k] += 1
answer = 0
for r in range(N):
    row = matrix[r]
    mansCnt = sum(row)
    leftMan = mansCnt - attackCounts[r+1]
    if leftMan < 0: leftMan = 0
    answer += leftMan
print(answer)