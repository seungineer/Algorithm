class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            min_el = min(nums)
            min_el_idx = nums.index(min_el)
            nums[min_el_idx] *= multiplier
        return (nums)
