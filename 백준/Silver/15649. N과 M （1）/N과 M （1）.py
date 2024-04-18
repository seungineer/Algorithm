n, m = map(int, input().split())
arr = [0 for _ in range(m)]
isused = [False for _ in range(n+1)]

def backtracking(k):
    if k == m:
        print(*arr)
        return

    for i in range(1, n+1):
        if isused[i] != True:
            arr[k] = i
            isused[i] = True
            backtracking(k+1)
            isused[i] = False

backtracking(0)