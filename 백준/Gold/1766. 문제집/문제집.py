N, M = map(int, input().split())
inorder_list = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    inorder_list[b] += 1

while True:
    v = inorder_list.index(0, 1)
    print(v, end= ' ')
    inorder_list[v] = -1
    for i in graph[v]:
        inorder_list[i] -= 1

    try:
        inorder_list.index(0,1)
    except:
        break
    