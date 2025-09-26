def solution(prices):
    length = len(prices)
    answer = [i for i in range(length-1, -1, -1)]
    stk = [0]
    for i in range(1, length):
        while stk and prices[stk[-1]] > prices[i]:
            idx = stk.pop()
            answer[idx] = i - idx
        stk.append(i)
        
    return answer