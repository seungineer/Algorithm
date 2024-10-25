N = int(input())
stk = []
times = []
for _ in range(N):
    st, en = map(int, input().split())
    times.append((st, 1))
    times.append((en, -1))
times.sort()
cnt = 0
max_cnt = -1
for time, val in times:
    cnt += val
    max_cnt = max(max_cnt, cnt)
print(max_cnt)