N = int(input())
stk1 = []
stk2 = []
min_time = 4321
for _ in range(N):
    store, bread = map(int, input().split())
    stk1.append(store)
    stk2.append(bread)
    if stk1[-1] > stk2[-1] :
        stk1.pop()
        stk2.pop()
    else: #같거나 기다리는 시간 있는 경우
        stk1.pop()
        min_time = min(min_time, stk2.pop())
    
if min_time != 4321:
    print(min_time)
else:
    print(-1)
