n, r, c = map(int, input().split())
cnt = 0

for i in range(n, 0, -1):
    if r < 2**(i-1) and c < 2**(i-1): # 제1사분면
        cnt += 0
    if r < 2**(i-1) and c >= 2**(i-1): # 제2사분면
        cnt += 2**(i*2-2)
        c -= 2**(i-1)
    if r >= 2**(i-1) and c < 2**(i-1): # 제3사분면
        cnt += 2**(i*2-1)
        r -= 2**(i-1)
    if r >= 2**(i-1) and c >= 2**(i-1): # 제1사분면
        cnt += 2**(i*2-2) + 2**(i*2-1)
        c -= 2**(i-1)
        r -= 2**(i-1)
print(cnt)