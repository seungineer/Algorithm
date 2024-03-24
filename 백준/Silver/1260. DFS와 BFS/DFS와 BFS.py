N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)] # 노드랑 인덱스를 일치시켜주기 위해서 n+1개 생성
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0] * (N+1) # 노드 번호 = 인덱스 번호
visited2 = [0] * (N+1)

def dfs(V): # 스택에서 v 노드를 pop하고, 인접 노드를 push하는 함수
    visited1[V] = 1
    print(V, end=' ')
    for i in range(1, N+1): # 번호가 가장 적은 것부터 stack에 들어감
        if graph[V][i] == 1 and visited1[i] == 0 : # v에서 i로 갈 수 있고 and i를 방문한 적이 없을 때
            dfs(i)

def bfs(V): # 큐에 v노드를 push하고, 인접 노드를 push하는 함수
    queue = [V]
    visited2[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if graph[V][i] == 1 and visited2[i] == 0:
                queue.append(i)
                visited2[i] = 1

dfs(V)
print("")
bfs(V)