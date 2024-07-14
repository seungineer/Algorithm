class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        str_s = s
        res = []
        res.append(str_s)
        for i in range(n-1):
            temp_lst = list(str_s)
            if int(temp_lst[i+1]) % 2 == int(temp_lst[i]) % 2:    
                temp = temp_lst[i+1]
                temp_lst[i+1] = temp_lst[i]
                temp_lst[i] = temp
                str_s = ''.join(temp_lst)
                res.append(str_s)
                str_s = s
        res.sort()
        return(res[0])