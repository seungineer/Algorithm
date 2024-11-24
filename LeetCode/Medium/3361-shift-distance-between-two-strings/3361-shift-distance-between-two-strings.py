class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: list[int], previousCost: list[int]) -> int:
        s = list(s)
        t = list(t)
        answer = 0
        for i in range(len(s)):
            s_idx = ord(s[i]) - ord('a')
            t_idx = ord(t[i]) - ord('a')
            if s_idx == t_idx: continue
    
            forwardCost = 0
            backwardCost = 0
            if s_idx < t_idx:
                forwardCost = sum(nextCost[s_idx:t_idx])
            else:
                forwardCost += sum(nextCost[s_idx:])
                forwardCost += sum(nextCost[:t_idx])
            
            if s_idx > t_idx:
                backwardCost = sum(previousCost[t_idx+1:s_idx+1])
            else:
                backwardCost += sum(previousCost[:s_idx+1])
                backwardCost += sum(previousCost[t_idx+1:])
            
            answer += min(forwardCost, backwardCost)
        return(answer)