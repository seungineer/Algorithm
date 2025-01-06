def solution(N, seq):
    dp = [1 for _ in range(N)]
    for target in range(N):
        for j in range(target):
            if seq[target] > seq[j]:
                dp[target] = max(dp[target], dp[j] + 1)
    print(N-max(dp))
    return 

N = int(input())
lst = []
for _ in range(N): lst.append(int(input()))
solution(N, lst)