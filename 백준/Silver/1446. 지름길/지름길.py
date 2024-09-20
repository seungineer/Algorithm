N, D = map(int, input().split())
dp = [i for i in range(10000+1)]

shortcut = dict()
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort()
for l in lst:
    st, en, distance = l
    prev = dp[en]
    dp[en] = min(dp[en], dp[st] + distance)
    if prev != dp[en]:
        for d in range(1, D+1):
            for i in range(d+1):
                dp[d] = min(dp[d], dp[d-i]+i)

print(dp[D])