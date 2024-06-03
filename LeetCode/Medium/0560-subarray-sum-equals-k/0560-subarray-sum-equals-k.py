class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sum = 0
        dict = {}
        dict[0] = 1
        ans = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in dict.keys():
                ans += dict[prefix_sum - k]
            if prefix_sum in dict.keys():
                dict[prefix_sum] += 1
            else:
                dict[prefix_sum] = 1
        return ans