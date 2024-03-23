import sys
import heapq
read = sys.stdin.readline

n = int(read())
heap = []


for _ in range(n):
    heapq.heappush(heap, int(read()))
total = 0

while len(heap) != 1:
    temp1 = heapq.heappop(heap)
    temp2 = heapq.heappop(heap)
    total += temp1 + temp2
    heapq.heappush(heap, temp1 + temp2)

print(total)