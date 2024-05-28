n, m = map(int, input().split())
seq = sorted(list(set(list(map(int, input().split())))))
res = []

def bt(state, st):
    if state >= m:
        print(*res)
        return
    for i in range(st, len(seq)):
        res.append(seq[i])
        bt(state+1, i)
        res.pop()

bt(0, 0)