class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        st = 0
        en = 1
        min_length = 10**5 + 1
        sum_arr = [0 for _ in range(n+1)]
        sum_arr[1] = nums[0]
        for i in range(2, n+1):
            sum_arr[i] = sum_arr[i-1] + nums[i-1]
        while True:
            if st > en or en > n:
                break
            p_sum = sum_arr[en] - sum_arr[st]
            if p_sum >= target:
                min_length = min(min_length, en-st)
                st += 1
            else:
                en += 1
        if min_length == 10**5 + 1:
            return 0
        return min_length