# i 상태에서 0번(or 1번) 나무에 w번 위치를 이동하여 먹을 수 있는 감 개수
T, W = map(int, input().split())
falls = []
for _ in range(T):
    tree = int(input())
    falls.append(tree - 1)

dp = [[[0 for _ in range(W+1)],[0 for _ in range(W+1)]] for _ in range(T)]

for i in range(T):
    fall = falls[i]
    if i == 0:
        if fall == 0:
            dp[i][0][0] = 1
        else:
            dp[i][1][1] = 1
        continue
    
    if fall == 0:
        for k in range(W+1):
            if k != 0:
                dp[i][0][k] = max(dp[i-1][1][k-1], dp[i-1][0][k])
            else:
                dp[i][0][k] = dp[i-1][0][k]
        
        for k in range(W+1):
            dp[i][0][k] += 1
            dp[i][1][k] = dp[i-1][1][k]
            
    else:
        for k in range(W+1):
            if k != 0:
                dp[i][1][k] = max(dp[i-1][0][k-1], dp[i-1][1][k])
            else:
                dp[i][1][k] = dp[i-1][1][k]
        
        for k in range(W+1):
            dp[i][1][k] += 1
            dp[i][0][k] = dp[i-1][0][k]

first_tree = max(dp[-1][0])
second_tree = max(dp[-1][1])   
print(max(first_tree, second_tree))
