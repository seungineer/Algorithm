from collections import deque
class Solution:
    def validStrings(self, n: int) -> list[str]:
        temp = ["0", "1"]
        arr = deque()
        arr.append(temp[0])
        arr.append(temp[1])
        result = []
        while arr:
            cand = arr.popleft()
            if len(cand) == n:
                result.append(cand)
                continue
            for i in temp:
                if cand[-1] == "0":
                    if i == "1":
                        cand1 = cand + i
                        arr.append(cand1)
                else:
                    cand2 = cand + i
                    arr.append(cand2)
        return(result)    