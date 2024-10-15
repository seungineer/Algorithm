import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        u, v = map(int, input().split())
        
        if u in graph: graph[u].append(v)
        else: graph[u] = [v]
        
        if v in graph: graph[v].append(u)
        else: graph[v] = [u]

    color_lst = ["temp" for _ in range(V+1)]
    ans = [True]
    def dfs(node, color):
        # 주변이 모두 !color인지 확인
        if node in graph:
            for next_node in graph[node]:
                if node == next_node: continue
                if color_lst[next_node] != color:
                    if color_lst[next_node] == "temp":
                        color_lst[next_node] = not color
                        dfs(next_node, not color)
                else:
                    ans[0] = False
    
    for u in range(1, V+1):
        if u in graph:
            if color_lst[u] == "temp":
                # 별개의 그래프가 생성되는 경우도 체크
                color_lst[u] = True
                dfs(u, True)
        if not ans[0]: break

    if ans[0]: print("YES")
    else: print("NO")