X = int(input())
dp = [int(1e9) for _ in range(X+1)]
arr = [[] for _ in range(X+1)]
dp[0] = 0
dp[1] = 0
arr[1] = [1]
for i in range(1, X+1):
    if i+1 <= X and dp[i+1] > dp[i] + 1:
        dp[i+1] = dp[i] + 1
        arr[i+1] = [k for k in arr[i]]
        arr[i+1].append(i+1)
        
    if i*2 <= X and dp[i*2] > dp[i] + 1:
        dp[i*2] = dp[i] + 1
        arr[i*2] = [k for k in arr[i]]
        arr[i*2].append(i*2)
        
    if i*3 <= X and dp[i*3] > dp[i] + 1:
        dp[i*3] = dp[i] + 1
        arr[i*3] = [k for k in arr[i]]
        arr[i*3].append(i*3)

print(dp[X])        
print(*arr[X][::-1])        
    