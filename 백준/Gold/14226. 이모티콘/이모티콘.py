from collections import deque
def solution():
    S = int(input())
    qu = deque()
    qu.append((1, 0))
    
    visited = dict()
    visited[(1, 0)] = 0

    while qu:
        val, copied = qu.popleft()
        if val == S:
            print(visited[(val, copied)])
            break
        if (val, val) not in visited.keys():
            visited[(val, val)] = visited[(val, copied)] + 1
            qu.append((val, val))
        if (val + copied, copied) not in visited.keys():
            visited[(val + copied, copied)] = visited[(val, copied)] + 1
            qu.append((val + copied, copied))
        if (val - 1, copied) not in visited.keys():
            visited[(val - 1, copied)] = visited[(val, copied)] + 1
            qu.append((val - 1, copied))
    return
solution()