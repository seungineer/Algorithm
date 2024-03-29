n = int(input())

d = [0 for _ in range(n+3)]

d[1] = 1
if n == 1:
    print(d[n])
else:
    for i in range(1, n+1):
        d[2] = d[1]
        d[i+2] = d[i+1] + d[i]
    print(d[n])