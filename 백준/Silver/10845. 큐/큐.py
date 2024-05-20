import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
lst = deque()
for _ in range(n):
    input_str = list(input().split())
    if len(input_str) == 2:
        lst.append(input_str[1])
    if input_str[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    if input_str[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    if input_str[0] == 'size':
        print(len(lst))
    if input_str[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.popleft())
    if input_str[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)