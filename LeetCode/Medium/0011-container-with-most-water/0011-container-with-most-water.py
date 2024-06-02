from collections import deque
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        l = 0
        r = n -1
        max_area = 0
        while l < r:
            if l >= n or r >= n:
                break
            min_height = min(height[l], height[r])
            width = r-l
            print(height[l], height[r])
            temp_area = min_height * width
            if max_area < temp_area:
                max_area = temp_area

            if height[l] < height [r]:
                l += 1
            else:
                r -= 1



        return max_area