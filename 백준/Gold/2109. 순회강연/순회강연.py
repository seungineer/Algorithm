import heapq as hq
def solution():
    N = int(input())
    qu = []
    for _ in range(N):
        p, d = map(int, input().split())
        hq.heappush(qu, (-p, d))
    vis = [False for _ in range(10001)]
    ans = 0
    while qu:
        pay, due = hq.heappop(qu)
        pay *= -1
        if vis[due]:
            for j in range(due, 0, -1):
                if not vis[j]:
                    vis[j] = True
                    ans += pay
                    break
        else:
            vis[due] = True
            ans += pay
        
    print(ans)
solution()