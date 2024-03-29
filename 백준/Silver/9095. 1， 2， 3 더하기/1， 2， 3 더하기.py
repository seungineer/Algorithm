T = int(input())
input_lst = [int(input()) for _ in range(T)]

d = [0] * (13)
for i in input_lst:
    d[1] = 1
    d[2] = 2
    d[3] = 4

    if i  <= 2:
        print(d[i])
        continue

    for j in range(1, i-2):
        d[j+3] = d[j+2] + d[j+1] + d[j]
    print(d[i])
