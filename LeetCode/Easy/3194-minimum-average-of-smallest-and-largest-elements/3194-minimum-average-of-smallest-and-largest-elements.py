class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        min_avg = float("inf")
        while nums:
            a = min(nums)
            b = max(nums)
            avg = (a+b)/2
            min_avg = min(min_avg, avg)
            nums.remove(a)
            nums.remove(b)
        return(min_avg)
