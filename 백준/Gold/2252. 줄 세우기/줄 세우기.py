from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
inorder_list = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # [[], [], [], [1], [2]]
    inorder_list[b] += 1 # [0, 1, 1, 0, 0]

queue = deque()

while True:
    v = inorder_list.index(0, 1) # idx_num 1부터 inorder가 0인 가장 작은 idx(=노드) 반환
    print(v)
    inorder_list[v] = -1 # 그래프에서 노드 삭제하는 의미
    for i in graph[v]:
        inorder_list[i] -= 1
        
    try:
        inorder_list.index(0,1)
    except:
        break

    


