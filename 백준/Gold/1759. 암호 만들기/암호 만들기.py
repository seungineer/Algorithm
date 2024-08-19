l, c = map(int, input().split())
seq = sorted(list(map(str,input().split(" "))))
moeum = ['a', 'e', 'i', 'o', 'u']
def dfs(start, mCnt):
    if len(res) == l and mCnt > 0 and l - mCnt > 1:
        print(''.join(res))
        return

    for i in range(1, c - start):
        moeumCnt = 0
        res.append(seq[start+i])
        for m in moeum:
            if m in res:
                moeumCnt += 1
        dfs(start+i, moeumCnt)
        res.pop()
            
res = []
for i in range(c):
    res.append(seq[i])
    if seq[i] in moeum:
        dfs(i, 1)
    else:
        dfs(i, 0)
    res.clear()