n = int(input())
def dfs():
    if len(stk) == n:
        print(*stk)
        return

    for i in range(1, n+1):
        if i not in stk:
            stk.append(i)
            dfs()
            stk.pop()

stk = []
dfs()