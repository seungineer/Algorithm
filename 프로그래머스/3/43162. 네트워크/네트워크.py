def solution(n, computers):
    vis = [0 for _ in range(n)]
    def dfs(node):
        for i in range(len(computers[node])):
            if computers[node][i] == 1:
                if i != node and vis[i] == 0:
                    vis[i] = 1
                    dfs(i)
    answer = 0    
    for i in range(n):
        if vis[i] == 0:
            vis[i] = 1
            dfs(i)
            answer += 1
    return answer