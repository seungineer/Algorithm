import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # k번 째 큰 값
        max_heap = []
        for el in nums:
            heapq.heappush(max_heap, -el)
        for i in range(k-1):
            heapq.heappop(max_heap)
        return -heapq.heappop(max_heap)