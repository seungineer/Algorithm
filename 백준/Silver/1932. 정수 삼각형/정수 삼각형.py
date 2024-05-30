import sys
input = sys.stdin.readline

n = int(input())
matrix =[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))

for i in range(n):
    length = len(matrix[-i])
    for j in range(length-1):
        if matrix[-i][j] > matrix[-i][j+1]:
            matrix[-i-1][j] += matrix[-i][j]
        else:
            matrix[-i-1][j] += matrix[-i][j+1]
        
print(matrix[0][0])