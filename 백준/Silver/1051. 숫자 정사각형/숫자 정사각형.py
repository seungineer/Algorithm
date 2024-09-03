# 행을 순회하면서 자신과 같은게 있는 경우(-> 계속해서 같은 게 있을 수 있으니 전체 순회)
## 선분의 길이를 아니까 각 위치에 정말 자신과 같은 게 있는지 확인한다.
### 정사각형이 파악된 경우 넓이를 업데이트 한다.

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,list(input()))))
maxarea = 1
for i in range(N):
    for j in range(M):
        target = matrix[i][j]
        for k in range(j+1, M):
            if matrix[i][k] == target:
                length = k - j + 1
                if i+length-1 < N:
                    if matrix[i+length-1][j] == target and matrix[i+length-1][k] == target:
                        maxarea = max(maxarea, length**2)
print(maxarea)