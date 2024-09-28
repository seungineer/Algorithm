n = int(input())
dict = {}
max_x = -1e9
for _ in range(n):
    x, y = map(int, input().split())
    dict[x] = y
    max_x = max(max_x, x)

stk = []
answer = 0 # 최소 건물 개수
for key in dict.keys():
    height = dict[key]
    if stk:
        heightSet = set()
        while stk:
            if height < stk[-1]:
                prev_height = stk.pop()
                heightSet.add(prev_height)
            else:
                break
        if height != 0: stk.append(height)
        answer += len(heightSet)       
    else:
        if height != 0: stk.append(height)
    
heightSet = set()
while stk:
    prev_height = stk.pop()
    heightSet.add(prev_height)
answer += len(heightSet)
print(answer)