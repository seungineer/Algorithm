# lst sort를 역방향 순방향 각각 진행하여
# 스택의 peek이 맞닿는 곳에서 전달
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort() # x가 작은 값 부터
stk = []
max_h = -1e9
for l in lst:
    if stk:
        if stk[-1][1] < l[1]:
            stk.append(l)
    else:
        stk.append(l)

lst.sort(reverse=True)
stk2 = []
for l in lst:
    if stk2:
        if stk2[-1][1] < l[1]:
            stk2.append(l)
    else:
        stk2.append(l)

def calArea(stk):
    area = 0
    if len(stk) == 1: return area
    for i in range(len(stk) - 1):
        width = abs(stk[i][0] - stk[i+1][0])
        height = stk[i][1]
        area += width * height
    return area

# stk1 면적 계산
a1 = calArea(stk)
# stk2 면적 계산
a2 = calArea(stk2)

# 각각의 스택 peek 간 계산
width = abs(stk[-1][0] - stk2[-1][0]) + 1
height = stk[-1][1]
a3 = width * height
print(a1+a2+a3)