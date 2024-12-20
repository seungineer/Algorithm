import sys
sys.setrecursionlimit(10**6)
TC = int(input())
for _ in range(TC):
    N = int(input())
    temp = list(map(int, input().split()))
    seq = [0]
    for el in temp: seq.append(el)

    vis = [0 for _ in range(N+1)]
    vis_set = set()

    def dfs(node):
        next_node = seq[node]
        
        if vis[next_node] != 0:
            vis_set.add(node)
            vis[node] = -1
            return -1

        if next_node in vis_set: # 고리 완성
            vis_set.add(node)
            vis[node] = next_node
            return next_node
        
        if vis[next_node] == 0:
            vis_set.add(next_node)
            root = dfs(next_node)
            vis[next_node] = root
            # print(node, root)
            
            if root == next_node: return -1
            return root

    for i in range(1, N+1):
        if vis[i] != 0: continue
        # print(i)
        vis_set = set()
        vis_set.add(i)
        root = dfs(i)
        vis[i] = root
        # print(vis)
        # print(vis_set)
        
    print(vis.count(-1))