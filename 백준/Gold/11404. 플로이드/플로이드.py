n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
matrix = [[float("inf") for _ in range(n)]for _ in range(n)]
queue = []
for _ in range(m):
    st, en, w = map(int, input().split())
    if matrix[st-1][en-1] > w:
        matrix[st-1][en-1] = w
        queue.append([st-1, en-1])

while queue:
    st, en = map(int, queue.pop())
    cur = matrix[st][en]
    for k in range(n):
        sub = matrix[en][k]
        if sub != float("inf"):
            if cur + sub < matrix[st][k]:
                matrix[st][k] = cur + sub
                queue.append([st, k])
for i in range(n):
    for j in range(n):
        if i == j:
            print(0, end=" ")
        else:
            if matrix[i][j] == float("inf"):
                print(0, end=" ")
            else:
                print(matrix[i][j], end=" ")
    print()