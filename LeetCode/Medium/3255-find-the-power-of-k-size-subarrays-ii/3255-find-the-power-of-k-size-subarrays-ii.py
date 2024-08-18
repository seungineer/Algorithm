class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        answer = [-1 for _ in range(len(nums) - k + 1)]
        conti_cnt = 0
        for i in range(1,k):
            if nums[i] == nums[i-1] + 1:
                conti_cnt += 1
            else:
                conti_cnt = 0
        isFind = False
        if conti_cnt == k-1:
            isFind = True
            answer[0] = nums[k-1]

        for j in range(k, len(nums)):
            print(conti_cnt)
            if k == 1:
                answer[j-k+1] = nums[j]
                continue
            if isFind:
                if nums[j] == nums[j-1] + 1:
                    conti_cnt += 1
                    answer[j-k+1] = nums[j]
                else:
                    conti_cnt = 0
                    isFind = False
            else:
                if nums[j] == nums[j-1] + 1:
                    conti_cnt += 1
                    if conti_cnt >= k-1:
                        answer[j-k+1] = nums[j]
                        isFind = True
                else:
                    conti_cnt = 0
                    isFind = False
        return(answer)