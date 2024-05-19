n = int(input())
cnt = 1
last = 1
while True:
    if n <= last:
        print(cnt)
        break
    last +=  6 * cnt
    cnt += 1

