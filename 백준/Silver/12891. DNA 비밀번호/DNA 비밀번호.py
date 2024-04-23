import sys
from collections import deque
read = sys.stdin.readline
s, p = map(int, read().split())
seq = list(read().strip())
a, c, g, t = map(int, read().split())
dic = {}
pw = deque()
dic['A'] = a
dic['C'] = c
dic['G'] = g
dic['T'] = t
cnt = 0

for i in range(len(seq)+1):
    if len(pw) < p:
        pw.append(seq[i])
        dic[seq[i]] -= 1
    elif len(pw) == p:
        if max(dic.values()) <= 0:
            cnt += 1
            if i == len(seq):
                break
        if i == len(seq):
            break
        remove = pw.popleft()
        dic[remove] += 1
        pw.append(seq[i])
        dic[seq[i]] -= 1

print(cnt)