n, m = map(int, input().split())
visited = [False for _ in range(n+1)] # idx는 수열에 들어가는 값
arr = [0 for _ in range(m)]

def backtracking(k, prev):
    if k == m:
        print(*arr)
        return
    for i in range(1, n+1):
        if visited[i] == True or prev > i:
            continue
        arr[k] = i
        visited[i] = True
        backtracking(k+1, i)
        visited[i] = False
    
backtracking(0, 0)