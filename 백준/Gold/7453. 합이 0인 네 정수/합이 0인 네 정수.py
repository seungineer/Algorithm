import sys
input = sys.stdin.readline
N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().rstrip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

group_ab_cnt = dict()
group_cd_cnt = dict()
for a in A:
    for b in B:
        if a+b in group_ab_cnt: group_ab_cnt[a+b] += 1
        else: group_ab_cnt[a+b] = 1
ans = 0
for c in C:
    for d in D:
        if -1*(c+d) in group_ab_cnt:
            ans += group_ab_cnt[-1*(c+d)]

print(ans)
