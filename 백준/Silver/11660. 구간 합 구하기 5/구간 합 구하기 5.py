import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0 for _ in range(n)]]
for i in range(n):
    input_lst = list(map(int, input().split()))
    temp_lst = [matrix[-1][i] + input_lst[i] for i in range(n)]
    matrix.append(temp_lst)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split()) #x행, y열
    y1 -= 1
    y2 -= 1
    total = 0
    for i in range(y1, y2+1):
        total += matrix[x2][i] - matrix[x1-1][i]
    print(total)