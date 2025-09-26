from collections import deque, defaultdict
def solution(n, edge):
    answer = 0
    # BFS로 1번 노드에서 떨어진 거리 업데이트 후
    matrix = defaultdict(list)
    for e in edge:
        a, b = e
        matrix[a].append(b)
        matrix[b].append(a)
    dis = [int(1e9) for _ in range(n+1)]
    qu = deque()
    qu.append([1, 0])
    while qu:
        node, distance = qu.popleft()
        for nextNode in matrix[node]:
            if dis[nextNode] > distance + 1:
                dis[nextNode] = distance + 1
                qu.append([nextNode, distance + 1])
    
    # max 값의 개수가 몇 개 있는지 개수 리턴
    maxD = max(dis[2:])
    for i in range(2, len(dis)):
        if dis[i] == maxD:
            answer += 1
    return answer