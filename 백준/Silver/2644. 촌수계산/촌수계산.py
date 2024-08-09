n = int(input())
st, en = map(int, input().split())
lines_cnt = int(input())
matrix = [[] for _ in range(n+1)] # 사람 번호를 인덱스로 사용
for i in range(lines_cnt):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
vis = [False for _ in range(n+1)]

# 100log100 회 recursion
res = -1
def dfs(node, length):
    global res
    if node == en:
        res = length
        return
    
    for k in matrix[node]:
        if not vis[k]:
            vis[k] = True
            dfs(k, length+1)
dfs(st, 0)

print(res)