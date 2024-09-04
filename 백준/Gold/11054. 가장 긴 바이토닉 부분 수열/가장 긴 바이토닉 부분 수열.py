N = int(input())
seq = list(map(int, input().split()))

dp_l = [1 for _ in range(N)]
dp_r = [1 for _ in range(N)]

# 왼쪽, 오른쪽에서부터 가장 긴 증가하는 부분수열 만들기
for i in range(N):
    for j in range(i):
        if seq[j] < seq[i]:
            dp_l[i] = max(dp_l[i], dp_l[j] + 1)
        if seq[N-1-j] < seq[N-1-i]:
            dp_r[N-1-i] = max(dp_r[N-1-i], dp_r[N-1-j] + 1)
ans = -1
for i in range(N):
    ans = max(ans, dp_l[i] + dp_r[i] - 1)
print(ans)