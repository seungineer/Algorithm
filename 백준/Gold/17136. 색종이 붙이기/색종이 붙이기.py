matrix = [list(map(int, input().split())) for _ in range(10)]
shapes_used = [0 for _ in range(5+1)]

def restore(x, y, shape):
    for i in range(x, x + shape):
        for j in range(y, y + shape):
            matrix[i][j] = 1

def paste(x, y, shape, shapes_used):
    # shape이 가능한지 확인하고,
    # 가능하면 x, y에서 nx, ny까지 0으로 칠하기
    # 순회하면서 paste 재귀로 ㄱㄱ
    
    isPossible = True
    if 0 <= x + shape <= 10 and 0 <= y + shape <= 10:
        for i in range(x, x + shape):
            for j in range(y, y + shape):
                if matrix[i][j] == 0: isPossible = False
    else: isPossible = False
    
    if answer[0] < sum(shapes_used): return False
    if isPossible:
        for i in range(x, x + shape):
            for j in range(y, y + shape):
                if matrix[i][j] == 1: matrix[i][j] = 0
    else:
        return False
    
    isAllZero = True
    isStop = False
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1:
                isAllZero = False
                for shape in range(1, 6):
                    if shapes_used[shape] >= 5: continue
                    shapes_used[shape] += 1
                    isPasted = paste(i, j, shape, shapes_used)
                    if isPasted: restore(i, j, shape)
                    shapes_used[shape] -= 1
                isStop = True
            if isStop: break
        if isStop: break
    if isAllZero: answer[0] = min(answer[0], sum(shapes_used))
    
    return True

answer = [1e9]
isZero = True
isStop = False
for i in range(10):
    for j in range(10):
        if matrix[i][j] == 1:
            isZero = False
            for shape in range(1, 6):
                if shapes_used[shape] >= 5: continue
                shapes_used[shape] += 1
                pasted = paste(i, j, shape, shapes_used)
                if pasted: restore(i, j, shape)
                shapes_used[shape] -= 1
            isStop = True
        if isStop: break
    if isStop: break
    

if isZero: answer[0] = min(answer[0], sum(shapes_used))
if answer[0] == 1e9: print(-1)
else: print(answer[0])