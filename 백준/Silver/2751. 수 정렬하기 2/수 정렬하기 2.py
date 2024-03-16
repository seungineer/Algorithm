import sys

read = sys.stdin.readline
N = int(read())
data = [int(read()) for _ in range(N)]

data.sort()
for i in data:
    print(i)