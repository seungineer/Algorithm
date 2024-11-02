import heapq
N, M = map(int, input().split())
seq = list(map(int, input().split()))
heapq.heapify(seq)
for _ in range(M):
    prev_x1 = heapq.heappop(seq)
    prev_x2 = heapq.heappop(seq)
    heapq.heappush(seq, prev_x1 + prev_x2)
    heapq.heappush(seq, prev_x1 + prev_x2)

print(sum(seq))