# B시작, W시작 2 가지 케이스에 대해서
# 8*8 모두 잘라 가면서 개수를 센다.
## 가장 작은 개수를 선택한다.

n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(input().strip()))

width = m - 8
height = n - 8
color = ['B', 'W']
min_change_cnt = 54321
change_cnt = 0

for h in range(height+1):
    for w in range(width+1):
        for case in range(2):
            must_color = color[case] # 시작 색상
            change_cnt = 0
            for i in range(8):
                if must_color == 'B':
                        must_color = 'W'
                else:
                        must_color = 'B'
                    
                for j in range(8):
                    if matrix[h+j][w+i] != must_color:
                        change_cnt += 1
                    
                    if must_color == 'B':
                        must_color = 'W'
                    else:
                        must_color = 'B'
            
            min_change_cnt = min(min_change_cnt, change_cnt)

print(min_change_cnt)
