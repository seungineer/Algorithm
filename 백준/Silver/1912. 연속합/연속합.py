N = int(input())
seq = list(map(int, input().split()))

tot = 0
answer = max(seq)
for i in range(N):
    if tot + seq[i] > 0:
        tot += seq[i]
        answer = max(answer, tot)
    else:
        tot = 0
print(answer)
