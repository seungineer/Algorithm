def solution():
    N, M = map(int, input().split())
    graph = dict()
    for _ in range(N-1):
        a, b, d = map(int, input().split())
        if a in graph: graph[a].append((b, d))
        else: graph[a] = [(b, d)]
        if b in graph: graph[b].append((a, d))
        else: graph[b] = [(a, d)]
    
    def dfs(node, curr_d, en, vis):
        if node == en:
            print(curr_d)
            isFind[0] = True
            return
        if not node in graph: return
        for next, dist in graph[node]:
            if vis[next] == 0:
                vis[next] = 1
                dfs(next, curr_d + dist, en, vis)
                if isFind[0]: return


    def find(st, en):
        vis = [0 for _ in range(N+1)]
        vis[st] = 1
        if not st in graph: return
        for next, dist in graph[st]:
            if vis[next] == 0:
                vis[next] = 1
                dfs(next, dist, en, vis)
                if isFind[0]: return

    for _ in range(M):
        a, b = map(int, input().split())
        isFind = [False]
        find(a, b)
        
solution()