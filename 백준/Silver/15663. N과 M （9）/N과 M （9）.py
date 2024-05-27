n, m = map(int, input().split())
seq = sorted(list(map(int,input().split())))

res = []
vis = [0] * n
last = -1
temp = -1
def bt(j, state):
    global last
    global temp
    if state == m:
        print(*res)
        return
    for i in range(n):
        if state == temp and last == seq[i]:
            continue
        if vis[i] == 1:
            continue
        res.append(seq[i])
        vis[i] = 1
        bt(i, state+1)
        last = res.pop()
        temp = len(res)
        vis[i] = 0
bt(0, 0)