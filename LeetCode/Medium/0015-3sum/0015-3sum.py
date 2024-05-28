class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        last = []
        res = []
        
        for i in range(n-2):
            target = -nums[i]
            st = i+1
            en = n-1
            if nums[i] >0:
                break
            while True:
                if st >= en:
                    break
                    
                temp = nums[st] + nums[en]
                
                if temp < target:
                    st += 1
                elif temp > target:
                    en -= 1
                else:
                    res.append([nums[i], nums[st], nums[en]])
                    st += 1
                    en -= 1
        
        res = list(set([tuple(k) for k in res]))
        return res