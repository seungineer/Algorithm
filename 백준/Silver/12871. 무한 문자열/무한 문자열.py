import sys
read = sys.stdin.readline

data = [read().strip() for _ in range(2)]

# 로직
s = data[0]
t = data[1]
flag = False

# 최소 공배수 구하기
if s * len(t) == t * len(s):
    print(1)
else:
    print(0)
