class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        arr = [0 for _ in range(24)]
        for k in hours:
            arr[k%24] += 1
        print(arr)
        res = 0
        for i in range(1, 12):
            res += arr[i]*arr[24-i]
        if arr[0] > 1:
            res += arr[0]*(arr[0]-1)//2
        if arr[12] > 1:
            res += arr[12]*(arr[12]-1)//2
        print(res)


        return res