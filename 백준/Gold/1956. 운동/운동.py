def solution():
    # V, E = 5, 6
    # edges = [[1, 2, 1],
    #          [3, 2, 1],
    #          [1, 3, 5],
    #          [2, 3, 2],
    #          [4, 5, 1],
    #          [5, 4, 1]]
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    graph = [[int(1e9) for _ in range(V)] for _ in range(V)]
    for st, en, d in edges:
        st -= 1
        en -= 1
        graph[st][en] = d
    for node in range(V): graph[node][node] = 0

    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
    minDistance = [int(1e9)]
    for st in range(V):
        for en in range(V):
            if en == st: continue
            minDistance[0] = min(minDistance[0], graph[st][en] + graph[en][st])
        
    if minDistance[0] == int(1e9):
        print(-1)
    else:
        print(minDistance[0])
    return
solution()

