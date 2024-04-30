n = int(input())
seq = []
sub = n * 0.15
if sub % 1 >= 0.5:
    sub = int(sub) +1
else:
    sub = int(sub)
for _ in range(n):
    seq.append(int(input()))
seq.sort()
sub_seq = seq[sub:n-sub]
if n != 0:
    res = sum(sub_seq) / (n - 2*sub)
    if res % 1 >= 0.5:
        res = int(res) +1
    else:
        res = int(res)
    print(res)
else:
    print(0)