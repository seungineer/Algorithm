class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            j = i + 1
            k = j + 1
            if (nums[i] + nums[k]) * 2 == nums[j]: ans += 1
        # print(ans)
        return ans
                    