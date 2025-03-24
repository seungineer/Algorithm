def solution():
    target = input()
    N = len(target)
    dp =[[0,0] for _ in range(N)]
    dp[0][0] = 1
    dp[0][1] = 0
    if 1 < N:
        if target[1] != '0':
            dp[1][0] = 1
            if 10 <= int(target[0]+target[1]) <= 34:
                dp[1][1] = 1
        else:
            dp[1][0] = 0
            dp[1][1] = 1
    else:
        print(1)
        return
    for i in range(2, N):
        if target[i] != '0':
            dp[i][0] = sum(dp[i-1])
            if 10 <= int(target[i-1]+target[i]) <= 34:
                dp[i][1] = sum(dp[i-2])
        else:
            dp[i][1] = sum(dp[i-2])
    
    print(sum(dp[-1]))
    

solution()