import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
matrix = []
time = [0 for _ in range(257)]
min_time = float("inf")
max_height = 0
spare = b
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for height in range(257):
    hours = 0
    b = spare
    dif_b = 0
    isImpossible = True
    for i in range(n):
        for j in range(m):
            diff = (height - matrix[i][j])
            if diff < 0 : #깎기
                dif_b += -diff
                hours += -diff*2
            elif diff > 0: #얹기        
                dif_b -= diff
                hours += diff

    if 0 <= b + dif_b:
        isImpossible = False
    if not isImpossible:
        if min_time >= hours:
            min_time = hours
            max_height = height
        else:
            break
    
    
print(min_time, max_height)
