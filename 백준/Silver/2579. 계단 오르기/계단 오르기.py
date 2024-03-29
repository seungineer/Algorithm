n = int(input())

point_lst = [int(input()) for _ in range(n)]

d = [[0, 0, 0] for _ in range(n+1)]
d[1][1] = point_lst[0]

if n == 1:
    print(max(d[n][1], d[n][2]))
else:
    d[2][1] = point_lst[1]
    d[2][2] = d[1][1] + point_lst[1]

    for i in range(3, n+1):
        d[i][2] = d[i-1][1] + point_lst[i-1]
        d[i][1] = max(d[i-2][1], d[i-2][2]) + point_lst[i-1]

    print(max(d[n][1], d[n][2]))
