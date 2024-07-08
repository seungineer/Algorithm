import heapq
T = int(input())
for _ in range(T):
    k = int(input())
    min_heap, max_heap = [], []
    vis = [0 for _ in range(k)]
    for i in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(min_heap, [num, i])
            heapq.heappush(max_heap, [-num, i])
            vis[i] = 1 #들어갔어요 표시
        else:
            if num == -1:
                while min_heap and not vis[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    temp, idx = heapq.heappop(min_heap)
                    vis[idx] = 0 #나왔어요 표시
            else:
                while max_heap and not vis[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    temp , idx = heapq.heappop(max_heap)
                    vis[idx] = 0 #나왔어요 표시
        while min_heap and not vis[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and not vis[max_heap[0][1]]:
            heapq.heappop(max_heap)
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")