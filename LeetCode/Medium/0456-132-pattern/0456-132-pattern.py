class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stk = []
        j_cand = -10**9-1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < j_cand:
                return True
            while stk and nums[i] > stk[-1]: # 
                j_cand = stk.pop()
            stk.append(nums[i])
        return False
    