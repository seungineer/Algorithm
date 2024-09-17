H, W = map(int, input().split())
seq = list(map(int, input().split()))
stk = []
answer = 0
for height in seq:
    if not stk:
        stk.append(height)
        continue
    if stk[0] > height:
        stk.append(height)
        continue
    
    while stk:
        answer += abs(stk[-1] -  stk[0])
        stk.pop()
    stk.append(height)
    
if stk:
    max_height = stk.pop()
    while stk:
        if max_height > stk[-1]:
            answer += abs(stk[-1] - max_height)
            stk.pop()
        else:
            max_height = stk.pop()
print(answer)