n = int(input())
res = n
min_n = float("inf")
flag = False
while True:
    n -= 1
    sub_sum = 0
    for i in str(n):
        sub_sum += int(i)
    temp = n + sub_sum

    if temp == res:
        min_n = min(min_n, n)
        flag = True

    if n == 0:
        if flag:
            print(min_n)
        else:
            print(0)
        break