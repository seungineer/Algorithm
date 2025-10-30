import heapq as hq

def findMaxInfo(cand, l, r):
    maxNum = -1
    leftIdx = -1
    # 뽑아 내고,
    # l, r 사이에 있는지 확인하기(범위가 아니라면 계속 버리기)
    
    while cand:
        n, idx = hq.heappop(cand)
        
        if l <= idx < r:
            leftIdx = idx
            maxNum = -1 * n
            break
            
    return maxNum, leftIdx
    

def solution(number, k):
    answer = ''
    nums = list(map(int, number))
    t = k
    l = 0
    r = k + 1

    cand = []
    
    for i in range(l, r): hq.heappush(cand, [-1 * nums[i], i])
    
    while len(answer) != len(nums) - t:
        maxNum, leftIdx = findMaxInfo(cand, l, r)
        
        answer += str(maxNum)
        k -= 1
        
        if r < len(nums):
            hq.heappush(cand, [-1 * nums[r], r])
            
        l = leftIdx + 1
        r += 1
        
    
    return answer