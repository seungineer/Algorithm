import sys
n, k = map(int, input().split())
coin_type = []

for _ in range(n):
    coin_type.append(int(input()))

coin_type = list(set(coin_type))
coin_type.sort()

dp = [54321] * (k+1)
dp[0] = 0

for i in range(1, k+1):
    for coin in coin_type:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin]+1)
        else:
            break


if dp[k] != 54321:
    print(dp[k])
else:
    print(-1)