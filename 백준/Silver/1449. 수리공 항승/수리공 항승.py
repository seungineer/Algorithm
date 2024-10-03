# 테이프를 붙이는 시점에 안전 지대 r이 update됨
N, L = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
r = 0.5
cnt = 0
for s in seq:
    if s + 0.5 > r:
        cnt += 1
        r = s - 0.5 + L
print(cnt)
