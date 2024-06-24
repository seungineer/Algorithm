n = int(input())
a = 0
# 3a + 5b = 18
min_cnt = float("inf")
flag = False
while True:
    left = (n - 3*a)%5
    if n - 3*a < 0:
        break
    if left == 0:
        min_cnt = min(min_cnt, (a+int((n-3*a)/5)))
        flag = True
    a += 1
if flag:
    print(min_cnt)
else:
    print(-1)