import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
graph = {}
for _ in range(M):
    st, en, cost = map(int, input().split())
    st -= 1
    en -= 1
    if st in graph: graph[st].append([en, cost])
    else: graph[st] = [[en, cost]]
    
    if en in graph: graph[en].append([st, cost])
    else: graph[en] = [[st, cost]]

st, en = map(int, input().split())
START, END = st - 1, en - 1

def isReach(node, mid):
    if node == END: return True

    res = False
    for j in range(len(graph[node])):
        next_node, c = graph[node][j]
        if c >= mid and vis[next_node] == 0:
            vis[next_node] = 1
            res = isReach(next_node, mid)
            if res: break

    return res

max_w = -1
l = 0
r = int(1e9)
while l <= r:
    mid = (l + r) // 2
    vis = [0 for _ in range(N)]
    if isReach(START, mid):
        max_w = max(max_w, mid)
        l = mid + 1
    else:
        r = mid - 1
print(max_w)