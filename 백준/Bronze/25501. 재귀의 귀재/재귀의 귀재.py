import sys
read = sys.stdin.readline
N = int(read())
data = [read().strip() for _ in range(N)]
cnt = [0]

#로직

def recursion(s, l, r):
    cnt[0] += 1
    if (l >= r): return 1
    elif (s[l] != s[r]):
        return 0
    else: return recursion(s,l+1,r-1)

for k in data:
    l = 0
    r = len(k) - 1
    s = k
    print(recursion(s, l, r), end= ' ')
    print(cnt[0])
    cnt[0] = 0