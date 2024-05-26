n, m = map(int, input().split())
seq = sorted(list(map(int, input().split())))
res = []

def bt():
    if len(res) == m:
        print(*res)
        return
    for i in range(n):
        res.append(seq[i])
        bt()
        res.pop()
bt()