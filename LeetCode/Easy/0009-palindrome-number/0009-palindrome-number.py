class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        seq = str(x)
        for i in range(len(seq)):
            if seq[-i] != seq[i-1]:
                return False
        return True
            

        

        