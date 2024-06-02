class Solution:
    def trap(self, height: list[int]) -> int:
        stk = []
        area = 0
        for i in range(len(height)):
            while stk and height[i] > height[stk[-1]]:
                stk_top = stk.pop()
                if not len(stk):
                    break
                min_height = min(height[i], height[stk[-1]])
                width = i - stk[-1] - 1
                area += (min_height- height[stk_top]) * width
            stk.append(i)
        print(area)
        return area
