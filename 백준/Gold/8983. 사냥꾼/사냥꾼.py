import sys
M, N, L = map(int, input().rstrip().split()) # 사대, 동물, 거리
seq = list(map(int, input().rstrip().split()))
seq.sort()
animals = [list(map(int, input().rstrip().split())) for _ in range(N)]

def bisect(target, bound):
    l = 0
    r = M - 1
    while l <= r:
        mid = (l+r)//2
        if seq[mid] == target:
            cnt[0] += 1
            return
        elif seq[mid] > target:
            if seq[mid] - target <= bound:
                cnt[0] += 1
                return
            r = mid - 1
        else:
            if target - seq[mid] <= bound:
                cnt[0] += 1
                return
            l = mid + 1
        
cnt = [0]
for j, i in animals:
    bound = L - i # 사정권 [j +/- bound]
    if bound < 0: continue # 불가능 케이스

    bisect(j, bound)

print(cnt[0])