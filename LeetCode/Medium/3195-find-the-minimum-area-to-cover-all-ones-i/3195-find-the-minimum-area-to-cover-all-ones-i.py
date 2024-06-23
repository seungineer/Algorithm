class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        min_i = float("inf")
        max_i = -float("inf")
        min_j = float("inf")
        max_j = -float("inf")
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    max_i = max(max_i, i)
                    min_j = min(min_j, j)
                    max_j = max(max_j, j)
        temp_a = max_i - min_i + 1
        temp_b = max_j - min_j + 1
        return(temp_a*temp_b)