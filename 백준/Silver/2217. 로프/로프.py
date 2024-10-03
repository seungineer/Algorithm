N = int(input())
seq = [int(input()) for _ in range(N)]
seq.sort()
max_w = -1e9
left = N
for s in seq:
    max_w = max(max_w, s * left)
    left -= 1
print(max_w)