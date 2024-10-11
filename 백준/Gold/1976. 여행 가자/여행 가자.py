N = int(input())
M = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
seq = list(map(int, input().split()))

def dfs(v1, target):
    if v1 == target:
        ans[0] = True
        return
    for j in range(N):
        if matrix[v1][j] and vis[j] == 0:
            vis[j] = 1
            dfs(j, target)
    return

isImpossible = False
for i in range(1, M):
    ans = [False]
    if isImpossible: break
    prev_node = seq[i-1] - 1
    curr_node = seq[i] - 1
    
    vis = [0 for _ in range(N)]
    vis[prev_node] = 1
    dfs(prev_node, curr_node)
    
    if ans[0]: continue
    else: isImpossible = True

if isImpossible: print("NO")
else: print("YES")