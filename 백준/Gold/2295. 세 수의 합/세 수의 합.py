N = int(input())
seq = [int(input()) for _ in range(N)]
seq.sort()

twoSums = set()
for i in range(N):
    for j in range(N):
        twoSums.add(seq[i]+seq[j])

ans = -1
for i in range(N):
    for j in range(N):
        if seq[j] - seq[i] in twoSums:
            ans = max(ans, seq[j])
print(ans)