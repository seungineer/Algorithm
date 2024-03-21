import sys
read = sys.stdin.readline

n = int(read())
a = [int(read()) for _ in range(n)]

cnt = 1
target = a[-1]# peek -> 저장
a.pop()

while len(a) != 0:
    if a[-1] > target:
        cnt += 1
        target = a[-1]
    a.pop()
    
print(cnt)