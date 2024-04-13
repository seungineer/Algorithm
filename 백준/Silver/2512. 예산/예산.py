# 상한액을 잡아야 하는 문제
## 1초로 제한 시간이 짧으므로 이진 탐색 방식으로 접근
## 가장 큰 수 - 차이를 st, 가장 큰 수를 en로 잡고
### 토탈 520이면, target인 485와 35차이.
### mid를 정하고, 반복을 돌면서 넘는지 체크
import sys
read = sys.stdin.readline

n = int(read())
ask_list = list(map(int, read().split()))
target = int(read())

max_asked = max(ask_list)
sum_asked = sum(ask_list)
difference = sum_asked - target

st = max_asked - difference
en = max_asked
tot = 0
candidate_maxline = 0


while True:
    # 상한선이 필요 없는 경우
    if sum_asked <= target:
        print(max_asked)
        break
    # 상한선이 필요한 경우
    maxline = (st + en) // 2
    for k in ask_list:
        if k > maxline:
            tot += maxline
        else:
            tot += k
    
    if tot > target: # maxline이 target 대비 높은 경우
        en = maxline - 1
    elif tot < target: # maxline이 target 대비 낮은 경우
        candidate_maxline = max(candidate_maxline, maxline)
        st = maxline + 1
    else:
        print(maxline)
        break
    
    if st > en:
        print(candidate_maxline)
        break
    tot = 0    