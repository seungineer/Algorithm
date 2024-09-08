N = int(input())
seq = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for s in seq:
    if (s-B) <= 0:
        answer += 1
        continue
    if (s-B)%C == 0:
        answer += (s-B)//C + 1
    else:
        answer += (s-B)//C + 1 + 1
print(answer)
