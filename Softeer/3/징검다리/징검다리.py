import sys
input = sys.stdin.readline
N = int(input().rstrip())
seq = list(map(int, input().rstrip().split()))

dp = [1 for _ in range(N)]
for en in range(N):
    max_val = -1e9
    for st in range(en):
        if seq[st] < seq[en]:
            max_val = max(max_val, dp[st] + dp[en])
    if max_val != -1e9:
        dp[en] = max_val
            
print(max(dp))