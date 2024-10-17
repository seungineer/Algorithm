N = int(input())
dp = [0 for _ in range(501)]
seq = [0 for _ in range(501)]
for _ in range(N):
    a, b = map(int, input().split())
    seq[a] = b

for i in range(501):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))