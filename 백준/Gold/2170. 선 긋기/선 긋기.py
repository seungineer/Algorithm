import sys
import heapq as hq
input = sys.stdin.readline
def solution():
    N = int(input().rstrip())
    positions = []
    stk = 0
    for _ in range(N):
        st, en = map(int, input().rstrip().split())
        hq.heappush(positions, (st, -1))
        hq.heappush(positions, (en, 1))
    
    start = -1    
    ans = 0
    while positions:
        pos, point = hq.heappop(positions)
        point *= -1
        if stk == 0:
            if start == -1:
                start = pos
        stk += point
        if stk == 0:
            ans += (pos - start)
            start = -1
    print(ans)
    return
solution()