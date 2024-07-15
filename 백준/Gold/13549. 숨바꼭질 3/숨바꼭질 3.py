import heapq
n, k = map(int, input().split())
res = []
if n < k:
    vis = [float("inf") for _ in range(k+2)] # k+1 까지 반영
    

    heapq.heappush(res, [0, n])#[시간, node]

    while res:
        sec, node = heapq.heappop(res)
        if vis[node] > sec:
            vis[node] = sec
        if node == k:
            break
        for i in range(3):
            if i == 0:
                if 0 <= node*2 <= k+1 and vis[node*2] > sec:
                    heapq.heappush(res, [sec, node*2])
            elif i == 1:
                if 0 <= node+1 <= k+1 and vis[node+1] > sec:
                    heapq.heappush(res, [sec+1, node+1])
            else:
                if 0 <= node-1 <= k+1 and vis[node-1] > sec:
                    heapq.heappush(res, [sec+1, node-1])
    print(vis[k])
else:
    print(n-k)