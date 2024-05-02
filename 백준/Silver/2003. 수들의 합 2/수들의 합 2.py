n, m = map(int, input().split())
seq = list(map(int, input().split()))

start = 0
end = 0
cnt = 0
while True:
    sub_sum = sum(seq[start:end+1])
    if sub_sum == m:
        cnt += 1
        end += 1
    elif sub_sum > m:
        start += 1
    else:
        end += 1

    if end >= n:
        break

print(cnt)
