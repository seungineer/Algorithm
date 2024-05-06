n = int(input())
seq = list(map(int, input().split()))
seq.sort()
res = 0

for k in seq:
    res += k * n
    n -= 1
print(res)