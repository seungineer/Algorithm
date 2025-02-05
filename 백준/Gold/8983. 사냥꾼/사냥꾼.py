import sys, bisect
M, N, L = map(int, input().rstrip().split()) # 사대, 동물, 거리
seq = list(map(int, input().rstrip().split()))
seq.sort()
animals = [list(map(int, input().rstrip().split())) for _ in range(N)]
cnt = 0

for j, i in animals:
    bound = L - i # 사정권 [j +/- bound]
    if bound < 0: continue # 불가능 케이스
    
    idx = bisect.bisect_left(seq, j)
    if idx != M and idx != 0:
        if seq[idx] - j <= bound:
            cnt += 1
            continue
        if idx < 1: continue
        
        if j - seq[idx-1] <= bound:
            cnt += 1
            continue
    
    if idx == M:
        if j - seq[-1] <= bound:
            cnt += 1
            continue
    if idx == 0:
        if seq[0] - j <= bound:
            cnt += 1
            continue

print(cnt)