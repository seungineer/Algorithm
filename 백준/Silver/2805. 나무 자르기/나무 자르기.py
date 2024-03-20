import sys
read = sys.stdin.readline

n, m = map(int, read().split()) # n 개 / 적어도 m미터
data = list(map(int, read().split())) # 나무 리스트

#로직

st = 0
en = sum(data)
data.sort()

while st <= en:
    left = 0
    mid = (st + en) // 2
    
    for i in data:
        if i > mid:
            left += (i - mid) # 잘려진 나무들 합

    if left < m:
        en = mid - 1
    else:
        st = mid + 1
print(en)
