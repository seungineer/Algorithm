n = int(input())
seq = list(map(int, input().split()))
dp = [1 for _ in range(len(seq))]

for i in range(1, len(seq)):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))