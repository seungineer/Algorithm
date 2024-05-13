import sys
input = sys.stdin.readline
a, b = map(int, input().split())

if a < b:
    temp = b
    b = a
    a = temp
# 무조건 a > b
n = b + 1
while True: # 최대 공약수
    n -= 1
    if a % n == 0 and b % n == 0:
        print(n)
        break

if a % b == 0:
    print(a)
else:
    m = 0
    while True:
        m += 1
        if (b * m) % a == 0:
            print(b*m)
            break