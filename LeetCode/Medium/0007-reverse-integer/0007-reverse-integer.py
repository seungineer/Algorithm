from collections import deque
class Solution:
    def reverse(self, x: int) -> int:
        string = ''
        x = str(x)
        res = deque()
        flag = True
        for i in range(len(x)-1, -1, -1):
            if len(res) == 0:
                if x[i] == '0':
                    continue
            if x[i] == '-':
                for k in res:
                    string += k
                res = -int(string)
                flag = False
                continue
            res.append(x[i])
        if flag:
            if len(res) == 0:
                return 0
            for k in res:
                string += k
                res = int(string)
        if res >= 1<<31 or res < (-1<<31):
            return 0

        return res