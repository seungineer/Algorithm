import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
for _ in range(n):
    str = input().strip().split()
    dict[str[0]] = str[1]

for _ in range(m):
    site = input().strip()
    print(dict[site])
