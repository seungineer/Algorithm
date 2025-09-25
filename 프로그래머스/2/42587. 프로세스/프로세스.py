from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
        
    while queue:
        idx, prior = queue.popleft()
        print(idx, prior)
        maxPrior = -1
        for i in range(len(queue)):
            t, p = queue[i]
            maxPrior = max(maxPrior, p)
        
        if prior >= maxPrior:
            answer += 1
            if idx == location:
                return answer
        else:
            queue.append((idx, prior))
        
    
    return answer