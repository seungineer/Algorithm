def solution():
    N = int(input())
    heights = [int(input()) for _ in range(N)]
    
    stk = []
    ans = 0
    for i in range(N):
        h = heights[i]
        if not stk:
            stk.append(h)
            continue
        while stk and stk[-1] <= h:
            ans += (len(stk) - 1)
            stk.pop()
        stk.append(h)
    while stk:
        ans += (len(stk) - 1)
        stk.pop()
    
    print(ans)
    return

solution()