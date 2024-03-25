import sys
read = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
matrix.append([0] * (m+2))
for _ in range(n):
    matrix.append([0] + list(read().strip()) + [0])
matrix.append([0] * (m+2))

visited = [[False] * (m+2) for _ in range(n+2)]

def bfs(x, y):
    step = 1
    queue = [[x, y, step]]
    visited[x][y] = True
    while queue:
        temp_lst = queue.pop(0)
        temp_lst[2] += 1
        lst = [[temp_lst[0]+1, temp_lst[1], temp_lst[2]], [temp_lst[0], temp_lst[1]+1, temp_lst[2]], [temp_lst[0], temp_lst[1]-1, temp_lst[2]], [temp_lst[0]-1, temp_lst[1], temp_lst[2]]]
    
        for i in lst:
            if visited[i[0]][i[1]] == False and matrix[i[0]][i[1]] == '1':
                queue.append(i)
                
                visited[i[0]][i[1]] = True

                if i[0] == n and i[1] == m :
                    return i[2]


print(bfs(1,1))
