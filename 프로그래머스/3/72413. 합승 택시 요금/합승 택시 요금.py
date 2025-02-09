def solution(n, s, a, b, fares):
    # 플로이드 워셜로 모든 지점 간 최단 거리를 구하기(O(n^3))
    # s에서 어디든 가는 것 + 어디든에서 a 가는 것 + 어디든에서 b가는 것 완탐 중 최솟값 반환
    matrix = [[int(1e9) for _ in range(n)] for _ in range(n)]
    for st, en, cost in fares:
        matrix[st-1][en-1] = cost
        matrix[en-1][st-1] = cost
    
    for i in range(n):
        matrix[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    ans = int(1e9)
    for k in range(n):
        ans = min(ans, matrix[s-1][k] + matrix[k][a-1] + matrix[k][b-1])
    
    return ans