n, m = map(int, input().split())
lst = list(map(int,input().split()))
lst.sort()
def dfs(res):
    if len(res) == m:
        print(*res)
        return
    for k in lst:
        if not k in res:
            if len(res) == 0 or k > res[-1]:
                res.append(k)
                dfs(res)
                res.pop()
dfs([])