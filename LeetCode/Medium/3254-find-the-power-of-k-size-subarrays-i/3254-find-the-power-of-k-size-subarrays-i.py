class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        length = len(nums)
        answer = []
        for i in range(length):
            if i+k > length:
                break
            temp = nums[i:i+k]
            hasSorted = True
            for j in range(1, len(temp)):
                if temp[j] != temp[j-1] + 1:
                    hasSorted = False
                    break
            if hasSorted:
                answer.append(temp[-1])
            else:
                answer.append(-1)

        return(answer)