def solution():
    N = int(input())
    seq = list(map(int, input().split()))
    seq = [0] + seq
    dp = [i for i in seq]
    for state in range(N+1):
        for i in range(state):
            dp[state] = min(dp[state], dp[state-i] + seq[i])
    print(dp[N])
    return

solution()