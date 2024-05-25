


q = []
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

def dfs(l):
    if len(q) == M:
        print(' '.join(map(str, q)))
        return

    for i in range(l, N):
        q.append(a[i])
        dfs(i)
        q.pop()
        
dfs(0)