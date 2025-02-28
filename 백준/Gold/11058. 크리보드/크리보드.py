def solution():
    N = int(input())
    dp = [i for i in range(N+1)]
    for i in range(7, N+1):
        for j in range(3, i):
            dp[i] = max(dp[i], dp[i - j] * (j - 1))
    print(dp[N])

    
solution()