import sys
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        st = 0
        en = len(nums)-1
        res = []
        min_mid = sys.maxsize
        num_cnt = nums.count(target)
        isfind = False
        while  st <= en :
            mid = (st + en)//2
            if nums[mid] < target:
                st = mid + 1
            elif nums[mid] > target:
                en = mid - 1
            else:
                isfind = True
                min_mid = min(min_mid, mid)
                en -= 1
        if isfind:
            res.append(min_mid)
            res.append(min_mid+num_cnt-1)
        else:
            res.append(-1)
            res.append(-1)
        return res 