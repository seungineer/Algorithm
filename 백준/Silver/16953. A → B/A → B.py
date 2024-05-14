import sys
input = sys.stdin.readline
a, b = map(int, input().split())
cnt = 1
while True:
    if a > b :
        print(-1)
        break
    if b % 10 == 1:
        b //= 10
        cnt += 1
        if a == b:
            print(cnt)
            break
    
    elif b % 2 == 0:
        b //= 2
        cnt += 1
        if a == b:
            print(cnt)
            break
    else:
        print(-1)
        break