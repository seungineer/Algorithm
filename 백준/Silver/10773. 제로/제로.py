import sys
read = sys.stdin.readline

N = int(input())


lst = []

while N > 0:
    d = int(input())
    if d == 0:
        lst.pop()
    else:
        lst.append(d)
    N -= 1

print(sum(lst))