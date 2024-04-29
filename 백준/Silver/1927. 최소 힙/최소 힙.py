import heapq
import sys
input = sys.stdin.readline
n = int(input())
seq = []

for _ in range(n):
    k = int(input())
    if k == 0:
        if len(seq)!=0:
            print(heapq.heappop(seq))
        else:
            print(0)
    else:
        heapq.heappush(seq, k)