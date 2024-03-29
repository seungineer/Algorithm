n = int(input())

d = [0 for _ in range(n+3)]

d[1] = 1
d[2] = 2
if n == 1:
    print(d[n])
else:
    for i in range(1, n-1):
        d[i+2] = (d[i+1] + d[i]) % 15746

    print(d[n] % 15746)