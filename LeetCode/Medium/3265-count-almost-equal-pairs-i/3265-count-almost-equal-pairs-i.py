class Solution:
    def countPairs(self, nums: list[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            el1 = str(nums[i])
            for j in range(i+1, n):
                el2 = str(nums[j])
                if el1 == el2:
                    answer += 1
                    continue

                if len(el1) <= len(el2):
                    target = el1
                    mani = el2
                else:
                    target = el2
                    mani = el1
                mani_lst = list(mani)
                for i in range(len(mani)):
                    for j in range(i+1, len(mani)):
                        temp = mani_lst[j]
                        mani_lst[j] = mani_lst[i]
                        mani_lst[i] = temp
                        mani_int = int(''.join(mani_lst))
                        if mani_int == int(target):
                            answer += 1
                        mani_lst = list(mani)
        return (answer)