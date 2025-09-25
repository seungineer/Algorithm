from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1
    qu = deque([0 for _ in range(bridge_length)])
    waitlist = deque(truck_weights)
    
    qu.popleft()
    curWeight = waitlist.popleft()
    qu.append(curWeight)
    
    while curWeight != 0:
        answer += 1
        curWeight -= qu.popleft()
        
        # 대기 트럭이 곧장 오면 되는 케이스
        if waitlist and curWeight + waitlist[0] <= weight:
            w = waitlist.popleft()
            curWeight += w
            qu.append(w)
            continue
        
        # 대기 트럭이 못 오는 케이스
        qu.append(0)
        
    return answer