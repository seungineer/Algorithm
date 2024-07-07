class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        str = s*(k+1) #연장
        res = ""
        for i in range(len(s)):
            res += str[i+k]
        return(res)
        