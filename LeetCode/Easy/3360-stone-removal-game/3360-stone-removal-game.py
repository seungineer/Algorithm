class Solution:
    def canAliceWin(self, n: int) -> bool:
        subtract = 10
        isAliceWin = False
        while n != 0:
            if n >= subtract:
                isAliceWin = not isAliceWin
            n -= subtract
            subtract -= 1
            if n < 0: n = 0
        if isAliceWin: return(True)
        else: return(False)
            
            
            
        