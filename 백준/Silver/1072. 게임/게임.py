def solution():
    X, Y = map(int, input().split())
    
    l = 1
    r = X
    ans = int(1e9) + 1
    while l <= r:
        mid = (l+r)//2
        if (Y+mid)*100//(X+mid) > Y*100//(X):
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1
    if ans == int(1e9) + 1:
        print(-1)
        return
    print(ans)
    return 
solution()