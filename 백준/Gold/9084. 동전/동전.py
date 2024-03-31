t = int(input())

for _ in range(t):
    n = int(input())
    coin_types = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m+1)
    dp[0] = 1
    coin_types.sort()
    for coin in coin_types:
        for j in range(1, m+1):
            if j >= coin:
                dp[j] = dp[j] + dp[j-coin]

    print(dp[m])
