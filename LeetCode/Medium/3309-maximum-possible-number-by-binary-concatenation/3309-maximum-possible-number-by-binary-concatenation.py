from itertools import permutations
class Solution:
    def maxGoodNumber(self, nums: list[int]) -> int:
        answer = 0
        bin1 = bin(nums[0])[2:]
        bin2 = bin(nums[1])[2:]
        bin3 = bin(nums[2])[2:]
        bin_lst = [bin1, bin2, bin3]
        comb = list(permutations(range(3), 3))
        max_int = -1e9
        for com in comb:
            idx1 = com[0]
            idx2 = com[1]
            idx3 = com[2]
            binary_str = ''
            binary_str += bin_lst[idx1]
            binary_str += bin_lst[idx2]
            binary_str += bin_lst[idx3]
            strtoint = int(binary_str, 2)
            max_int = max(max_int, strtoint)
        return max_int