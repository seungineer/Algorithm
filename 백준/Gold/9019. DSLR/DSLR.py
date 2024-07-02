from collections import deque
import sys
input = sys.stdin.readline
def D(n):
    res = (2*n)%10000
    return res
def S(n):
    if n == 0:
        res = 9999
    else:
        res = n - 1
    return res
def L(n):
    str_n = str(n)
    if len(str_n) == 1:
        res = str_n[0] + '0'
    elif len(str_n) == 2 or len(str_n) == 3:
        res = str_n + '0'
    else:
        res = str_n[1:] + str_n[0]
    return int(res)
def R(n):
    str_n = str(n)
    if len(str_n) == 1:
        res = str_n[0] + '000'
    elif len(str_n) == 2:
        res = str_n[1] + '00' + str_n[0]
    elif len(str_n) == 3:
        res = str_n[2] + '0' + str_n[0] + str_n[1]
    else:
        res = str_n[len(str_n)-1] + str_n[0:len(str_n)-1]
    return int(res)

t = int(input())

for _ in range(t):
    vis = [0 for _ in range(10001)]
    a, b = map(int, input().split())
    res = -1
    queue = deque()
    queue.append([a, ""])
    isCorrect = False
    while True:
        n, cl = queue.popleft()
        if vis[n] == 1:
            continue
        vis[n] = 1
        for i in range(4):
            if i == 0:
                res = D(n)
                cmd = cl + "D"
                queue.append([res, cmd])
                if res == b:
                    isCorrect = True
                    break
            elif i == 1:
                res = S(n)
                cmd = cl + "S"
                queue.append([res, cmd])
                if res == b:
                    isCorrect = True
                    break
            elif i == 2:
                res = L(n)
                cmd = cl + "L"
                queue.append([res, cmd])
                if res == b:
                    isCorrect = True
                    break
            else:
                res = R(n)
                cmd = cl + "R"
                queue.append([res, cmd])
                if res == b:
                    isCorrect = True
                    break
        if isCorrect:
            print(cmd)
            break