from collections import deque
import sys
read = sys.stdin.readline

N = int(read())
q = deque([])



for _ in range(N):
    str = read().strip().split()
    if len(str) == 2:
        q.append(str[1])
        continue
    elif str[0] == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
        continue

    elif str[0] == 'size':
        print(len(q))
        continue

    elif str[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
        continue
    
    elif str[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
        continue

    elif str[0] == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
        continue

    

    

