t = int(input())
lst = []
for _ in range(t):
    x, y = map(int, input().split())
    lst.append([y,x])
lst.sort()
for i in range(t):
    print(lst[i][1], lst[i][0])