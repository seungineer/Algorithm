import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
q = deque()
for i in range(1, N+1):
    q.append(i)

while len(q) != 1:
    # 마지막 popleft() 출력하면 됨
    q.popleft()
    q.append(q.popleft())
print(q[0])
