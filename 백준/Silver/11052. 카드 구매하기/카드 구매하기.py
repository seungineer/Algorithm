N = int(input())
lst = list(map(int, input().split()))
seq = [0]
[seq.append(el) for el in lst]

dp = [0 for _ in range(N+1)]

for en in range(N+1):
    for st in range(en):
        dp[en] = max(dp[en], dp[st] + seq[en - st])
print(dp[-1])