n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

coin.sort(reverse=True)
cnt = 0
for i in coin:
    a = k//i
    if a == 0:
        continue
    k = k - a * i
    cnt += a

print(cnt)