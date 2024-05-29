n, m = map(int, input().split())
matrix = []
matrix2 = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
for _ in range(n):
    matrix2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(matrix[i][j] + matrix2[i][j], end=' ')
    print()