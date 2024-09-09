class Solution:
    def findMaximumScore(self, nums: list[int]) -> int:
        answer = 0
        target = nums[0]
        if len(nums) == 1:
            return 0
        for i in range(1, len(nums)):
            answer += target
            if nums[i] > target:
                target = nums[i]
        return(answer)