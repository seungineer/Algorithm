import sys
input = sys.stdin.readline
n = int(input())
S = set()
for _ in range(n):
    cl = input().split()
    if cl[0] == "all":
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        continue
    if cl[0] == "empty":
        S = set()
        continue
    command = cl[0]
    k = int(cl[1])
    
    if command == "add":
        S.add(k)
        continue
    if command == "remove":
        S.discard(k)
        continue
    if command == "check":
        if k in S:
            print(1)
        else:
            print(0)
    if command == "toggle":
        if k in S:
            S.discard(k)
        else:
            S.add(k)
    