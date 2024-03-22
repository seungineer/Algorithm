from collections import deque
n, m = map(int, input().split())
q = deque()
result = deque()

for i in range(1, n+1):
    q.append(i)

#로직
while len(result) != n:
    for i in range(m-1):
        q.append(q.popleft())

    result.append(q.popleft())

str = ''.join(str(list(result)))

print(f"<{str[1:-1]}>")
