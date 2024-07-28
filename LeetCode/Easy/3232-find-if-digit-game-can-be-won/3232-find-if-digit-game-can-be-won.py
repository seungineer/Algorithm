class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        al_sum = 0
        bob_sum = 0
        for k in nums:
            if k >= 10:
                al_sum += k
            else:
                bob_sum += k
        if al_sum == bob_sum:
            return False
        else:
            return True