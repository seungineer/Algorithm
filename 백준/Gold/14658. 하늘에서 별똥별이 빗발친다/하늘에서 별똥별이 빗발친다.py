import sys
def solution():
    input = sys.stdin.readline
    N, M, L, K = map(int, input().rstrip().split())
    points = []
    for _ in range(K): points.append(list(map(int, input().rstrip().split())))
    
    matrix = dict()
    for point in points:
        x, y = point
        if x in matrix: matrix[x].append(y)
        else: matrix[x] = [y]
    
    def count_covered(st_x, st_y):
        for op_x, op_y in points:
            cnt = 0
            for x, y in points:
                if st_x <= x and x <= st_x + L and op_y <= y and y <= op_y + L:
                    cnt += 1
            max_covered[0] = max(max_covered[0], cnt)
        

    
    max_covered = [-1]
    for x, y in points:
        # point의 위치 네 꼭짓점
        count_covered(x, y)
        
    print(K - max_covered[0])
    return

solution()