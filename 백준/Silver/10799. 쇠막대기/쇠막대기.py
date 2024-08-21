# 스택에 들어온 친구가 몇 번의 레이저를 거쳐서 자기 짝을 만나는지를 세주면 됨
# 내가 열리고 난 후에 내가 닫힐 때 총 몇개의 레이저가 있었는지?

seq = input()
stk = []
raser_cnt = []
answer = 0
for s in seq:
    if s == '(':
        stk.append(s)
        raser_cnt.append(0)
        isRaser = True
    else:
        if stk and stk[-1] == '(':
            if isRaser:
                raser_cnt.pop()
                for i in range(len(raser_cnt)):
                    raser_cnt[i] += 1
                isRaser = False
                
            else:
                answer += raser_cnt[-1] + 1
                raser_cnt.pop()
            stk.pop()
    if len(stk) == 0:
        raser_cnt = []

print(answer)