import heapq
import sys

read = sys.stdin.readline

n = int(read())
seq = [int(read().strip()) for i in range(n)]

max_heap = []
min_heap = []

for i in seq:
    if len(max_heap) == len(min_heap):
        # print(f"idx : {i} check1")
        heapq.heappush(max_heap, -i)
    else:
        # print(f"idx : {i} check2")
        heapq.heappush(min_heap, i)
    if len(min_heap) == 0:
        # print(f"idx : {i} check3")
        print(-max_heap[0])
        continue
    while -max_heap[0] > min_heap[0]:
        # print(f"idx : {i} check4")
        temp = heapq.heappop(min_heap)
        temp2 = heapq.heappop(max_heap)
        heapq.heappush(max_heap, -temp)
        heapq.heappush(min_heap, -temp2)

    print(-max_heap[0])
