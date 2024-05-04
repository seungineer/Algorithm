import heapq
import sys
input = sys.stdin.readline
seq = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(seq, [x, x])
    elif x < 0:
        heapq.heappush(seq, [-x, x])
    else:
        try:
            print(heapq.heappop(seq)[1])   
        except:
            print(0)