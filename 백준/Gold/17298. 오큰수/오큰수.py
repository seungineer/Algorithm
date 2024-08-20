n = int(input())
seq = list(map(int,input().split()))

answer = [-1 for _ in range(n)]

stk = [[seq[0], 0]]
for i in range(1, n):
    while stk and stk[-1][0] < seq[i]:
        temp, index = stk.pop()
        answer[index] = seq[i]
    stk.append([seq[i],i])

for s in answer:
    print(s, end=" ")
exit()