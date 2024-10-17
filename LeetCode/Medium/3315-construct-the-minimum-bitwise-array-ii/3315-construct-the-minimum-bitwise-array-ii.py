class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        # a와 a+1을 비트와이즈 해서 num을 만족시키는 a 찾기
        ans = []

        for num in nums:
            mask = 1
            while (num & mask) != 0:
                mask <<= 1
            if mask == 1: ans.append(-1)
            else: ans.append(num - (mask >> 1))
        return ans