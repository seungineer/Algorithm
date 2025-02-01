# 그리디하게 가장 작은 값을 현재 일수보다 작게 유지하도록 우선순위 큐를 유지함
import heapq as hq
import sys
input = sys.stdin.readline
N = int(input().rstrip())
seq = dict()
days = set()
for _ in range(N):
    day, score = map(int, input().rstrip().split())
    if day in seq: seq[day].append(score)
    else: seq[day] = [score]
    days.add(day)

days = sorted(list(days))
qu = []

for day in days:
    for score in seq[day]:
        hq.heappush(qu, score)
    while len(qu) > day:
        hq.heappop(qu)

print(sum(qu))
