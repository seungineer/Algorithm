n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

matrix.sort()

for i in range(n):
    print(*matrix[i])