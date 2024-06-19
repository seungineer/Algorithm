from collections import deque
n = int(input())
bar = list(map(int, input().split()))
length = len(bar)
fruit_type = set()
fruit_stk = deque()
max_len = -float("inf")

for k in bar:
    fruit_type.add(k)
    fruit_stk.append(k)
    while len(fruit_type) >= 3:
        temp = fruit_stk.popleft()
        if not temp in fruit_stk:
            fruit_type.discard(temp)
    max_len = max(max_len, len(fruit_stk))

print(max_len)