import sys
sys.setrecursionlimit(10**6)
n, s = map(int, input().split())
seq = list(map(int, input().split()))

isused = [False for _ in range(n)]
cnt = 0
arr = []
res = []
def bt(k, score, start):
    global cnt
    global isused
    if k == n+1:
        return
    if k > 0 and score == s:
        
        cnt += 1
        

    for i in range(start, n):
        if not isused[i]:
            score += seq[i]
            isused[i] = True
            start += 1
            # print(k+1, score, start)
            bt(k+1, score, start)
            isused[i] = False
            score -= seq[i]

bt(0, 0, 0)
print(cnt)
